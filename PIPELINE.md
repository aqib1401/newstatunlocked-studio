# DAILY PIPELINE: New Stat Unlocked (v2)

This file is the complete instruction for each scheduled run. Nobody is watching: don't ask questions, don't wait for approval. Make the most reasonable call, keep going, and report at the end.

Two runs happen every day at different times. Each run:
1. **Learns** from the latest numbers.
2. **Makes one new Short** (idea → script → critic → voice → video) and commits it.
3. **Publishes one Short per platform** to the New Stat Unlocked YouTube channel and Facebook page through Zernio.

**You have creative freedom.** The rules below protect variety and quality; inside them, pick the idea, the story shape, the length, the look and the ending that make *this* video the one a stranger can't scroll past. If an idea in the bank is weak, invent a better one. If you think a rule is hurting the videos, follow it anyway this run and say so in the report.

Paths assume the repo is cloned at `/home/claude/newstatunlocked-studio` (`$R`).

---

## 0. Setup

```bash
R=/home/claude/newstatunlocked-studio
cd $R && git config user.name "NSU Studio Bot" && git config user.email "bot@newstatunlocked.local"
git fetch origin main && git reset --hard origin/main
```

Read, in this order: `LEARNINGS.md`, `WRITING.md`, `engine/ENGINE_GUIDE.md`. They replace anything you remember about how this channel used to work (no countdowns, no kid-in-danger climax, no purple-room-only videos).

## 1. Learn (one call per platform, cheap)

1. Zernio `accounts_list` with `platform: "youtube"`, then `"facebook"`. The target on each platform is the account whose username or display name, lowercased with spaces removed, contains `newstatunlocked`. Never touch any other account (for example `dailystickchaos`).
2. Zernio `analytics_get_analytics` for each target account: `account_id`, `limit: 40`, `sort_by: "date"`, `from_date`: 30 days ago. Save each raw result to a file (`/tmp/yt.json`, `/tmp/fb.json`) exactly as returned.
3. `python3 $R/tools/learn.py --youtube /tmp/yt.json --facebook /tmp/fb.json`. This writes per-episode stats into `episodes.json` and refreshes the table in `LEARNINGS.md`.
4. Read the table. If something new and real shows up (a lane, shape or length clearly beating the others over at least 3 videos each, a v2 video breaking past 5,000 views, Facebook watch time jumping), add **one dated line** to the Log in `LEARNINGS.md`. Don't add a line when nothing changed.

## 2. Pick today's idea

- Next episode number = highest `ep` in `episodes.json` + 1.
- Look at the last 6 episodes in `episodes.json` (`lane`, `shape`, `ending`, `duration_s`) so today's video is different:
  - not the same lane as both of the last two episodes
  - not the same shape or ending as the previous episode
  - over any 4 v2 episodes, at least one under 60 s and at least one over 100 s
- **Exploit vs. explore.** Once there are at least 8 v2 episodes with 48 h+ of stats, about 2 runs in 3 should lean on what the table says works (best lane, shape, length), and 1 in 3 should test something new. Before that, explore freely.
- Choose from `ideas.json`: ideas with `"status": "planned"` and `"v": 2` first. These are seeds (premise, real-science spine, possible twist), not scripts: keep what's strong, change what isn't. v1-style planned ideas (no `"v"`) are a backlog: use one only if it passes WRITING.md's playground test as a big, extreme fantasy.
- You may invent a new idea instead if it's clearly stronger than everything in the bank (WRITING.md section 1). Add it to `ideas.json` as used.
- Mark the chosen idea `"status": "used"`, `"ep": NN`.
- If fewer than 10 `"v": 2` ideas are still planned, add 10 new ones across all four lanes in the same format (title, lane, premise, science, twist), checked against every title already in `ideas.json` and `episodes.json`.

## 3. Write the script (writer + one critic)

1. Write it following WRITING.md (lane, shape, ending, length the story deserves). Save the draft in the WRITING.md section 5 format.
2. **One critic pass.** Launch exactly **one** subagent with the Agent tool, `model: "sonnet"`, with a prompt containing: the full text of `CRITIC.md`, a "RECENT EPISODES" list (for each of the last 5 episodes: title, lane, shape, ending and its first sentence; read the first sentence from `episodes/epNN/episode.json` "script"), and the script. Nothing about how you wrote it.
3. **REVISE:** fix every TOP FIX in one rewrite yourself, then re-check facts, freshness and length. Don't call the critic again.
4. **PASS:** keep it (apply obvious small fixes).
5. Save the final `$R/episodes/epNN/script.md` including the critic's verdict and scores.

## 4. Build, voice and render

```bash
E=$R/episodes/epNN && mkdir -p $E
```

1. **Voice first** (so you direct to real timing). Read `$R/studio.json`.
   - **`"voice": "qwen3_clone"` (the channel voice):** open-source Qwen3-TTS, cloned from `voice/ref_liam.wav`, voiced on free GitHub Actions as **one take of the whole script** so the model keeps its own natural rhythm and pauses.
     1. Write a minimal `$E/episode.json` (`"ep"`, `"script"`, `"voiceover": "voiceover.wav"`, `"scenes": [{"bg": "void"}]`, `"hud": []`) and `$E/voice_request.json` = `{"engine": "qwen3_clone", "text": <the script>, "speed": <qwen_speed>}`.
     2. Commit and push just those two files (`git add $E && git commit -m "EP NN: voice request" && git push origin HEAD:main`). The Voice workflow starts on its own.
     3. Poll every 30 s for up to 25 minutes: `git fetch origin main`, then `git show FETCH_HEAD:episodes/epNN/voiceover.wav > /dev/null 2>&1` (done) or `git show FETCH_HEAD:episodes/epNN/voice_error.txt` (failed). Typical time: 5–10 minutes. While you wait, plan the scenes.
     4. `git pull --rebase origin main`. Read `$E/voice_check.json`: `"ok": true` means every word was heard. `voice_meta.json` says whether it was one take (`full`) or re-voiced in passages. If `voiceover_groups.json` exists, the renderer uses it for exact caption timing; otherwise it aligns captions from the audio.
     5. **Fallback** (error, timeout, or `"ok": false`): voice it locally with Kokoro instead: set `"tts_voice"` = `kokoro_voice`, `"tts_speed"` = `kokoro_speed` in `episode.json`, delete `$E/voiceover.wav`, run `python3 $R/engine/nsu_voice.py $E`, and say so in the report.
   - **`"voice": "kokoro"`:** set `"voiceover": "voiceover.wav"`, `"tts_voice"` = `kokoro_voice`, `"tts_speed"` = `kokoro_speed`, `"scenes": [{"bg": "void"}]`, `"hud": []`, then `python3 $R/engine/nsu_voice.py $E`. It prints `speech check: N/N sentences fully heard`; if a sentence is flagged, rephrase it and voice again.
   - **`"voice": "elevenlabs"`:** same as qwen3_clone, but the request is `{"engine": "elevenlabs", "text": <script with 3–6 Eleven v4 audio tags>, "voice_id": <elevenlabs_voice_id>, "model_id": <elevenlabs_model>}` and the result is `voiceover.mp3` (needs the ELEVENLABS_API_KEY repo secret).
   - Any engine: you can re-check a voiceover any time with `python3 $R/engine/nsu_voice.py $E --check-only`. Never ship a voiceover that fails the check.
   - If the voiceover is far off the length you planned, trim lines and voice again rather than changing the speed.
2. **Direct it.** Write the full `$E/episode.json` following ENGINE_GUIDE.md, especially **Motion and camera tools (v2)** and **Directing rules (v2)**. Write it with a small Python script (`$E/build.py`) when there are many props; reusable SVG strings keep it manageable. Checklist:
   - Open on the subject in motion with a `title` card of the spoken question. Something moves in the first half second.
   - 40%+ of scenes without the hero; a continuous motion source in every scene; no two consecutive scenes with the same background and camera; `lab` at most once.
   - 3–6 `title` cards for key numbers and words; at most 2 game cards; no `countdown`; no timer `choice`.
   - `shakes` / `flashes` / `transition` on the 2–4 biggest beats.
   - Music from `music/library.json`, max 3 segments, following the story's mood; don't reuse the exact track pair from the last 2 episodes.
   - The last scene echoes the first shot so the loop is seamless.
   - Set `"thumbnail"` to an anchor on the most striking frame.
3. **Preview:** `python3 $R/engine/nsu_render.py $E --preview`, open `$E/out/preview_sheet.jpg` (one still per scene) and look at it properly. Fix overlaps (title cards vs captions vs faces), faces in the bottom 20% or past x 470, empty or confusing frames, props that don't read. Ask: do any three stills look like three different places? Preview again after real changes.
4. **Render:** `python3 $R/engine/nsu_render.py $E`. On an error, read it, fix `episode.json`, rerun (up to 3 attempts). "phrase not found" means an anchor isn't in the script.
5. **Check:** pull 5 frames from `$E/out/epNN.mp4` with ffmpeg (0.3 s, 3 s, middle, the biggest beat, last second) and look at them. Re-render only if something is clearly broken.
6. **Move the outputs:**
   ```bash
   mkdir -p $R/videos
   cp $E/out/epNN.mp4 $R/videos/epNN.mp4
   cp $E/out/epNN_thumb.jpg $E/thumb.jpg
   rm -rf $E/out $E/voiceover_chunks.json
   # keep voiceover.wav, voice_request.json, voice_meta.json and voice_check.json: they are small and the Voice workflow skips episodes that already have a voiceover
   ```
   Over 40 MB? `ffmpeg -i in.mp4 -c:v libx264 -crf 24 -preset veryfast -c:a copy out.mp4`.
7. Write `$E/upload.md` (WRITING.md section 6). The description ends with one credit line per music track, from `music/library.json`'s `credit_template`.
8. Add the episode to `episodes.json`:
   ```json
   {"ep": NN, "v": 2, "title": "...", "lane": "MIND|BODY|TIME|WORLD", "shape": "A epic|B timeline|C spiral|D twist|E survival|F dilemma",
    "ending": "fact|twist|dilemma|question|punchline", "duration_s": 0.0, "status": "rendered", "video": "videos/epNN.mp4",
    "rendered_at": "<ISO>", "critic": "<verdict + average>", "posted": {"youtube": null, "facebook": null}}
   ```
9. Commit and push:
   ```bash
   cd $R && git add -A && git commit -m "EP NN: <title>" && git push origin HEAD:main || (git fetch origin main && git rebase origin/main && git push origin HEAD:main)
   ```

If the episode can't be rendered after 3 attempts, don't commit a broken episode. Skip to step 5 (publishing still happens) and report the failure.

## 5. Publish (YouTube + Facebook)

At most **one video per platform** per run. Platforms are independent: if one fails, still do the other.

1. **Pick the episode for each platform:** the lowest `ep` with `"v": 2`, `"status"` not `"shelved"`, a video in `videos/`, and nothing posted yet on that platform. If there is none, fall back to the lowest `"status": "reserve"` episode not yet posted there (old v1 videos kept for emergencies).
2. Video URL: `https://raw.githubusercontent.com/aqib1401/newstatunlocked-studio/main/videos/epNN.mp4`. Check it with `curl -sI` (expect 200); right after a push, retry every 20 s for up to 5 minutes.
3. Read the episode's `upload.md`. **TITLE = the TITLE line exactly** (short, Title Case). Never use the description's first sentence as the title.
4. Post with Zernio `posts_create`, `publish_now: true`, the platform's `account_id`, `media_urls`: the video URL.
   - **YouTube:** `platform: "youtube"`, `title`: TITLE, `content`: the description + a blank line + the hashtags.
   - **Facebook:** `platform: "facebook"`, `content`: TITLE on the first line, a blank line, the description, then at most 3 hashtags (#whatif #newstatunlocked + one topic tag).
5. If Zernio rejects the media or the post fails, retry once with jsDelivr: `https://cdn.jsdelivr.net/gh/aqib1401/newstatunlocked-studio@<sha>/videos/epNN.mp4` (`git log -1 --format=%H -- videos/epNN.mp4`). If that fails too, leave it for the next run and report Zernio's exact error.
6. **First comment:** right after each successful post, Zernio `comments_reply_to_inbox_post` (`post_id`: the Zernio post id, `account_id`, no `comment_id`) with the FIRST COMMENT from `upload.md`. Retry once on failure; never block the run on it.
7. **Record it** in `episodes.json`: `posted.<platform>` = `{"at": "<ISO>", "zernio_post": "<post id>", "first_comment": "<comment id or null>"}`. Set `"status": "posted"` once both platforms have it. Commit and push.

## 6. Housekeeping

- Delete `videos/epNN.mp4` for episodes posted on every connected platform more than 7 days ago (`git rm`), commit, push. Keep `episodes/` folders forever. Keep reserve videos until they're posted or 21 days old.
- Engine changes: allowed only to fix a clear bug that blocks today's render, or to add a small, backward-compatible capability the story genuinely needs (a new background, prop helper or effect). Document anything you add in ENGINE_GUIDE.md in the same commit, test it with `--preview`, and mention it in the report.

## 7. Report

Finish with a short summary (use SendUserMessage if available):
- **Made:** EP NN "<title>": lane, shape, ending, length, critic verdict + scores. Or the failure reason.
- **Published:** per platform: EP NN "<title>" → posted / skipped / failed (why).
- **Numbers:** v2 median vs v1 median so far, the best v2 video, and anything new in LEARNINGS.md.
- Anything that needs the user's attention.
