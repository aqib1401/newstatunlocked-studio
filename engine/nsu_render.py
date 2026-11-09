#!/usr/bin/env python3
"""
New Stat Unlocked - render engine.

Turns an episode folder into a finished YouTube Short:
    episode.json   scene plan (written by Claude, see the ENGINE GUIDE)
    voiceover.mp3  ElevenLabs narration (any audio format ffmpeg reads)
    music.mp3      optional; otherwise a soft background bed is generated

Usage:
    python3 nsu_render.py EPISODE_DIR --preview   # 6 still frames + contact sheet, ~20 s
    python3 nsu_render.py EPISODE_DIR             # full MP4 (1080x1920, 30 fps)

Output goes to EPISODE_DIR/out/.
Everything (sound effects, music bed, fonts) is generated or fetched for free.
"""
import argparse, asyncio, json, math, os, re, shutil, subprocess, sys, wave
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SR = 44100
W, H = 540, 960          # layout units; rendered at 2x = 1080x1920

# --------------------------------------------------------------------------- setup
def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)

def ensure_playwright():
    try:
        import playwright  # noqa
    except ImportError:
        sh([sys.executable, "-m", "pip", "install", "-q", "--break-system-packages", "playwright"])
    for p in ["/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]:
        if os.path.exists(p):
            return p
    try:
        sh([sys.executable, "-m", "playwright", "install", "chromium"])
    except Exception:
        pass
    return None

FONT_URLS = {
    "ChakraPetch-Medium.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/chakrapetch/ChakraPetch-Medium.ttf",
    "ChakraPetch-SemiBold.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/chakrapetch/ChakraPetch-SemiBold.ttf",
    "ChakraPetch-Bold.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/chakrapetch/ChakraPetch-Bold.ttf",
    "Inter.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf",
}

def ensure_fonts():
    d = Path.home() / ".cache" / "nsu_fonts"
    d.mkdir(parents=True, exist_ok=True)
    for name, url in FONT_URLS.items():
        f = d / name
        if not f.exists() or f.stat().st_size < 10000:
            try:
                sh(["curl", "-sSfL", "-o", str(f), url])
            except Exception:
                print(f"! could not download {name}; falling back to system fonts")
    return d

# --------------------------------------------------------------------------- audio io
def load_audio(path, sr=SR):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(out, dtype=np.float32).copy()

def write_wav(path, x, sr=SR):
    x = np.clip(x, -1, 1)
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((x * 32767).astype("<i2").tobytes())

# --------------------------------------------------------------------------- alignment
def speech_segments(voice, sr=SR, thresh_db=-38.0, min_sil=0.14):
    """Return list of (start, end) seconds where speech is present."""
    hop = int(sr * 0.01)
    n = len(voice) // hop
    if n == 0:
        return [(0.0, len(voice) / sr)]
    frames = voice[: n * hop].reshape(n, hop)
    rms = np.sqrt((frames ** 2).mean(1) + 1e-12)
    db = 20 * np.log10(rms / (rms.max() + 1e-9))
    active = db > thresh_db
    segs, start, sil = [], None, 0
    for i, a in enumerate(active):
        if a:
            if start is None:
                start = i
            sil = 0
        elif start is not None:
            sil += 1
            if sil * 0.01 >= min_sil:
                segs.append((start * 0.01, (i - sil + 1) * 0.01))
                start, sil = None, 0
    if start is not None:
        segs.append((start * 0.01, n * 0.01))
    return [s for s in segs if s[1] - s[0] > 0.05] or [(0.0, len(voice) / sr)]

def tokenize(script):
    script = re.sub(r"\[[^\]]*\]", " ", script)   # drop ElevenLabs audio tags like [excited]
    toks = []
    for m in re.finditer(r"\S+", script):
        raw = m.group(0)
        norm = re.sub(r"[^a-z0-9']", "", raw.lower().replace("’", "'"))
        if norm:
            toks.append({"raw": raw, "norm": norm})
        elif toks:  # stray punctuation like "..." on its own
            toks[-1]["raw"] += " " + raw
    return toks

PUNCT_END = re.compile(r"(\.\.\.|[.?!,:;…])$")

def _chunk_words(words):
    chunks, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        if PUNCT_END.search(w["raw"]):
            chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    return chunks

def _spread(words, idxs, segs):
    """Spread words over the speech inside segs, by word length, skipping silences."""
    total = sum(e - s for s, e in segs) or 1e-3
    wts = np.array([max(2, len(words[i]["norm"])) + 1.5 for i in idxs], float)
    cum = np.concatenate([[0], np.cumsum(wts)]) / wts.sum() * total
    def real(st):
        acc = 0.0
        for s, e in segs:
            if st <= acc + (e - s) + 1e-9:
                return s + (st - acc)
            acc += e - s
        return segs[-1][1]
    for k, i in enumerate(idxs):
        words[i]["start"] = real(cum[k] + 1e-4)
        words[i]["end"] = real(cum[k + 1] - 1e-4)

def align(script, voice, sr=SR, chunk_times=None):
    """Word timings. Each punctuation-delimited phrase of the script is matched to a
    run of speech segments (dynamic programming on durations and pauses); words are
    then spread inside their phrase. If exact phrase times are known (free voice),
    they are used directly."""
    words = tokenize(script)
    segs = speech_segments(voice, sr)
    chunks = _chunk_words(words)
    if chunk_times and len(chunk_times) == len(chunks):
        for idxs, (a, b) in zip(chunks, chunk_times):
            _spread(words, idxs, [(a, b)])
        return words, segs
    C, S = len(chunks), len(segs)
    wts = [sum(max(2, len(words[i]["norm"])) + 1.5 for i in ch) for ch in chunks]
    total_speech = sum(e - s for s, e in segs)
    if S >= C:
        rate = total_speech / sum(wts)
        exp = [w * rate for w in wts]
        dur = [e - s for s, e in segs]
        gap = [segs[j + 1][0] - segs[j][1] for j in range(S - 1)]
        pre = np.concatenate([[0], np.cumsum(dur)])
        INF = 1e18
        dp = np.full((C, S), INF); bk = np.zeros((C, S), int)
        def cost(k, i, j):  # chunk k covers segs i..j
            sp = pre[j + 1] - pre[i]
            c = (sp - exp[k]) ** 2 / max(exp[k], 0.2)
            inner = sum(max(0, g - 0.22) for g in gap[i:j])
            return c + 3.0 * inner
        for j in range(S):
            dp[0][j] = cost(0, 0, j)
        for k in range(1, C):
            for j in range(k, S):
                best, bi = INF, -1
                for i in range(k - 1, j):
                    if dp[k - 1][i] >= INF:
                        continue
                    v = dp[k - 1][i] + cost(k, i + 1, j)
                    if v < best:
                        best, bi = v, i
                dp[k][j], bk[k][j] = best, bi
        j = S - 1
        ends = [0] * C
        for k in range(C - 1, -1, -1):
            ends[k] = j
            j = bk[k][j] if k > 0 else 0
        start = 0
        for k, ch in enumerate(chunks):
            _spread(words, ch, segs[start: ends[k] + 1])
            start = ends[k] + 1
    else:
        _spread(words, list(range(len(words))), segs)
    for i in range(1, len(words)):
        words[i]["start"] = max(words[i]["start"], words[i - 1]["end"] - 0.02)
        words[i]["end"] = max(words[i]["end"], words[i]["start"] + 0.08)
    return words, segs

def find_phrase(words, phrase, nth=1):
    target = [t["norm"] for t in tokenize(phrase)]
    if not target:
        raise ValueError(f"empty phrase: {phrase!r}")
    hits = 0
    for i in range(len(words) - len(target) + 1):
        if all(words[i + j]["norm"] == target[j] for j in range(len(target))):
            hits += 1
            if hits == nth:
                return i, i + len(target) - 1
    raise ValueError(f"phrase not found in script: {phrase!r} (occurrence {nth})")

def resolve_time(anchor, words, default=None):
    """Anchors: 3.2 | "phrase" | "phrase#2" | "end:phrase" | "phrase+0.4" | "phrase-0.2" """
    if anchor is None:
        return default
    if isinstance(anchor, (int, float)):
        return float(anchor)
    a = anchor.strip()
    off = 0.0
    m = re.match(r"^(.*?)([+-]\d+(?:\.\d+)?)$", a)
    if m and m.group(1).strip():
        a, off = m.group(1).strip(), float(m.group(2))
    use_end = a.startswith("end:")
    if use_end:
        a = a[4:].strip()
    nth = 1
    m = re.match(r"^(.*)#(\d+)$", a)
    if m:
        a, nth = m.group(1).strip(), int(m.group(2))
    i0, i1 = find_phrase(words, a, nth)
    return (words[i1]["end"] if use_end else words[i0]["start"]) + off

# --------------------------------------------------------------------------- captions
def build_captions(words, highlights):
    hl = {}
    for k, v in (highlights or {}).items():
        hl[tuple(t["norm"] for t in tokenize(k))] = v
    colors = [None] * len(words)
    for key, col in hl.items():
        for i in range(len(words) - len(key) + 1):
            if tuple(words[i + j]["norm"] for j in range(len(key))) == key:
                for j in range(len(key)):
                    colors[i + j] = col
    chunks, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        brk = re.search(r"[.?!,:;…]$|\.\.\.$", w["raw"]) is not None
        long_word = len(w["norm"]) > 9
        if brk or len(cur) >= 3 or (len(cur) >= 2 and long_word):
            chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    out = []
    for ci, ch in enumerate(chunks):
        s = words[ch[0]]["start"]
        e_last = words[ch[-1]]["end"]
        nxt = words[chunks[ci + 1][0]]["start"] if ci + 1 < len(chunks) else e_last + 0.6
        e = nxt if nxt - e_last < 0.55 else e_last + 0.35
        toks = []
        for i in ch:
            txt = words[i]["raw"]
            toks.append({"t": txt, "c": colors[i]})
        out.append({"s": s, "e": e, "w": toks})
    return out

# --------------------------------------------------------------------------- sound design
def env(n, a, d, sr=SR):
    t = np.arange(n) / sr
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / max(d, 1e-4))
    return e

def tone(freq, dur, sr=SR, kind="sine"):
    t = np.arange(int(dur * sr)) / sr
    if callable(freq):
        ph = 2 * np.pi * np.cumsum(freq(t)) / sr
    else:
        ph = 2 * np.pi * freq * t
    if kind == "sine":
        return np.sin(ph)
    if kind == "tri":
        return 2 / np.pi * np.arcsin(np.sin(ph))
    if kind == "square":
        return np.sign(np.sin(ph)) * 0.6
    return np.sin(ph)

def lowpass(x, cutoff, sr=SR):
    from scipy.signal import butter, lfilter
    b, a = butter(2, min(cutoff / (sr / 2), 0.99), "low")
    return lfilter(b, a, x)

def bandpass(x, lo, hi, sr=SR):
    from scipy.signal import butter, lfilter
    b, a = butter(2, [lo / (sr / 2), min(hi / (sr / 2), 0.99)], "band")
    return lfilter(b, a, x)

RNG = np.random.default_rng(7)

def sfx(name):
    n = lambda d: int(d * SR)
    if name == "pop":       # stat card in
        d = 0.32
        x = tone(lambda t: 380 + 900 * (1 - np.exp(-t * 30)), d, kind="tri") * env(n(d), 0.004, 0.09)
        x += 0.5 * tone(1320, d) * env(n(d), 0.002, 0.05)
        return 0.55 * x
    if name == "tick":      # UI blip
        d = 0.05
        return 0.22 * tone(2100, d) * env(n(d), 0.001, 0.012)
    if name == "whoosh":    # scene transition
        d = 0.42
        noise = RNG.standard_normal(n(d))
        t = np.arange(n(d)) / SR
        sweep = bandpass(noise, 500, 5000)
        shape = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2
        return 0.18 * sweep * shape
    if name == "swish":
        d = 0.22
        noise = RNG.standard_normal(n(d))
        t = np.arange(n(d)) / SR
        return 0.15 * bandpass(noise, 1500, 7000) * np.sin(np.pi * t / d) ** 2
    if name == "buzz":      # side effect
        d = 0.55
        x = tone(196, d, kind="square") + 0.6 * tone(185, d, kind="square")
        x = lowpass(x, 1400) * env(n(d), 0.01, 0.22)
        x[n(0.2):] *= 0.0
        y = tone(165, 0.35, kind="square")
        y = lowpass(y, 1200) * env(n(0.35), 0.01, 0.18)
        out = np.zeros(n(0.6)); out[: len(x)] += x; out[n(0.24): n(0.24) + len(y)] += y
        return 0.28 * out
    if name == "clock":     # choice countdown
        d = 0.06
        x = bandpass(RNG.standard_normal(n(d)), 2500, 6000) * env(n(d), 0.0005, 0.01)
        return 0.35 * x
    if name == "heartbeat":
        d = 0.5
        b = lowpass(tone(55, 0.12), 200) * env(n(0.12), 0.003, 0.05)
        out = np.zeros(n(d)); out[: len(b)] += b; out[n(0.17): n(0.17) + len(b)] += 0.7 * b
        return 0.9 * out
    if name == "chime":     # choice made
        out = np.zeros(n(1.1))
        for i, f in enumerate([523.25, 659.25, 783.99, 1046.5]):
            s = n(0.07 * i)
            nd = n(0.8)
            out[s: s + nd] += 0.22 * tone(f, 0.8) * env(nd, 0.004, 0.28)
        return out
    if name == "boom":      # slow-mo hit
        d = 1.4
        x = tone(lambda t: 70 * np.exp(-t * 1.2) + 30, d) * env(n(d), 0.005, 0.5)
        x += 0.3 * lowpass(RNG.standard_normal(n(d)), 300) * env(n(d), 0.002, 0.15)
        return 0.7 * x
    if name == "thud":
        d = 0.25
        return 0.6 * lowpass(tone(lambda t: 140 * np.exp(-t * 8) + 50, d), 600) * env(n(d), 0.002, 0.07)
    if name == "ding":
        d = 0.9
        return 0.25 * (tone(1568, d) + 0.4 * tone(3136, d)) * env(n(d), 0.002, 0.25)
    if name == "boing":
        d = 0.45
        return 0.3 * tone(lambda t: 300 + 180 * np.sin(t * 40) * np.exp(-t * 6), d, kind="tri") * env(n(d), 0.003, 0.18)
    if name == "click":
        d = 0.03
        return 0.3 * bandpass(RNG.standard_normal(n(d)), 1500, 5000) * env(n(d), 0.0005, 0.006)
    if name == "riser":
        d = 1.2
        noise = bandpass(RNG.standard_normal(n(d)), 800, 6000)
        t = np.arange(n(d)) / SR
        return 0.12 * noise * (t / d) ** 2 + 0.08 * tone(lambda t: 200 + 600 * (t / d) ** 2, d) * (t / d) ** 2
    if name == "crowd":
        d = 1.6
        t = np.arange(n(d)) / SR
        x = bandpass(RNG.standard_normal(n(d)), 300, 2500)
        return 0.16 * x * np.sin(np.pi * t / d)
    if name == "glitch":
        d = 0.3
        x = tone(lambda t: 800 + 600 * np.sign(np.sin(t * 90)), d, kind="square")
        return 0.12 * lowpass(x, 3000) * env(n(d), 0.001, 0.12)
    if name == "fill":      # compare bar growing
        d = 0.6
        t = np.arange(n(d)) / SR
        return 0.1 * tone(lambda t: 300 + 700 * (t / d), d, kind="tri") * np.sin(np.pi * t / d)
    raise ValueError(f"unknown sfx {name!r}")

SFX_NAMES = ["pop", "tick", "whoosh", "swish", "buzz", "clock", "heartbeat", "chime", "boom",
             "thud", "ding", "boing", "click", "riser", "crowd", "glitch", "fill"]

def music_bed(dur, slow_ranges):
    """Soft synth bed: Am-F-C-G pads with a gentle pluck arpeggio, 84 bpm."""
    total = int(dur * SR)
    out = np.zeros(total)
    beat = 60 / 84
    bar = beat * 4
    chords = [[57, 60, 64], [53, 57, 60], [48, 55, 60], [55, 59, 62]]   # midi
    mtof = lambda m: 440 * 2 ** ((m - 69) / 12)
    t_bar = 0.0
    ci = 0
    while t_bar < dur:
        ch = chords[ci % 4]
        nb = int(bar * SR)
        s = int(t_bar * SR)
        seg = np.zeros(nb)
        tt = np.arange(nb) / SR
        for m in ch:
            f = mtof(m)
            seg += (np.sin(2 * np.pi * f * tt) + 0.5 * np.sin(2 * np.pi * f * 1.003 * tt)
                    + 0.25 * np.sin(2 * np.pi * f * 2 * tt))
        pad_env = np.minimum(1, tt / 0.6) * np.minimum(1, (bar - tt) / 0.4)
        seg *= 0.05 * pad_env
        # pluck arpeggio, 8th notes
        arp = ch + [ch[0] + 12]
        for k in range(8):
            ps = int(k * beat / 2 * SR)
            nd = int(0.5 * SR)
            f = mtof(arp[k % 4] + 12)
            pl = (np.sin(2 * np.pi * f * np.arange(nd) / SR)) * np.exp(-np.arange(nd) / SR / 0.12)
            e = min(nb, ps + nd)
            seg[ps:e] += 0.035 * pl[: e - ps]
        # soft kick on 1 and 3
        for k in (0, 2):
            ks = int(k * beat * SR)
            kd = int(0.25 * SR)
            kk = np.sin(2 * np.pi * np.cumsum(55 + 90 * np.exp(-np.arange(kd) / SR * 25)) / SR) * np.exp(-np.arange(kd) / SR / 0.08)
            e = min(nb, ks + kd)
            seg[ks:e] += 0.08 * kk[: e - ks]
        e = min(total, s + nb)
        out[s:e] += seg[: e - s]
        t_bar += bar
        ci += 1
    out = lowpass(out, 3500)
    # duck + darken during slow-mo
    gain = np.ones(total)
    for a, b in slow_ranges:
        ia, ib = int(a * SR), min(total, int(b * SR))
        gain[ia:ib] = 0.35
    from scipy.ndimage import uniform_filter1d
    gain = uniform_filter1d(gain, int(0.3 * SR))
    fade = np.minimum(1, np.arange(total) / (0.8 * SR)) * np.minimum(1, (total - np.arange(total)) / (1.0 * SR))
    return out * gain * fade

def place(buf, x, t, gain=1.0):
    s = int(max(0, t) * SR)
    if s >= len(buf):
        return
    e = min(len(buf), s + len(x))
    buf[s:e] += gain * x[: e - s]

# --------------------------------------------------------------------------- plan
def build_plan(ep, words, dur):
    R = lambda a, d=None: resolve_time(a, words, d)
    scenes = ep["scenes"]
    plan_scenes = []
    for i, sc in enumerate(scenes):
        s = 0.0 if i == 0 else R(sc.get("start"))
        plan_scenes.append(dict(sc, t0=s))
    for i, sc in enumerate(plan_scenes):
        sc["t1"] = plan_scenes[i + 1]["t0"] if i + 1 < len(plan_scenes) else dur
    def resolve_keys(keys, scene_t0):
        out = []
        for k in keys or []:
            k = dict(k)
            k["t"] = R(k.get("at"), scene_t0) if k.get("at") is not None else scene_t0
            out.append(k)
        out.sort(key=lambda k: k["t"])
        return out
    for sc in plan_scenes:
        for a in sc.get("actors", []):
            a["keys"] = resolve_keys(a.get("keys"), sc["t0"])
        for o in sc.get("objects", []):
            o["keys"] = resolve_keys(o.get("keys"), sc["t0"])
    huds = []
    for h in ep.get("hud", []):
        h = dict(h)
        h["t0"] = R(h["at"])
        h["t1"] = R(h.get("until"), None) if h.get("until") else None
        if h.get("pick_at"):
            h["tp"] = R(h["pick_at"])
        huds.append(h)
    huds.sort(key=lambda h: h["t0"])
    for i, h in enumerate(huds):
        if h["t1"] is None:
            h["t1"] = huds[i + 1]["t0"] if i + 1 < len(huds) else min(dur, h["t0"] + 4)
        if i + 1 < len(huds):
            h["t1"] = min(h["t1"], huds[i + 1]["t0"])
    extra_sfx = []
    for s in ep.get("sfx", []):
        extra_sfx.append({"name": s["name"], "t": R(s["at"]), "gain": s.get("gain", 1.0)})
    return {"scenes": plan_scenes, "hud": huds, "sfx": extra_sfx}

def build_audio(ep, plan, voice, dur, ep_dir):
    total = int((dur) * SR)
    v = np.zeros(total); v[: min(total, len(voice))] = voice[:total]
    peak = np.max(np.abs(v)) + 1e-9
    v = v / peak * 0.89
    fx = np.zeros(total)
    slow_ranges = [(s["t0"], s["t1"]) for s in plan["scenes"] if s.get("slowmo")]
    for i, sc in enumerate(plan["scenes"]):
        if i > 0 and sc.get("transition", "cut") != "none":
            place(fx, sfx("whoosh"), sc["t0"] - 0.2)
        if sc.get("slowmo"):
            place(fx, sfx("boom"), sc["t0"])
        for a in sc.get("actors", []) + sc.get("objects", []):
            for k in a.get("keys", []):
                if k.get("sfx"):
                    place(fx, sfx(k["sfx"]), k["t"])
    for h in plan["hud"]:
        if h["type"] == "stat":
            place(fx, sfx("pop"), h["t0"])
            for j in range(10):
                place(fx, sfx("tick"), h["t0"] + 0.28 + 0.04 * j, 0.8)
        elif h["type"] == "compare":
            place(fx, sfx("fill"), h["t0"] + 0.1)
            place(fx, sfx("fill"), h["t0"] + 0.55)
        elif h["type"] == "warn":
            place(fx, sfx("buzz"), h["t0"])
        elif h["type"] == "choice":
            tp = h.get("tp", h["t1"])
            t = h["t0"]
            k = 0
            while t < tp - 0.05:
                place(fx, sfx("clock"), t)
                if k % 2 == 0:
                    place(fx, sfx("heartbeat"), t, 0.8)
                t += 0.5; k += 1
            place(fx, sfx("chime"), tp)
        elif h["type"] == "level":
            place(fx, sfx("ding"), h["t0"])
    for s in plan["sfx"]:
        place(fx, sfx(s["name"]), s["t"], s["gain"])
    mpath = ep.get("music", "auto")
    if mpath == "none":
        m = np.zeros(total)
    elif mpath and mpath != "auto" and (ep_dir / mpath).exists():
        m = load_audio(ep_dir / mpath)
        if len(m) < total:
            m = np.tile(m, total // max(1, len(m)) + 1)
        m = m[:total]
        m = m / (np.max(np.abs(m)) + 1e-9) * 0.12
        fade = np.minimum(1, np.arange(total) / (0.8 * SR)) * np.minimum(1, (total - np.arange(total)) / (1.0 * SR))
        m *= fade
    else:
        m = music_bed(dur, slow_ranges)
        m = m / (np.max(np.abs(m)) + 1e-9) * 0.16
    # duck music under the voice
    from scipy.ndimage import uniform_filter1d
    venv = uniform_filter1d(np.abs(v), int(0.15 * SR))
    duck = 1 - 0.45 * np.clip(venv / (venv.max() + 1e-9) * 3, 0, 1)
    mix = v + fx * float(ep.get("sfx_volume", 1.0)) + m * duck * float(ep.get("music_volume", 1.0))
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.95
    return mix

# --------------------------------------------------------------------------- rendering
def html_page(fonts_dir):
    ff = ""
    for name, fam, wt in [("ChakraPetch-Medium.ttf", "Chakra Petch", 500), ("ChakraPetch-SemiBold.ttf", "Chakra Petch", 600),
                          ("ChakraPetch-Bold.ttf", "Chakra Petch", 700), ("Inter.ttf", "InterNSU", "100 900")]:
        p = fonts_dir / name
        if p.exists():
            ff += f"@font-face{{font-family:'{fam}';src:url('file://{p}');font-weight:{wt};}}\n"
    return (HERE / "nsu_engine.html").read_text().replace("/*FONTS*/", ff)

async def render_frames(page_html, plan_json, times, out_dir, workers=2, ext="jpg"):
    from playwright.async_api import async_playwright
    chrome = ensure_playwright()
    html_path = out_dir / "_engine.html"
    html_path.write_text(page_html)
    async with async_playwright() as p:
        kw = {"executable_path": chrome} if chrome else {}
        browser = await p.chromium.launch(**kw, args=["--disable-gpu", "--font-render-hinting=none"])
        async def worker(idx):
            page = await browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
            await page.goto(f"file://{html_path}")
            await page.evaluate("p => window.NSU.load(p)", plan_json)
            await page.evaluate("document.fonts.ready.then(()=>1)")
            for fi in range(idx, len(times), workers):
                t, name = times[fi]
                await page.evaluate("t => window.NSU.render(t)", t)
                if ext == "jpg":
                    await page.screenshot(path=str(out_dir / name), type="jpeg", quality=92)
                else:
                    await page.screenshot(path=str(out_dir / name))
                if idx == 0 and fi % 150 == 0:
                    print(f"  frame {fi}/{len(times)}", flush=True)
            await page.close()
        await asyncio.gather(*[worker(i) for i in range(workers)])
        await browser.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode_dir")
    ap.add_argument("--preview", action="store_true", help="render a few stills only")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--workers", type=int, default=max(2, min(4, os.cpu_count() or 2)))
    args = ap.parse_args()
    ep_dir = Path(args.episode_dir).resolve()
    ep = json.loads((ep_dir / "episode.json").read_text())
    out = ep_dir / "out"
    out.mkdir(exist_ok=True)

    vo = ep.get("voiceover", "voiceover.mp3")
    vpath = ep_dir / vo
    if not vpath.exists():
        cands = [p for p in ep_dir.iterdir() if p.suffix.lower() in (".mp3", ".wav", ".m4a", ".aac", ".ogg") and "music" not in p.name.lower()]
        if not cands:
            sys.exit("No voiceover audio found in the episode folder.")
        vpath = cands[0]
    print(f"voiceover: {vpath.name}")
    voice = load_audio(vpath)
    dur = len(voice) / SR + float(ep.get("tail", 0.4))
    ct = None
    tfile = vpath.with_name(vpath.stem + "_chunks.json")
    if tfile.exists():
        ct = [tuple(x) for x in json.loads(tfile.read_text())]
    words, segs = align(ep["script"], voice, chunk_times=ct)
    plan = build_plan(ep, words, dur)
    caps = build_captions(words, ep.get("highlights"))
    (out / "timing.json").write_text(json.dumps([{"w": w["raw"], "s": round(w["start"], 2), "e": round(w["end"], 2)} for w in words], indent=0))
    payload = {"ep": ep.get("ep", "??"), "dur": dur, "scenes": plan["scenes"], "hud": plan["hud"], "captions": caps,
               "accent": ep.get("accent", "#C8FF4D")}
    fonts = ensure_fonts()
    page = html_page(fonts)

    if args.preview:
        marks = [("start", 0.6)]
        for h in plan["hud"]:
            marks.append((h["type"], min(h["t1"] - 0.05, h["t0"] + 0.9)))
            if h["type"] == "choice" and h.get("tp"):
                marks.append(("picked", h["tp"] + 0.5))
        marks.append(("end", dur - 0.5))
        times = [(t, f"preview_{i:02d}_{n}.png") for i, (n, t) in enumerate(marks)]
        asyncio.run(render_frames(page, payload, times, out, workers=2, ext="png"))
        imgs = [str(out / n) for _, n in times]
        cols = min(4, len(imgs))
        sheet = out / "preview_sheet.jpg"
        flt = "".join(f"[{i}:v]scale=360:-1[v{i}];" for i in range(len(imgs)))
        rows = math.ceil(len(imgs) / cols)
        layout = "|".join(f"{(i % cols) * 360}_{(i // cols) * 640}" for i in range(len(imgs)))
        inputs = sum([["-i", p] for p in imgs], [])
        if len(imgs) > 1:
            sh(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex",
                flt + "".join(f"[v{i}]" for i in range(len(imgs))) + f"xstack=inputs={len(imgs)}:layout={layout}:fill=black", str(sheet)])
        print("preview:", sheet)
        print("timing (s):", " ".join(f"{h['type']}@{h['t0']:.1f}" for h in plan["hud"]))
        return

    frames_dir = out / "_frames"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir()
    n = int(math.ceil(dur * args.fps))
    times = [(i / args.fps, f"{i:05d}.jpg") for i in range(n)]
    print(f"rendering {n} frames ({dur:.1f} s) ...")
    asyncio.run(render_frames(page, payload, times, frames_dir, workers=args.workers))
    print("mixing audio ...")
    mix = build_audio(ep, plan, voice, dur, ep_dir)
    write_wav(out / "_mix.wav", mix)
    name = f"ep{str(ep.get('ep', 'xx')).zfill(2)}"
    mp4 = out / f"{name}.mp4"
    print("encoding ...")
    sh(["ffmpeg", "-y", "-v", "error", "-framerate", str(args.fps), "-i", str(frames_dir / "%05d.jpg"),
        "-i", str(out / "_mix.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p",
        "-af", "loudnorm=I=-14:TP=-1.2:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-shortest", "-movflags", "+faststart", str(mp4)])
    tt = resolve_time(ep.get("thumbnail"), words, dur * 0.6) if ep.get("thumbnail") else dur * 0.6
    fi = min(n - 1, int(tt * args.fps))
    shutil.copy(frames_dir / f"{fi:05d}.jpg", out / f"{name}_thumb.jpg")
    shutil.rmtree(frames_dir)
    (out / "_engine.html").unlink(missing_ok=True)
    print("done:", mp4)

if __name__ == "__main__":
    main()
