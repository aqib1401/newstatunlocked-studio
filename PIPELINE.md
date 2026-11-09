# DAILY PIPELINE: New Stat Unlocked

This file is the complete instruction for the daily scheduled run. Nobody is watching: don't ask questions, don't wait for approval. Make the most reasonable call, keep going, and report at the end.

Each run does two things:
1. **Makes one new Short** (idea → script → voice → video) and commits it to this repo.
2. **Publishes exactly one Short**: the oldest episode that's rendered but not yet posted, to the New Stat Unlocked YouTube channel through Zernio.

There's normally a one-video buffer: today's run publishes yesterday's video and renders tomorrow's. If a render fails, the channel still posts that day.

Paths below assume the repo is cloned at `/home/claude/newstatunlocked-studio` (call it `$R`).

---

## 0. Setup

```bash
R=/home/claude/newstatunlocked-studio
cd $R && git config user.name "NSU Studio Bot" && git config user.email "bot@newstatunlocked.local"
git fetch origin main && git reset --hard origin/main
```

Read these before doing anything else: `WRITING.md` (channel rules, MODE 1, MODE 2 and MODE 5) and `engine/ENGINE_GUIDE.md` (how to build `episode.json`). Ignore WRITING.md's MODE 4: this file replaces it.

Read `episodes.json`. It's a list of every episode:
```json
{"ep": 1, "title": "...", "ability": "reaction time", "status": "rendered" | "posted", "video": "videos/ep01.mp4", "rendered_at": "...", "posted_at": null, "zernio_post": null}
```

## 1. Pick today's idea

- Next episode number = highest `ep` + 1.
- Following WRITING.md MODE 1, think of 10 candidate titles. Throw out anything whose ability is already used in `episodes.json` (same ability at a different number counts as used for the next 10 episodes), and anything too close to an existing title.
- Pick the single strongest: clearest picture, biggest cost, most drawable as stick-figure animation, best climax choice.
- Vary the ability category from the last 3 episodes (don't do three brain abilities in a row).

## 2. Write the script

- Follow WRITING.md MODE 2 exactly. Length 60 s (155–170 words).
- Run the silent self-check, especially: **standalone** (a stranger understands everything), **flows like one story told out loud**, no catchphrases, every side character introduced by relationship, at least 3 real facts, nothing invented.
- Rewrite it once more with fresh eyes before moving on. The script is what decides whether people keep watching.
- Save `$R/episodes/epNN/script.md` with the full MODE 2 output block (title, script, HUD plan, facts, loop check).

## 3. Build and render the video

```bash
E=$R/episodes/epNN
mkdir -p $E
```

1. Write `$E/episode.json` following `engine/ENGINE_GUIDE.md` and `engine/example_ep01_episode.json`:
   - `"ep": NN`, `"script"`: the exact script, `"voiceover": "voiceover.wav"`, `"tts_voice": "af_heart"`, `"tts_speed": 1.05`.
   - `hud` and `highlights` from the HUD PLAN. A new scene every 3–6 s, `lab` for the ability/number beats, real places for the story, `slowmo` for the choice, and the last scene setting up the loop.
   - Build clear, funny SVG props and objects for every beat. This is what makes the video watchable.
2. Voice: `python3 $R/engine/nsu_voice.py $E`. Target 52–64 s. If it's longer, raise `tts_speed` (max 1.2) and rerun; if it's under 50 s, lower it (min 0.95).
3. Preview: `python3 $R/engine/nsu_render.py $E --preview`, then open `$E/out/preview_sheet.jpg` and look at it. Fix faces hidden by the HUD or captions, faces in the bottom 20% or at the right edge, floating characters and unreadable props, then preview again.
4. Render: `python3 $R/engine/nsu_render.py $E`. On an error, read it, fix `episode.json` and rerun (up to 3 attempts). "phrase not found" means an anchor isn't in the script.
5. Check: pull 4 frames from `$E/out/epNN.mp4` with ffmpeg (around the stat card, the warning card, the choice, and the last second) and look at them. Re-render if something is clearly broken.
6. Move the outputs:
   ```bash
   mkdir -p $R/videos
   cp $E/out/epNN.mp4 $R/videos/epNN.mp4
   cp $E/out/epNN_thumb.jpg $E/thumb.jpg
   rm -rf $E/out $E/voiceover.wav $E/voiceover_chunks.json
   ```
   If `videos/epNN.mp4` is over 40 MB, re-encode it with `ffmpeg -i in.mp4 -c:v libx264 -crf 24 -preset veryfast -c:a copy out.mp4`.
7. Write `$E/upload.md` with the MODE 5 upload pack (title, description, hashtags, tags, pinned comment).
8. Add the episode to `episodes.json` with `"status": "rendered"`.
9. Commit and push:
   ```bash
   cd $R && git add -A && git commit -m "EP NN: <title>" && git push origin HEAD:main || (git fetch origin main && git rebase origin/main && git push origin HEAD:main)
   ```

If the episode can't be rendered after 3 attempts, don't commit a broken episode. Skip to step 4 (publishing still happens) and report the failure.

## 4. Publish one Short

1. Find the target account: call Zernio `accounts_list` with `platform: "youtube"`. The target is the account whose username or display name, lowercased with spaces removed, contains `newstatunlocked`.
   - **If no such account exists, do NOT post anything.** Never post to any other account (for example `dailystickchaos`), even if it's the only YouTube account. Report "New Stat Unlocked isn't connected in Zernio yet" and finish.
2. Pick the episode to post: the lowest `ep` in `episodes.json` with `"status": "rendered"`. If there isn't one, finish.
3. Its public video URL is `https://raw.githubusercontent.com/aqib1401/newstatunlocked-studio/main/videos/epNN.mp4`. Check it with `curl -sI <url>` (expect 200). Right after a push it can take a minute; retry every 20 s for up to 5 minutes.
4. Post it with Zernio `posts_create`:
   - `platform: "youtube"`, `account_id`: the id from step 1
   - `title`: the episode's title from its `upload.md`
   - `content`: the description + a blank line + the hashtags from its `upload.md`
   - `media_urls`: the raw URL
   - `publish_now: true`
5. If Zernio reports an error, retry once. If it still fails, leave the status as `rendered` (tomorrow's run will try again) and report the error.
6. On success: set that episode's `"status": "posted"`, `"posted_at"` (ISO time) and `"zernio_post"` (the post id from the response), then commit and push (same command as above).

## 5. Housekeeping

- Delete `videos/epNN.mp4` files for episodes posted more than 7 days ago (`git rm`), commit and push. Keep `episodes/` folders forever.
- Never edit the `engine/` files during a daily run.

## 6. Report

Finish with a short summary sent to the user (use SendUserMessage if it's available):
- Rendered: EP NN, "<title>" (length), or the failure reason.
- Published: EP NN, "<title>" → posted / not posted (why).
- Anything that needs the user's attention.
