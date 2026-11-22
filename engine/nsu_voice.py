#!/usr/bin/env python3
"""
New Stat Unlocked - free narrator voice (Kokoro, open-source, Apache-2.0).

    python3 nsu_voice.py EPISODE_DIR [--voice am_michael] [--speed 1.1]

Reads "script" from EPISODE_DIR/episode.json and writes EPISODE_DIR/voiceover.wav
plus voiceover_groups.json (exact timing of each spoken group, used for caption sync).

The narration is voiced in whole sentences (grouped up to ~260 characters), so the
model keeps natural intonation across a sentence. Only a short breath is added
between groups. The model (~350 MB) downloads once from GitHub and is cached.
"""
import argparse, json, re, subprocess, sys
from pathlib import Path
import numpy as np

CACHE = Path.home() / ".cache" / "nsu_kokoro"
BASE = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
FILES = ["kokoro-v1.0.onnx", "voices-v1.0.bin"]
MAX_CHARS = 260

def setup():
    try:
        import kokoro_onnx, soundfile  # noqa
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--break-system-packages", "kokoro-onnx", "soundfile"], check=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    for f in FILES:
        p = CACHE / f
        if not p.exists() or p.stat().st_size < 1_000_000:
            print(f"downloading {f} ...", flush=True)
            subprocess.run(["curl", "-sSfL", "-o", str(p), BASE + f], check=True)

ASR = CACHE.parent / "nsu_asr" / "sherpa-onnx-whisper-tiny.en"
ASR_URL = "https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-tiny.en.tar.bz2"
NUMW = set("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen "
           "eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million billion "
           "trillion percent point half quarter".split())

def asr_setup():
    """Offline speech checker (Whisper tiny.en via sherpa-onnx, ~100 MB from GitHub). Returns None if unavailable."""
    try:
        try:
            import sherpa_onnx  # noqa
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--break-system-packages", "sherpa-onnx"], check=True)
            import sherpa_onnx  # noqa
        if not (ASR / "tiny.en-encoder.int8.onnx").exists():
            ASR.parent.mkdir(parents=True, exist_ok=True)
            tb = ASR.parent / "m.tar.bz2"
            subprocess.run(["curl", "-sSfL", "-o", str(tb), ASR_URL], check=True)
            subprocess.run(["tar", "xjf", str(tb), "-C", str(ASR.parent)], check=True)
            tb.unlink()
        return sherpa_onnx.OfflineRecognizer.from_whisper(
            encoder=str(ASR / "tiny.en-encoder.int8.onnx"), decoder=str(ASR / "tiny.en-decoder.int8.onnx"),
            tokens=str(ASR / "tiny.en-tokens.txt"), language="en", task="transcribe", num_threads=2)
    except Exception as e:
        print(f"(speech check unavailable: {e})", flush=True)
        return None

CONTRACT = [("you are", "you're"), ("we are", "we're"), ("they are", "they're"), ("i am", "i'm"), ("it is", "it's"),
            ("that is", "that's"), ("there is", "there's"), ("what is", "what's"), ("do not", "don't"), ("does not", "doesn't"),
            ("did not", "didn't"), ("can not", "can't"), ("cannot", "can't"), ("will not", "won't"), ("would not", "wouldn't"),
            ("is not", "isn't"), ("are not", "aren't"), ("was not", "wasn't"), ("you would", "you'd"), ("you will", "you'll"),
            ("you have", "you've"), ("let us", "let's"), ("he is", "he's"), ("she is", "she's"), ("could not", "couldn't")]

def _words(t):
    t = " " + re.sub(r"[^a-z0-9' ]+", " ", t.lower().replace("’", "'")) + " "
    for full, short in CONTRACT:  # "you are" and "you're" count as the same words
        t = t.replace(f" {full} ", f" {short} ")
    return re.findall(r"[a-z0-9']+", t)

def heard(rec, audio, sr, text):
    """Transcribe one sentence and compare with the script. Returns (ok, recall, transcript)."""
    from scipy.signal import resample_poly
    x = resample_poly(np.asarray(audio, dtype=np.float64), 16000, sr).astype(np.float32)
    st = rec.create_stream(); st.accept_waveform(16000, x); rec.decode_stream(st)
    hyp = st.result.text.strip()
    ref = [w for w in _words(text) if w not in NUMW]
    got = [w for w in _words(hyp) if not any(c.isdigit() for c in w) and w not in NUMW]
    if not ref:
        return True, 1.0, hyp
    import difflib
    stem = lambda w: re.sub(r"('s|s)$", "", w)[:5]
    sm = difflib.SequenceMatcher(None, [stem(w) for w in ref], [stem(w) for w in got])
    recall = sum(b.size for b in sm.get_matching_blocks()) / len(ref)
    last = stem(ref[-1])[:4]
    last_ok = any(stem(w)[:4] == last for w in got[-3:]) or len(ref) < 2
    return (recall >= 0.75 and last_ok), round(recall, 2), hyp

def check_audio(rec, y, sr, script, win=24.0):
    """Check a whole voiceover against the script. Splits at pauses into <= win s windows,
    transcribes each, and returns {"recall", "last_ok", "missing", "heard", "ok"}."""
    from scipy.signal import resample_poly
    import difflib
    x = resample_poly(np.asarray(y, dtype=np.float64), 16000, sr).astype(np.float32)
    H = 320; e = np.array([np.sqrt(np.mean(x[i:i + H] ** 2)) for i in range(0, len(x) - H, H)])
    quiet = e < (e.max() * 0.03)
    cuts, start = [], 0
    while start < len(x):
        end = min(len(x), start + int(win * 16000))
        if end < len(x):  # back up to the longest quiet spot in the last 6 s of the window
            lo, hi = (end - 6 * 16000) // H, end // H
            q = np.where(quiet[lo:hi])[0]
            if len(q):
                end = (lo + q[len(q) // 2]) * H
        cuts.append((start, end)); start = end
    hyp = []
    for a, b in cuts:
        st = rec.create_stream(); st.accept_waveform(16000, x[a:b]); rec.decode_stream(st); hyp.append(st.result.text.strip())
    hyp = " ".join(hyp)
    stem = lambda w: re.sub(r"('s|s)$", "", w)[:5]
    ref = [w for w in _words(script) if w not in NUMW]
    got = [w for w in _words(hyp) if not any(c.isdigit() for c in w) and w not in NUMW]
    sm = difflib.SequenceMatcher(None, [stem(w) for w in ref], [stem(w) for w in got], autojunk=False)
    matched = set()
    for bl in sm.get_matching_blocks():
        matched.update(range(bl.a, bl.a + bl.size))
    missing, run = [], []
    for i, w in enumerate(ref):  # report runs of 2+ consecutive missing words (single misses are usually ASR noise)
        if i in matched:
            if len(run) >= 2: missing.append(" ".join(run))
            run = []
        else:
            run.append(w)
    if len(run) >= 2: missing.append(" ".join(run))
    recall = len(matched) / max(1, len(ref))
    last_ok = any(stem(w)[:4] == stem(ref[-1])[:4] for w in got[-4:]) if ref else True
    return {"recall": round(recall, 3), "last_ok": last_ok, "missing": missing, "heard": hyp,
            "ok": recall >= 0.93 and last_ok and not missing}

PARA = CACHE.parent / "nsu_asr" / "sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8"
PARA_URL = "https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8.tar.bz2"

def align_words(ep_dir, script, vo_name="voiceover.wav"):
    """Exact word timing for a voiceover made in one take (Qwen): transcribe with a timestamped
    speech model (Parakeet, ~630 MB from GitHub), match the script's words to it, and write
    voiceover_alignment.json in the ElevenLabs character format the renderer already reads."""
    import soundfile as sf, difflib
    import sherpa_onnx
    from scipy.signal import resample_poly
    if not (PARA / "encoder.int8.onnx").exists():
        PARA.parent.mkdir(parents=True, exist_ok=True)
        tb = PARA.parent / "p.tar.bz2"
        subprocess.run(["curl", "-sSfL", "-o", str(tb), PARA_URL], check=True)
        subprocess.run(["tar", "xjf", str(tb), "-C", str(PARA.parent)], check=True); tb.unlink()
    rec = sherpa_onnx.OfflineRecognizer.from_transducer(
        encoder=str(PARA / "encoder.int8.onnx"), decoder=str(PARA / "decoder.int8.onnx"), joiner=str(PARA / "joiner.int8.onnx"),
        tokens=str(PARA / "tokens.txt"), model_type="nemo_transducer", num_threads=2)
    y, sr = sf.read(str(ep_dir / vo_name), dtype="float32", always_2d=False)
    y = y.mean(axis=1) if y.ndim > 1 else y
    x = resample_poly(y.astype(np.float64), 16000, sr).astype(np.float32)
    dur = len(x) / 16000
    # windows of <= 25 s, cut at quiet spots
    H = 320; e = np.array([np.sqrt(np.mean(x[i:i + H] ** 2)) for i in range(0, len(x) - H, H)]); quiet = e < e.max() * 0.03
    hyp, start = [], 0
    while start < len(x):
        end = min(len(x), start + 25 * 16000)
        if end < len(x):
            lo, hi = (end - 6 * 16000) // H, end // H; q = np.where(quiet[lo:hi])[0]
            if len(q): end = (lo + q[len(q) // 2]) * H
        st = rec.create_stream(); st.accept_waveform(16000, x[start:end]); rec.decode_stream(st)
        r = st.result; off = start / 16000; cur = None
        for tok, t in zip(r.tokens, r.timestamps):
            if tok.startswith(" ") or cur is None:
                if cur: hyp.append(cur)
                cur = {"w": tok.strip(), "s": off + t}
            else:
                cur["w"] += tok
        if cur: hyp.append(cur)
        start = end
    for i, h in enumerate(hyp):
        nxt = hyp[i + 1]["s"] if i + 1 < len(hyp) else dur
        h["e"] = min(nxt, h["s"] + 0.15 + 0.075 * len(h["w"]))
        h["n"] = re.sub(r"('s|s)$", "", re.sub(r"[^a-z0-9']", "", h["w"].lower()))[:5]
    # match script words to heard words
    toks = [t for t in _render_tokenize(script)]
    ref = [re.sub(r"('s|s)$", "", t["norm"])[:5] for t in toks]
    sm = difflib.SequenceMatcher(None, ref, [h["n"] for h in hyp], autojunk=False)
    T = [None] * len(toks)
    for bl in sm.get_matching_blocks():
        for k in range(bl.size):
            T[bl.a + k] = (hyp[bl.b + k]["s"], hyp[bl.b + k]["e"])
    # fill gaps (numbers like "seventeen hundred" -> "1700", ASR slips) by spreading between neighbours
    i = 0
    while i < len(T):
        if T[i] is None:
            j = i
            while j < len(T) and T[j] is None: j += 1
            a = T[i - 1][1] if i > 0 else 0.0
            b = T[j][0] if j < len(T) else dur
            n = j - i; w = [len(toks[k]["norm"]) + 1.5 for k in range(i, j)]; tot = sum(w); c = a
            for k in range(i, j):
                d = (b - a) * w[k - i] / tot; T[k] = (c, c + d); c += d
            i = j
        else:
            i += 1
    chars, cs, ce = [], [], []
    for t, (a, b) in zip(toks, T):
        if chars:
            chars.append(" "); cs.append(a); ce.append(a)
        for ch in t["raw"].split(" ")[0]:
            chars.append(ch); cs.append(round(a, 3)); ce.append(round(b, 3))
    (ep_dir / "voiceover_alignment.json").write_text(json.dumps(
        {"characters": chars, "character_start_times_seconds": cs, "character_end_times_seconds": ce}))
    matched = sum(1 for bl in sm.get_matching_blocks() for _ in range(bl.size))
    return matched, len(toks)

def _render_tokenize(script):
    script = re.sub(r"\[[^\]]*\]", " ", script)
    toks = []
    for m in re.finditer(r"\S+", script):
        raw = m.group(0)
        norm = re.sub(r"[^a-z0-9']", "", raw.lower().replace("’", "'"))
        if norm:
            toks.append({"raw": raw, "norm": norm})
        elif toks:
            toks[-1]["raw"] += " " + raw
    return toks

def sentences(script):
    text = re.sub(r"\[[^\]]*\]", " ", script)
    text = re.sub(r"\s+", " ", text).strip()
    return [x.strip() for x in re.findall(r".+?(?:\.\.\.|[.?!])(?=\s|$)|.+$", text) if x.strip()]

def groups(script):
    text = re.sub(r"\[[^\]]*\]", " ", script)
    text = re.sub(r"\s+", " ", text).strip()
    sents = re.findall(r".+?(?:\.\.\.|[.?!])(?=\s|$)|.+$", text)
    out, cur = [], ""
    for s in (x.strip() for x in sents if x.strip()):
        if cur and len(cur) + 1 + len(s) > MAX_CHARS:
            out.append(cur); cur = s
        else:
            cur = (cur + " " + s).strip()
    if cur:
        out.append(cur)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode_dir")
    ap.add_argument("--voice", default=None)
    ap.add_argument("--speed", type=float, default=None)
    ap.add_argument("--no-check", action="store_true", help="skip the speech check")
    ap.add_argument("--check-only", action="store_true", help="only check an existing voiceover against the script")
    ap.add_argument("--align", action="store_true", help="write exact word timing (voiceover_alignment.json) for an existing one-take voiceover")
    a = ap.parse_args()
    ep_dir = Path(a.episode_dir)
    ep = json.loads((ep_dir / "episode.json").read_text())
    voice = a.voice or ep.get("tts_voice", "am_michael")
    speed = a.speed or float(ep.get("tts_speed", 1.1))
    if a.align:
        m, n = align_words(ep_dir, ep["script"], ep.get("voiceover", "voiceover.wav"))
        print(f"aligned: {m}/{n} words matched exactly, the rest placed between neighbours -> voiceover_alignment.json")
        sys.exit(0)
    if a.check_only:
        import soundfile as sf
        vo = ep_dir / ep.get("voiceover", "voiceover.wav")
        y, sr0 = sf.read(str(vo), dtype="float32", always_2d=False)
        y = y.mean(axis=1) if y.ndim > 1 else y
        r = check_audio(asr_setup(), y, sr0, ep["script"])
        (ep_dir / "voice_check.json").write_text(json.dumps(r, indent=1))
        print(f"speech check: {'OK' if r['ok'] else 'PROBLEM'} (recall {r['recall']:.0%}, last word {'ok' if r['last_ok'] else 'MISSING'})"
              + (f", missing: {r['missing']}" if r["missing"] else ""))
        sys.exit(0 if r["ok"] else 3)
    setup()
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(str(CACHE / FILES[0]), str(CACHE / FILES[1]))
    # "am_fenrir+am_eric" blends voices 50/50; "am_fenrir:0.6+am_eric:0.4" sets the weights.
    vname = voice
    if "+" in voice:
        parts = [p.split(":") for p in voice.split("+")]
        ws = [float(p[1]) if len(p) > 1 else 1.0 for p in parts]
        voice = sum(k.get_voice_style(p[0]) * (w / sum(ws)) for p, w in zip(parts, ws))
    sr = 24000
    # Each sentence is voiced on its own, then joined with a real pause that fits its punctuation,
    # so "What if the Earth stopped spinning?" ... "Not slowly." never run into each other.
    P = {"?": 0.46, "...": 0.53, "!": 0.33, ".": 0.29, "short": 0.36}  # plus ~0.09 s of kept tail = heard pause
    P.update(ep.get("pauses") or {})
    pieces, pos, meta = [np.zeros(int(0.12 * sr), dtype=np.float32)], 0.12, []
    lang = "en-gb" if vname.startswith("b") else "en-us"
    def synth(text, spd, tail):
        a, r = k.create(text, voice=voice, speed=spd, lang=lang, trim=False)
        a = np.asarray(a, dtype=np.float32)
        # Trim only real silence: a low threshold plus generous margins so soft word endings
        # ("s", "t", "f") are never shaved off.
        nz = np.where(np.abs(a) > 0.002)[0]
        if len(nz):
            a = a[max(0, nz[0] - int(0.05 * r)): min(len(a), nz[-1] + int(tail * r))]
        return a, r
    rec = asr_setup() if not a.no_check else None
    report, bad = [], 0
    for g in sentences(ep["script"]):
        s, sr = synth(g, speed, 0.14)
        if rec is not None:
            ok, recall, hyp = heard(rec, s, sr, g)
            if not ok:  # re-voice once, a touch slower with more tail, keep the better take
                s2, _ = synth(g, speed * 0.95, 0.22)
                ok2, recall2, hyp2 = heard(rec, s2, sr, g)
                if recall2 > recall or ok2:
                    s, ok, recall, hyp = s2, ok2, recall2, hyp2
            report.append({"text": g, "heard": hyp, "recall": recall, "ok": ok})
            bad += 0 if ok else 1
        if g.endswith("..."):
            gap = P["..."]
        elif g.endswith("?"):
            gap = P["?"]
        elif g.endswith("!"):
            gap = P["!"]
        else:
            gap = P["."]
        if len(g.split()) <= 3:
            gap = max(gap, P["short"])  # punchy fragments ("Not slowly.") need air around them
        meta.append({"text": g, "start": round(pos, 3), "end": round(pos + len(s) / sr, 3)})
        pieces += [s, np.zeros(int(gap * sr), dtype=np.float32)]
        pos += len(s) / sr + int(gap * sr) / sr
    y = np.concatenate(pieces)
    y = y / (np.max(np.abs(y)) + 1e-9) * 0.9
    sf.write(ep_dir / "voiceover.wav", y, sr)
    (ep_dir / "voiceover_groups.json").write_text(json.dumps(meta, indent=1))
    old = ep_dir / "voiceover_chunks.json"
    if old.exists():
        old.unlink()
    print(f"voice: {vname} @ {speed}x -> {ep_dir/'voiceover.wav'} ({len(y)/sr:.1f} s, {len(meta)} groups)")
    if report:
        (ep_dir / "voice_check.json").write_text(json.dumps(report, indent=1))
        print(f"speech check: {len(report) - bad}/{len(report)} sentences fully heard" + ("" if not bad else
              f". CHECK THESE in voice_check.json: " + " | ".join(r["text"] for r in report if not r["ok"])))

if __name__ == "__main__":
    main()
