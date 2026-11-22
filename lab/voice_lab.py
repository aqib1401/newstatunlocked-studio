#!/usr/bin/env python3
"""
Voice lab: voice the same test passage with one open-source TTS engine, on CPU,
sentence by sentence with the channel's pause rules, and record how long it took.

    python3 lab/voice_lab.py ENGINE OUT_DIR

Runs inside GitHub Actions (free on this public repo; the runner can reach Hugging Face).
Writes OUT_DIR/<ENGINE>.wav and OUT_DIR/<ENGINE>.json (timing, real-time factor, errors).
"""
import json, re, sys, time, traceback
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
TEXT = ("What if the Earth stopped spinning? Not slowly. All at once. Right now, even sitting still, you're moving. "
        "At the equator, the ground under your feet spins at almost seventeen hundred kilometers an hour. "
        "You just can't feel it, because the air, the oceans and you are all moving with it. "
        "So when the planet slams on the brakes... nothing else does.")
REF_WAV = str(HERE / "ref_liam.wav")
REF_TXT = (HERE / "ref_liam.txt").read_text().strip()
STYLE = ("A young adult American male storyteller narrating a mind-blowing science video for YouTube. "
         "Energetic, warm and curious, with natural rises and falls, clear and confident, never robotic.")
PAUSE = {"?": 0.55, "...": 0.62, "!": 0.42, ".": 0.38, "short": 0.45}


def sentences(t):
    return [x.strip() for x in re.findall(r".+?(?:\.\.\.|[.?!])(?=\s|$)|.+$", t) if x.strip()]


def trim(a, sr, tail=0.12):
    a = np.asarray(a, dtype=np.float32).reshape(-1)
    nz = np.where(np.abs(a) > 0.003)[0]
    return a[max(0, nz[0] - int(0.04 * sr)): min(len(a), nz[-1] + int(tail * sr))] if len(nz) else a


def make_engine(name):
    import torch
    torch.set_num_threads(max(1, torch.get_num_threads()))
    if name in ("chatterbox_turbo", "chatterbox_turbo_liam"):
        from chatterbox.tts_turbo import ChatterboxTurboTTS
        try:
            m = ChatterboxTurboTTS.from_pretrained(device="cpu")
        except Exception:
            from huggingface_hub import snapshot_download
            m = ChatterboxTurboTTS.from_local(snapshot_download("ResembleAI/chatterbox-turbo", token=False), "cpu")
        ref = REF_WAV if name.endswith("_liam") else None
        def gen(t):
            kw = {"audio_prompt_path": ref} if ref else {}
            return m.generate(t, **kw).squeeze().cpu().numpy(), m.sr
        return gen
    if name in ("chatterbox", "chatterbox_liam"):
        from chatterbox.tts import ChatterboxTTS
        m = ChatterboxTTS.from_pretrained(device="cpu")
        ref = REF_WAV if name.endswith("_liam") else None
        def gen(t):
            kw = {"audio_prompt_path": ref} if ref else {}
            return m.generate(t, exaggeration=0.6, cfg_weight=0.4, **kw).squeeze().cpu().numpy(), m.sr
        return gen
    if name.startswith("qwen3"):
        from qwen_tts import Qwen3TTSModel
        size = "1.7B" if "17" in name else "0.6B"
        if "design" in name:
            m = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign", device_map="cpu", dtype=torch.float32)
            def gen(t):
                w, sr = m.generate_voice_design(text=t, language="English", instruct=STYLE)
                return w[0], sr
            return gen
        if "clone" in name:
            m = Qwen3TTSModel.from_pretrained(f"Qwen/Qwen3-TTS-12Hz-{size}-Base", device_map="cpu", dtype=torch.float32)
            prompt = m.create_voice_clone_prompt(ref_audio=REF_WAV, ref_text=REF_TXT)
            def gen(t):
                w, sr = m.generate_voice_clone(text=t, language="English", voice_clone_prompt=prompt)
                return w[0], sr
            return gen
        speaker = "Aiden" if "aiden" in name else "Ryan"
        m = Qwen3TTSModel.from_pretrained(f"Qwen/Qwen3-TTS-12Hz-{size}-CustomVoice", device_map="cpu", dtype=torch.float32)
        def gen(t):
            kw = {"instruct": "Energetic, curious storyteller narrating an amazing science fact."} if size == "1.7B" else {}
            w, sr = m.generate_custom_voice(text=t, language="English", speaker=speaker, **kw)
            return w[0], sr
        return gen
    raise SystemExit(f"unknown engine {name}")


def main():
    name, out = sys.argv[1], Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    info = {"engine": name}
    try:
        import soundfile as sf
        t0 = time.time()
        gen = make_engine(name)
        info["load_s"] = round(time.time() - t0, 1)
        t1 = time.time()
        pieces, sr = [], 24000
        for s in sentences(TEXT):
            a, sr = gen(s)
            a = trim(a, sr)
            gap = PAUSE["..."] if s.endswith("...") else PAUSE["?"] if s.endswith("?") else PAUSE["."]
            if len(s.split()) <= 3:
                gap = max(gap, PAUSE["short"])
            pieces += [a, np.zeros(int(gap * sr), dtype=np.float32)]
        y = np.concatenate(pieces)
        y = y / (np.abs(y).max() + 1e-9) * 0.9
        sf.write(out / f"{name}.wav", y, sr)
        info["gen_s"] = round(time.time() - t1, 1)
        info["audio_s"] = round(len(y) / sr, 1)
        info["realtime_factor"] = round(info["gen_s"] / info["audio_s"], 2)
        info["ok"] = True
    except Exception as e:
        info["ok"] = False
        info["error"] = f"{type(e).__name__}: {e}"
        info["trace"] = traceback.format_exc()[-3000:]
    (out / f"{name}.json").write_text(json.dumps(info, indent=1))
    print(json.dumps({k: v for k, v in info.items() if k != "trace"}))


if __name__ == "__main__":
    main()
