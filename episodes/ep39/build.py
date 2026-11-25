import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"


def clock(r=150):
    ticks = "".join(
        f"<rect x='-4' y='{-r+14}' width='8' height='{22 if i % 3 == 0 else 12}' rx='3' fill='{INK}' transform='rotate({i*30})'/>"
        for i in range(12))
    return (f"<circle r='{r*1.35}' fill='#7FD1FF' opacity='.10'/><circle r='{r}' fill='#F4F1FF' stroke='{INK}' stroke-width='9'/>"
            f"<circle r='{r*.86}' fill='none' stroke='#7FD1FF' stroke-width='5' stroke-dasharray='14 10' opacity='.7'/>{ticks}"
            f"<path d='M{-r*.55} {-r*1.15} A{r*1.2} {r*1.2} 0 0 0 {-r*1.15} {-r*.35}' fill='none' stroke='#C8FF4D' stroke-width='10' stroke-linecap='round'/>"
            f"<path d='M{-r*1.15} {-r*.35} l-14 -30 l34 6 z' fill='#C8FF4D'/>")


def hand(length, width, color=INK):
    return f"<rect x='{-width/2}' y='{-length}' width='{width}' height='{length+12}' rx='{width/2}' fill='{color}'/>"


HUB = f"<circle r='14' fill='#FF6B6B' stroke='{INK}' stroke-width='5'/>"


def clock_objs(prefix, x=270, y=560, s=1.0, speed=1.0):
    return [
        {"id": f"{prefix}face", "x": x, "y": y, "scale": s, "svg": clock(), "anim": {"pulse": 0.025, "period": 1.2}},
        {"id": f"{prefix}min", "x": x, "y": y, "scale": s, "svg": hand(115, 12), "anim": {"spin": -360 * speed}},
        {"id": f"{prefix}hr", "x": x, "y": y, "scale": s, "svg": hand(75, 16), "anim": {"spin": -45 * speed}},
        {"id": f"{prefix}hub", "x": x, "y": y, "scale": s, "svg": HUB},
    ]


TABLE = (f"<rect x='250' y='640' width='260' height='18' rx='6' fill='#8A5A44' stroke='{INK}' stroke-width='5'/>"
         f"<rect x='275' y='656' width='14' height='150' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/>"
         f"<rect x='470' y='656' width='14' height='150' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/>"
         f"<rect x='330' y='600' width='60' height='40' rx='8' fill='#FFD27A' stroke='{INK}' stroke-width='4'/>")
PHONE = (f"<rect x='-14' y='-24' width='28' height='48' rx='6' fill='#2B2840' stroke='{INK}' stroke-width='4'/>"
         f"<rect x='-10' y='-18' width='20' height='34' rx='3' fill='#7FD1FF'/>")
PHONE_UP = (f"<rect x='-18' y='-30' width='36' height='60' rx='7' fill='#2B2840' stroke='{INK}' stroke-width='4'/>"
            f"<rect x='-13' y='-23' width='26' height='44' rx='3' fill='#FFE7A0'/><circle cx='0' cy='0' r='7' fill='#FF6B6B'/>")
TOWER = (f"<path d='M300 790 L330 330 L360 790 Z' fill='#2B2840' stroke='{INK}' stroke-width='6'/>"
         f"<path d='M312 620 L348 620 M318 500 L342 500 M323 420 L337 420' stroke='#4A4466' stroke-width='6'/>"
         f"<rect x='326' y='280' width='8' height='52' fill='#4A4466' stroke='{INK}' stroke-width='3'/>"
         f"<circle cx='330' cy='278' r='7' fill='#FF6B6B'/>")
BOLT = (f"<path d='M40 -260 L-10 -120 L30 -110 L-30 40 L60 -130 L18 -140 L70 -260 Z' fill='#FFF6B0' stroke='#FFE7A0' stroke-width='6'/>"
        f"<path d='M40 -260 L-10 -120 L30 -110 L-30 40 L60 -130 L18 -140 L70 -260 Z' fill='none' stroke='#FFFFFF' stroke-width='2'/>")
SKYGLOW = "<rect x='0' y='0' width='540' height='960' fill='#E8E6FF'/>"
GOAL = (f"<rect x='150' y='560' width='300' height='150' fill='none' stroke='#F4F1FF' stroke-width='10'/>"
        + "".join(f"<path d='M{x} 565 L{x} 705' stroke='#F4F1FF' stroke-width='2' opacity='.45'/>" for x in range(170, 450, 22))
        + "".join(f"<path d='M155 {y} L445 {y}' stroke='#F4F1FF' stroke-width='2' opacity='.45'/>" for y in range(585, 705, 22)))
BALL = (f"<circle r='16' fill='#F4F1FF' stroke='{INK}' stroke-width='4'/>"
        f"<path d='M0 -7 L7 -2 L4 7 L-4 7 L-7 -2 Z' fill='{INK}'/>")
GHOST = "<circle r='150' fill='#7FD1FF' opacity='.08'/>"
PAGE = lambda n, c: (f"<rect x='-90' y='-110' width='180' height='220' rx='14' fill='#F4F1FF' stroke='{INK}' stroke-width='7'/>"
                     f"<rect x='-90' y='-110' width='180' height='56' rx='14' fill='{c}' stroke='{INK}' stroke-width='7'/>"
                     f"<circle cx='-45' cy='-110' r='9' fill='{INK}'/><circle cx='45' cy='-110' r='9' fill='{INK}'/>"
                     f"<text x='0' y='60' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='96' fill='{INK}'>{n}</text>")
HANDS = {
    "rock": f"<circle r='26' fill='#F2C9A0' stroke='{INK}' stroke-width='5'/>",
    "scissors": (f"<circle r='20' fill='#F2C9A0' stroke='{INK}' stroke-width='5'/>"
                 f"<rect x='-16' y='-62' width='12' height='46' rx='6' fill='#F2C9A0' stroke='{INK}' stroke-width='4' transform='rotate(-14)'/>"
                 f"<rect x='4' y='-62' width='12' height='46' rx='6' fill='#F2C9A0' stroke='{INK}' stroke-width='4' transform='rotate(14)'/>"),
}

scenes = [
    # 1. Giant clock spinning backwards (premise in motion).
    {"bg": "void", "fx": ["stars", {"type": "rays", "x": 270, "y": 560, "spin": -12, "opacity": 0.12, "color": "#7FD1FF"}, "glitch"],
     "cam_start": {"zoom": 1.3, "cx": 270, "cy": 560},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 545, "dur": 2.0, "ease": "out"}],
     "objects": clock_objs("c1", speed=1.4)},
    # 2. Blink twice: closeup on you.
    {"start": "Any moment you want", "bg": "warm_interior", "camera": "closeup", "focus": "hero", "zoom": 2.3, "transition": "zoom",
     "fx": [{"type": "pulse", "x": 230, "y": 560, "r": 160, "period": 0.9, "color": "#C8FF4D"}],
     "actors": [{"id": "hero", "char": "hero", "x": 230, "y": 810, "scale": 1.3, "pose": "idle", "face": "smug", "look": 0.4,
                 "keys": [{"at": "blinking twice", "face": "focused", "dur": 0.12}]}]},
    # 3. Phone slips off the table... and is back in your hand.
    {"start": "Your phone slips", "bg": "warm_interior", "camera": "push", "transition": "cut",
     "props": TABLE, "fx": ["dust"],
     "objects": [{"id": "phone", "x": 300, "y": 628, "svg": PHONE, "front": True,
                  "keys": [{"at": "slips off", "x": 250, "y": 790, "rot": 160, "dur": 0.55, "ease": "in", "arc": 20, "sfx": "thud"},
                           {"at": "blink blink", "x": 250, "y": 790, "dur": 0.01},
                           {"at": "it's back", "attach": "hero.hand", "dx": 0, "dy": -20, "rot": 0, "dur": 0.15}]}],
     "actors": [{"id": "hero", "char": "hero", "x": 165, "y": 810, "scale": 1.25, "pose": "idle", "face": "happy",
                 "keys": [{"at": "slips off+0.3", "pose": "catch", "face": "shocked", "dur": 0.12},
                          {"at": "it's back", "pose": "hold", "face": "smug", "dur": 0.15}]}]},
    # 4. Lightning hits a tower: too fast to film.
    {"start": "Lightning hits", "bg": "night_city", "camera": "tilt_up", "from_y": 640, "to_y": 420, "zoom": 1.3, "transition": "flash",
     "props": TOWER, "fx": [{"type": "rain", "n": 120, "speed": 1.4}],
     "objects": [{"id": "glow", "x": 0, "y": 0, "opacity": 0, "svg": SKYGLOW,
                  "keys": [{"at": "Lightning hits", "opacity": 0.55, "dur": 0.05}, {"at": "Lightning hits+0.35", "opacity": 0, "dur": 0.3}]},
                 {"id": "bolt", "x": 300, "y": 290, "opacity": 0, "svg": BOLT, "front": True,
                  "keys": [{"at": "Lightning hits", "opacity": 1, "dur": 0.04}, {"at": "the flash is over", "opacity": 0, "dur": 0.2}],
                  "anim": {"flicker": 0.6}}]},
    # 5. Blink blink: this time the camera is ready.
    {"start": "Blink blink#2", "bg": "night_city", "camera": "closeup", "focus": "hero", "zoom": 1.8, "transition": "whip", "whip_dir": "left",
     "fx": ["glitch", {"type": "rain", "n": 90, "speed": 1.4}],
     "props": TOWER,
     "objects": [{"id": "phone5", "x": 0, "y": 0, "svg": PHONE_UP, "attach": "hero.hand", "dx": 0, "dy": -26, "front": True},
                 {"id": "bolt5", "x": 300, "y": 290, "opacity": 0, "svg": BOLT,
                  "keys": [{"at": "camera is ready", "opacity": 1, "dur": 0.04, "sfx": "click"}, {"at": "camera is ready+0.6", "opacity": 0, "dur": 0.2}]}],
     "actors": [{"id": "hero", "char": "hero", "x": 160, "y": 812, "scale": 1.3, "pose": "reach_up", "face": "determined", "look": 0.6,
                 "keys": [{"at": "camera is ready+0.3", "face": "happy", "dur": 0.15}]}]},
    # 6. Penalty kick in a cup final.
    {"start": "Then it's a penalty", "bg": "stadium", "camera": "pan_right", "transition": "whip", "whip_dir": "right",
     "props": GOAL, "fx": [{"type": "pulse", "x": 300, "y": 700, "r": 120, "period": 1.4, "color": "#FFD27A"}],
     "objects": [{"id": "ball", "x": 165, "y": 805, "svg": BALL, "front": True}],
     "actors": [{"id": "keeper", "char": "extra", "shirt": "#FF6B6B", "x": 300, "y": 712, "scale": 0.8, "pose": "crouch", "face": "focused",
                 "keys": [{"at": "dive early", "x": 400, "pose": "dive", "rot": 70, "dur": 0.35, "ease": "out"}]},
                {"id": "hero", "char": "hero", "x": 110, "y": 860, "scale": 1.1, "pose": "idle", "face": "focused"}]},
    # 7. Rewind, kick the other way. Goal.
    {"start": "You watch which way", "bg": "stadium", "camera": "reveal", "focus": "keeper", "zoom": 2.0, "transition": "cut",
     "props": GOAL, "fx": ["glitch"],
     "objects": [{"id": "ball7", "x": 165, "y": 805, "svg": BALL, "front": True,
                  "keys": [{"at": "kick the other way", "x": 215, "y": 610, "dur": 0.45, "ease": "out", "arc": 60, "sfx": "thud"}]}],
     "actors": [{"id": "keeper", "char": "extra", "shirt": "#FF6B6B", "x": 300, "y": 712, "scale": 0.8, "pose": "crouch", "face": "focused",
                 "keys": [{"at": "which way he dives", "x": 400, "pose": "dive", "rot": 70, "dur": 0.35},
                          {"at": "rewind", "x": 300, "pose": "crouch", "rot": 0, "dur": 0.3},
                          {"at": "kick the other way", "x": 400, "pose": "dive", "rot": 70, "dur": 0.35, "face": "shocked"}]},
                {"id": "hero", "char": "hero", "x": 110, "y": 860, "scale": 1.1, "pose": "idle", "face": "smug",
                 "keys": [{"at": "kick the other way", "pose": "swing", "dur": 0.12},
                          {"at": "Goal", "pose": "cheer", "face": "happy", "dur": 0.2}]}]},
    # 8. Only you remember: the world resets, you don't.
    {"start": "The catch", "bg": "void", "camera": "drift", "transition": "cut",
     "fx": [{"type": "pulse", "x": 270, "y": 620, "r": 220, "period": 1.6, "color": "#C8FF4D"}, "dust"],
     "objects": [{"id": "halo", "x": 270, "y": 640, "svg": GHOST, "anim": {"pulse": 0.08, "period": 1.2}}],
     "actors": [{"id": "g1", "char": "extra", "shirt": "#5A5670", "x": 110, "y": 790, "scale": 0.95, "pose": "walk_a", "face": "neutral", "opacity": 0.45, "shadow": False},
                {"id": "g2", "char": "extra", "shirt": "#5A5670", "x": 420, "y": 790, "scale": 0.95, "pose": "walk_b", "face": "neutral", "flip": True, "opacity": 0.45, "shadow": False},
                {"id": "hero", "char": "hero", "x": 270, "y": 800, "scale": 1.3, "pose": "think", "face": "worried", "shadow": False,
                 "keys": [{"at": "live those ten seconds twice", "pose": "shrug", "face": "focused", "dur": 0.3}]}]},
    # 9. A hundred rewinds a day = four extra days a year.
    {"start": "Rewind just a hundred", "bg": "lab", "camera": "zoom_in", "zoom": 1.2, "cx": 270, "cy": 560, "transition": "zoom",
     "fx": ["dust"],
     "objects": [{"id": "p1", "x": 270, "y": 560, "scale": 1.6, "svg": PAGE(1, "#7FD1FF"), "anim": {"bob": 5, "period": 1.5},
                  "keys": [{"at": "by the end of the year", "y": 380, "rot": -25, "opacity": 0, "dur": 0.35}]},
                 {"id": "p2", "x": 270, "y": 560, "scale": 1.6, "opacity": 0, "svg": PAGE(2, "#C8FF4D"),
                  "keys": [{"at": "by the end of the year", "opacity": 1, "dur": 0.05}, {"at": "you've lived", "y": 380, "rot": 25, "opacity": 0, "dur": 0.3}]},
                 {"id": "p3", "x": 270, "y": 560, "scale": 1.6, "opacity": 0, "svg": PAGE(3, "#FFD27A"),
                  "keys": [{"at": "you've lived", "opacity": 1, "dur": 0.05}, {"at": "four whole days", "y": 380, "rot": -25, "opacity": 0, "dur": 0.3}]},
                 {"id": "p4", "x": 270, "y": 560, "scale": 1.6, "opacity": 0, "svg": PAGE(4, "#FF6B6B"),
                  "keys": [{"at": "four whole days", "opacity": 1, "dur": 0.05, "sfx": "ding"}], "anim": {"pulse": 0.05, "period": 0.8}}]},
    # 10. If someone else had it, you'd never know: busy street.
    {"start": "And that means", "bg": "city_day", "camera": "pan_left", "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "clouds", "speed": 10, "opacity": 0.5, "y0": 90, "h": 250}],
     "actors": [{"id": "a", "char": "extra", "shirt": "#E46F8E", "x": 60, "y": 815, "scale": 1.0, "pose": "walk_a", "keys": [{"at": "And that means", "x": 300, "dur": 5, "cycle": "walk", "ease": "linear"}]},
                {"id": "b", "char": "extra", "shirt": "#7FD1FF", "x": 470, "y": 815, "scale": 1.0, "flip": True, "pose": "walk_a", "keys": [{"at": "And that means", "x": 220, "dur": 5, "cycle": "walk", "ease": "linear"}]},
                {"id": "c", "char": "extra", "shirt": "#FFD27A", "x": 300, "y": 815, "scale": 1.0, "pose": "walk_b", "keys": [{"at": "And that means", "x": 440, "dur": 5, "cycle": "walk", "ease": "linear"}]}]},
    # 11. Deja vu: the same moment, twice.
    {"start": "Most people say", "bg": "dusk", "camera": "push", "transition": "flash",
     "fx": ["glitch", {"type": "embers", "n": 20, "speed": 0.5, "color": "#FFD27A"}],
     "actors": [{"id": "m1", "char": "mia", "x": 200, "y": 815, "scale": 1.25, "pose": "walk_a", "face": "neutral", "keys": [{"at": "Most people say", "x": 280, "dur": 3, "cycle": "walk", "ease": "linear"}]},
                {"id": "m2", "char": "mia", "x": 230, "y": 815, "scale": 1.25, "pose": "walk_b", "face": "neutral", "opacity": 0.35, "keys": [{"at": "Most people say", "x": 310, "dur": 3, "cycle": "walk", "ease": "linear"}, {"at": "Scientists call it", "opacity": 0, "dur": 0.4}]}]},
    # 12. Your friend who never loses at rock paper scissors.
    {"start": "So your friend", "bg": "warm_interior", "camera": "closeup", "focus": "mia", "zoom": 1.3, "transition": "cut",
     "fx": [{"type": "pulse", "x": 330, "y": 560, "r": 140, "period": 1.1, "color": "#FF6B6B"}],
     "objects": [{"id": "hs", "x": 0, "y": 0, "svg": HANDS["scissors"], "attach": "hero.hand", "dx": 10, "dy": -20, "front": True},
                 {"id": "hr", "x": 0, "y": 0, "svg": HANDS["rock"], "attach": "mia.hand", "dx": -10, "dy": -10, "front": True}],
     "actors": [{"id": "hero", "char": "hero", "x": 170, "y": 812, "scale": 1.25, "pose": "point", "face": "bored"},
                {"id": "mia", "char": "mia", "x": 340, "y": 812, "scale": 1.25, "flip": True, "pose": "point", "face": "smug", "look": 0.5,
                 "keys": [{"at": "watch how they blink", "face": "happy", "dur": 0.2}]}]},
    # 13. Loop: back to the spinning clock.
    {"start": "blink#5", "bg": "void", "transition": "zoom",
     "fx": ["stars", {"type": "rays", "x": 270, "y": 560, "spin": -12, "opacity": 0.12, "color": "#7FD1FF"}, "glitch"],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 545},
     "cam": [{"at": "blink#5", "zoom": 1.3, "cx": 270, "cy": 560, "dur": 1.6, "ease": "inout"}],
     "objects": clock_objs("c2", speed=1.4)},
]

hud = [
    {"type": "title", "at": 0.05, "until": "Any moment you want", "small": "WHAT IF YOU COULD", "text": "REWIND 10 SECONDS?", "color": "#C8FF4D", "size": 54, "top": 150},
    {"type": "title", "at": "less than a second", "until": "Blink blink#2", "small": "A LIGHTNING FLASH LASTS", "text": "UNDER 1 SECOND", "color": "#FFF6B0", "size": 60, "top": 150, "captions": True},
    {"type": "title", "at": "under half a second", "until": "You watch which way", "small": "A PENALTY REACHES THE GOAL IN", "text": "UNDER 0.5 S", "color": "#FFD27A", "size": 70, "top": 150, "captions": True},
    {"type": "title", "at": "Goal", "until": "The catch", "text": "GOAL!", "color": "#C8FF4D", "size": 110, "top": 170, "sfx": "crowd", "gain": 0.6},
    {"type": "title", "at": "Only you remember", "until": "Rewind just a hundred", "text": "ONLY YOU REMEMBER", "color": "#C8FF4D", "size": 54, "top": 150, "captions": True},
    {"type": "title", "at": "four whole days", "until": "And that means", "small": "100 REWINDS A DAY =", "text": "+4 DAYS A YEAR", "color": "#FF6B6B", "size": 62, "top": 150, "captions": True},
    {"type": "title", "at": "you would never know", "until": "Most people say", "text": "YOU'D NEVER KNOW", "color": "#7FD1FF", "size": 58, "top": 150, "captions": True},
    {"type": "title", "at": "deja vu", "until": "So your friend", "text": "DEJA VU", "color": "#FFD27A", "size": 90, "top": 150, "captions": True},
]

ep.update({
    "ep": 39,
    "voiceover": "voiceover.wav",
    "accent": "#C8FF4D",
    "show_ep": False,
    "thumbnail": "kick the other way+0.3",
    "highlights": {"ten seconds": "green", "half a second": "amber", "four whole days": "amber", "deja vu": "amber", "blink": "green"},
    "music": [{"track": "music/the-forest-awakes.mp3", "at": 0},
              {"track": "music/surreptitious.mp3", "at": "The catch"}],
    "music_db_below_voice": 20,
    "hud": hud,
    "shakes": [{"at": "Lightning hits", "amp": 14, "dur": 0.45}, {"at": "Goal", "amp": 10, "dur": 0.4}],
    "flashes": [{"at": "Lightning hits", "dur": 0.12, "color": "#fff"}, {"at": "camera is ready", "dur": 0.1, "color": "#fff"}],
    "scenes": scenes,
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
