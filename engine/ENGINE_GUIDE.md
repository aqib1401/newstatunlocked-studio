# ENGINE GUIDE: writing episode.json for nsu_render.py

The engine turns `episode.json` + `voiceover.mp3` into a finished 1080×1920 Short. You (Claude) write `episode.json`. The engine handles everything else automatically: word timing from the audio, captions, the game HUD, camera moves, blinking and breathing, transitions, sound effects, background music, mixing and loudness.

The example `example_ep01_episode.json` is a complete, working episode. Copy its patterns.

## Folder and commands

```
/home/claude/newstatunlocked-studio/engine/nsu_render.py
/home/claude/newstatunlocked-studio/engine/nsu_engine.html      (must sit next to nsu_render.py)
/home/claude/nsu/ep01/episode.json
/home/claude/nsu/ep01/voiceover.mp3           (the user's ElevenLabs file, any name/format)
/home/claude/nsu/ep01/music.mp3               (optional)

python3 /home/claude/newstatunlocked-studio/engine/nsu_render.py /home/claude/nsu/ep01 --preview   # ~10 s, stills + preview_sheet.jpg
python3 /home/claude/newstatunlocked-studio/engine/nsu_render.py /home/claude/nsu/ep01             # ~2-3 min, out/ep01.mp4 + out/ep01_thumb.jpg
```

`out/timing.json` lists every word with its start and end time. Read it if a scene lands at the wrong moment.

## Coordinates

The layout is 540 × 960 (rendered at 2×). x goes right, y goes down.
- **HUD** occupies y 88–300. **Captions** sit around y 300–400. Keep characters' heads below y ≈ 430.
- **Bottom 20%** (y > 768) is floor only: feet can stand there, but no faces or key props below y 790.
- **Right edge:** keep faces and key action at x < 470 (the Shorts buttons cover x > 480, y 450–830).
- Hero at scale 1.3 is about 270 px tall from feet to head top.

## Top level

```json
{
  "ep": 1,
  "script": "exact script text, identical to what was voiced (ElevenLabs [tags] are ignored)",
  "voiceover": "voiceover.mp3",
  "music": [ {"track": "music/daybreak.mp3", "at": 0},
             {"track": "music/ominosity.mp3", "at": "But then"} ],   // see Music below
  "music_db_below_voice": 20,
  "music_volume": 1.0, "sfx_volume": 1.0,
  "thumbnail": "your hand is already",    // anchor for the thumbnail frame
  "accent": "#C8FF4D",
  "highlights": {"hundredths": "green", "ten hours": "amber"},
  "hud": [ ... ],
  "sfx": [ {"name": "crowd", "at": "Gun up", "gain": 0.8} ],
  "scenes": [ ... ]
}
```

**The script must match the voiceover word for word.** If the user changed words in ElevenLabs, update `script` first.

## Anchors (every "at", "start", "until", "pick_at")

- `"Because today"`: the start of the first word of that phrase (case and punctuation ignored).
- `"Sam#2"`: the 2nd occurrence.
- `"end:times ten"`: the end of the phrase's last word.
- `"Leo pitches+0.4"` / `"miss-0.2"`: an offset in seconds.
- `3.5`: an absolute number of seconds.

Phrases must exist in the script, or the render stops with "phrase not found".

## Scenes

A scene runs from its `start` anchor to the next scene's start. The first scene starts at 0, so it has no `start`.

```json
{
  "start": "Leo pitches",
  "bg": "day_park",
  "camera": "push",            // push | pull | static | pan_left | pan_right | closeup
  "focus": "hero", "zoom": 2.4, // closeup only: whose face, how close (2.0-3.0)
  "slowmo": false,              // true = desaturated, vignette, SLOW-MO chip, boom sfx, music dips
  "transition": "cut",          // "none" = no whoosh or cut-punch
  "props": "<svg markup>",      // static set dressing, drawn behind actors
  "front_props": "<svg markup>",// static, drawn in front of actors
  "actors": [ ... ],
  "objects": [ ... ]
}
```

**Backgrounds and their floor y** (put actors' `y` at the floor):

| bg | Looks like | Floor y |
|---|---|---|
| `warm_interior` | cosy room, dusk window | 800–815 |
| `cool_interior` | school/office, sunbeam | 800–815 |
| `dusk` | hills at sunset | 800–830 |
| `day_park` | park, afternoon | 800–830 |
| `stadium` | crowd, grass, running track | 700–880 (track) |
| `night_city` | skyline, stars | 805–820 |
| `lab` | dark grid "inside the game" space. **Max once per video**, and prefer `void` | 820–845 |
| `void` | dark radial glow, no floor: hero shots of objects, diagrams, big numbers | none (objects float) |
| `space` | stars, nebula, a planet bottom-right | none |
| `earth_orbit` | black sky with Earth's curve along the bottom | none |
| `sky` | blue sky, sun, clouds, no ground: flying, falling | none |
| `underwater` | teal water, light shafts, seabed | 815–830 |
| `city_day` | daytime skyline and street | 810–820 |
| `future_city` | neon towers at night | 810–820 |
| `forest` | moonlit pine forest | 815–825 |
| `desert` | dunes and a huge sun | 820–835 |
| `snow` | snowy mountains at night | 800–815 |
| `mars` | red rocky planet | 815–830 |

You can also add any custom scenery on top of any background with `props` / `front_props` (e.g. a sea, a lighthouse, a kitchen). Use `"bg": "void"` plus props when none of these fit.

Props are plain SVG in the 540×960 space. Keep them flat: solid fills, palette colours, `#141218` outlines. Examples: a table `<rect x='70' y='652' width='400' height='16' rx='6' fill='#6B4A3A'/>`, a chalkboard, a clock, a desk, a railing. Use single quotes inside SVG strings.

## Actors

```json
{"id": "hero", "char": "hero", "x": 165, "y": 812, "scale": 1.3, "flip": false,
 "pose": "idle", "face": "neutral", "look": 0,
 "keys": [
   {"at": "A cup falls+0.15", "pose": "catch", "face": "focused", "dur": 0.12, "sfx": "swish"},
   {"at": "You run", "x": 370, "dur": 0.9, "cycle": "run"},
   {"at": "You catch him", "cycle": null, "pose": "carry", "face": "happy"}
 ]}
```

- `char`: `hero` (blue, always "you") · `mia` · `leo` · `drlee` · `sam` · `mom` · `extra` (grey crowd/anyone; set `"shirt": "#hex"`).
- `flip: true` = facing left.
- `y` = where the feet touch the floor. Poses auto-ground (sitting and crouching just work).
- **Poses:** idle, stand, catch, reach_up, point, wave, cheer, shrug, think, facepalm, hold, throw_back, throw, swing_ready, swing, crouch, sit, slump, lie, fall, jump, dive, run_a, run_b, walk_a, walk_b, tired, hug, carry.
- **Faces:** neutral, happy, shocked, smug, worried, determined, bored, sad, focused.
- `look`: −1 to 1, shifts the eyes back or forward.
- `rot` (degrees, around the feet) also works as a starting value on the actor itself, not only in keys: `"rot": -90` with `"pose": "idle"` and `"shadow": false` lays someone flat (feet at x, head pointing left), which reads better than the `lie` pose for sleeping or floating.
- **Key fields:** `at`, `dur` (default 0.25), `ease` (inout · out · in · linear · back), `x`, `y`, `scale`, `rot`, `opacity`, `lift` (px off the ground), `arc` (jump height for this move), `pose`, `face`, `look`, `flip`, `cycle` ("run" | "walk" | null), `sfx`.
- Moving across the screen: set `cycle` and a new `x` with `dur` = travel time.
- Pose changes snap faster with `dur` 0.1–0.15 for action beats and ease slower (0.3–0.6) for emotional beats.
- Hands are exposed as `"<id>.hand"` (front) and `"<id>.hand_back"` for objects to attach to.

## Objects (anything that moves that isn't a person)

```json
{"id": "cup", "x": 370, "y": 628, "rot": 0, "front": false,
 "svg": "<path d='M-18 -20 L18 -20 L14 20 Q0 26 -14 20 Z' fill='#F4F1FF'/>",
 "keys": [
   {"at": "A cup", "x": 300, "y": 640, "rot": -50, "dur": 0.35, "ease": "in", "arc": 25},
   {"at": "Your hand's", "attach": "hero.hand", "dx": 0, "dy": -26, "sfx": "thud"}
 ]}
```

- Draw `svg` centred on (0,0).
- `attach: "hero.hand"` makes it follow a hand. `attach: null` releases it.
- `arc` throws it in a parabola. `front: true` draws it in front of actors.
- Good uses: balls, cups, phones, books, lightning sparks, clocks, a falling screen, a giant number, a brain icon.

## HUD (one card at a time; the engine trims overlaps)

**v2:** the HUD is optional and light. Use **at most 2 game cards** (`stat`, `compare`, `warn`, `note`, `level`) per video, and only where they make a beat clearer. Big moments use `title` cards instead. **Never use `countdown`, and never use a `choice` card with a draining timer.** `endcard` only when the video ends on a question.

```json
{"type": "title", "at": 0.05, "until": "Not slowly", "small": "WHAT IF THE EARTH", "text": "STOPPED SPINNING?", "color": "#FFD27A", "top": 150}
{"type": "title", "at": "seventeen hundred", "until": "You just", "small": "SPEED AT THE EQUATOR", "text": "1,670 KM/H", "color": "#C8FF4D", "size": 70, "captions": true}
{"type": "title", "at": "slams on the brakes", "text": "STOP.", "color": "#FF6B6B", "size": 110, "sfx": "thud"}
```

- `title`: big glowing kinetic text, no box. `text` (big line), optional `small` (line above), `sub` (small line below), `color`, `size` (default 62), `top` (default 170), `sfx` (default a quiet pop; any sound name, or "" for none; `gain` to adjust).
- While a `title` is up, captions hide, unless you set `"captions": true` (then they move down below it automatically). Use the title on the opening question (spoken words = title text) and on 3–6 key words or numbers per video ("TIME DILATION", "YEAR 2473", "6 MONTHS OF NIGHT").

```json
{"type": "stat",    "at": "Because today", "until": "A normal person", "name": "REACTION TIME", "mult": "×10", "tag": "+900%"}
{"type": "compare", "at": "A normal person", "until": "So what if", "label": "REACTION TIME · COMPARE", "a": ["Average human", "0.25 s", 1.0], "b": ["You", "0.025 s", 0.1]}
{"type": "note",    "at": "The rule", "until": "Leo pitches", "label": "THE RULE", "text": "Brain ×10. Body ×1."}
{"type": "warn",    "at": "The catch", "until": "Gun up", "text": "Every class lasts ten hours."}
{"type": "choice",  "at": "The medal", "pick_at": "You run", "until": "You catch him", "a": "The gold medal", "b": "Sam", "pick": "b"}
{"type": "level",   "at": "Last place", "until": "Sam grins", "label": "RACE RESULT", "text": "LAST PLACE · WORTH IT", "color": "#FFB547"}
```

```json
{"type": "marker",    "at": "Day three", "until": "Day seven", "label": "DAY", "text": "3", "sub": "LANGUAGES LEARNED: 3"}
{"type": "choice",    "at": "You look at the bus", "until": "Who do you save", "a": "Your brother", "b": "27 strangers", "pick": null}
{"type": "endcard",   "at": "Who do you save", "text": "Your brother or 27 strangers?", "a": "BROTHER", "b": "STRANGERS"}
```

- `marker`: big centered label/number for time jumps and big results ("DAY 30", "20 LIVES SAVED"). Optional `label` (small, above), `sub` (small, below), `color`, `size` (default 84).
- `countdown` still exists in the engine for old episodes. **Don't use it.**
- `choice`: only for a shape-F dilemma, and only with `"pick": null` placed right on the final question so no timer drains on screen. Prefer a `title` or `endcard` with the two options.
- `endcard`: the closing question with optional two answer pills, plus comment and subscribe badges. Captions hide while it's up, since it shows the question itself. Put it on the final question.
- `compare` bar lengths are 0–1. Use real proportions.
- `note` uses a cyan "REAL SCIENCE" style label. Use it for the rule or one key fact.
- A `stat` card is optional (good for BODY and MIND lanes, where "you unlock" a stat). The narration never says "stat".

## Sound (automatic; add extras only when a moment needs one)

Less is more: sound effects should be felt, not noticed. Use at most 3–4 extra sounds per video, on the biggest beats only. Never put a sound on every cut.

Automatic (v2, kept deliberately quiet): plain cuts are silent; `whip`, `zoom` and `flash` transitions get a soft whoosh (at most one every 4 s); title cards get a quiet pop. Older automatic sounds: pop + ticks on the stat card, fill sweeps on compare, buzz + amber flash on warn, clock + heartbeat during choice then a chime on the pick, a boom on entering slow-mo (the SLOW-MO chip only shows with `"chip": true`), whoosh + pop on title cards, and a generated music bed ducked under the voice.

Extra sounds go on actor or object keys (`"sfx": "thud"`) or in the top-level `sfx` list: pop, tick, whoosh, swish, buzz, clock, heartbeat, chime, boom, thud, ding, boing, click, riser, crowd, glitch, fill.

## Motion and camera tools (v2)

**Ambient motion (`fx`, per scene):** a list of effect names or objects. Each one moves on its own for the whole scene.

```json
"fx": ["stars", {"type": "speedlines", "dir": "right", "speed": 1.5}, {"type": "rays", "x": 270, "y": 470, "spin": 6, "opacity": 0.14}]
```

| fx | What it does | Options |
|---|---|---|
| `stars` | twinkling, slowly drifting star field | `n`, `speed`, `dx`, `dy` |
| `warp` | hyperspace streaks flying out of a point | `x`, `y`, `n`, `speed`, `color` |
| `speedlines` | streaks across the screen (speed, wind, falling) | `dir` left/right, `n`, `speed` |
| `rain` / `snow` | weather in front of the scene | `n`, `speed`, `color` |
| `embers` / `bubbles` / `dust` | rising sparks, rising bubbles, floating motes | `n`, `speed`, `color` |
| `confetti` | falling confetti | `n` |
| `rays` | rotating light rays behind everything | `x`, `y`, `spin`, `opacity`, `color` |
| `clouds` | clouds drifting across | `speed`, `opacity`, `y0`, `h` |
| `pulse` | expanding rings from a point (alerts, signals, "here") | `x`, `y`, `r`, `period`, `color` |
| `glitch` | brief RGB glitch bands (reality breaking, time skips) | |
| `alarm` | pulsing red screen edge (danger) | `period`, `color` |

**Object animation (`anim`, per object):** continuous motion on top of its keys. `{"spin": deg_per_s, "bob": px, "sway": deg, "pulse": 0.1, "period": s, "drift": [vx, vy], "flicker": 0.5}`. A key with `"stop_anim": true` freezes the animation at that moment (e.g. a spinning planet that stops dead).

**Camera presets (`camera`):** `push`, `pull`, `static`, `pan_left`, `pan_right`, `closeup` (`focus`, `zoom`, `focus_y`), plus:
- `reveal`: starts zoomed in (`zoom`, default 2.3) on `focus` (an actor id) or on `cx`/`cy`, then pulls back to the full scene. Great for "and then you see…".
- `zoom_in`: slow zoom toward `cx`/`cy` to `zoom` (default 1.3).
- `tilt_up` / `tilt_down`: pan vertically from `from_y` to `to_y` at `zoom` (default 1.35). Use for sky, towers, rockets.
- `drift`: handheld sway. Good under tension.

**Camera keyframes (`cam`, per scene):** full control. The camera looks at point (`cx`, `cy`) at `zoom`, optionally rotated by `rot` degrees, and eases between keys.
```json
"cam_start": {"zoom": 1.35, "cx": 270, "cy": 560},
"cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 520, "dur": 2.2, "ease": "out"},
        {"at": "the whole city", "zoom": 0.85, "dur": 1.2}]
```

**Transitions (`transition`, per scene):** `cut` (default punch-in), `whip` (slides in with motion blur; `whip_dir` left/right), `zoom` (rushes in), `flash` (white flash), `none`.

**Impacts (top level):** `"shakes": [{"at": "slams", "amp": 16, "dur": 0.5}]` (adds a soft boom; set `"sfx": "thud"` or `""` to change it, `"gain"` to adjust) and `"flashes": [{"at": "All at once", "dur": 0.15, "color": "#fff"}]`.

**Actors:** `"shadow": false` for anyone floating, flying or in space.

**`show_ep`** (top level, default false): the EP chip is off now. Episodes must not look like parts of a series.

## Directing rules (v2)

The old videos all looked like one video: a stick figure standing in the middle of a purple room. Every rule here exists to break that.

1. **Show the thing, not just the hero.** At least 40% of scenes have no hero on screen: the planet, the wave, the brain, the city, the number, the object. Wide shots with a tiny figure for scale count as "no hero".
2. **Every scene moves on its own.** Each scene has at least one continuous motion source: `fx`, an object `anim`, a walking/running cycle, or a real camera move. A camera push alone doesn't count.
3. **Never the same look twice in a row.** Consecutive scenes differ in background or camera (ideally both). No background more than 3 times per video. `lab` at most once.
4. **Scale changes.** Mix extreme wides (the whole Earth, a skyline), mediums and close-ups. At least one `closeup` or `reveal` on the emotional or mind-blowing beat.
5. **The first frame is the premise.** Open on the subject in motion with a `title` card of the spoken question. No hero standing still in a room.
6. **Title cards for key numbers and words**, 3–6 per video. Captions carry the rest.
7. **Impacts land.** Use `shakes`, `flashes` and `transition` on the big beats (a stop, a crash, a reveal), not everywhere.
8. **Build real props.** Draw the objects the story names (cars, waves, planets, a brain, a rocket) as clear, flat SVG with `#141218` outlines. This is what makes the video watchable.
9. **A new scene every 3–5 seconds.** Cut on sentence ends and "..." pauses.
10. **Faces react on the word**, not after it.
11. **Loop visually.** The last scene echoes the first shot so a replay feels seamless.
12. Keep it readable on a phone: at most 3 characters on screen, big simple shapes, faces above y 770 and left of x 470.

## Checklist before the full render

1. Run `--preview` and open `out/preview_sheet.jpg` (one still per scene). Ask: if I screenshot 3 random moments, do they look like 3 different places?
2. Check that nobody's face is hidden by the HUD or captions, nothing important is in the bottom 20% or at the right edge, characters stand on the floor, and props make sense.
3. Fix `episode.json`, preview again if anything changed, then run the full render.

## Voice

Read `studio.json`. `"voice"` decides the narrator:

**`"qwen3_clone"` (the channel voice, free):** Qwen3-TTS 0.6B (Apache-2.0) cloned from `voice/ref_liam.wav`, run on GitHub Actions because this sandbox can't reach Hugging Face. It voices the whole script in one take, so commas, questions and "..." get the model's own natural pauses. See PIPELINE.md step 4 for the request/poll flow. After it arrives, `nsu_voice.py EP_DIR --align` writes `voiceover_alignment.json` (exact word timing from a timestamped speech model) so captions and anchors are frame-accurate.


**`"kokoro"` (free, runs here):** voices can be blended: `"am_fenrir+am_eric"` mixes two voices 50/50, `"am_fenrir:0.6+am_eric:0.4"` sets the weights. Each sentence is voiced separately and joined with a real pause (heard as about 0.55 s after "?", 0.62 s after "...", 0.42 s after "!", 0.38 s after ".", at least 0.45 s after sentences of three words or fewer; the values in the code are ~0.09 s lower because each sentence keeps a little tail so word endings are never clipped). Override per episode with `"pauses": {"?": 0.5, ".": 0.32}`. After voicing, a built-in speech check (Whisper tiny, offline) transcribes every sentence, re-voices any that come out clipped or garbled, and writes `voice_check.json`. If it still flags a sentence, rephrase that sentence and voice again. The channel voice is whatever `studio.json` says. Set `"voiceover": "voiceover.wav"`, `"tts_voice"` and `"tts_speed"` from studio.json, then run `python3 /home/claude/newstatunlocked-studio/engine/nsu_voice.py EPISODE_DIR`. It voices whole sentences (natural intonation) and writes `voiceover_groups.json`, which the renderer uses for exact caption sync. Too long? Raise `tts_speed` (max 1.2).

**`"elevenlabs"` (paid, via GitHub Actions):** see PIPELINE.md step 3. The workflow writes `voiceover.mp3` plus `voiceover_alignment.json` (per-character timing) and the renderer uses it automatically for exact caption sync. The ElevenLabs text may contain v4 audio tags like `[excited]`; keep `"script"` in episode.json identical to the spoken words without the tags.


## Music

Real tracks live in `music/` (19 originals by Tanner Helland, CC BY 4.0). `music/library.json` lists each file's title and mood: **wonder**, **tension**, **emotional** or **epic**.

- `"music"` is a list of segments. Each starts at its anchor and crossfades (1.5 s) from the previous one. Optional `"offset"` (seconds) skips into the track.
- Typical shape: a **wonder** or **epic** track from 0, then switch to **tension** at the turn ("But then..."). Optionally switch to **emotional** for a sad climax, or to **epic** for a heroic one.
- Use at most 3 segments. Don't reuse the exact same pair of tracks as the previous 2 episodes (check their episode.json).
- The engine levels the music about 20 dB under the voice and dips it a little under words. Leave `music_db_below_voice` at 20 unless the music is clearly too loud or too quiet.
- `"auto"` still gives the old generated bed, and `"none"` gives silence.
- **Credit is required:** every track used must be credited in the description (see PIPELINE.md step 3).
