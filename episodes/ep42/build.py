import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"
FLOAT = {"shadow": False}


def ruler(x=440, top=300, bottom=812, step=40):
    """A tall measuring pole with tick marks."""
    t = "".join(f"<rect x='{x-14}' y='{y}' width='{28 if i % 2 == 0 else 16}' height='5' fill='{INK}'/>"
                for i, y in enumerate(range(bottom - step, top, -step)))
    return (f"<rect x='{x-14}' y='{top}' width='28' height='{bottom-top}' rx='4' fill='#FFD27A' stroke='{INK}' stroke-width='4'/>{t}")


RULER = ruler()
MARK = f"<rect x='-30' y='-4' width='60' height='8' rx='4' fill='#FF6B6B' stroke='{INK}' stroke-width='3'/>"

BED = (f"<rect x='60' y='735' width='300' height='40' rx='10' fill='#7FD1FF' stroke='{INK}' stroke-width='5'/>"
       f"<rect x='60' y='772' width='300' height='20' fill='#6B4A3A' stroke='{INK}' stroke-width='5'/>"
       f"<rect x='50' y='660' width='24' height='140' rx='6' fill='#6B4A3A' stroke='{INK}' stroke-width='5'/>"
       f"<rect x='346' y='700' width='24' height='100' rx='6' fill='#6B4A3A' stroke='{INK}' stroke-width='5'/>"
       f"<rect x='80' y='712' width='70' height='28' rx='12' fill='#F4F1FF' stroke='{INK}' stroke-width='4'/>")
SHOEBOX = (f"<rect x='-34' y='-22' width='68' height='40' rx='4' fill='#FF8A5B' stroke='{INK}' stroke-width='4'/>"
           f"<rect x='-38' y='-30' width='76' height='12' rx='3' fill='#FFB547' stroke='{INK}' stroke-width='4'/>")
HOOP = (f"<rect x='402' y='420' width='14' height='395' fill='#9AA3C4' stroke='{INK}' stroke-width='4'/>"
        f"<rect x='330' y='400' width='100' height='70' rx='4' fill='#F4F1FF' stroke='{INK}' stroke-width='5'/>"
        f"<rect x='360' y='425' width='40' height='28' fill='none' stroke='#FF6B6B' stroke-width='4'/>"
        f"<ellipse cx='365' cy='478' rx='34' ry='8' fill='none' stroke='#FF8A3D' stroke-width='6'/>"
        f"<path d='M334 480 L344 520 M352 482 L356 522 M378 482 L374 522 M396 480 L386 520' stroke='#F4F1FF' stroke-width='3'/>")
BALL = (f"<circle r='22' fill='#FF8A3D' stroke='{INK}' stroke-width='4'/>"
        f"<path d='M-22 0 L22 0 M0 -22 L0 22' stroke='{INK}' stroke-width='3'/>")
DOOR = (f"<rect x='250' y='590' width='130' height='222' fill='#6B4A3A' stroke='{INK}' stroke-width='6'/>"
        f"<rect x='262' y='602' width='106' height='210' fill='#2B2840'/>"
        f"<rect x='200' y='540' width='240' height='44' rx='6' fill='#FF6B6B' stroke='{INK}' stroke-width='5'/>"
        f"<text x='320' y='571' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='26' fill='#FFF'>SCHOOL</text>")


def cubes(n, s=60):
    """n x n x n isometric-ish block of cubes, centred."""
    g = ""
    off = (n * s) / 2
    for z in range(n):
        for y in range(n):
            for x in range(n):
                px = x * s - off + z * s * 0.45
                py = -y * s + off - z * s * 0.45
                g += (f"<rect x='{px:.0f}' y='{py - s:.0f}' width='{s}' height='{s}' fill='#5BA8FF' stroke='{INK}' stroke-width='4'/>"
                      f"<path d='M{px:.0f} {py - s:.0f} l{s*0.45:.0f} {-s*0.45:.0f} l{s} 0 l{-s*0.45:.0f} {s*0.45:.0f} z' fill='#9FD0FF' stroke='{INK}' stroke-width='4'/>"
                      f"<path d='M{px + s:.0f} {py - s:.0f} l{s*0.45:.0f} {-s*0.45:.0f} l0 {s} l{-s*0.45:.0f} {s*0.45:.0f} z' fill='#3E7FD0' stroke='{INK}' stroke-width='4'/>")
    return g


BONE = (f"<g stroke='{INK}' stroke-width='6' fill='#F4F1FF'><rect x='-110' y='-20' width='220' height='40' rx='18'/>"
        f"<circle cx='-112' cy='-22' r='24'/><circle cx='-112' cy='22' r='24'/><circle cx='112' cy='-22' r='24'/><circle cx='112' cy='22' r='24'/></g>"
        f"<rect x='-108' y='-16' width='216' height='32' fill='#F4F1FF'/>")
CRACK = f"<path d='M-10 -22 L6 -6 L-6 4 L10 22' stroke='#FF6B6B' stroke-width='6' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"

GIRAFFE = (f"<g stroke='{INK}' stroke-width='5'>"
           f"<path d='M-50 0 L-46 -110 M-20 0 L-22 -110 M30 0 L26 -110 M58 0 L56 -110' stroke-width='12' stroke-linecap='round' stroke='#E8B04A'/>"
           f"<ellipse cx='5' cy='-130' rx='75' ry='38' fill='#E8B04A'/>"
           f"<path d='M50 -150 L92 -300 L112 -296 L80 -130 Z' fill='#E8B04A'/>"
           f"<ellipse cx='112' cy='-310' rx='34' ry='18' fill='#E8B04A'/>"
           f"<path d='M98 -326 L96 -344 M110 -328 L110 -346' stroke-width='5'/></g>"
           f"<circle cx='-20' cy='-136' r='9' fill='#8A5A2B'/><circle cx='22' cy='-124' r='11' fill='#8A5A2B'/><circle cx='80' cy='-220' r='8' fill='#8A5A2B'/>"
           f"<circle cx='118' cy='-314' r='4' fill='{INK}'/>")
CAR = (f"<rect x='-56' y='-22' width='112' height='34' rx='10' fill='#FF6B6B' stroke='{INK}' stroke-width='4'/>"
       f"<path d='M-32 -22 L-20 -46 L24 -46 L38 -22 Z' fill='#FFB0A8' stroke='{INK}' stroke-width='4'/>"
       f"<circle cx='-30' cy='12' r='11' fill='{INK}'/><circle cx='30' cy='12' r='11' fill='{INK}'/>")
TENT = (f"<path d='M40 812 L210 560 L380 812 Z' fill='#FF6B6B' stroke='{INK}' stroke-width='6'/>"
        f"<path d='M110 812 L210 560 L310 812' fill='#F4F1FF' stroke='{INK}' stroke-width='5'/>"
        f"<path d='M160 812 L210 560 L260 812' fill='#FF6B6B' stroke='{INK}' stroke-width='5'/>"
        f"<path d='M210 560 L210 520 L250 534 L210 548' fill='#FFD27A' stroke='{INK}' stroke-width='4'/>")
ELEPHANT = (f"<g stroke='{INK}' stroke-width='4' fill='#9AA3C4'>"
            f"<rect x='-40' y='-34' width='16' height='34' rx='4'/><rect x='20' y='-34' width='16' height='34' rx='4'/>"
            f"<ellipse cx='0' cy='-50' rx='52' ry='32'/><circle cx='50' cy='-62' r='24'/>"
            f"<path d='M68 -56 Q86 -30 76 -6' fill='none' stroke-width='9' stroke='#9AA3C4'/><ellipse cx='40' cy='-60' rx='14' ry='20' fill='#B8BFD8'/></g>"
            f"<circle cx='56' cy='-68' r='3' fill='{INK}'/>")
BRIDGE = (f"<rect x='-20' y='700' width='580' height='28' fill='#6B6680' stroke='{INK}' stroke-width='5'/>"
          f"<path d='M-20 700 Q270 520 560 700' stroke='#E0443E' stroke-width='10' fill='none'/>"
          + "".join(f"<path d='M{x} 700 L{x} {700 - int(180 * (1 - ((x - 270) / 290) ** 2))}' stroke='#E0443E' stroke-width='4'/>" for x in range(30, 540, 60))
          + f"<rect x='60' y='728' width='30' height='232' fill='#6B6680' stroke='{INK}' stroke-width='5'/><rect x='450' y='728' width='30' height='232' fill='#6B6680' stroke='{INK}' stroke-width='5'/>")
RIVER = "<rect x='0' y='800' width='540' height='160' fill='#2F6FD6'/><path d='M0 800 L540 800' stroke='#DFF8FF' stroke-width='3' opacity='.6'/>"
SIGN = (f"<rect x='-6' y='0' width='12' height='70' fill='#9AA3C4' stroke='{INK}' stroke-width='3'/>"
        f"<circle cx='0' cy='-20' r='40' fill='#F4F1FF' stroke='#E0443E' stroke-width='10'/>"
        f"<text x='0' y='-10' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='30' fill='{INK}'>10t</text>")
HEART = (f"<path d='M0 60 C-90 0 -90 -70 -40 -80 C-15 -84 0 -60 0 -50 C0 -60 15 -84 40 -80 C90 -70 90 0 0 60 Z' fill='#FF6B6B' stroke='{INK}' stroke-width='7'/>"
         f"<path d='M-40 -50 Q-55 -30 -45 -10' stroke='#FFB0A8' stroke-width='8' fill='none' stroke-linecap='round'/>")
DROP = f"<path d='M0 -16 Q12 0 0 12 Q-12 0 0 -16 Z' fill='#E0443E' stroke='{INK}' stroke-width='3'/>"
PIPE = (f"<rect x='255' y='470' width='30' height='200' rx='10' fill='#3A1C2A' stroke='{INK}' stroke-width='5'/>"
        f"<circle cx='270' cy='450' r='56' fill='#F2D3B8' stroke='{INK}' stroke-width='6'/>"
        f"<circle cx='252' cy='442' r='6' fill='{INK}'/><circle cx='288' cy='442' r='6' fill='{INK}'/>")
THERMO = (f"<rect x='-16' y='-140' width='32' height='170' rx='16' fill='#F4F1FF' stroke='{INK}' stroke-width='5'/>"
          f"<circle cx='0' cy='44' r='30' fill='#FF6B6B' stroke='{INK}' stroke-width='5'/>"
          f"<rect x='-8' y='-110' width='16' height='150' rx='8' fill='#FF6B6B'/>")
TRUCK = (f"<rect x='-110' y='-60' width='170' height='70' rx='6' fill='#E0443E' stroke='{INK}' stroke-width='5'/>"
         f"<rect x='60' y='-50' width='60' height='60' rx='6' fill='#E0443E' stroke='{INK}' stroke-width='5'/>"
         f"<rect x='74' y='-40' width='34' height='24' fill='#BFE3FF' stroke='{INK}' stroke-width='3'/>"
         f"<rect x='-100' y='-80' width='150' height='12' fill='#C9D2EE' stroke='{INK}' stroke-width='3'/>"
         f"<circle cx='-70' cy='12' r='18' fill='{INK}'/><circle cx='80' cy='12' r='18' fill='{INK}'/>")
SPRAY = "".join(f"<circle cx='{i*26}' cy='{-int(260*(i/10)*(1-i/14))}' r='{9 + i % 3 * 2}' fill='#7FD1FF' opacity='.85'/>" for i in range(1, 14))
ROADCRACK = (f"<path d='M120 830 L170 812 L200 840 L250 818 L300 846 L350 820 L400 838' stroke='{INK}' stroke-width='6' fill='none'/>"
             f"<path d='M200 840 L190 870 M300 846 L318 880 M170 812 L150 790' stroke='{INK}' stroke-width='5' fill='none'/>")
ROAD = "<rect x='0' y='812' width='540' height='80' fill='#3A3550'/><path d='M0 852 L540 852' stroke='#F2C94C' stroke-width='5' stroke-dasharray='34 24'/>"
SAND = "<rect x='0' y='780' width='540' height='180' fill='#E9C98A'/><path d='M0 780 Q140 764 270 780 T540 780' fill='#F2D9A2'/>"
SEA = ("<rect x='0' y='690' width='540' height='270' fill='#2F6FD6'/>"
       "<path d='M0 690 Q35 676 70 690 T140 690 T210 690 T280 690 T350 690 T420 690 T490 690 T560 690' stroke='#DFF8FF' stroke-width='5' fill='none'/>")
SEA_FRONT = "<rect x='0' y='740' width='540' height='220' fill='#2F6FD6' opacity='.92'/><path d='M0 740 Q45 726 90 740 T180 740 T270 740 T360 740 T450 740 T540 740' stroke='#DFF8FF' stroke-width='5' fill='none'/>"
WHALE = (f"<path d='M-200 0 Q-180 -70 -40 -70 Q120 -70 170 -20 L230 -60 L220 0 L240 50 L170 20 Q120 60 -40 56 Q-180 56 -200 0 Z' fill='#4A6FA5' stroke='{INK}' stroke-width='6'/>"
         f"<path d='M-190 16 Q-100 50 60 44' stroke='#C9D2EE' stroke-width='14' fill='none' stroke-linecap='round'/>"
         + "".join(f"<path d='M{-170 + i*24} 22 L{-160 + i*24} 46' stroke='#2B4470' stroke-width='3'/>" for i in range(8))
         + f"<circle cx='-150' cy='-14' r='7' fill='{INK}'/><path d='M-60 30 Q-40 70 -10 52' fill='#4A6FA5' stroke='{INK}' stroke-width='5'/>")
GLOBE = (f"<circle r='170' fill='#2F6FD6' stroke='{INK}' stroke-width='7'/>"
         f"<path d='M-110 -90 q50 -40 90 -10 q20 50 -20 80 q-40 30 -70 -10 z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>"
         f"<path d='M30 20 q60 -20 80 30 q-10 70 -60 90 q-40 -50 -20 -120 z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>")
BIGSHOE = (f"<path d='M-90 0 L-90 -60 Q-30 -70 0 -34 L90 -22 Q106 0 90 0 Z' fill='#E46F8E' stroke='{INK}' stroke-width='6'/>"
           f"<path d='M-60 -50 L-20 -40 M-56 -36 L-14 -28' stroke='#F4F1FF' stroke-width='5'/><rect x='-92' y='-6' width='186' height='10' rx='4' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/>")
EQUATION = (f"<text x='0' y='0' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='54' fill='#F4F1FF'>2x TALL</text>")


def hero(x, y, scale, **kw):
    a = {"id": "hero", "char": "hero", "x": x, "y": y, "scale": scale}
    a.update(kw)
    return a


scenes = [
    # 1. Opening: you shoot up next to a measuring pole in the street.
    {"bg": "city_day", "transition": "none",
     "fx": [{"type": "pulse", "x": 440, "y": 560, "r": 50, "period": 0.8, "color": "#FFD27A"}, "clouds"],
     "cam_start": {"zoom": 1.5, "cx": 270, "cy": 700},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 560, "dur": 3.0, "ease": "out"}],
     "props": RULER,
     "objects": [{"id": "mk1", "x": 440, "y": 640, "svg": MARK, "front": True,
                  "keys": [{"at": 0.2, "y": 470, "dur": 2.6, "ease": "out"}]}],
     "actors": [hero(220, 812, 1.0, pose="cheer", face="shocked",
                     keys=[{"at": 0.2, "scale": 1.75, "dur": 2.6, "ease": "out"},
                           {"at": "every single day", "face": "happy", "pose": "idle", "dur": 0.3}])]},
    # 2. The warning: a bone under a red alarm glow.
    {"start": "It sounds amazing", "bg": "void", "camera": "push", "transition": "zoom",
     "fx": [{"type": "alarm", "period": 1.2}, "dust"],
     "objects": [{"id": "bone2", "x": 270, "y": 600, "rot": -12, "svg": BONE, "anim": {"sway": 4, "period": 0.9}},
                 {"id": "cr2", "x": 270, "y": 600, "scale": 0.0, "svg": CRACK, "front": True,
                  "keys": [{"at": "turns against you", "scale": 2.0, "dur": 0.2, "ease": "back", "sfx": "thud"}]}]},
    # 3. Day one: feet off the bed, mom with a shoebox.
    {"start": "Day one", "bg": "warm_interior", "camera": "pan_right", "transition": "whip", "whip_dir": "right",
     "fx": ["dust"],
     "props": BED,
     "actors": [hero(395, 742, 1.5, pose="idle", face="shocked", rot=-90, **FLOAT),
                {"id": "mom", "char": "mom", "x": 440, "y": 810, "scale": 1.15, "flip": True, "pose": "idle", "face": "neutral",
                 "keys": [{"at": "your mom sighs", "pose": "facepalm", "face": "bored", "dur": 0.3},
                          {"at": "buys you new shoes", "pose": "hold", "face": "neutral", "dur": 0.3}]}],
     "objects": [{"id": "box3", "x": 440, "y": 690, "scale": 0.0, "svg": SHOEBOX, "front": True,
                  "keys": [{"at": "buys you new shoes", "scale": 1.0, "dur": 0.3, "ease": "back", "sfx": "pop"}]}]},
    # 4. Day two: the basketball court, coach crying happy tears.
    {"start": "Day two", "bg": "day_park", "camera": "static", "transition": "cut",
     "fx": ["confetti"],
     "props": HOOP,
     "actors": [hero(250, 815, 1.9, pose="throw", face="happy"),
                {"id": "coach", "char": "extra", "shirt": "#FFB547", "x": 90, "y": 815, "scale": 0.9, "pose": "cheer", "face": "happy",
                 "keys": [{"at": "cries happy tears", "pose": "hug", "face": "sad", "dur": 0.3}]}],
     "objects": [{"id": "ball4", "x": 300, "y": 430, "svg": BALL, "anim": {"spin": 200},
                  "keys": [{"at": "taller than the tallest+0.3", "x": 365, "y": 470, "dur": 0.7, "arc": 60, "ease": "in", "sfx": "swish"}]}]},
    # 5. Day three: crawling into school.
    {"start": "Day three", "bg": "cool_interior", "camera": "push", "transition": "cut",
     "fx": ["dust"],
     "props": DOOR,
     "actors": [hero(150, 812, 1.9, pose="crouch", face="worried", look=0.6,
                     keys=[{"at": "on your knees", "x": 230, "dur": 1.4, "cycle": "walk"}])]},
    # 6. It's math.
    {"start": "But what stops you", "bg": "void", "camera": "zoom_in", "zoom": 1.25, "cx": 270, "cy": 560, "transition": "flash",
     "fx": [{"type": "rays", "x": 270, "y": 560, "spin": 8, "opacity": 0.14, "color": "#C8FF4D"}],
     "objects": [{"id": "rul6", "x": 0, "y": 0, "svg": ruler(270, 380, 760, 38), "anim": {"bob": 6, "period": 1.5}}]},
    # 7. One cube becomes eight.
    {"start": "When you get twice as tall", "bg": "void", "camera": "static", "transition": "cut",
     "fx": ["stars"],
     "objects": [{"id": "c1", "x": 150, "y": 640, "svg": cubes(1, 70), "anim": {"bob": 4, "period": 1.2}},
                 {"id": "c8", "x": 360, "y": 660, "scale": 0.0, "svg": cubes(2, 70), "anim": {"bob": 4, "period": 1.2},
                  "keys": [{"at": "eight times heavier", "scale": 1.0, "dur": 0.4, "ease": "back", "sfx": "thud"}]}]},
    # 8. Bones fall behind (compare card).
    {"start": "But your bones only", "bg": "void", "camera": "drift", "transition": "zoom",
     "fx": [{"type": "pulse", "x": 270, "y": 640, "r": 90, "period": 1.1, "color": "#FF6B6B"}],
     "objects": [{"id": "bone8", "x": 270, "y": 640, "svg": BONE, "anim": {"pulse": 0.05, "period": 0.7}},
                 {"id": "cr8", "x": 250, "y": 640, "scale": 0.0, "svg": CRACK, "front": True,
                  "keys": [{"at": "falls further behind", "scale": 2.4, "dur": 0.25, "ease": "back", "sfx": "thud"}]}]},
    # 9. Day five: taller than a giraffe, next to two cars.
    {"start": "Day five", "bg": "dusk", "camera": "pan_left", "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "dust", "n": 20}],
     "objects": [{"id": "gir", "x": 380, "y": 815, "svg": GIRAFFE, "anim": {"sway": 1.5, "period": 2.2}},
                 {"id": "car9a", "x": 70, "y": 800, "scale": 0.8, "svg": CAR},
                 {"id": "car9b", "x": 160, "y": 800, "scale": 0.8, "svg": CAR}],
     "actors": [hero(250, 818, 1.55, pose="walk_a", face="happy", cycle="walk",
                     keys=[{"at": "your knees ache", "pose": "tired", "face": "worried", "cycle": None, "dur": 0.3}])]},
    # 10. Sleeping in the park under a circus tent.
    {"start": "You sleep in the park", "bg": "night_city", "camera": "push", "transition": "cut",
     "fx": ["stars"],
     "props": TENT,
     "actors": [hero(470, 805, 1.45, pose="idle", face="bored", rot=-90, **FLOAT)]},
    # 11. Day ten: nineteen tonnes, three elephants on the scale.
    {"start": "Day ten", "bg": "city_day", "camera": "reveal", "focus": "hero", "zoom": 2.0, "transition": "zoom",
     "fx": ["clouds"],
     "objects": [{"id": "el1", "x": 330, "y": 815, "scale": 0.8, "svg": ELEPHANT, "anim": {"bob": 2, "period": 1.0}},
                 {"id": "el2", "x": 400, "y": 815, "scale": 0.8, "svg": ELEPHANT, "anim": {"bob": 2, "period": 1.1}},
                 {"id": "el3", "x": 365, "y": 760, "scale": 0.8, "svg": ELEPHANT, "anim": {"bob": 2, "period": 0.9}}],
     "actors": [hero(150, 815, 1.9, pose="idle", face="neutral",
                     keys=[{"at": "about three elephants", "pose": "point", "face": "shocked", "dur": 0.25}])]},
    # 12. The bridge and the warning sign.
    {"start": "You try to cross a bridge", "bg": "dusk", "camera": "pan_right", "transition": "cut",
     "props": RIVER + BRIDGE,
     "fx": [{"type": "pulse", "x": 470, "y": 600, "r": 50, "period": 0.7, "color": "#FF6B6B"}],
     "objects": [{"id": "sign", "x": 470, "y": 630, "svg": SIGN, "front": True, "anim": {"sway": 3, "period": 0.5}}],
     "actors": [hero(60, 700, 1.4, pose="walk_a", face="neutral", cycle="walk",
                     keys=[{"at": "You try to cross", "x": 200, "dur": 2.2},
                           {"at": "the warning signs", "cycle": None, "pose": "shrug", "face": "worried", "dur": 0.25}])]},
    # 13. The heart can't lift blood that high.
    {"start": "Your heart can't push", "bg": "void", "camera": "tilt_up", "from_y": 660, "to_y": 520, "zoom": 1.2, "transition": "zoom",
     "fx": [{"type": "pulse", "x": 270, "y": 690, "r": 80, "period": 0.9, "color": "#FF6B6B"}],
     "props": PIPE,
     "objects": [{"id": "heart", "x": 270, "y": 700, "svg": HEART, "anim": {"pulse": 0.08, "period": 0.45}},
                 {"id": "dr1", "x": 270, "y": 620, "svg": DROP, "keys": [{"at": "Your heart can't push+0.2", "y": 520, "dur": 2.0, "ease": "out"}]},
                 {"id": "dr2", "x": 270, "y": 660, "svg": DROP, "keys": [{"at": "Your heart can't push+0.8", "y": 560, "dur": 2.0, "ease": "out"}]},
                 {"id": "dr3", "x": 270, "y": 680, "svg": DROP, "keys": [{"at": "all the way up", "y": 600, "dur": 2.0, "ease": "out"}]}]},
    # 14. Stand up too fast: blackout.
    {"start": "so if you stand up", "bg": "night_city", "camera": "closeup", "focus": "hero", "zoom": 2.0, "transition": "cut",
     "fx": [{"type": "glitch"}],
     "actors": [hero(250, 810, 1.3, pose="sit", face="neutral",
                     keys=[{"at": "stand up too fast", "pose": "stand", "dur": 0.3},
                           {"at": "everything goes black", "pose": "fall", "face": "shocked", "rot": 12, "dur": 0.4}])]},
    # 15. Cooking: heat trapped inside.
    {"start": "And you're cooking", "bg": "desert", "camera": "push", "transition": "flash",
     "fx": [{"type": "embers", "n": 50, "speed": 1.4, "color": "#FFB547"}],
     "objects": [{"id": "th", "x": 430, "y": 600, "svg": THERMO, "anim": {"bob": 4, "period": 0.6}}],
     "actors": [hero(220, 828, 1.7, pose="tired", face="worried")]},
    # 16. Firefighters spray you.
    {"start": "So firefighters spray", "bg": "city_day", "camera": "pan_left", "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "rain", "n": 40, "speed": 1.0, "color": "#BFE3FF"}],
     "objects": [{"id": "truck", "x": 110, "y": 795, "svg": TRUCK},
                 {"id": "spray", "x": 100, "y": 700, "svg": SPRAY, "front": True, "anim": {"flicker": 0.3, "period": 0.2}}],
     "actors": [hero(380, 815, 1.9, pose="cheer", face="happy", flip=True)]},
    # 17. Day twenty: the road cracks.
    {"start": "Day twenty", "bg": "future_city", "camera": "drift", "transition": "zoom",
     "fx": [{"type": "dust", "n": 40, "speed": 1.4}],
     "props": ROAD,
     "objects": [{"id": "rc", "x": 0, "y": 0, "opacity": 0.0, "svg": ROADCRACK,
                  "keys": [{"at": "the road cracks", "opacity": 1.0, "dur": 0.1}]}],
     "actors": [hero(140, 820, 2.0, pose="walk_a", face="worried", cycle="walk",
                     keys=[{"at": "Day twenty", "x": 260, "dur": 3.0}])]},
    # 18. Lying down squeezes your lungs, like a stranded whale.
    {"start": "Even lying down", "bg": "void", "camera": "pull", "transition": "cut",
     "fx": [{"type": "alarm", "period": 1.6}],
     "props": SAND,
     "objects": [{"id": "wh18", "x": 400, "y": 770, "scale": 0.55, "svg": WHALE, "anim": {"pulse": 0.02, "period": 1.6}}],
     "actors": [hero(240, 790, 0.9, pose="idle", face="sad", rot=-90, **FLOAT)]},
    # 19. The clue: one place on Earth.
    {"start": "And that's the clue", "bg": "space", "camera": "zoom_in", "zoom": 1.3, "cx": 270, "cy": 600, "transition": "flash",
     "fx": ["stars", {"type": "pulse", "x": 270, "y": 600, "r": 120, "period": 1.2, "color": "#5BE7FF"}],
     "objects": [{"id": "g19", "x": 270, "y": 600, "svg": GLOBE, "anim": {"spin": 10}}]},
    # 20. You walk into the sea.
    {"start": "You walk into the sea", "bg": "dusk", "camera": "push", "transition": "cut",
     "props": SEA, "front_props": SEA_FRONT,
     "fx": [{"type": "bubbles", "n": 20, "speed": 0.6, "color": "#DFF8FF"}],
     "actors": [hero(120, 830, 1.9, pose="walk_a", face="tired", cycle="walk",
                     keys=[{"at": "You walk into the sea", "x": 300, "y": 900, "dur": 2.4},
                           {"at": "the pain stops", "cycle": None, "pose": "cheer", "face": "happy", "dur": 0.3}])]},
    # 21. The blue whale, biggest animal ever.
    {"start": "The biggest animal", "bg": "underwater", "camera": "pan_right", "transition": "zoom",
     "fx": ["bubbles", {"type": "rays", "x": 270, "y": 0, "spin": 3, "opacity": 0.1, "color": "#DFF8FF"}],
     "objects": [{"id": "wh21", "x": 120, "y": 600, "svg": WHALE, "anim": {"bob": 8, "period": 2.4},
                  "keys": [{"at": "The biggest animal", "x": 330, "dur": 6.0, "ease": "linear"}]}]},
    # 22. Only water can carry it.
    {"start": "Only water can carry", "bg": "underwater", "camera": "tilt_up", "from_y": 700, "to_y": 450, "zoom": 1.25, "transition": "cut",
     "fx": [{"type": "bubbles", "n": 60, "speed": 1.4}],
     "objects": [{"id": "wh22", "x": 270, "y": 560, "rot": -8, "scale": 1.1, "svg": WHALE, "anim": {"bob": 10, "period": 2.0, "sway": 3}}]},
    # 23. Day thirty: floating next to one.
    {"start": "Day thirty", "bg": "underwater", "camera": "reveal", "focus": "hero", "zoom": 1.9, "transition": "flash",
     "fx": [{"type": "bubbles", "n": 30, "speed": 0.8}],
     "objects": [{"id": "wh23", "x": 330, "y": 470, "scale": 0.9, "svg": WHALE, "anim": {"bob": 8, "period": 2.6}}],
     "actors": [hero(370, 700, 1.3, pose="idle", face="happy", rot=-80, **FLOAT,
                     keys=[{"at": "finally comfortable", "face": "happy", "lift": 10, "dur": 0.6}])]},
    # 24. Loop: back to the street-style pull, mom on the beach with rowboat shoes.
    {"start": "And back on the beach", "bg": "day_park", "transition": "whip", "whip_dir": "right",
     "props": SAND,
     "fx": ["clouds", {"type": "pulse", "x": 300, "y": 760, "r": 70, "period": 0.8, "color": "#FFD27A"}],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 560},
     "cam": [{"at": "your mom is waving", "zoom": 1.5, "cx": 270, "cy": 700, "dur": 4.0, "ease": "inout"}],
     "objects": [{"id": "sh1", "x": 300, "y": 790, "scale": 0.0, "svg": BIGSHOE, "front": True,
                  "keys": [{"at": "two shoes the size", "scale": 1.0, "dur": 0.4, "ease": "back", "sfx": "boing"}]},
                 {"id": "sh2", "x": 330, "y": 740, "scale": 0.0, "svg": BIGSHOE,
                  "keys": [{"at": "two shoes the size+0.2", "scale": 0.9, "dur": 0.4, "ease": "back"}]}],
     "actors": [{"id": "mom", "char": "mom", "x": 140, "y": 812, "scale": 1.2, "pose": "wave", "face": "happy"}]},
]

hud = [
    {"type": "title", "at": 0.05, "until": "It sounds amazing", "small": "WHAT IF YOU GREW", "text": "1 METER A DAY?", "color": "#FFD27A", "size": 54, "top": 150},
    {"type": "marker", "at": "Day one", "until": "Day two", "label": "DAY", "text": "1", "sub": "2.6 METERS TALL"},
    {"type": "marker", "at": "Day two", "until": "Day three", "label": "DAY", "text": "2", "sub": "TALLEST HUMAN EVER"},
    {"type": "title", "at": "it's math", "until": "When you get twice", "text": "IT'S MATH.", "color": "#C8FF4D", "size": 96, "top": 170, "sfx": "thud"},
    {"type": "title", "at": "eight times heavier", "until": "But your bones only", "small": "2x TALLER =", "text": "8x HEAVIER", "color": "#FFD27A", "size": 80, "top": 150, "captions": True},
    {"type": "compare", "at": "But your bones only", "until": "Day five", "label": "WHEN YOU GET 2x TALLER",
     "a": ["Weight", "x8", 1.0], "b": ["Bone strength", "x4", 0.5]},
    {"type": "marker", "at": "Day five", "until": "You sleep in the park", "label": "DAY", "text": "5", "sub": "6.6 METERS · TALLER THAN A GIRAFFE"},
    {"type": "marker", "at": "Day ten", "until": "You try to cross", "label": "DAY", "text": "10", "sub": "11 METERS · 19 TONNES"},
    {"type": "title", "at": "everything goes black", "until": "And you're cooking", "text": "BLACKOUT", "color": "#FF6B6B", "size": 90, "top": 170},
    {"type": "marker", "at": "Day twenty", "until": "Even lying down", "label": "DAY", "text": "20", "sub": "21 METERS · 120 TONNES"},
    {"type": "title", "at": "The biggest animal", "until": "Only water can carry", "small": "BIGGEST ANIMAL EVER", "text": "BLUE WHALE", "color": "#5BE7FF", "size": 78, "top": 150, "captions": True},
    {"type": "marker", "at": "Day thirty", "until": "And back on the beach", "label": "DAY", "text": "30", "sub": "31 METERS · FINALLY FLOATING"},
]

ep.update({
    "ep": 42,
    "voiceover": "voiceover.wav",
    "accent": "#FFD27A",
    "show_ep": False,
    "thumbnail": "Day ten+1.0",
    "highlights": {"one meter taller": "amber", "it's math": "green", "eight times heavier": "amber", "four times stronger": "amber",
                   "Nineteen tonnes": "amber", "blue whale": "green", "Only water": "green", "rowboats": "amber"},
    "music": [{"track": "music/the-forest-awakes.mp3", "at": 0},
              {"track": "music/now-or-never.mp3", "at": "But what stops you"},
              {"track": "music/find-you.mp3", "at": "You walk into the sea"}],
    "music_db_below_voice": 20,
    "hud": hud,
    "shakes": [{"at": "turns against you", "amp": 10, "dur": 0.35, "sfx": ""},
               {"at": "the road cracks", "amp": 16, "dur": 0.5},
               {"at": "everything goes black", "amp": 8, "dur": 0.3, "sfx": ""}],
    "flashes": [{"at": "everything goes black", "dur": 0.35, "color": "#000000"},
                {"at": "the pain stops", "dur": 0.15, "color": "#DFF8FF"}],
    "sfx": [{"name": "riser", "at": "There's only one place", "gain": 0.5}],
    "scenes": scenes,
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
