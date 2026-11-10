# DAILY PIPELINE: New Stat Unlocked

This file is the complete instruction for the daily scheduled run. Nobody is watching: don't ask questions, don't wait for approval. Make the most reasonable call, keep going, and report at the end.

Two runs happen every day at different times (see the scheduled tasks). Each run does two things:
1. **Makes one new Short** (idea → script → voice → video) and commits it to this repo.
2. **Publishes one Short per platform**: the oldest episode not yet posted there, to the New Stat Unlocked YouTube channel and Facebook page through Zernio.

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

Read `episodes.json` (it replaces WRITING.md's ALREADY MADE list). It's a list of every episode:
```json
{"ep": 1, "title": "...", "ability": "reaction time", "status": "rendered" | "posted", "video": "videos/ep01.mp4", "rendered_at": "...", "posted": {"youtube": null, "facebook": null}}
```

## 1. Pick today's idea

- Next episode number = highest `ep` in `episodes.json` + 1.
- Open `ideas.json`. Take the **first idea with `"status": "planned"`** (they're in a deliberate order that mixes body, senses and brain abilities). Mark it `"status": "used"` and add `"ep": NN`.
- Ideas come in two formats (older ones list hook/rule/beats/climax; newer ones list opening/early_wins/mystery_and_reveal/climax). Either way, it gives you the hook, the rule (the limit that makes the ability backfire), escalation beats, the climax choice, the ending and the loop, plus real facts. Treat it as a strong first draft: keep its core, improve anything that's weak, and only state facts you're confident are true. Drop any fact you're not sure of.
- If there are no planned ideas left, invent one following WRITING.md MODE 1, using an ability not already in `episodes.json`. Then add 10 new planned ideas to `ideas.json` in the same format, so tomorrow's run has a queue again.

## 2. Write the script (writer + one critic)

1. **Write it.** Follow WRITING.md MODE 2, the clarity guards and the VIRAL & RETENTION RULES. Default 45 s (130–150 words). The idea from `ideas.json` is a starting point, not a cage: keep what's strong, change what isn't.
2. **One critic pass.** Launch exactly **one** subagent with the Agent tool, `model: "sonnet"`, and a prompt containing the full text of `CRITIC.md` plus the script (and nothing about how you wrote it). This keeps usage low: never more than one critic per episode.
3. **If the verdict is REVISE:** fix every TOP FIX yourself in one rewrite, then do the loop check and word count again. Don't call the critic a second time; move on.
4. **If PASS:** keep the script as is (apply any small fixes that are obviously right).
5. Save `$R/episodes/epNN/script.md` with the final script, the HUD plan, the facts and the critic's verdict and scores (so we can learn later which scores predict views).

## 3. Build and render the video

```bash
E=$R/episodes/epNN
mkdir -p $E
```

1. Write `$E/episode.json` following `engine/ENGINE_GUIDE.md` and `engine/example_ep01_episode.json`:
   - `"ep": NN`, `"script"`: the exact script, `"voiceover": "voiceover.wav"`, `"tts_voice": "af_heart"`, `"tts_speed": 1.05`.
   - Music: pick tracks from `music/library.json` by mood and set `"music"` as described in ENGINE_GUIDE.md's Music section.
   - HUD, kept light: the stat card on the opening title question, optionally one `note` (REAL SCIENCE) at the reveal, the `choice` card at the climax, and a final `level` card on the debate question (label "WOULD YOU TAKE IT?", text "COMMENT: YES OR NO"). Use `warn`/`compare` only when they make a beat clearer. `highlights` from the HUD PLAN. A new scene every 3–6 s, `lab` for the ability/number beats, real places for the story, `slowmo` for the choice.
   - **Visual loop:** the last scene uses the same background, characters and positions as the first scene, so when the Short replays, the cut from last frame to first frame is invisible.
   - The first scene must have movement inside the first second (an object falling, a character reacting). No static opening frame.
   - Build clear, funny SVG props and objects for every beat. This is what makes the video watchable.
2. **Voice.** Read `$R/studio.json`.
   - If `"voice": "elevenlabs"`: write `$E/voice_request.json` = `{"text": <the script with 3–6 Eleven v4 audio tags like [excited] [whispers] [deadpan], words unchanged>, "voice_id": <elevenlabs_voice_id>, "model_id": <elevenlabs_model>}`. Commit and push just that file. A GitHub workflow voices it and commits `voiceover.mp3` + `voiceover_alignment.json` into `$E`. Poll every 20 s for up to 10 minutes (`git fetch origin main` then `git show FETCH_HEAD:episodes/epNN/voiceover.mp3` or `voice_error.txt`), then `git pull --rebase origin main`. Set `"voiceover": "voiceover.mp3"`. If you get `voice_error.txt` or a timeout, fall back to Kokoro below and report the error.
   - If `"voice": "kokoro"` (or as a fallback): set `"voiceover": "voiceover.wav"`, `"tts_voice"`/`"tts_speed"` from studio.json, and run `python3 $R/engine/nsu_voice.py $E`.
   - Target 40–52 s. If Kokoro comes out longer, raise `tts_speed` (max 1.2) or trim a line; if it's under 38 s, lower it.
3. Preview: `python3 $R/engine/nsu_render.py $E --preview`, then open `$E/out/preview_sheet.jpg` and look at it. Fix faces hidden by the HUD or captions, faces in the bottom 20% or at the right edge, floating characters and unreadable props, then preview again.
4. Render: `python3 $R/engine/nsu_render.py $E`. On an error, read it, fix `episode.json` and rerun (up to 3 attempts). "phrase not found" means an anchor isn't in the script.
5. Check: pull 4 frames from `$E/out/epNN.mp4` with ffmpeg (around the stat card, the warning card, the choice, and the last second) and look at them. Re-render if something is clearly broken.
6. Move the outputs:
   ```bash
   mkdir -p $R/videos
   cp $E/out/epNN.mp4 $R/videos/epNN.mp4
   cp $E/out/epNN_thumb.jpg $E/thumb.jpg
   rm -rf $E/out $E/voiceover.wav $E/voiceover_groups.json $E/voiceover_chunks.json
   ```
   If `videos/epNN.mp4` is over 40 MB, re-encode it with `ffmpeg -i in.mp4 -c:v libx264 -crf 24 -preset veryfast -c:a copy out.mp4`.
7. Write `$E/upload.md` with the MODE 5 upload pack (title, description, hashtags, tags, first comment). **The description must end with one credit line per music track used**, from `music/library.json`'s `credit_template`, e.g. `Music: "Daybreak" by Tanner Helland, CC BY 4.0, https://tannerhelland.com/music`. Include the credit lines in the YouTube and Facebook post text.
8. Add the episode to `episodes.json` with `"status": "rendered"` and `"posted": {"youtube": null, "facebook": null}`.
9. Commit and push:
   ```bash
   cd $R && git add -A && git commit -m "EP NN: <title>" && git push origin HEAD:main || (git fetch origin main && git rebase origin/main && git push origin HEAD:main)
   ```

If the episode can't be rendered after 3 attempts, don't commit a broken episode. Skip to step 4 (publishing still happens) and report the failure.

## 4. Publish (YouTube + Facebook)

Each run publishes at most **one video per platform**. The platforms are independent: if one isn't connected or fails, still do the other.

1. **Find the target accounts.** Call Zernio `accounts_list` with `platform: "youtube"`, then again with `platform: "facebook"`. On each platform the target is the account whose username or display name, lowercased with spaces removed, contains `newstatunlocked`.
   - **If a platform has no such account, skip that platform.** Never post to any other account or page (for example `dailystickchaos`), even if it's the only one on that platform.
2. **Pick the episode for each platform:** the lowest `ep` in `episodes.json` with `"status"` other than `"shelved"` that has a rendered video and isn't yet posted on that platform (`posted.youtube` / `posted.facebook` is null).
3. Its public video URL is `https://raw.githubusercontent.com/aqib1401/newstatunlocked-studio/main/videos/epNN.mp4`. Check it with `curl -sI <url>` (expect 200). Right after a push it can take a minute; retry every 20 s for up to 5 minutes.
4. **Post it** with Zernio `posts_create`, `publish_now: true`, the platform's `account_id`, and `media_urls`: the video URL.
   - **YouTube:** `platform: "youtube"`, `title`: the title from the episode's `upload.md`, `content`: the description + a blank line + the hashtags.
   - **Facebook:** `platform: "facebook"`, `content`: the title on the first line, a blank line, the description, then 3 hashtags at most (#whatif #newstatunlocked + one topic tag). Facebook posts vertical videos under 90 seconds as Reels.
5. If Zernio rejects the media or the post fails, retry once with the jsDelivr link instead (it serves the file as `video/mp4`): `https://cdn.jsdelivr.net/gh/aqib1401/newstatunlocked-studio@<commit sha that added the video>/videos/epNN.mp4` (get the sha with `git log -1 --format=%H -- videos/epNN.mp4`). If that fails too, leave that platform unposted (tomorrow's run tries again) and report Zernio's exact error.
6. **Start the conversation:** right after each successful post, add the first comment with Zernio `comments_reply_to_inbox_post` (`post_id`: the Zernio post id from step 4, `account_id`: that platform's account, no `comment_id`). Use the FIRST COMMENT line from the episode's `upload.md`. If it fails, retry once; never block the run on it. (YouTube's API can't pin comments; that stays manual.)
7. **Record it:** in `episodes.json` set `posted.<platform>` to `{"at": "<ISO time>", "zernio_post": "<post id>", "first_comment": "<comment id or null>"}`. Set `"status": "posted"` once every connected platform has it. Commit and push (same command as above).

`episodes.json` entries look like this:
```json
{"ep": 1, "title": "...", "ability": "...", "status": "rendered", "video": "videos/ep01.mp4", "rendered_at": "...", "posted": {"youtube": null, "facebook": null}}
```

## 5. Housekeeping

- Delete `videos/epNN.mp4` files for episodes posted on every connected platform more than 7 days ago (`git rm`), commit and push. Keep `episodes/` folders forever.
- Never edit the `engine/` files during a daily run.

## 6. Report

Finish with a short summary sent to the user (use SendUserMessage if it's available):
- Rendered: EP NN, "<title>" (length), or the failure reason.
- Published: per platform (YouTube, Facebook): EP NN, "<title>" → posted / skipped / failed (why).
- Anything that needs the user's attention.
