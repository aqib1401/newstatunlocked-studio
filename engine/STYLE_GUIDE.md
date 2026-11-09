# New Stat Unlocked: Visual Style Guide

This is the look of every Short on the channel. Whoever animates (Claude Code, a plugin, or you by hand) follows this file. When this file and a reference image disagree, the reference image wins.

Live style board (for humans): https://claude.ai/artifact/BfjP1LExwHtzBr8ApGjrkY

## What's in this kit

| Folder | What it is | How to use it |
|---|---|---|
| `reference/` | 1080×1920 PNGs of four sample frames, plus the full style sheet | Look at these first. Match them. |
| `characters/` | The hero (3 poses), 4 face expressions, and 4 side characters as clean SVG | Reuse them. Don't redraw characters from scratch. |
| `ui/ui-components.html` | Every game UI element as HTML/CSS at 1080×1920 scale | Copy the markup and CSS, change only the text and numbers. |
| `source-frames/` | The HTML source of each sample frame (540×960, render at 2× for 1080×1920) | Starting point for building scenes. |

---

## 1. Format

- 1080 × 1920, 9:16, 30 fps, H.264 MP4, with the ElevenLabs voiceover as the audio track.
- The video is exactly as long as the voiceover plus 0.3 s of tail.

## 2. Safe zones (1080×1920)

| Zone | y range | What goes there |
|---|---|---|
| Top bar | 60–160 | `EP. 01` chip on the left; `SLOW-MO ×0.1` chip on the right (only in slow-mo) |
| HUD | 176–460 | One game card at a time (stat, compare, side effect, choice), 888 px wide, centred |
| Captions | 500–780 | Spoken captions, centred |
| Scene | 760–1650 | Characters and action |
| Bottom 20% | 1536–1920 | Floor/background only. **No text, no faces, nothing important** (Shorts UI covers it) |
| Right edge | x > 960, y 900–1650 | Nothing important (like/comment buttons sit here) |

## 3. Colour

| Token | Hex | Use |
|---|---|---|
| Stat green | `#C8FF4D` | Upgrades, "you" numbers, key caption words for the upside |
| Side-effect amber | `#FFB547` | Costs, warnings, caption key words for the downside |
| Danger | `#FF8A8A` | Timers, slow-mo chip |
| Hero blue | `#3D7BF0` | The hero's tee. Only the hero wears it |
| Rim light | `#F2C48D` | Outline on every character edge |
| Ink | `#141218` | Heads and limbs |
| HUD background | `rgba(10,9,22,0.88)` | All game cards |
| Text | `#F4F1FF` / muted `#A9A3C9` | |

Side cast tees: Mia `#9B7BF0`, Leo `#F28A3D` (orange cap), Dr. Lee white coat `#E9F4EF` with green tie `#3FBF8A` and round glasses, Sam `#F2C94C` (smaller, kid proportions).

Backgrounds are flat shapes with soft gradients:
- **Dusk exterior:** `#22194A → #5A3F86 → #C77790 → #F0A57A`, sun `#FFE2B0`.
- **Warm interior:** wall `#241A3A → #4E3350`, window showing dusk.
- **Cool interior** (school, office): `#1E2640 → #3A4566`, warm sunbeam.
- **Slow-mo / choice:** the same scene, desaturated (`#2B2838 → #5E5566 → #8C7A7A`) with a dark radial vignette.

## 4. Typography

- **Chakra Petch** (500/600/700): all game UI. Labels are 24 px, uppercase, letter-spacing 0.22em.
- **Inter** 900: spoken captions, 88–96 px, white, with a hard ink shadow `0 8px 0 #141218` and a soft glow `0 0 36px rgba(0,0,0,.7)`.
- Captions show 2–4 words at a time. One key word is green (upside) or amber (cost). Never more than two lines.

## 5. Characters

Use the SVGs in `characters/`. Construction rules for new poses:
- Round ink head (r = 32 in the hero's 140×240 box) with a 3 px rim-light stroke.
- White dot eyes; the mouth is a single white stroke. Expressions: neutral, shocked (big eyes with pupils, O mouth), smug (squint lines, side smile), worried (brows, wavy mouth, blue sweat drop `#8FD3FF`).
- Limbs are two stacked strokes: rim `#F2C48D` at 13 px, ink `#141218` at 9 px on top. Round caps and joins.
- The tee is a slightly tapered shape in the character's colour.
- A soft ellipse shadow `rgba(0,0,0,.4)` sits under the feet.
- The hero stands about 300 px tall in a 1080×1920 frame. Side characters are 10–20% smaller; Sam is about 70%.
- Max two side characters in one Short.

## 6. Game UI (copy from `ui/ui-components.html`)

1. **EP chip:** top-left on every frame. The number goes up each upload.
2. **Stat Unlocked card:** green border and glow, stat name, multiplier (×10, ×100, 0, MAX), and 10 segments. Appears in the first 1.5 seconds of every Short.
3. **Compare bars:** "Average human" vs "You", with real numbers from the script. Bar length is proportional. When lower is better (time), the green bar is the short one.
4. **Side Effect card:** amber border, triangle icon, one short line. Appears when the narration turns to the cost.
5. **Choice card:** a draining red timer plus options A and B. The option the hero picks lights up green as the narration resolves.
6. **Captions:** see Typography.

Only one HUD card on screen at a time.

## 7. Motion

- **Something moves at least every 1.5 s.** No shot stays still longer than 2.5 s.
- **Stat card in:** scale 0.6 → 1.05 → 1 over 0.35 s; the segments fill left to right, 40 ms each; a short glow pulse when full.
- **Compare bars:** grow from 0 over 0.6 s, ease-out; the "you" bar lands second.
- **Side Effect in:** a 120 ms amber flash on the frame edge, then the card slides down 30 px with a 2-frame shake.
- **Choice:** the timer drains in step with the narration. On the decision the picked option scales to 1.05 and glows, and the other fades to 40%.
- **Captions:** each chunk pops in (scale 0.9 → 1, 120 ms), synced to the voiceover word timing.
- **Characters:** idle breathing (2 px bob, 1.2 s loop); a blink every 3–4 s (eyes squash to 10% height for 100 ms); expressions swap on the beat they're spoken; poses ease between keyframes over 150–250 ms, never snapping unless it's a comic beat.
- **Slow-mo moments:** desaturate, add the vignette, a slow 4% push-in, the `SLOW-MO ×0.1` chip, and a ticking number or clock.
- **Camera:** gentle push-ins and pans only. Cut on the narration's "..." pauses.

## 8. Things to never do

- Stock photos, realistic humans, 3D, or other channels' characters.
- Text in the bottom 20%, or captions over faces.
- More than one HUD card at once.
- Emojis in captions or UI.
- Gore, or a realistic crash. Danger is shown up to the moment of choice, then resolved.
