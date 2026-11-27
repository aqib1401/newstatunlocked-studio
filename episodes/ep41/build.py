import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"
FLOAT = {"shadow": False}


def globe(r=170):
    """Earth seen from the side, with a glowing hole at the North Pole."""
    land = (f"<path d='M{-r*.55:.0f} {-r*.45:.0f} q{r*.25:.0f} {-r*.2:.0f} {r*.45:.0f} {-r*.05:.0f} q{r*.1:.0f} {r*.25:.0f} {-r*.1:.0f} {r*.4:.0f} "
            f"q{-r*.2:.0f} {r*.15:.0f} {-r*.35:.0f} {-r*.05:.0f} z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>"
            f"<path d='M{r*.15:.0f} {r*.05:.0f} q{r*.3:.0f} {-r*.1:.0f} {r*.4:.0f} {r*.15:.0f} q{-r*.05:.0f} {r*.35:.0f} {-r*.3:.0f} {r*.45:.0f} "
            f"q{-r*.2:.0f} {-r*.25:.0f} {-r*.1:.0f} {-r*.6:.0f} z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>")
    caps = (f"<path d='M{-r*.45:.0f} {-r*.89:.0f} Q0 {-r*1.02:.0f} {r*.45:.0f} {-r*.89:.0f} Q0 {-r*.78:.0f} {-r*.45:.0f} {-r*.89:.0f} z' fill='#F4F1FF'/>"
            f"<path d='M{-r*.4:.0f} {r*.92:.0f} Q0 {r*1.02:.0f} {r*.4:.0f} {r*.92:.0f} Q0 {r*.82:.0f} {-r*.4:.0f} {r*.92:.0f} z' fill='#F4F1FF'/>")
    hole = (f"<ellipse cx='0' cy='{-r*.9:.0f}' rx='{r*.16:.0f}' ry='{r*.05:.0f}' fill='#05040A' stroke='#5BE7FF' stroke-width='4'/>"
            f"<ellipse cx='0' cy='{r*.92:.0f}' rx='{r*.12:.0f}' ry='{r*.04:.0f}' fill='#05040A' stroke='#5BE7FF' stroke-width='3'/>")
    return (f"<circle r='{r*1.12:.0f}' fill='#5BE7FF' opacity='.12'/>"
            f"<circle r='{r}' fill='#3E8EDE' stroke='{INK}' stroke-width='7'/>{land}{caps}{hole}"
            f"<path d='M{-r*.7:.0f} {-r*.3:.0f} A{r} {r} 0 0 1 {-r*.2:.0f} {-r*.85:.0f}' stroke='#FFFFFF' stroke-width='8' fill='none' opacity='.35' stroke-linecap='round'/>")


def cutaway(r=200, tunnel=True):
    t = (f"<rect x='-9' y='{-r-6}' width='18' height='{2*r+12}' fill='#05040A' stroke='#5BE7FF' stroke-width='3'/>" if tunnel else "")
    return (f"<circle r='{r*1.08:.0f}' fill='#FF8A3D' opacity='.10'/>"
            f"<circle r='{r}' fill='#3E8EDE' stroke='{INK}' stroke-width='7'/>"
            f"<circle r='{r*.95:.0f}' fill='#E0582E' stroke='{INK}' stroke-width='5'/>"
            f"<circle r='{r*.55:.0f}' fill='#FFB547' stroke='{INK}' stroke-width='5'/>"
            f"<circle r='{r*.19:.0f}' fill='#FFF6D8' stroke='{INK}' stroke-width='5'/>{t}")


def topdown(r=200):
    """Earth seen from above the North Pole with a tunnel through the equator (a diameter)."""
    return (f"<circle r='{r}' fill='#3E8EDE' stroke='{INK}' stroke-width='7'/>"
            f"<path d='M{-r*.3:.0f} {-r*.6:.0f} q{r*.4:.0f} {-r*.15:.0f} {r*.6:.0f} {r*.1:.0f} q{-r*.1:.0f} {r*.3:.0f} {-r*.4:.0f} {r*.2:.0f} z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>"
            f"<path d='M{-r*.7:.0f} {r*.2:.0f} q{r*.2:.0f} {r*.4:.0f} {r*.55:.0f} {r*.35:.0f} q{-r*.05:.0f} {-r*.3:.0f} {-r*.25:.0f} {-r*.45:.0f} z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>"
            f"<rect x='-14' y='{-r}' width='28' height='{2*r}' fill='#05040A' stroke='#5BE7FF' stroke-width='3'/>"
            f"<circle r='16' fill='#F4F1FF' stroke='{INK}' stroke-width='4'/>")


def arrow(length=80, col="#5BE7FF", w=9):
    return (f"<path d='M0 0 L0 {length}' stroke='{col}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<path d='M{-w*1.6} {length-w*1.4} L0 {length+w*1.2} L{w*1.6} {length-w*1.4} Z' fill='{col}' stroke='{INK}' stroke-width='3'/>")


ARROWS_IN = "".join(f"<g transform='rotate({a}) translate(0 -250)'>{arrow(100)}</g>" for a in range(0, 360, 45))
TINY = (f"<circle cx='0' cy='-30' r='9' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/>"
        f"<path d='M0 -21 L0 0 M0 -14 L-10 -4 M0 -14 L10 -4 M0 0 L-7 14 M0 0 L7 14' stroke='#5BA8FF' stroke-width='5' stroke-linecap='round'/>")
DOT = "<circle r='30' fill='#5BE7FF' opacity='.3'/><circle r='13' fill='#F4F1FF' stroke='#141218' stroke-width='4'/>"
HOLE = (f"<ellipse cx='270' cy='812' rx='130' ry='30' fill='#5BE7FF' opacity='.25'/>"
        f"<ellipse cx='270' cy='812' rx='115' ry='24' fill='#05040A' stroke='#9FD8FF' stroke-width='6'/>")
SNOW_LIP = (f"<path d='M0 818 L155 818 Q270 846 385 818 L540 818 L540 960 L0 960 Z' fill='#E8EEFA'/>"
            f"<path d='M155 818 Q270 846 385 818' stroke='#9FD8FF' stroke-width='6' fill='none'/>")
FLAG = (f"<path d='M420 812 L420 640' stroke='{INK}' stroke-width='7'/>"
        f"<path d='M420 644 L500 664 L420 690 Z' fill='#FF6B6B' stroke='{INK}' stroke-width='5'/>")
FLAG_N = FLAG + "<text x='436' y='672' font-family='Chakra Petch' font-weight='700' font-size='22' fill='#FFF'>N</text>"
FLAG_S = FLAG.replace("#FF6B6B", "#FFD27A") + "<text x='436' y='672' font-family='Chakra Petch' font-weight='700' font-size='22' fill='#141218'>S</text>"
PENGUIN = (f"<g transform='translate(110 812)'><ellipse cx='0' cy='-40' rx='26' ry='40' fill='#141218'/>"
           f"<ellipse cx='0' cy='-34' rx='17' ry='30' fill='#F4F1FF'/><circle cx='-7' cy='-62' r='4' fill='#141218'/><circle cx='7' cy='-62' r='4' fill='#141218'/>"
           f"<path d='M-6 -54 L6 -54 L0 -46 Z' fill='#FFB547'/></g>")


def walls(col, glow):
    return (f"<rect x='0' y='0' width='120' height='960' fill='{col}'/><rect x='420' y='0' width='120' height='960' fill='{col}'/>"
            f"<rect x='112' y='0' width='14' height='960' fill='{glow}' opacity='.8'/><rect x='414' y='0' width='14' height='960' fill='{glow}' opacity='.8'/>")


def streaks(col):
    """Tall strip of wall marks; drifts upward so you feel the fall."""
    s = ""
    for i in range(24):
        y = i * 90
        s += f"<rect x='{20 + (i*37) % 70}' y='{y}' width='{30 + (i*13) % 40}' height='10' rx='5' fill='{col}' opacity='.7'/>"
        s += f"<rect x='{430 + (i*29) % 70}' y='{y+45}' width='{30 + (i*17) % 40}' height='10' rx='5' fill='{col}' opacity='.7'/>"
    return f"<g transform='translate(-270 0)'>{s}</g>"


MOON = (f"<circle r='60' fill='#C9D2EE' stroke='{INK}' stroke-width='5'/><circle cx='-18' cy='-12' r='12' fill='#9AA3C4'/>"
        f"<circle cx='20' cy='18' r='9' fill='#9AA3C4'/><circle cx='14' cy='-24' r='6' fill='#9AA3C4'/>")
IRON = (f"<circle r='230' fill='#FFF6D8' opacity='.12'/><circle r='190' fill='#FFE7A0' opacity='.25'/>"
        f"<circle r='160' fill='#FFF6D8' stroke='{INK}' stroke-width='7'/><circle r='120' fill='#FFFFFF' opacity='.6'/>")
SAT = (f"<rect x='-16' y='-12' width='32' height='24' rx='4' fill='#C9D2EE' stroke='{INK}' stroke-width='4'/>"
       f"<rect x='-62' y='-8' width='40' height='16' fill='#5BA8FF' stroke='{INK}' stroke-width='3'/>"
       f"<rect x='22' y='-8' width='40' height='16' fill='#5BA8FF' stroke='{INK}' stroke-width='3'/>")


def clock_face(r=60):
    ticks = "".join(f"<g transform='rotate({a})'><rect x='-3' y='{-r+8}' width='6' height='12' fill='{INK}'/></g>" for a in range(0, 360, 30))
    return f"<circle r='{r}' fill='#F4F1FF' stroke='{INK}' stroke-width='6'/>{ticks}"


def clock_hand(r=60):
    return f"<rect x='-4' y='{-r+14}' width='8' height='{r-14}' rx='4' fill='#FF6B6B'/><circle r='8' fill='{INK}'/>"


scenes = [
    # 1. Opening: Earth in space, a glowing hole at the North Pole, a tiny you on the rim.
    {"bg": "space", "fx": ["stars", {"type": "pulse", "x": 270, "y": 467, "r": 60, "period": 1.0, "color": "#5BE7FF"}],
     "cam_start": {"zoom": 1.45, "cx": 270, "cy": 470},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 560, "dur": 2.4, "ease": "out"}],
     "objects": [{"id": "g1", "x": 270, "y": 640, "svg": globe(190), "anim": {"bob": 4, "period": 3}},
                 {"id": "t1", "x": 270, "y": 458, "scale": 0.9, "svg": TINY, "anim": {"bob": 3, "period": 0.8}}]},
    # 2. Cutaway: a dot falls straight through, top to bottom.
    {"start": "You'd pop out", "bg": "void", "camera": "push", "transition": "zoom",
     "fx": [{"type": "rays", "x": 270, "y": 580, "spin": 6, "opacity": 0.10, "color": "#FFB547"}],
     "objects": [{"id": "c2", "x": 270, "y": 580, "svg": cutaway(210), "anim": {"pulse": 0.015, "period": 1.4}},
                 {"id": "d2", "x": 270, "y": 370, "svg": DOT, "anim": {"pulse": 0.15, "period": 0.5},
                  "keys": [{"at": "You'd pop out+0.3", "y": 790, "dur": 3.0, "ease": "inout"}]}]},
    # 3. The tunnel mouth in the Arctic ice.
    {"start": "Picture a tunnel", "bg": "snow", "camera": "tilt_down", "from_y": 420, "to_y": 600, "zoom": 1.3, "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "snow", "n": 50, "speed": 0.8}, {"type": "pulse", "x": 270, "y": 812, "r": 120, "period": 1.4, "color": "#5BE7FF"}],
     "props": HOLE + FLAG_N, "front_props": SNOW_LIP,
     "actors": [{"id": "hero", "char": "hero", "x": 110, "y": 812, "scale": 1.15, "pose": "point", "face": "happy", "look": 0.5}]},
    # 4. Why pole to pole: seen from above, the spinning Earth swings a tunnel into your path.
    {"start": "It has to go pole to pole", "bg": "void", "camera": "static", "transition": "cut",
     "fx": ["stars", {"type": "pulse", "x": 300, "y": 470, "r": 50, "period": 0.7, "color": "#FF6B6B"}],
     "objects": [{"id": "td4", "x": 270, "y": 580, "rot": 0, "svg": topdown(210), "anim": {"spin": 28}},
                 {"id": "d4", "x": 270, "y": 380, "svg": DOT, "front": True,
                  "keys": [{"at": "because Earth spins", "y": 470, "x": 290, "dur": 1.6, "ease": "in"},
                           {"at": "slam you", "x": 305, "y": 475, "dur": 0.1, "sfx": "thud"}]}]},
    # 5. The step: you at the edge, then gone.
    {"start": "You step off the edge", "bg": "snow", "camera": "closeup", "focus": "hero", "zoom": 1.9, "transition": "cut",
     "fx": [{"type": "snow", "n": 60, "speed": 1.2}],
     "props": HOLE, "front_props": SNOW_LIP,
     "actors": [{"id": "hero", "char": "hero", "x": 215, "y": 812, "scale": 1.2, "pose": "idle", "face": "determined",
                 "keys": [{"at": "You step off+0.3", "x": 262, "pose": "walk_a", "dur": 0.4},
                          {"at": "and the ground is gone", "y": 1080, "pose": "fall", "face": "shocked", "dur": 0.45, "ease": "in", "sfx": "swish"}]}]},
    # 6. Falling down the shaft, wall marks racing upward.
    {"start": "For the first minute", "bg": "void", "camera": "drift", "transition": "zoom",
     "props": walls("#5A5470", "#8E9AC4"),
     "fx": [{"type": "dust", "n": 30, "speed": 1.5, "color": "#C9D2EE"}],
     "objects": [{"id": "s6", "x": 270, "y": 0, "svg": streaks("#8E9AC4"), "anim": {"drift": [0, -700]}}],
     "actors": [{"id": "hero", "char": "hero", "x": 270, "y": 730, "scale": 1.1, "pose": "fall", "face": "happy", **FLOAT,
                 "keys": [{"at": "never stop speeding up", "face": "shocked", "pose": "dive", "dur": 0.2}]}]},
    # 7. Orange-hot walls; you are small.
    {"start": "Ten minutes in", "bg": "void", "camera": "pull", "transition": "flash",
     "props": walls("#B8401F", "#FFB547"),
     "fx": [{"type": "embers", "n": 60, "speed": 2.2, "color": "#FFB547"}],
     "objects": [{"id": "s7", "x": 270, "y": 0, "svg": streaks("#FFD27A"), "anim": {"drift": [0, -1100]}}],
     "actors": [{"id": "hero", "char": "hero", "x": 270, "y": 700, "scale": 0.8, "pose": "dive", "face": "worried", **FLOAT}]},
    # 8. The liquid iron sea, with the Moon for scale.
    {"start": "Then the walls turn", "bg": "void", "camera": "zoom_in", "zoom": 1.2, "cx": 270, "cy": 600, "transition": "cut",
     "fx": [{"type": "bubbles", "n": 40, "speed": 1.0, "color": "#FFE7A0"}],
     "objects": [{"id": "core8", "x": 270, "y": 620, "svg": cutaway(330, tunnel=False), "anim": {"pulse": 0.02, "period": 1.0}},
                 {"id": "moon8", "x": 400, "y": 520, "scale": 0.0, "svg": MOON, "anim": {"bob": 5, "period": 1.6},
                  "keys": [{"at": "bigger than the Moon", "scale": 1.0, "dur": 0.4, "ease": "back", "sfx": "pop"}]}]},
    # 9. Hyperspeed streaks.
    {"start": "You're falling about twenty", "bg": "void", "camera": "push", "transition": "zoom",
     "fx": [{"type": "warp", "x": 270, "y": 600, "n": 120, "speed": 3.0, "color": "#FFD27A"}],
     "objects": [{"id": "t9", "x": 270, "y": 600, "scale": 1.6, "svg": TINY, "anim": {"spin": 40}}]},
    # 10. The centre: you float, pulled from every side.
    {"start": "And right at the center", "bg": "void", "camera": "reveal", "focus": "hero", "zoom": 2.2, "transition": "flash",
     "fx": [{"type": "rays", "x": 270, "y": 600, "spin": 10, "opacity": 0.16, "color": "#FFF6D8"}, "dust"],
     "objects": [{"id": "arr10", "x": 270, "y": 600, "scale": 0.0, "svg": ARROWS_IN, "anim": {"spin": -10},
                  "keys": [{"at": "equally from every side", "scale": 1.0, "dur": 0.5, "ease": "back"}]}],
     "actors": [{"id": "hero", "char": "hero", "x": 270, "y": 700, "scale": 1.0, "pose": "fall", "face": "shocked", **FLOAT,
                 "keys": [{"at": "you weigh nothing", "pose": "cheer", "face": "happy", "lift": 20, "dur": 0.4}]}]},
    # 11. Through the solid iron ball.
    {"start": "straight through a solid", "bg": "void", "camera": "pan_right", "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "embers", "n": 40, "speed": 1.0, "color": "#FFF6D8"}],
     "objects": [{"id": "iron", "x": 270, "y": 600, "svg": IRON, "anim": {"pulse": 0.03, "period": 0.8}},
                 {"id": "t11", "x": 270, "y": 250, "scale": 1.4, "svg": TINY, "front": True,
                  "keys": [{"at": "straight through a solid", "y": 960, "dur": 3.2, "ease": "linear"}]}]},
    # 12. Climbing the second half, slowing down.
    {"start": "Now gravity is behind you", "bg": "void", "camera": "static", "transition": "cut",
     "fx": ["stars"],
     "objects": [{"id": "c12", "x": 270, "y": 560, "svg": cutaway(210), "anim": {"pulse": 0.015, "period": 1.4}},
                 {"id": "d12", "x": 270, "y": 560, "svg": DOT, "anim": {"pulse": 0.15, "period": 0.5},
                  "keys": [{"at": "Now gravity", "y": 760, "dur": 2.6, "ease": "out"}]},
                 {"id": "a12", "x": 330, "y": 760, "rot": 180, "svg": arrow(120, "#FF6B6B", 10), "anim": {"bob": 4, "period": 0.6}}]},
    # 13. Antarctica: pop out, hang, fall back in.
    {"start": "About forty minutes after", "bg": "snow", "camera": "push", "transition": "flash",
     "fx": [{"type": "snow", "n": 40, "speed": 0.6}],
     "props": HOLE + FLAG_S + PENGUIN, "front_props": SNOW_LIP,
     "actors": [{"id": "hero", "char": "hero", "x": 270, "y": 1080, "scale": 1.2, "pose": "reach_up", "face": "shocked", **FLOAT,
                 "keys": [{"at": "your head pops out", "y": 800, "dur": 0.5, "ease": "out", "sfx": "boing"},
                          {"at": "one perfect second", "face": "happy", "pose": "wave", "dur": 0.2},
                          {"at": "and fall back in", "y": 1080, "pose": "fall", "face": "shocked", "dur": 0.45, "ease": "in"}]}]},
    # 14. Forever: the dot bouncing pole to pole.
    {"start": "Again and again", "bg": "void", "camera": "pull", "transition": "zoom",
     "fx": [{"type": "rays", "x": 270, "y": 580, "spin": -6, "opacity": 0.10, "color": "#5BE7FF"}],
     "objects": [{"id": "c14", "x": 270, "y": 580, "svg": cutaway(210)},
                 {"id": "d14", "x": 270, "y": 580, "svg": DOT, "anim": {"bob": 190, "period": 1.3}}]},
    # 15. A satellite skimming Earth's curve, a clock spinning.
    {"start": "And here's the strangest", "bg": "earth_orbit", "camera": "pan_left", "transition": "whip", "whip_dir": "left",
     "fx": ["stars"],
     "objects": [{"id": "sat", "x": 40, "y": 700, "svg": SAT, "anim": {"sway": 6, "period": 1.2},
                  "keys": [{"at": "satellite skimming", "x": 500, "y": 690, "dur": 5.0, "arc": 60, "ease": "linear"}]},
                 {"id": "clk", "x": 270, "y": 520, "svg": clock_face(60)},
                 {"id": "hand", "x": 270, "y": 520, "svg": clock_hand(60), "anim": {"spin": 160}}]},
    # 16. Loop: back to the opening shot, camera pushing in to where scene 1 starts.
    {"start": "Fall through the Earth, or", "bg": "space", "transition": "zoom",
     "fx": ["stars", {"type": "pulse", "x": 270, "y": 467, "r": 60, "period": 1.0, "color": "#5BE7FF"}],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 560},
     "cam": [{"at": "Fall through the Earth, or", "zoom": 1.45, "cx": 270, "cy": 470, "dur": 4.0, "ease": "inout"}],
     "objects": [{"id": "g16", "x": 270, "y": 640, "svg": globe(190), "anim": {"bob": 4, "period": 3}},
                 {"id": "t16", "x": 270, "y": 458, "scale": 0.9, "svg": TINY, "anim": {"bob": 3, "period": 0.8}}]},
]

hud = [
    {"type": "title", "at": 0.05, "until": "You'd pop out", "small": "WHAT IF YOU JUMPED", "text": "THROUGH EARTH?", "color": "#5BE7FF", "size": 66, "top": 150},
    {"type": "title", "at": "about forty minutes later", "until": "Picture a tunnel", "small": "TO THE OTHER SIDE", "text": "40 MINUTES", "color": "#FFD27A", "size": 76, "top": 150, "captions": True},
    {"type": "title", "at": "hotter than lava", "until": "Then the walls turn", "small": "THE MANTLE", "text": "HOTTER THAN LAVA", "color": "#FF8A5B", "size": 58, "top": 150, "captions": True},
    {"type": "title", "at": "twenty times faster", "until": "And right at the center", "small": "TOP SPEED", "text": "20x SOUND", "color": "#FFD27A", "size": 80, "top": 150, "captions": True},
    {"type": "title", "at": "you weigh nothing", "until": "straight through a solid", "small": "THE CENTER OF THE EARTH", "text": "WEIGHTLESS", "color": "#C8FF4D", "size": 74, "top": 150, "captions": True},
    {"type": "compare", "at": "Forty minutes is also", "until": "Fall through the Earth, or", "label": "TIME · COMPARE",
     "a": ["Fall through Earth", "~40 min", 1.0], "b": ["Half an orbit", "~40 min", 1.0]},
    {"type": "title", "at": "same clock", "until": "end:same clock+1.0", "text": "SAME CLOCK", "color": "#5BE7FF", "size": 86, "top": 160, "sfx": "chime"},
]

ep.update({
    "ep": 41,
    "voiceover": "voiceover.wav",
    "accent": "#5BE7FF",
    "show_ep": False,
    "thumbnail": "about forty minutes later+0.6",
    "highlights": {"forty minutes": "amber", "pole to pole": "green", "hotter than lava": "amber",
                   "bigger than the Moon": "green", "you weigh nothing": "green", "same clock": "green"},
    "music": [{"track": "music/lost-islands.mp3", "at": 0},
              {"track": "music/deeper.mp3", "at": "Ten minutes in"},
              {"track": "music/destiny.mp3", "at": "And right at the center"}],
    "music_db_below_voice": 20,
    "hud": hud,
    "shakes": [{"at": "and the ground is gone", "amp": 12, "dur": 0.4}, {"at": "slam you", "amp": 10, "dur": 0.3, "sfx": ""},
               {"at": "and fall back in", "amp": 8, "dur": 0.3}],
    "flashes": [{"at": "you weigh nothing", "dur": 0.12, "color": "#FFF6D8"}],
    "sfx": [{"name": "riser", "at": "You're falling about twenty", "gain": 0.6}],
    "scenes": scenes,
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
