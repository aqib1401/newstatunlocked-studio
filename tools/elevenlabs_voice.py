#!/usr/bin/env python3
"""Runs inside GitHub Actions. For every episodes/*/voice_request.json without a
voiceover.mp3 next to it, calls ElevenLabs and saves voiceover.mp3 + voiceover_alignment.json
(word timing for captions). On failure writes voice_error.txt instead."""
import base64, json, os, sys, urllib.request, urllib.error
from pathlib import Path

KEY = os.environ.get("ELEVENLABS_API_KEY", "").strip()

def call(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"xi-api-key": KEY, "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read(), r.headers.get("Content-Type", "")

def main():
    done = 0
    for req_file in sorted(Path("episodes").glob("*/voice_request.json")):
        d = req_file.parent
        if (d / "voiceover.mp3").exists():
            continue
        (d / "voice_error.txt").unlink(missing_ok=True)
        if not KEY:
            (d / "voice_error.txt").write_text("ELEVENLABS_API_KEY secret is not set in the repo settings.")
            continue
        r = json.loads(req_file.read_text())
        body = {"text": r["text"], "model_id": r.get("model_id", "eleven_v4")}
        if r.get("voice_settings"):
            body["voice_settings"] = r["voice_settings"]
        base = f"https://api.elevenlabs.io/v1/text-to-speech/{r['voice_id']}"
        try:
            raw, _ = call(base + "/with-timestamps?output_format=mp3_44100_128", body)
            j = json.loads(raw)
            (d / "voiceover.mp3").write_bytes(base64.b64decode(j["audio_base64"]))
            if j.get("alignment"):
                (d / "voiceover_alignment.json").write_text(json.dumps(j["alignment"]))
            done += 1
        except urllib.error.HTTPError as e:
            first_err = f"{e.code} {e.read().decode(errors='ignore')[:500]}"
            try:   # some models don't support timestamps: fall back to plain audio
                raw, _ = call(base + "?output_format=mp3_44100_128", body)
                (d / "voiceover.mp3").write_bytes(raw)
                done += 1
            except urllib.error.HTTPError as e2:
                (d / "voice_error.txt").write_text(f"with-timestamps: {first_err}\nplain: {e2.code} {e2.read().decode(errors='ignore')[:500]}")
        except Exception as e:
            (d / "voice_error.txt").write_text(repr(e))
    print(f"generated {done} voiceover(s)")

if __name__ == "__main__":
    main()
