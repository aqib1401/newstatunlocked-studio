#!/usr/bin/env python3
"""
New Stat Unlocked - free narrator voice (Kokoro, open-source, Apache-2.0).

    python3 nsu_voice.py EPISODE_DIR [--voice af_heart] [--speed 1.05]

Reads "script" from EPISODE_DIR/episode.json and writes EPISODE_DIR/voiceover.wav.
The model (~350 MB) downloads once from GitHub and is cached in ~/.cache/nsu_kokoro.
Pauses are controlled here, not by the model: sentence ends, "..." and commas
get fixed silences so the delivery has the channel's dramatic rhythm.
"""
import argparse, json, re, subprocess, sys
from pathlib import Path
import numpy as np

CACHE = Path.home() / ".cache" / "nsu_kokoro"
BASE = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
FILES = ["kokoro-v1.0.onnx", "voices-v1.0.bin"]
PAUSE = {"...": 0.48, ".": 0.34, "?": 0.38, "!": 0.32, ",": 0.14, ":": 0.2, ";": 0.2}

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

def chunks(script):
    """Split into speakable chunks, each ending with the pause that follows it."""
    text = re.sub(r"\[[^\]]*\]", " ", script)          # drop ElevenLabs-style tags
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(\.\.\.|[.?!,:;])", text)
    out, buf = [], ""
    for p in parts:
        if p in PAUSE:
            buf = (buf + (p if p != "..." else ",")).strip()
            if buf.strip(",. "):
                out.append((buf, PAUSE[p]))
            buf = ""
        else:
            buf += p
    if buf.strip():
        out.append((buf.strip() + ".", 0.3))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode_dir")
    ap.add_argument("--voice", default=None)
    ap.add_argument("--speed", type=float, default=None)
    a = ap.parse_args()
    ep_dir = Path(a.episode_dir)
    ep = json.loads((ep_dir / "episode.json").read_text())
    voice = a.voice or ep.get("tts_voice", "af_heart")
    speed = a.speed or float(ep.get("tts_speed", 1.05))
    setup()
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(str(CACHE / FILES[0]), str(CACHE / FILES[1]))
    pieces, sr = [np.zeros(int(0.15 * 24000), dtype=np.float32)], 24000
    pos, times = 0.15, []
    for text, pause in chunks(ep["script"]):
        s, sr = k.create(text, voice=voice, speed=speed, lang="en-us")
        s = np.asarray(s, dtype=np.float32)
        # trim the model's own leading/trailing silence so our pauses are exact
        nz = np.where(np.abs(s) > 0.01)[0]
        if len(nz):
            s = s[max(0, nz[0] - int(0.02 * sr)): nz[-1] + int(0.05 * sr)]
        pieces += [s, np.zeros(int(pause * sr), dtype=np.float32)]
        times.append((round(pos, 3), round(pos + len(s) / sr, 3)))
        pos += len(s) / sr + int(pause * sr) / sr
    y = np.concatenate(pieces)
    y = y / (np.max(np.abs(y)) + 1e-9) * 0.9
    out = ep_dir / "voiceover.wav"
    sf.write(out, y, sr)
    (ep_dir / "voiceover_chunks.json").write_text(json.dumps(times))
    print(f"voice: {voice} @ {speed}x -> {out} ({len(y)/sr:.1f} s)")

if __name__ == "__main__":
    main()
