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
| `lab` | dark grid "inside the game" space; use it for stat/number explainer moments | 820–845 |

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
{"type": "countdown", "at": "Ten seconds", "until": "Who do you save", "from": 10}
{"type": "choice",    "at": "You look at the bus", "until": "Who do you save", "a": "Your brother", "b": "27 strangers", "pick": null}
{"type": "endcard",   "at": "Who do you save", "text": "Your brother or 27 strangers?", "a": "BROTHER", "b": "STRANGERS"}
```

- `marker`: big centered label/number for time jumps and big results ("DAY 30", "20 LIVES SAVED"). Optional `label` (small, above), `sub` (small, below), `color`, `size` (default 84).
- `countdown`: huge red digits counting from `from` to 0 evenly between `at` and `until`, with ticks, heartbeats and a buzzer at zero. Put `at` on the spoken "Ten seconds" and `until` just after the last spoken number.
- `choice` with `"pick": null`: the timer drains and the card shows "YOUR CALL" with both options pulsing (no chime). Use this when the video leaves the choice to the viewer.
- `endcard`: the closing question with optional two answer pills, plus comment and subscribe badges. Captions hide while it's up, since it shows the question itself. Put it on the final question.
- `compare` bar lengths are 0–1. Use real proportions.
- `note` uses a cyan "REAL SCIENCE" style label. Use it for the rule or one key fact.
- Every Short has exactly one `stat` card, landing on the phrase that names the ability (the HUD PLAN's STAT CARD LANDS ON). The narration never says "stat"; the card is visual only. `warn` and `choice` follow the HUD plan from the script.

## Sound (automatic; add extras only when a moment needs one)

Automatic: a whoosh on every cut, pop + ticks on the stat card, fill sweeps on compare, buzz + amber flash on warn, clock + heartbeat during choice then a chime on the pick, a boom on entering slow-mo, and a generated music bed ducked under the voice.

Extra sounds go on actor or object keys (`"sfx": "thud"`) or in the top-level `sfx` list: pop, tick, whoosh, swish, buzz, clock, heartbeat, chime, boom, thud, ding, boing, click, riser, crowd, glitch, fill.

## Directing rules

- At least one `closeup` scene per episode on the most emotional beat (shock, heartbreak, the choice).
- A new scene every 3–6 seconds. Cut on the "..." pauses and sentence ends.
- Something moves at least every 1.5 s: a pose change, a face change, an object, a cycle. The camera push alone isn't enough.
- Faces change on the emotional word, not after it.
- Use the `lab` background for the stat and number beats, real places for the story.
- The choice scene is `slowmo: true`. The resolution scene right after is normal speed.
- The last scene should set up the loop back to the first line.
- Keep it readable on a phone: at most 3 characters on screen, big simple props.

## Checklist before the full render

1. Run `--preview` and open `out/preview_sheet.jpg`.
2. Check that nobody's face is hidden by the HUD or captions, nothing important is in the bottom 20% or at the right edge, characters stand on the floor, and props make sense.
3. Fix `episode.json`, preview again if anything changed, then run the full render.

## Voice

Read `studio.json`. `"voice"` decides the narrator:

**`"kokoro"` (free, runs here):** set `"voiceover": "voiceover.wav"`, `"tts_voice"` and `"tts_speed"` from studio.json, then run `python3 /home/claude/newstatunlocked-studio/engine/nsu_voice.py EPISODE_DIR`. It voices whole sentences (natural intonation) and writes `voiceover_groups.json`, which the renderer uses for exact caption sync. Too long? Raise `tts_speed` (max 1.2).

**`"elevenlabs"` (paid, via GitHub Actions):** see PIPELINE.md step 3. The workflow writes `voiceover.mp3` plus `voiceover_alignment.json` (per-character timing) and the renderer uses it automatically for exact caption sync. The ElevenLabs text may contain v4 audio tags like `[excited]`; keep `"script"` in episode.json identical to the spoken words without the tags.


## Music

Real tracks live in `music/` (19 originals by Tanner Helland, CC BY 4.0). `music/library.json` lists each file's title and mood: **wonder**, **tension**, **emotional** or **epic**.

- `"music"` is a list of segments. Each starts at its anchor and crossfades (1.5 s) from the previous one. Optional `"offset"` (seconds) skips into the track.
- Typical shape: a **wonder** or **epic** track from 0, then switch to **tension** at the turn ("But then..."). Optionally switch to **emotional** for a sad climax, or to **epic** for a heroic one.
- Use at most 3 segments. Don't reuse the exact same pair of tracks as the previous 2 episodes (check their episode.json).
- The engine levels the music about 20 dB under the voice and dips it a little under words. Leave `music_db_below_voice` at 20 unless the music is clearly too loud or too quiet.
- `"auto"` still gives the old generated bed, and `"none"` gives silence.
- **Credit is required:** every track used must be credited in the description (see PIPELINE.md step 3).
