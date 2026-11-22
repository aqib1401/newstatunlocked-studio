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
    a = ap.parse_args()
    ep_dir = Path(a.episode_dir)
    ep = json.loads((ep_dir / "episode.json").read_text())
    voice = a.voice or ep.get("tts_voice", "am_michael")
    speed = a.speed or float(ep.get("tts_speed", 1.1))
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
    P = {"?": 0.55, "...": 0.62, "!": 0.42, ".": 0.38, "short": 0.45}
    P.update(ep.get("pauses") or {})
    pieces, pos, meta = [np.zeros(int(0.12 * sr), dtype=np.float32)], 0.12, []
    for g in sentences(ep["script"]):
        s, sr = k.create(g, voice=voice, speed=speed, lang="en-gb" if vname.startswith("b") else "en-us")
        s = np.asarray(s, dtype=np.float32)
        nz = np.where(np.abs(s) > 0.01)[0]
        if len(nz):
            s = s[max(0, nz[0] - int(0.02 * sr)): nz[-1] + int(0.05 * sr)]
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

if __name__ == "__main__":
    main()
