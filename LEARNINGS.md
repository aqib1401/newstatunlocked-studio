# LEARNINGS: what the numbers say

Read this before picking an idea. The daily run refreshes the table at the bottom (tools/learn.py) and adds a line to the log when something new is learned. Keep the log short: one dated line per real insight, no restating.

## The v1 baseline (EP 1–31, Nov 9–22, 2026)

- **YouTube:** every video landed between 926 and 1,442 views. Topic, length (45 s vs 90 s) and posting slot made no visible difference. A flat line like this means YouTube showed each Short to its test audience and none of them earned a wider push.
- **Facebook:** average watch time was **5–18 seconds** on 50–90 second videos. Most people left within the first 10 seconds. The opening is where we lose them.
- **Best of v1:** "10x Stronger" (1,442 YT, 1,184 FB) and "Never Felt Fear" (1,968 FB). Both are simple, desirable powers. The weakest were the small, curious ones (glow in the dark, see in the dark, never hungry).
- **Sameness:** every v1 episode used the same skeleton (question → wins → "but then" → science → kid in danger → spoken countdown → "Yes or no?") and the same look (purple room or lab grid, hero standing mid-frame, HUD card on top).
- **Title bug:** YouTube titles were posted as the description's long first sentence ("What if your voice was a hundred times louder, and even your…") instead of the short title. Fixed in PIPELINE.md v2.

## What a breakout channel in our style does differently (Stickadox, studied Nov 22)

Same stick-figure "What if" style, about as old as us, 42 videos, 11.8K subs. Its Shorts get 10K–1.3M views; 8 of its last 20 passed 100K.
- **Huge fantasies at absurd scale:** IQ of a million, 99.999% light speed, live 10,000 years, Earth 100x bigger, aliens with IQ 1,000. Its two flops were grounded, realistic premises (a $1 cancer cure: 1.8K; the police wanted level: 8.6K).
- **Long Shorts:** 130–160 seconds each, not 45–90.
- **A mind-bending twist** in the middle (the universe is a simulation; no child born in 200 years; the aliens are hiding from something worse), then a choice with civilization-sized stakes where both sides are defensible.
- **Cinematic visuals:** the subject fills the frame (a rocket in space, a launchpad at dusk, a clock for "time dilation"). The character is often tiny or absent. Big glowing keyword titles instead of game cards.
- Their 10-second timer is their signature. We dropped ours so we don't look like a copy.

## v2 bets (from EP 32)

1. Bigger premises across four lanes (MIND, BODY, TIME, WORLD).
2. Rotating story shapes and endings; no countdown; no kid-in-danger climax.
3. Subject-first visuals with constant motion, 11 new backgrounds, title cards, real camera moves.
4. Longer stories when the shape can carry them (testing 100 s+).
5. Short, clean titles.

Every v2 episode records `v`, `lane`, `shape`, `ending` and `duration_s` in episodes.json so the table below can tell us which bets pay.

## Log (newest first)

- 2026-11-26: EP 35 (Sun Vanished, WORLD, D twist, 49 s) reached 1,524 YT views at 48 h, the first v2 video past the v1 best (1,443); every other v2 is still 1,000-1,313. The Facebook lift hasn't returned for EP 35-38 (229-576 FB views), though EP 36 and 38 hold the best FB average watch (21-25 s).
- 2026-11-25: The Facebook lift didn't repeat for EP 35 (434 FB views at 24 h) and EP 36 (569 at 19 h), against 3,000-6,000 for EP 32-34 at a similar age, so the early FB push looks inconsistent rather than locked in. EP 36 (MIND, F dilemma, 77 s) still set the best FB average watch so far (24.9 s). YouTube unchanged: all six v2 episodes 980-1,330.
- 2026-11-24: Facebook lift holds across all three posted v2 episodes (EP 32: 5,994, EP 33: 5,307, EP 34: 3,049 FB views within 19-43 h; avg watch 14-18 s), every one above the best v1 FB video (1,969) and ~15-25x the v1 typical (~200). It's not lane-specific (WORLD, TIME, BODY all hit). YouTube unchanged at 940-1,244.
- 2026-11-23: First v2 signal is on Facebook: EP 32 (Earth Stopped Spinning, WORLD, C spiral, 64 s) hit 5,752 FB views in 19 h with 17.7 s average watch, about 3x the best v1 FB video (1,968) and near the top of the v1 watch-time range. YouTube still flat (1,195 at 19 h). One video only, so watch whether WORLD/space premises repeat it.
- 2026-11-23: Voice lab on free GitHub runners (CPU): Chatterbox, Chatterbox Turbo, Qwen3-TTS. Aqib picked Qwen3-TTS 0.6B cloned from the Liam clip, voiced as one take of the whole script (natural pauses). About 7x real time on CPU, so ~8 min per 70 s episode. Kokoro Liam stays as the fallback.
- 2026-11-23: Sound: plain scene cuts are now silent (v1 put a hissy whoosh on every cut, ~25 per video, and it was annoying). Soft whoosh only on whip/zoom/flash transitions, max one per 4 s; quiet pop on title cards. Voice speed 1.15, with an automatic speech check so no word is clipped.
- 2026-11-22: v2 launched. Baseline above.
- 2026-11-22: Narrator changed from Kokoro am_michael to am_liam (Aqib's pick after comparing samples). Reference: Stickadox's narrator measures male, median pitch ~140-145 Hz with a wide expressive range; Michael measured flat (median 124 Hz, 104-141 Hz). Sentences are now voiced one at a time with real pauses (0.55 s after questions, 0.6 s after "...", 0.45 s around short punches). From EP 32 on.

## Data (auto-generated, don't edit by hand)

<!-- AUTO:START -->
_Updated 2026-11-26 17:48 UTC_

**By version** (YouTube views, posts at least 48 h old)

| version | videos | median views | best |
|---|---|---|---|
| 2 | 3 | 1261 | 1313 |
| 1 | 26 | 1260 | 1443 |

**By lane** (YouTube views, posts at least 48 h old)

| lane | videos | median views | best |
|---|---|---|---|
| TIME | 1 | 1313 | 1313 |
| WORLD | 1 | 1261 | 1261 |
| BODY | 1 | 1004 | 1004 |

**By shape** (YouTube views, posts at least 48 h old)

| shape | videos | median views | best |
|---|---|---|---|
| A epic | 1 | 1313 | 1313 |
| C spiral | 1 | 1261 | 1261 |
| B timeline | 1 | 1004 | 1004 |

**By ending** (YouTube views, posts at least 48 h old)

| ending | videos | median views | best |
|---|---|---|---|
| twist | 1 | 1313 | 1313 |
| question | 1 | 1261 | 1261 |
| punchline | 1 | 1004 | 1004 |

**By length** (YouTube views, posts at least 48 h old)

| length | videos | median views | best |
|---|---|---|---|
| 60-99 s | 2 | 1287 | 1313 |
| 100 s+ | 1 | 1004 | 1004 |

**Every episode with YouTube stats** (newest first)

| EP | title | v | lane | shape | length | YT views | likes | comments | FB views | FB avg watch | age h |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 38 | What If You Could Teleport Anywhere? | 2 | BODY | A epic | 101 s | 1000 | 13 | 1 | 293 | 21.1 s | 19.1 |
| 37 | What If You Fell Into a Black Hole? | 2 | WORLD | E survival | 65 s | 1049 | 22 | 1 | 229 | 7.4 s | 23.9 |
| 36 | What If Your Brain Ran 1,000x Faster? | 2 | MIND | F dilemma | 77 s | 1196 | 25 | 5 | 576 | 24.8 s | 43.4 |
| 35 | What If the Sun Vanished? | 2 | WORLD | D twist | 49 s | 1524 | 24 | 3 | 439 | 16.1 s | 47.7 |
| 34 | What If You Were 1,000x Stronger? | 2 | BODY | B timeline | 105 s | 1004 | 16 | 3 | 3067 | 14.5 s | 67.4 |
| 33 | What If You Could Freeze Time? | 2 | TIME | A epic | 89 s | 1313 | 26 | 5 | 5341 | 14.7 s | 71.9 |
| 32 | What If Earth Stopped Spinning? | 2 | WORLD | C spiral | 64 s | 1261 | 18 | 1 | 6034 | 17.6 s | 91.4 |
| 26 | What If Your Voice Was 100x Louder? | 1 |  |  | 91 s | 1143 | 16 | 1 | 212 | 11.2 s | 95.4 |
| 25 | What If You Had No Fingerprints? | 1 |  |  | 52 s | 1068 | 22 | 3 | 456 | 6.7 s | 163.3 |
| 24 | What If Your Memory Reset Every Day? | 1 |  |  | 86 s | 1020 | 27 | 1 | 211 | 10.9 s | 167.9 |
| 23 | What If Your Skin Couldn't Be Cut? | 1 |  |  | 48 s | 1165 | 17 | 1 | 220 | 6.2 s | 187.4 |
| 22 | What If You Could See in the Dark? | 1 |  |  | 88 s | 1265 | 29 | 3 | 252 | 4.1 s | 191.9 |
| 21 | What If Your Body Glowed in the Dark? | 1 |  |  | 49 s | 1018 | 8 | 1 | 494 | 8.3 s | 211.2 |
| 20 | What If You Never Felt Fear? | 1 |  |  | 86 s | 1211 | 21 | 1 | 1969 | 9.9 s | 215.9 |
| 19 | What If You Never Felt Hungry Again? | 1 |  |  | 49 s | 1141 | 23 | 5 | 38 | 5.1 s | 235.2 |
| 18 | What If You Healed 1,000,000x Faster? | 1 |  |  | 89 s | 1226 | 16 | 5 | 54 | 18.2 s | 239.8 |
| 17 | What If You Weighed 10x Less? | 1 |  |  | 48 s | 1113 | 20 | 1 | 188 | 11.7 s | 259.2 |
| 16 | What If You Could Hear 100x Better? | 1 |  |  | 94 s | 1343 | 25 | 1 | 0 | 0.0 s | 263.9 |
| 15 | What If You Could Control Every Dream? | 1 |  |  | 50 s | 1354 | 24 | 5 | 360 | 9.1 s | 283.2 |
| 14 | What If You Aged 10x Slower? | 1 |  |  | 86 s | 1305 | 25 | 4 | 4 | 43.6 s | 287.6 |
| 13 | What If You Remembered Being a Baby? | 1 |  |  | 51 s | 1394 | 25 | 3 | 213 | 10.3 s | 287.8 |
| 12 | What If You Shrank to the Size of an Ant? | 1 |  |  | 88 s | 1349 | 21 | 4 | 220 | 10.9 s | 288.7 |
| 11 | What If You Could See Heat? | 1 |  |  | 49 s | 1292 | 23 | 1 | 212 | 5.3 s | 288.9 |
| 10 | What If You Never Needed Sleep Again? | 1 |  |  | 90 s | 1211 | 12 | 3 | 93 | 1.9 s | 307.3 |
| 9 | What If You Could See Sounds as Colors? | 1 |  |  | 51 s | 1255 | 26 | 3 | 56 | 10.3 s | 311.9 |
| 8 | What If You Could Never Forget Anything? | 1 |  |  | 89 s | 1406 | 29 | 3 | 214 | 14.2 s | 331.3 |
| 7 | What If You Felt Everyone Else's Pain? | 1 |  |  | 49 s | 1364 | 30 | 2 | 221 | 11.6 s | 335.8 |
| 6 | What If You Grew 10x Taller? | 1 |  |  | 90 s | 1045 | 27 | 7 | 202 | 9.2 s | 355.3 |
| 5 | What If Your Heart Beat Only Six Times a Minute? | 1 |  |  | 50 s | 1271 | 25 | 5 | 105 | 13.9 s | 359.7 |
| 4 | What If You Could Smell 10,000x Better? | 1 |  |  | 0 s | 926 | 20 | 3 | 793 | 14.2 s | 379.4 |
| 3 | What If You Never Blinked Again? | 1 |  |  | 0 s | 1337 | 32 | 1 | 162 | 5.0 s | 383.9 |
| 2 | What If You Were 10x Stronger? | 1 |  |  | 0 s | 1443 | 46 | 3 | 1185 | 13.5 s | 403.3 |
| 1 | What If Your Reaction Time Was 10x Faster? | 1 |  |  | 0 s | 1318 | 38 | 1 | 325 | 17.8 s | 407.8 |
<!-- AUTO:END -->
