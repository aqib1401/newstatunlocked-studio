#!/usr/bin/env python3
"""
Runs inside GitHub Actions (free on this public repo; the runner can reach Hugging Face).

For every episodes/*/voice_request.json with "engine": "qwen3_clone" and no voiceover.wav yet:
  1. Voice the WHOLE script in one take with Qwen3-TTS 0.6B Base, cloned from voice/ref_liam.wav,
     so the model keeps its own natural rhythm, commas and pauses.
  2. Transcribe it (offline Whisper tiny) and check every word was spoken.
  3. If the one take drops or garbles words, re-voice in passages of a few sentences
     (still natural prosody inside each passage) and check again.
Writes voiceover.wav, voice_meta.json and voice_check.json, or voice_error.txt on failure.

voice_request.json: {"engine": "qwen3_clone", "text": "<script>", "speed": 1.0 (optional, 0.9-1.15)}
"""
import json, re, sys, time, traceback
from pathlib import Path
import numpy as np

R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / "engine"))
import nsu_voice as V  # noqa: E402  (speech check helpers)

MODEL = "Qwen/Qwen3-TTS-12Hz-0.6B-Base"
REF_WAV = R / "voice" / "ref_liam.wav"
REF_TXT = (R / "voice" / "ref_liam.txt").read_text().strip()
_model = _prompt = None


def model():
    global _model, _prompt
    if _model is None:
        import torch
        from qwen_tts import Qwen3TTSModel
        _model = Qwen3TTSModel.from_pretrained(MODEL, device_map="cpu", dtype=torch.float32)
        _prompt = _model.create_voice_clone_prompt(ref_audio=str(REF_WAV), ref_text=REF_TXT)
    return _model, _prompt


def say(text):
    m, p = model()
    try:
        w, sr = m.generate_voice_clone(text=text, language="English", voice_clone_prompt=p, max_new_tokens=4096)
    except TypeError:
        w, sr = m.generate_voice_clone(text=text, language="English", voice_clone_prompt=p)
    a = np.asarray(w[0], dtype=np.float32).reshape(-1)
    nz = np.where(np.abs(a) > 0.003)[0]
    if len(nz):
        a = a[max(0, nz[0] - int(0.04 * sr)): min(len(a), nz[-1] + int(0.15 * sr))]
    return a, sr


def passages(text, limit=320):
    out, cur = [], ""
    for s in V.sentences(text):
        if cur and len(cur) + 1 + len(s) > limit:
            out.append(cur); cur = s
        else:
            cur = (cur + " " + s).strip()
    if cur:
        out.append(cur)
    return out


def stretch(y, sr, speed):
    if abs(speed - 1.0) < 0.01:
        return y
    import subprocess, soundfile as sf, tempfile
    with tempfile.TemporaryDirectory() as td:
        sf.write(f"{td}/a.wav", y, sr)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", f"{td}/a.wav", "-filter:a", f"atempo={speed}", f"{td}/b.wav"], check=True)
        return sf.read(f"{td}/b.wav", dtype="float32")[0]


def voice_episode(d, req, rec):
    import soundfile as sf
    text = re.sub(r"\[[^\]]*\]", " ", req["text"]).strip()
    speed = float(req.get("speed", 1.0))
    meta = {"engine": "qwen3_clone", "model": MODEL, "ref": "voice/ref_liam.wav"}
    t0 = time.time()
    # 1) one take
    y, sr = say(text)
    y = stretch(y, sr, speed)
    chk = V.check_audio(rec, y, sr, text) if rec else {"ok": True, "note": "no checker"}
    meta.update(mode="full", gen_s=round(time.time() - t0, 1))
    groups = None
    if not chk["ok"]:
        # 2) passages of a few sentences, joined with a natural sentence gap
        t1 = time.time()
        pieces, groups, pos = [], [], 0.0
        for ptxt in passages(text):
            a, sr = say(ptxt)
            a = stretch(a, sr, speed)
            groups.append({"text": ptxt, "start": round(pos, 3), "end": round(pos + len(a) / sr, 3)})
            gap = 0.42 if ptxt.endswith(("?", "...")) else 0.34
            pieces += [a, np.zeros(int(gap * sr), dtype=np.float32)]
            pos += len(a) / sr + gap
        y2 = np.concatenate(pieces)
        chk2 = V.check_audio(rec, y2, sr, text) if rec else chk
        meta.update(full_take_check=chk, mode="passages", passages_gen_s=round(time.time() - t1, 1))
        if chk2["recall"] >= chk["recall"]:
            y, chk = y2, chk2
        else:
            groups = None
            meta["mode"] = "full (passages were worse)"
    y = y / (np.abs(y).max() + 1e-9) * 0.9
    sf.write(d / "voiceover.wav", y, sr)
    if groups:
        (d / "voiceover_groups.json").write_text(json.dumps(groups, indent=1))
    meta.update(audio_s=round(len(y) / sr, 1), total_s=round(time.time() - t0, 1), ok=chk["ok"])
    (d / "voice_meta.json").write_text(json.dumps(meta, indent=1))
    (d / "voice_check.json").write_text(json.dumps(chk, indent=1))
    print(f"{d.name}: {meta['mode']}, {meta['audio_s']} s audio in {meta['total_s']} s, check {'OK' if chk['ok'] else 'PROBLEM'} "
          f"(recall {chk.get('recall')}, missing {chk.get('missing')})", flush=True)


def main():
    todo = []
    for rf in sorted((R / "episodes").glob("*/voice_request.json")):
        req = json.loads(rf.read_text())
        if req.get("engine") == "qwen3_clone" and not (rf.parent / "voiceover.wav").exists():
            todo.append((rf.parent, req))
    if not todo:
        print("nothing to voice"); return
    rec = V.asr_setup()
    for d, req in todo:
        (d / "voice_error.txt").unlink(missing_ok=True)
        try:
            voice_episode(d, req, rec)
        except Exception as e:
            (d / "voice_error.txt").write_text(f"{type(e).__name__}: {e}\n{traceback.format_exc()[-2000:]}")
            print(f"{d.name}: FAILED {e}", flush=True)


if __name__ == "__main__":
    main()
