import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"

BUS = (f"<rect x='-120' y='-46' width='240' height='86' rx='14' fill='#F2C94C' stroke='{INK}' stroke-width='5'/>"
       + "".join(f"<rect x='{-104 + i*44}' y='-32' width='34' height='30' rx='4' fill='#BFE3FF' stroke='{INK}' stroke-width='3'/>" for i in range(5))
       + f"<rect x='-120' y='12' width='240' height='8' fill='#E0443E'/>"
       f"<circle cx='-70' cy='42' r='18' fill='{INK}'/><circle cx='70' cy='42' r='18' fill='{INK}'/>"
       f"<circle cx='-70' cy='42' r='7' fill='#C9D2EE'/><circle cx='70' cy='42' r='7' fill='#C9D2EE'/>")
CRACK = (f"<path d='M0 0 L-30 -40 L-18 -70 M0 0 L36 -30 L60 -24 M0 0 L10 50 L-14 80 M0 0 L-46 18 M0 0 L44 30' stroke='{INK}' stroke-width='5' fill='none' stroke-linecap='round'/>")
WALL_HOLE = f"<circle r='30' fill='#2B2840' stroke='{INK}' stroke-width='4'/>" + CRACK
BED_L = f"<rect x='-110' y='-18' width='110' height='30' rx='6' fill='#7FD1FF' stroke='{INK}' stroke-width='4'/><rect x='-110' y='12' width='110' height='14' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/><rect x='-110' y='-60' width='18' height='90' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/>"
BED_R = f"<rect x='0' y='-18' width='110' height='30' rx='6' fill='#7FD1FF' stroke='{INK}' stroke-width='4'/><rect x='0' y='12' width='110' height='14' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/><rect x='92' y='-40' width='18' height='70' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/>"
MIRROR = f"<rect x='150' y='420' width='260' height='240' rx='16' fill='#BFE3FF' stroke='{INK}' stroke-width='6'/><path d='M190 460 L240 420 M220 500 L300 430' stroke='#F4F1FF' stroke-width='8' opacity='.7'/><rect x='120' y='690' width='320' height='24' rx='8' fill='#F4F1FF' stroke='{INK}' stroke-width='4'/>"
TUBE = f"<path d='M-40 -14 L30 -14 L44 -6 L44 6 L30 14 L-40 14 Z' fill='#F4F1FF' stroke='{INK}' stroke-width='4'/><rect x='-40' y='-14' width='22' height='28' fill='#E0443E'/><rect x='44' y='-5' width='12' height='10' fill='#3FAE6A' stroke='{INK}' stroke-width='3'/>"
SPLAT = "".join(f"<circle cx='{x}' cy='{y}' r='{r}' fill='#F4F1FF' stroke='#7FD1FF' stroke-width='4'/>" for x, y, r in
                [(0, 0, 34), (-50, -20, 18), (46, -30, 22), (30, 40, 16), (-40, 36, 14), (70, 10, 12), (-80, 0, 10), (10, -60, 14)])
FIST = (f"<rect x='-70' y='-60' width='140' height='120' rx='40' fill='#F2D3B8' stroke='{INK}' stroke-width='7'/>"
        + "".join(f"<path d='M{-50 + i*34} -60 Q{-33 + i*34} -84 {-16 + i*34} -60' fill='#F2D3B8' stroke='{INK}' stroke-width='6'/>" for i in range(4))
        + f"<path d='M-70 0 Q-110 -10 -100 40 Q-80 60 -50 40' fill='#F2D3B8' stroke='{INK}' stroke-width='6'/>")
TRUCK = (f"<rect x='-150' y='-70' width='200' height='110' rx='8' fill='#F4F1FF' stroke='{INK}' stroke-width='6'/>"
         "<text x='-50' y='4' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='40' fill='#141218'>40 t</text>"
         f"<path d='M50 -40 L110 -40 L150 0 L150 40 L50 40 Z' fill='#2F6FD6' stroke='{INK}' stroke-width='6'/><rect x='70' y='-30' width='40' height='26' fill='#BFE3FF' stroke='{INK}' stroke-width='3'/>"
         + "".join(f"<circle cx='{x}' cy='46' r='20' fill='{INK}'/><circle cx='{x}' cy='46' r='8' fill='#C9D2EE'/>" for x in (-120, -70, 100)))
CAN = f"<rect x='-16' y='-28' width='32' height='56' rx='6' fill='#E0443E' stroke='{INK}' stroke-width='3'/><rect x='-16' y='-6' width='32' height='10' fill='#F4F1FF'/>"
CAN_CRUSH = f"<path d='M-18 -10 L-8 -16 L6 -8 L18 -14 L14 6 L18 12 L-16 14 L-10 2 Z' fill='#E0443E' stroke='{INK}' stroke-width='3'/>"
CAR = (f"<rect x='-80' y='-30' width='160' height='46' rx='14' fill='#7FD1FF' stroke='{INK}' stroke-width='5'/><path d='M-46 -30 L-30 -66 L36 -66 L54 -30 Z' fill='#BFE3FF' stroke='{INK}' stroke-width='5'/>"
       f"<circle cx='-46' cy='18' r='18' fill='{INK}'/><circle cx='46' cy='18' r='18' fill='{INK}'/><circle cx='-46' cy='18' r='7' fill='#C9D2EE'/><circle cx='46' cy='18' r='7' fill='#C9D2EE'/>")
CAR_NOBUMP = CAR
BUMPER = f"<rect x='-10' y='-26' width='20' height='52' rx='6' fill='#C9D2EE' stroke='{INK}' stroke-width='4'/>"
SMOKE = "<g fill='#C9D2EE' opacity='.7'><circle r='16'/><circle cx='14' cy='-14' r='12'/><circle cx='-10' cy='-20' r='10'/></g>"
ROAD = "<rect x='0' y='812' width='540' height='60' fill='#3A3550'/><path d='M0 842 L540 842' stroke='#F2C94C' stroke-width='4' stroke-dasharray='30 22'/>"
GROUND = f"<rect x='-220' y='0' width='440' height='60' fill='#6B6680' stroke='{INK}' stroke-width='5'/>"
SHOE = f"<path d='M-60 0 L-60 -40 Q-20 -46 0 -22 L60 -14 Q70 0 60 0 Z' fill='#E46F8E' stroke='{INK}' stroke-width='5'/>"
def arrow(x1, y1, x2, y2, color, w=10):
    return (f"<path d='M{x1} {y1} L{x2} {y2}' stroke='{color}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<circle cx='{x2}' cy='{y2}' r='{w}' fill='{color}'/>")
def label(x, y, t, color="#F4F1FF", size=26):
    return f"<text x='{x}' y='{y}' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='{size}' fill='{color}'>{t}</text>"
GRIP_DIAGRAM = (f"<g transform='translate(270 640)'>{GROUND}{SHOE}</g>"
                + arrow(260, 560, 260, 400, "#7FD1FF") + label(260, 380, "STRENGTH x1000", "#7FD1FF")
                + arrow(250, 660, 250, 760, "#FFD27A") + label(360, 760, "WEIGHT x1", "#FFD27A")
                + arrow(200, 650, 90, 650, "#FF6B6B", 8) + label(120, 620, "GRIP", "#FF6B6B"))
SIDEWALK_CRACK = f"<g transform='translate(200 812) scale(1.6 .5)'>{CRACK}</g>"
BONE = (f"<g stroke='{INK}' stroke-width='7' fill='#F4F1FF'><rect x='-120' y='-22' width='240' height='44' rx='20'/>"
        "<circle cx='-130' cy='-24' r='30'/><circle cx='-130' cy='24' r='30'/><circle cx='130' cy='-24' r='30'/><circle cx='130' cy='24' r='30'/></g>"
        "<rect x='-120' y='-14' width='240' height='28' fill='#F4F1FF'/>")
CRATER = f"<ellipse cx='270' cy='822' rx='190' ry='34' fill='#4A3A2E' stroke='{INK}' stroke-width='5'/><ellipse cx='270' cy='828' rx='140' ry='20' fill='#2B2240'/>" + \
         "".join(f"<circle cx='{x}' cy='{y}' r='{r}' fill='#6B4A3A' stroke='{INK}' stroke-width='3'/>" for x, y, r in [(80, 800, 12), (460, 796, 14), (120, 780, 8), (430, 776, 9)])
BENCH = f"<rect x='400' y='740' width='110' height='12' fill='#6B4A3A' stroke='{INK}' stroke-width='3' transform='rotate(-28 455 746)'/>"
BALL = f"<circle r='12' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/><path d='M-6 -10 Q0 0 -6 10 M6 -10 Q0 0 6 10' stroke='#E0443E' stroke-width='2' fill='none'/>"
CONE = "<path d='M0 0 L-120 -70 M0 0 L-120 70' stroke='#F4F1FF' stroke-width='5' opacity='.8'/>"
EGG = f"<ellipse rx='18' ry='24' fill='#FFF6E0' stroke='{INK}' stroke-width='3'/>"
EGG_CRACK = f"<ellipse rx='18' ry='24' fill='#FFF6E0' stroke='{INK}' stroke-width='3'/><path d='M-16 -2 L-6 -8 L0 2 L8 -6 L16 0' stroke='{INK}' stroke-width='3' fill='none'/><ellipse cy='28' rx='22' ry='6' fill='#F2C94C'/>"
PIANO = (f"<rect x='-80' y='-60' width='160' height='100' rx='6' fill='#2B2840' stroke='{INK}' stroke-width='5'/>"
         f"<rect x='-80' y='10' width='160' height='26' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/>"
         + "".join(f"<rect x='{-74 + i*20}' y='10' width='10' height='16' fill='{INK}'/>" for i in range(8))
         + f"<rect x='-70' y='40' width='10' height='40' fill='#2B2840' stroke='{INK}' stroke-width='3'/><rect x='60' y='40' width='10' height='40' fill='#2B2840' stroke='{INK}' stroke-width='3'/>")
BUTTERFLY = ("<path d='M0 0 Q-40 -50 -60 -20 Q-56 10 0 0 Z' fill='#FF8E3C' stroke='#141218' stroke-width='3'/>"
             "<path d='M0 0 Q40 -50 60 -20 Q56 10 0 0 Z' fill='#FF8E3C' stroke='#141218' stroke-width='3'/>"
             "<path d='M0 0 Q-30 30 -40 20 Q-30 6 0 0 Z' fill='#F2C94C' stroke='#141218' stroke-width='3'/>"
             "<path d='M0 0 Q30 30 40 20 Q30 6 0 0 Z' fill='#F2C94C' stroke='#141218' stroke-width='3'/>"
             "<rect x='-3' y='-16' width='6' height='30' rx='3' fill='#141218'/>")
BLANKET = "<path d='M330 790 L500 790 L520 826 L310 826 Z' fill='#E46F8E' stroke='#141218' stroke-width='4'/><path d='M360 790 L350 826 M400 790 L395 826 M440 790 L440 826 M480 790 L485 826' stroke='#F4F1FF' stroke-width='5'/>"
ROPE = "<path d='M-140 0 Q0 10 140 0' stroke='#C9A06A' stroke-width='7' fill='none'/><rect x='-6' y='-14' width='12' height='28' fill='#E0443E'/>"
LINE = "<rect x='262' y='800' width='16' height='40' fill='#F4F1FF' opacity='.9'/>"
FEET_DIAGRAM = (f"<g transform='translate(270 690)'>{GROUND}</g>"
                + f"<g transform='translate(140 690) scale(.8)'>{SHOE}</g><g transform='translate(400 690) scale(-1.1 1.1)'>{SHOE}</g>"
                + arrow(140, 590, 140, 520, "#7FD1FF", 8) + label(140, 500, "YOU", "#7FD1FF")
                + arrow(400, 570, 400, 430, "#FFD27A", 14) + label(400, 410, "DAD", "#FFD27A")
                + arrow(110, 700, 60, 700, "#FF6B6B", 6) + arrow(440, 700, 520, 700, "#FF6B6B", 12))
RAYS = {"type": "rays", "x": 270, "y": 520, "spin": 8, "opacity": 0.12}


def hero(x, y, scale=1.3, **kw):
    a = {"id": "hero", "char": "hero", "x": x, "y": y, "scale": scale}
    a.update(kw)
    return a


def dad(x, y, scale=1.55, **kw):
    a = {"id": "dad", "char": "extra", "shirt": "#3FAE6A", "x": x, "y": y, "scale": scale}
    a.update(kw)
    return a


scenes = [
    # 1 open: you hold a bus over your head with one hand
    {"bg": "day_park", "fx": [{"type": "dust", "n": 30, "speed": 0.5}, {"type": "clouds", "speed": 6, "opacity": 0.5}],
     "cam_start": {"zoom": 1.25, "cx": 260, "cy": 600},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 540, "dur": 2.4, "ease": "out"}],
     "objects": [{"id": "bus", "x": 250, "y": 480, "scale": 0.9, "rot": -4, "front": True, "svg": BUS, "anim": {"bob": 8, "sway": 3, "period": 1.6},
                  "keys": [{"at": "Strong enough", "x": 235, "y": 470, "dur": 0.5, "ease": "back"}]}],
     "actors": [hero(220, 815, pose="reach_up", face="smug")]},
    # 2 the open loop: your dad, waiting (no hero)
    {"start": "And the thing", "bg": "dusk", "camera": "zoom_in", "zoom": 1.25, "cx": 270, "cy": 620, "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "rays", "x": 270, "y": 560, "spin": 6, "opacity": 0.16, "color": "#FFD27A"}],
     "actors": [dad(270, 815, scale=1.7, pose="idle", face="smug",
                    keys=[{"at": "it's your dad", "pose": "point", "face": "happy", "dur": 0.15}])]},
    # 3 second one: fist through the wall
    {"start": "Second one", "bg": "warm_interior", "camera": "push", "transition": "flash",
     "fx": [{"type": "dust", "n": 20, "speed": 0.4}],
     "objects": [{"id": "hole", "x": 360, "y": 560, "opacity": 0, "svg": WALL_HOLE,
                  "keys": [{"at": "straight through", "opacity": 1, "dur": 0.05, "sfx": "thud"}]}],
     "actors": [hero(220, 808, pose="lie", face="bored",
                     keys=[{"at": "You wake up", "pose": "sit", "dur": 0.4}, {"at": "stretch", "pose": "reach_up", "face": "happy", "dur": 0.3},
                           {"at": "straight through", "face": "shocked", "dur": 0.1}])]},
    # 4 the bed frame snaps
    {"start": "You sit up", "bg": "warm_interior", "camera": "closeup", "focus": "hero", "zoom": 1.35, "focus_y": 680,
     "fx": [{"type": "dust", "n": 25, "speed": 0.6}],
     "objects": [{"id": "bl", "x": 270, "y": 780, "svg": BED_L, "keys": [{"at": "snaps", "rot": -18, "x": 250, "dur": 0.2, "sfx": "thud"}]},
                 {"id": "br", "x": 270, "y": 780, "svg": BED_R, "keys": [{"at": "snaps", "rot": 18, "x": 290, "dur": 0.2}]}],
     "actors": [hero(260, 772, pose="sit", face="neutral", keys=[{"at": "snaps", "face": "shocked", "dur": 0.1}])]},
    # 5 minute five: toothpaste blasts across the mirror
    {"start": "Minute five", "bg": "cool_interior", "camera": "static", "transition": "whip", "whip_dir": "right",
     "props": MIRROR, "fx": [{"type": "bubbles", "n": 18, "speed": 0.5}],
     "objects": [{"id": "splat", "x": 280, "y": 540, "opacity": 0, "scale": 0.3, "svg": SPLAT,
                  "keys": [{"at": "blasts", "opacity": 1, "scale": 1.6, "dur": 0.2, "ease": "out", "sfx": "pop"}]},
                 {"id": "tube", "x": 150, "y": 640, "svg": TUBE, "front": True, "anim": {"sway": 4, "period": 1.2},
                  "keys": [{"at": "You squeeze", "attach": "hero.hand", "dx": 0, "dy": -10}]}],
     "actors": [hero(140, 812, pose="hold", face="focused", keys=[{"at": "blasts", "face": "shocked", "dur": 0.1}])]},
    # 6 a normal hand vs yours (no hero)
    {"start": "A normal hand", "bg": "void", "camera": "zoom_in", "zoom": 1.2, "cy": 600,
     "fx": [{"type": "pulse", "x": 270, "y": 640, "r": 170, "period": 1.2, "color": "#F2D3B8"}],
     "objects": [{"id": "fist", "x": 270, "y": 640, "scale": 1.3, "svg": FIST, "anim": {"pulse": 0.06, "period": 0.7}}]},
    # 7 forty tonnes: a loaded truck (no hero)
    {"start": "Yours squeezes", "bg": "space", "camera": "push", "transition": "zoom",
     "fx": ["stars", RAYS],
     "objects": [{"id": "truck", "x": 270, "y": 600, "scale": 1.2, "svg": TRUCK, "anim": {"bob": 10, "sway": 2, "period": 3}}]},
    # 8 holding things gently: a can crumples
    {"start": "So the hardest skill", "bg": "warm_interior", "camera": "closeup", "focus": "hero", "zoom": 2.0, "focus_y": 640,
     "fx": [{"type": "dust", "n": 15, "speed": 0.3}],
     "objects": [{"id": "can", "x": 0, "y": 0, "svg": CAN, "front": True, "keys": [{"at": 0, "attach": "hero.hand", "dx": 0, "dy": -18}]},
                 {"id": "can2", "x": 0, "y": 0, "svg": CAN_CRUSH, "front": True, "opacity": 0,
                  "keys": [{"at": 0, "attach": "hero.hand", "dx": 0, "dy": -14}, {"at": "gently", "opacity": 1, "dur": 0.05, "sfx": "click"}]}],
     "actors": [hero(230, 808, pose="hold", face="worried", keys=[{"at": "gently", "face": "sad", "dur": 0.2}])]},
    # 9 minute twenty: you push a car and slide backwards
    {"start": "Minute twenty", "bg": "city_day", "camera": "pan_right", "transition": "whip", "whip_dir": "left",
     "props": ROAD, "fx": [{"type": "dust", "n": 30, "speed": 0.7}],
     "objects": [{"id": "car", "x": 360, "y": 800, "scale": 1.2, "svg": CAR},
                 {"id": "smoke", "x": 440, "y": 740, "svg": SMOKE, "anim": {"drift": [10, -30], "flicker": 0.3, "period": 1}}],
     "actors": [hero(240, 818, pose="catch", face="determined",
                     keys=[{"at": "Your feet skid", "x": 130, "dur": 1.0, "ease": "out", "face": "shocked", "sfx": "swish"}])]},
    # 10 why: grip comes from weight (no hero)
    {"start": "Pushing needs grip", "bg": "void", "camera": "drift",
     "fx": [{"type": "pulse", "x": 250, "y": 650, "r": 120, "period": 1.4, "color": "#FF6B6B"}],
     "props": "<g transform='translate(0 60)'>" + GRIP_DIAGRAM + "</g>"},
    # 11 the bumper tears off like paper
    {"start": "So you lift it instead", "bg": "city_day", "camera": "zoom_in", "zoom": 1.2, "cx": 270, "cy": 700,
     "props": ROAD, "fx": [{"type": "dust", "n": 25, "speed": 0.5}],
     "objects": [{"id": "car", "x": 340, "y": 800, "scale": 1.2, "svg": CAR},
                 {"id": "bump", "x": 240, "y": 790, "svg": BUMPER,
                  "keys": [{"at": "tears off", "attach": "hero.hand", "dx": 0, "dy": -10, "rot": 70, "sfx": "swish"}]}],
     "actors": [hero(200, 818, pose="catch", face="focused",
                     keys=[{"at": "tears off", "pose": "throw_back", "face": "shocked", "dur": 0.12}])]},
    # 12 carry it to the curb like a pizza box
    {"start": "So you slide your hands", "bg": "city_day", "camera": "pan_left",
     "props": ROAD, "fx": [{"type": "clouds", "speed": 8, "opacity": 0.4}],
     "objects": [{"id": "car", "x": 0, "y": 0, "scale": 1.0, "front": True, "svg": CAR,
                  "keys": [{"at": 0, "attach": "hero.hand", "dx": 0, "dy": -60}]}],
     "actors": [hero(400, 818, pose="reach_up", face="happy", flip=True,
                     keys=[{"at": "carry it", "x": 140, "dur": 2.2, "cycle": "walk"}, {"at": "pizza box", "cycle": None, "pose": "reach_up"}])]},
    # 13 hour one: you jump for the bus, the sidewalk cracks (wide)
    {"start": "Hour one", "bg": "dusk", "camera": "static", "transition": "flash",
     "props": ROAD, "fx": [{"type": "speedlines", "dir": "right", "speed": 1.2, "n": 12}],
     "objects": [{"id": "bus2", "x": 380, "y": 770, "scale": 0.8, "svg": BUS,
                  "keys": [{"at": "pulling away", "x": 640, "dur": 3.0, "ease": "in"}]},
                 {"id": "crk", "x": 0, "y": 0, "opacity": 0, "svg": SIDEWALK_CRACK,
                  "keys": [{"at": "cracks like ice", "opacity": 1, "dur": 0.05}]}],
     "actors": [hero(200, 818, scale=1.0, pose="run_a", face="worried",
                     keys=[{"at": "so you jump", "pose": "crouch", "dur": 0.2},
                           {"at": "cracks like ice", "pose": "jump", "lift": 700, "dur": 0.6, "ease": "in", "face": "shocked"}])]},
    # 14 up past two hundred meters (tiny hero)
    {"start": "The air drags", "bg": "sky", "camera": "zoom_in", "zoom": 1.1, "cx": 270, "cy": 600,
     "fx": [{"type": "clouds", "speed": -30, "opacity": 0.7}, {"type": "speedlines", "dir": "left", "speed": 2, "n": 10}],
     "objects": [{"id": "tower", "x": 400, "y": 760, "svg": "<rect x='-40' y='-460' width='80' height='560' fill='#3A3550' stroke='#141218' stroke-width='4'/>" + "".join(f"<rect x='-28' y='{-440 + i*40}' width='56' height='16' fill='#F2C94C' opacity='.7'/>" for i in range(13))}],
     "actors": [hero(150, 800, scale=0.8, pose="jump", face="happy", shadow=False,
                     keys=[{"at": "The air drags", "y": 560, "dur": 3.5, "ease": "out"}])]},
    # 15 then you fall (tiny hero)
    {"start": "Then you fall", "bg": "sky", "camera": "drift",
     "fx": [{"type": "clouds", "speed": 40, "opacity": 0.7}, {"type": "speedlines", "dir": "right", "speed": 2.5, "n": 14}],
     "actors": [hero(270, 560, scale=0.8, pose="dive", face="shocked", rot=180, shadow=False,
                     keys=[{"at": "belly down", "rot": 90, "pose": "fall", "dur": 0.6}])]},
    # 16 bones a thousand times tougher (no hero)
    {"start": "Your bones got", "bg": "space", "camera": "closeup", "zoom": 1.4, "cx": 270, "cy": 600,
     "fx": ["stars", {"type": "pulse", "x": 270, "y": 600, "r": 200, "period": 1.0, "color": "#C8FF4D"}],
     "objects": [{"id": "bone", "x": 270, "y": 600, "rot": -20, "scale": 1.1, "svg": BONE, "anim": {"pulse": 0.05, "spin": 6, "period": 1.0}}]},
    # 17 the park now has a crater (wide)
    {"start": "The park you land in", "bg": "dusk", "camera": "reveal", "cx": 270, "cy": 780, "zoom": 2.0, "transition": "flash",
     "props": CRATER + BENCH, "fx": [{"type": "dust", "n": 25, "speed": 0.8, "color": "#C9A06A"}],
     "actors": [hero(270, 815, scale=1.0, pose="cheer", face="happy")]},
    # 18 day ten: a baseball breaks the sound barrier (wide)
    {"start": "Day ten", "bg": "stadium", "camera": "pan_right", "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "confetti", "n": 20}],
     "objects": [{"id": "ball", "x": 140, "y": 700, "svg": BALL, "anim": {"spin": 720},
                  "keys": [{"at": "leaves your hand", "x": 620, "y": 640, "dur": 0.25, "ease": "linear"}]},
                 {"id": "cone", "x": 470, "y": 650, "opacity": 0, "svg": CONE,
                  "keys": [{"at": "breaks the sound", "opacity": 1, "dur": 0.1}, {"at": "hears a boom", "opacity": 0, "x": 600, "dur": 0.6}]}],
     "actors": [hero(130, 800, scale=1.0, pose="throw_back", face="determined",
                     keys=[{"at": "leaves your hand-0.1", "pose": "throw", "dur": 0.1}, {"at": "hears a boom", "face": "shocked", "dur": 0.1}])]},
    # 19 day thirty: Mia's high five
    {"start": "Day thirty", "bg": "cool_interior", "camera": "push", "transition": "cut",
     "fx": [{"type": "dust", "n": 18, "speed": 0.3}],
     "actors": [{"id": "mia", "char": "mia", "x": 340, "y": 812, "scale": 1.25, "flip": True, "pose": "wave", "face": "happy"},
                hero(180, 812, pose="idle", face="worried", keys=[{"at": "before you dare", "pose": "shrug", "dur": 0.3}])]},
    # 20 practicing on eggs
    {"start": "you spend a whole week", "bg": "lab", "camera": "zoom_in", "zoom": 1.3, "cx": 300, "cy": 700,
     "fx": [{"type": "pulse", "x": 330, "y": 760, "r": 90, "period": 1.3, "color": "#FFF6E0"}],
     "objects": [{"id": f"e{i}", "x": 270 + i * 46, "y": 800, "svg": EGG_CRACK if i < 4 else EGG, "anim": {"bob": 1, "period": 1 + i * 0.1}} for i in range(5)],
     "actors": [hero(170, 830, pose="hold", face="focused", look=0.6)]},
    # 21 year one: you catch a falling piano
    {"start": "Year one", "bg": "future_city", "camera": "static", "transition": "flash",
     "fx": [{"type": "speedlines", "dir": "right", "speed": 0.8, "n": 6}, "stars"],
     "objects": [{"id": "piano", "x": 260, "y": 100, "svg": PIANO, "anim": {"sway": 6, "period": 0.8},
                  "keys": [{"at": "catch a falling piano", "y": 560, "dur": 0.7, "ease": "in", "stop_anim": True, "sfx": "thud"}]}],
     "actors": [hero(250, 815, pose="reach_up", face="focused", keys=[{"at": "catch a falling piano+0.7", "face": "smug", "dur": 0.2}])]},
    # 22 and you can hold a butterfly
    {"start": "and you can hold a butterfly", "bg": "forest", "camera": "closeup", "focus": "hero", "zoom": 1.9, "focus_y": 640,
     "fx": [{"type": "dust", "n": 30, "speed": 0.3, "color": "#C8FF4D"}],
     "objects": [{"id": "bf", "x": 360, "y": 520, "svg": BUTTERFLY, "front": True, "anim": {"pulse": 0.15, "period": 0.35},
                  "keys": [{"at": "hold a butterfly", "attach": "hero.hand", "dx": 0, "dy": -20, "dur": 0.8}]}],
     "actors": [hero(220, 818, pose="hold", face="happy")]},
    # 23 the picnic tug of war: you slide toward Dad
    {"start": "So at the family picnic", "bg": "day_park", "camera": "pan_left", "transition": "whip", "whip_dir": "left",
     "props": BLANKET, "fx": [{"type": "clouds", "speed": 6, "opacity": 0.5}, {"type": "confetti", "n": 10}],
     "objects": [{"id": "rope", "x": 270, "y": 700, "svg": ROPE, "anim": {"sway": 1, "period": 0.4},
                  "keys": [{"at": "you slide straight", "x": 340, "dur": 1.8}]}],
     "actors": [hero(110, 818, pose="throw_back", face="determined",
                     keys=[{"at": "you slide straight", "x": 200, "dur": 1.8, "face": "shocked", "sfx": "swish"}]),
                dad(430, 818, flip=True, pose="hold", face="smug")]},
    # 24 why: tug of war is won with your feet (no hero)
    {"start": "Because tug of war", "bg": "void", "camera": "push", "transition": "zoom",
     "fx": [RAYS], "props": "<g transform='translate(0 90)'>" + FEET_DIAGRAM + "</g>"},
    # 25 so you cheat: pick up your dad, carry him across the line (loop to the opening lift)
    {"start": "So you cheat", "bg": "day_park", "camera": "static",
     "cam_start": {"zoom": 1.7, "cx": 200, "cy": 640},
     "cam": [{"at": "You walk over", "zoom": 1.0, "cx": 270, "cy": 540, "dur": 1.6, "ease": "out"}],
     "props": BLANKET + LINE, "fx": [{"type": "confetti", "n": 30}, {"type": "clouds", "speed": 6, "opacity": 0.5}],
     "actors": [hero(160, 818, pose="idle", face="smug",
                     keys=[{"at": "You walk over", "x": 360, "dur": 1.0, "cycle": "walk"},
                           {"at": "pick up your dad", "cycle": None, "pose": "reach_up", "dur": 0.2},
                           {"at": "carry him", "x": 200, "dur": 1.6, "flip": True, "pose": "reach_up"}]),
                dad(400, 818, flip=True, pose="hold", face="smug",
                    keys=[{"at": "pick up your dad", "x": 300, "lift": 190, "pose": "lie", "face": "shocked", "dur": 0.3, "sfx": "boing"},
                          {"at": "carry him", "x": 140, "dur": 1.6}])]},
]

hud = [
    {"type": "title", "at": 0.05, "until": "Strong enough", "small": "WHAT IF YOU WERE", "text": "1,000x STRONGER?", "color": "#C8FF4D", "top": 120},
    {"type": "marker", "at": "Second one", "until": "You sit up", "label": "SECOND", "text": "1"},
    {"type": "marker", "at": "Minute five", "until": "You squeeze", "label": "MINUTE", "text": "5"},
    {"type": "compare", "at": "A normal hand", "until": "So the hardest", "label": "GRIP · COMPARE", "a": ["Normal hand", "40 kg", 0.02], "b": ["You", "40,000 kg", 1.0]},
    {"type": "title", "at": "forty tonnes", "until": "So the hardest", "small": "YOUR GRIP", "text": "40 TONNES", "sub": "A FULLY LOADED TRUCK", "color": "#FFD27A", "size": 76, "top": 160, "captions": True},
    {"type": "marker", "at": "Minute twenty", "until": "A car has", "label": "MINUTE", "text": "20"},
    {"type": "note", "at": "Pushing needs grip", "until": "So you lift it", "label": "REAL SCIENCE", "text": "Grip comes from weight. Strength x1000. Weight x1."},
    {"type": "marker", "at": "Hour one", "until": "You're late", "label": "HOUR", "text": "1"},
    {"type": "title", "at": "two hundred meters", "until": "Then you fall", "small": "JUMP HEIGHT", "text": "200+ METERS", "color": "#C8FF4D", "size": 70, "top": 160, "captions": True},
    {"type": "title", "at": "two hundred kilometers", "until": "Your bones", "small": "FALLING SPEED", "text": "200 KM/H", "color": "#FF6B6B", "size": 76, "top": 160, "captions": True},
    {"type": "marker", "at": "Day ten", "until": "You throw", "label": "DAY", "text": "10"},
    {"type": "marker", "at": "Day thirty", "until": "Your best friend", "label": "DAY", "text": "30"},
    {"type": "marker", "at": "Year one", "until": "You can catch", "label": "YEAR", "text": "1"},
    {"type": "title", "at": "It's won by pushing", "until": "So you cheat", "small": "TUG OF WAR IS WON", "text": "WITH YOUR FEET", "color": "#FFD27A", "size": 60, "top": 160, "captions": True},
    {"type": "title", "at": "So you cheat", "until": "You walk over", "text": "CHEAT.", "color": "#C8FF4D", "size": 110, "top": 180, "sfx": "thud"},
]

ep.update({
    "scenes": scenes, "hud": hud,
    "shakes": [{"at": "straight through", "amp": 12, "dur": 0.4}, {"at": "cracks like ice", "amp": 16, "dur": 0.5},
               {"at": "now has a crater", "amp": 18, "dur": 0.6}, {"at": "hears a boom", "amp": 14, "dur": 0.5}],
    "flashes": [{"at": "breaks the sound", "dur": 0.12}, {"at": "now has a crater", "dur": 0.12, "color": "#FFE7A0"}],
    "music": [{"track": "music/crossroads.mp3", "at": 0},
              {"track": "music/surreptitious.mp3", "at": "A car has broken"},
              {"track": "music/find-you.mp3", "at": "Year one"}],
    "highlights": {"forty tonnes": "amber", "same as yesterday": "green", "one millimeter": "amber", "two hundred meters": "green",
                   "sound barrier": "amber", "Dad weighs more": "green", "a butterfly": "green"},
    "thumbnail": "Strong enough",
    "accent": "#C8FF4D",
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
