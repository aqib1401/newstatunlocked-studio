import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"


def earth(r=150):
    return (f"<circle r='{r*1.25}' fill='#7FD1FF' opacity='.12'/>"
            f"<circle r='{r}' fill='#3A7BD5' stroke='{INK}' stroke-width='8'/>"
            f"<path d='M{-r*.6} {-r*.5} q{r*.3} {-r*.25} {r*.6} {-r*.05} q{r*.15} {r*.3} {-r*.1} {r*.45} q{-r*.3} {r*.1} {-r*.45} {-r*.1} z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>"
            f"<path d='M{r*.1} {r*.05} q{r*.35} {-r*.15} {r*.55} {r*.15} q{-r*.05} {r*.4} {-r*.35} {r*.45} q{-r*.25} {-r*.2} {-r*.2} {-r*.6} z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>"
            f"<path d='M{-r*.75} {r*.25} q{r*.2} {-r*.05} {r*.3} {r*.2} q{-r*.1} {r*.2} {-r*.3} {r*.1} z' fill='#6BCB77' stroke='{INK}' stroke-width='5'/>"
            f"<path d='M{-r*.5} {-r*.85} a{r} {r} 0 0 1 {r*1.1} {r*.1}' fill='none' stroke='#F4F1FF' stroke-width='6' opacity='.5' stroke-linecap='round'/>")


def bubble(inner="", w=90, h=64, fill="#F4F1FF"):
    return (f"<ellipse rx='{w/2}' ry='{h/2}' fill='{fill}' stroke='{INK}' stroke-width='5'/>"
            f"<circle cx='{-w*.25}' cy='{h/2+12}' r='8' fill='{fill}' stroke='{INK}' stroke-width='4'/>"
            f"<circle cx='{-w*.35}' cy='{h/2+28}' r='5' fill='{fill}' stroke='{INK}' stroke-width='3'/>"
            f"{inner}")


def txt(t, size=26, color=INK, y=9):
    return f"<text x='0' y='{y}' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='{size}' fill='{color}'>{t}</text>"


OVEN = (f"<rect x='-22' y='-20' width='44' height='38' rx='5' fill='#C9C6D8' stroke='{INK}' stroke-width='4'/>"
        f"<rect x='-15' y='-6' width='30' height='18' rx='3' fill='#FF8A3D' stroke='{INK}' stroke-width='3'/>"
        f"<circle cx='-10' cy='-13' r='3' fill='{INK}'/><circle cx='0' cy='-13' r='3' fill='{INK}'/><circle cx='10' cy='-13' r='3' fill='{INK}'/>")
EYES = (f"<ellipse cx='-14' cy='0' rx='12' ry='9' fill='#fff' stroke='{INK}' stroke-width='4'/><circle cx='-11' cy='0' r='4' fill='{INK}'/>"
        f"<ellipse cx='14' cy='0' rx='12' ry='9' fill='#fff' stroke='{INK}' stroke-width='4'/><circle cx='17' cy='0' r='4' fill='{INK}'/>")
SANDWICH = (f"<path d='M-26 4 L26 4 L0 -22 Z' fill='#F2C46D' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>"
            f"<rect x='-26' y='4' width='52' height='7' fill='#6BCB77' stroke='{INK}' stroke-width='3'/>"
            f"<rect x='-26' y='11' width='52' height='9' rx='3' fill='#F2C46D' stroke='{INK}' stroke-width='4'/>")
BURGER = (f"<path d='M-24 -2 Q0 -30 24 -2 Z' fill='#E0A050' stroke='{INK}' stroke-width='4'/>"
          f"<rect x='-26' y='-2' width='52' height='8' rx='3' fill='#7A4A2E' stroke='{INK}' stroke-width='3'/>"
          f"<rect x='-24' y='7' width='48' height='9' rx='4' fill='#E0A050' stroke='{INK}' stroke-width='4'/>")
HEART = f"<path d='M0 16 C-30 -4 -18 -26 0 -10 C18 -26 30 -4 0 16 Z' fill='#FF6B6B' stroke='{INK}' stroke-width='4'/>"
WAVE = txt("HI?", 30)

BUS = (f"<rect x='-170' y='-70' width='340' height='130' rx='22' fill='#FFC94D' stroke='{INK}' stroke-width='7'/>"
       + "".join(f"<rect x='{x}' y='-52' width='52' height='46' rx='8' fill='#BFE6FF' stroke='{INK}' stroke-width='4'/>"
                 f"<circle cx='{x+26}' cy='-20' r='11' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/>" for x in (-150, -88, -26, 36))
       + f"<rect x='104' y='-52' width='50' height='92' rx='6' fill='#BFE6FF' stroke='{INK}' stroke-width='4'/>"
       f"<rect x='-170' y='14' width='340' height='10' fill='#E08A2E'/>"
       f"<circle cx='-100' cy='62' r='24' fill='#2B2840' stroke='{INK}' stroke-width='6'/><circle cx='-100' cy='62' r='9' fill='#C9C6D8'/>"
       f"<circle cx='100' cy='62' r='24' fill='#2B2840' stroke='{INK}' stroke-width='6'/><circle cx='100' cy='62' r='9' fill='#C9C6D8'/>")

BUS_INSIDE = (f"<rect x='0' y='300' width='540' height='520' fill='#3B3656'/>"
              + "".join(f"<rect x='{x}' y='420' width='120' height='150' rx='14' fill='#BFE6FF' stroke='{INK}' stroke-width='6'/>" for x in (30, 210, 390))
              + f"<rect x='0' y='610' width='540' height='14' fill='#FFC94D' stroke='{INK}' stroke-width='4'/>"
              f"<rect x='0' y='810' width='540' height='150' fill='#2B2840'/>"
              + "".join(f"<rect x='{x}' y='660' width='100' height='120' rx='14' fill='#5A4FA0' stroke='{INK}' stroke-width='5'/>" for x in (40, 220, 400)))

BOARD = (f"<rect x='60' y='430' width='300' height='170' rx='10' fill='#2F5D50' stroke='{INK}' stroke-width='8'/>"
         f"<text x='210' y='500' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='34' fill='#F4F1FF'>TEST</text>"
         f"<text x='210' y='560' text-anchor='middle' font-family='Chakra Petch' font-size='26' fill='#F4F1FF' opacity='.8'>Q1 ___  Q2 ___</text>")
DESK = lambda x: (f"<rect x='{x-60}' y='700' width='120' height='14' rx='5' fill='#8A5A44' stroke='{INK}' stroke-width='4'/>"
                  f"<rect x='{x-50}' y='712' width='10' height='100' fill='#6B4A3A'/><rect x='{x+40}' y='712' width='10' height='100' fill='#6B4A3A'/>")

BRAIN = (f"<path d='M-110 20 C-140 -40 -90 -110 -30 -100 C0 -140 70 -120 85 -80 C140 -70 150 0 110 30 C110 80 40 100 0 80 C-40 105 -110 80 -110 20 Z' fill='#FF9EC4' stroke='{INK}' stroke-width='8'/>"
         f"<path d='M-70 -40 q30 -20 50 10 M10 -70 q25 30 0 55 M50 -20 q40 0 45 40 M-60 30 q30 -10 50 20' fill='none' stroke='#D9608F' stroke-width='7' stroke-linecap='round'/>")
FUNNEL = (f"<path d='M-90 -60 L90 -60 L20 20 L20 70 L-20 70 L-20 20 Z' fill='#7FD1FF' opacity='.85' stroke='{INK}' stroke-width='7' stroke-linejoin='round'/>"
          + "".join(f"<circle cx='{x}' cy='-40' r='5' fill='{INK}' opacity='.6'/>" for x in range(-60, 70, 20)))
CRACKED = (f"<path d='M-90 -60 L-5 -60 L-25 -20 L5 0 L-15 20 L-20 70 L-20 20 Z' fill='#7FD1FF' opacity='.85' stroke='{INK}' stroke-width='7' stroke-linejoin='round'/>"
           f"<path d='M10 -60 L90 -60 L20 20 L20 70 L5 40 L25 10 L0 -15 Z' fill='#7FD1FF' opacity='.85' stroke='{INK}' stroke-width='7' stroke-linejoin='round'/>")
BED = (f"<rect x='80' y='700' width='360' height='60' rx='12' fill='#5A4FA0' stroke='{INK}' stroke-width='6'/>"
       f"<rect x='70' y='640' width='26' height='170' rx='8' fill='#8A5A44' stroke='{INK}' stroke-width='5'/>"
       f"<rect x='100' y='672' width='90' height='36' rx='14' fill='#F4F1FF' stroke='{INK}' stroke-width='5'/>")
BLANKET = f"<rect x='180' y='690' width='260' height='60' rx='14' fill='#7FD1FF' stroke='{INK}' stroke-width='6'/>"
WINDOW = (f"<rect x='300' y='420' width='150' height='170' rx='10' fill='#2B2840' stroke='{INK}' stroke-width='7'/>"
          f"<path d='M375 420 L375 590 M300 505 L450 505' stroke='{INK}' stroke-width='6'/>"
          f"<circle cx='410' cy='460' r='14' fill='#FFE7A0'/>")


def cloud_of_bubbles(prefix, centre=(270, 560), radius=200, n=10, start_at=None, scale=0.55, icons=None):
    import math
    objs = []
    icons = icons or [OVEN, EYES, SANDWICH, BURGER, HEART, txt("?", 34)]
    for i in range(n):
        a = i / n * 2 * math.pi
        x = centre[0] + radius * math.cos(a)
        y = centre[1] + radius * 0.9 * math.sin(a)
        o = {"id": f"{prefix}{i}", "x": round(x), "y": round(y), "scale": scale, "svg": bubble(icons[i % len(icons)]),
             "anim": {"bob": 6, "period": 1.2 + (i % 4) * 0.25, "sway": 4}}
        if start_at:
            o["opacity"] = 0
            at = round(start_at + 0.12 * i, 2) if isinstance(start_at, (int, float)) else f"{start_at}+{0.12*i:.2f}"
            o["keys"] = [{"at": at, "opacity": 1, "dur": 0.15, "ease": "back"}]
        objs.append(o)
    return objs


scenes = [
    # 1. Earth surrounded by popping thought bubbles.
    {"bg": "space", "fx": ["stars", {"type": "pulse", "x": 270, "y": 580, "r": 230, "period": 1.3, "color": "#C8FF4D"}],
     "cam_start": {"zoom": 1.35, "cx": 270, "cy": 580},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 560, "dur": 2.2, "ease": "out"}],
     "objects": [{"id": "earth1", "x": 270, "y": 580, "svg": earth(), "anim": {"spin": 6}}]
     + cloud_of_bubbles("b1_", centre=(270, 580), radius=205, n=10, start_at=0.2)},
    # 2. Eight billion minds, no off switch: you, hands on head.
    {"start": "Eight billion minds", "bg": "void", "camera": "closeup", "focus": "hero", "zoom": 1.9, "transition": "zoom",
     "fx": [{"type": "pulse", "x": 250, "y": 560, "r": 200, "period": 0.7, "color": "#FF6B6B"}, "glitch"],
     "objects": cloud_of_bubbles("b2_", centre=(250, 560), radius=150, n=8, scale=0.45),
     "actors": [{"id": "hero", "char": "hero", "x": 250, "y": 800, "scale": 1.3, "pose": "facepalm", "face": "shocked", "shadow": False,
                 "keys": [{"at": "no off switch", "face": "worried", "dur": 0.2}]}]},
    # 3. Minute one: the bus rolls through the city.
    {"start": "Minute one", "bg": "city_day", "camera": "pan_right", "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "clouds", "speed": 12, "opacity": 0.5, "y0": 90, "h": 240}, {"type": "speedlines", "dir": "left", "n": 10, "speed": 0.8}],
     "objects": [{"id": "bus", "x": 120, "y": 740, "svg": BUS, "anim": {"bob": 3, "period": 0.35},
                  "keys": [{"at": "Minute one", "x": 330, "dur": 4.5, "ease": "linear"}]}]
     + [{"id": f"bb3_{i}", "x": 120 + i * 60 - 110, "y": 600, "scale": 0.45, "opacity": 0, "svg": bubble(ic),
         "anim": {"bob": 5, "period": 1.0 + i * 0.2},
         "keys": [{"at": f"Forty strangers+{0.15*i:.2f}", "opacity": 1, "dur": 0.15, "ease": "back"},
                  {"at": "Minute one", "x": 330 + i * 60 - 110, "dur": 4.5, "ease": "linear"}]}
        for i, ic in enumerate([OVEN, EYES, SANDWICH, txt("?", 34)])]},
    # 4. Inside the bus: three thoughts.
    {"start": "Did I leave", "bg": "void", "camera": "drift", "transition": "cut", "props": BUS_INSIDE,
     "fx": ["dust"],
     "objects": [{"id": "t_oven", "x": 110, "y": 520, "scale": 0.9, "opacity": 0, "svg": bubble(OVEN), "front": True, "anim": {"bob": 5, "period": 1.1},
                  "keys": [{"at": "Did I leave", "opacity": 1, "dur": 0.15, "ease": "back"}]},
                 {"id": "t_eyes", "x": 270, "y": 470, "scale": 0.9, "opacity": 0, "svg": bubble(EYES), "front": True, "anim": {"bob": 5, "period": 1.3},
                  "keys": [{"at": "Is he staring", "opacity": 1, "dur": 0.15, "ease": "back"}]},
                 {"id": "t_sand", "x": 420, "y": 520, "scale": 0.9, "opacity": 0, "svg": bubble(SANDWICH), "front": True, "anim": {"bob": 5, "period": 1.0},
                  "keys": [{"at": "I really need", "opacity": 1, "dur": 0.15, "ease": "back"}]}],
     "actors": [{"id": "p1", "char": "extra", "shirt": "#E46F8E", "x": 90, "y": 800, "scale": 1.0, "pose": "sit", "face": "worried"},
                {"id": "hero", "char": "hero", "x": 270, "y": 800, "scale": 1.05, "pose": "sit", "face": "shocked", "look": -0.5},
                {"id": "p3", "char": "extra", "shirt": "#FFD27A", "x": 440, "y": 800, "scale": 1.0, "pose": "sit", "face": "bored", "flip": True}]},
    # 5. Six thousand... (no) -> Hour one: school. Teacher thinks lunch, smart girl checks answers.
    {"start": "Hour one", "bg": "cool_interior", "camera": "pan_left", "transition": "whip", "whip_dir": "left",
     "props": BOARD + DESK(330) + DESK(130), "fx": ["dust"],
     "objects": [{"id": "t_lunch", "x": 110, "y": 400, "scale": 0.8, "opacity": 0, "svg": bubble(BURGER), "front": True, "anim": {"bob": 5, "period": 1.2},
                  "keys": [{"at": "thinking about lunch", "opacity": 1, "dur": 0.15, "ease": "back"}]},
                 {"id": "t_ans", "x": 400, "y": 520, "scale": 0.8, "opacity": 0, "svg": bubble(txt("A B C", 24), w=110), "front": True, "anim": {"bob": 5, "period": 1.0},
                  "keys": [{"at": "smartest girl", "opacity": 1, "dur": 0.15, "ease": "back"}]}],
     "actors": [{"id": "teach", "char": "drlee", "x": 120, "y": 810, "scale": 1.15, "pose": "point", "face": "neutral", "flip": False},
                {"id": "girl", "char": "extra", "shirt": "#9B7BFF", "x": 380, "y": 810, "scale": 1.0, "pose": "think", "face": "focused", "flip": True},
                {"id": "hero", "char": "hero", "x": 250, "y": 810, "scale": 1.05, "pose": "sit", "face": "neutral",
                 "keys": [{"at": "Free answers", "pose": "cheer", "face": "happy", "dur": 0.15}]}]},
    # 6. Day two: the whole city, bubbles rising off the skyline.
    {"start": "Then the power spreads", "bg": "night_city", "camera": "tilt_up", "from_y": 700, "to_y": 430, "zoom": 1.3, "transition": "zoom",
     "fx": [{"type": "bubbles", "n": 60, "speed": 1.2, "color": "#F4F1FF"}, {"type": "pulse", "x": 270, "y": 700, "r": 260, "period": 0.9, "color": "#FFD27A"}],
     "objects": cloud_of_bubbles("b6_", centre=(270, 640), radius=150, n=8, scale=0.45)},
    # 6a. By lunch the cafeteria sounds like a stadium.
    {"start": "like a stadium", "bg": "stadium", "camera": "zoom_in", "zoom": 1.25, "cx": 270, "cy": 500, "transition": "cut",
     "fx": [{"type": "confetti", "n": 40}, {"type": "pulse", "x": 270, "y": 480, "r": 200, "period": 0.7, "color": "#FF6B6B"}],
     "objects": cloud_of_bubbles("b6s_", centre=(270, 520), radius=180, n=9, scale=0.45)},
    # 7. Normally your brain filters noise: brain + funnel.
    {"start": "Normally, your brain", "bg": "void", "camera": "zoom_in", "zoom": 1.2, "cx": 270, "cy": 560, "transition": "cut",
     "fx": [{"type": "rays", "x": 270, "y": 600, "spin": 8, "opacity": 0.12, "color": "#7FD1FF"}],
     "objects": [{"id": "funnel", "x": 270, "y": 470, "scale": 1.2, "svg": FUNNEL, "anim": {"pulse": 0.03, "period": 1.0}},
                 {"id": "brain7", "x": 270, "y": 680, "scale": 0.9, "svg": BRAIN, "anim": {"pulse": 0.04, "period": 0.9}}]
     + [{"id": f"dot7_{i}", "x": 160 + i * 40, "y": 340, "svg": "<circle r='9' fill='#C8FF4D' stroke='#141218' stroke-width='3'/>",
         "anim": {"drift": [0, 50], "flicker": 0.3}} for i in range(6)]},
    # 8. Loud party: you follow one friend.
    {"start": "It's why you can follow", "bg": "warm_interior", "camera": "closeup", "focus": "hero", "zoom": 1.5, "transition": "cut",
     "fx": ["confetti", {"type": "pulse", "x": 300, "y": 560, "r": 120, "period": 1.0, "color": "#C8FF4D"}],
     "actors": [{"id": "x1", "char": "extra", "shirt": "#5A5670", "x": 70, "y": 810, "scale": 1.0, "pose": "cheer", "face": "happy", "opacity": 0.55},
                {"id": "hero", "char": "hero", "x": 210, "y": 812, "scale": 1.2, "pose": "idle", "face": "happy", "look": 0.5},
                {"id": "fr", "char": "mia", "x": 330, "y": 812, "scale": 1.2, "pose": "wave", "face": "happy", "flip": True},
                {"id": "x2", "char": "extra", "shirt": "#5A5670", "x": 450, "y": 810, "scale": 1.0, "pose": "cheer", "face": "happy", "opacity": 0.55, "flip": True}]},
    # 9. Your power has no filter: the funnel cracks.
    {"start": "Your power has no filter", "bg": "void", "camera": "drift", "transition": "flash",
     "fx": ["glitch", {"type": "alarm", "period": 0.8}],
     "objects": [{"id": "funnel9", "x": 270, "y": 470, "scale": 1.2, "svg": CRACKED, "anim": {"sway": 6, "period": 0.3}},
                 {"id": "brain9", "x": 270, "y": 690, "scale": 0.9, "svg": BRAIN, "anim": {"pulse": 0.08, "period": 0.35}}]
     + cloud_of_bubbles("b9_", centre=(270, 560), radius=210, n=8, scale=0.42)},
    # 10. Day five, the whole planet: Earth buried in thoughts.
    {"start": "Day five", "bg": "earth_orbit", "camera": "pull", "transition": "zoom",
     "fx": ["stars", {"type": "pulse", "x": 270, "y": 560, "r": 260, "period": 0.6, "color": "#FF6B6B"}],
     "objects": [{"id": "earth10", "x": 270, "y": 560, "scale": 0.85, "svg": earth(), "anim": {"spin": 10}}]
     + cloud_of_bubbles("b10a_", centre=(270, 560), radius=175, n=10, scale=0.42)
     + cloud_of_bubbles("b10b_", centre=(270, 560), radius=235, n=12, scale=0.36)},
    # 11. You can't sleep. You can't think.
    {"start": "You can't sleep", "bg": "warm_interior", "camera": "drift", "transition": "cut",
     "props": BED + WINDOW, "front_props": BLANKET, "fx": [{"type": "alarm", "period": 1.0}],
     "objects": cloud_of_bubbles("b11_", centre=(270, 560), radius=170, n=7, scale=0.4),
     "actors": [{"id": "hero", "char": "hero", "x": 230, "y": 700, "scale": 1.0, "pose": "lie", "face": "worried",
                 "keys": [{"at": "You can't think", "face": "shocked", "dur": 0.12}]}]},
    # 12. One voice says your name: everything else fades.
    {"start": "Until one voice", "bg": "void", "camera": "zoom_in", "zoom": 1.3, "cx": 270, "cy": 540, "transition": "flash",
     "fx": [{"type": "rays", "x": 270, "y": 540, "spin": 10, "opacity": 0.16, "color": "#C8FF4D"}, "dust"],
     "objects": [{"id": f"f12_{i}", "x": o["x"], "y": o["y"], "scale": 0.4, "svg": o["svg"], "anim": o["anim"],
                  "keys": [{"at": "the roar drops away", "opacity": 0, "dur": 0.6}]} for i, o in enumerate(cloud_of_bubbles("tmp", centre=(270, 540), radius=200, n=10))]
     + [{"id": "you12", "x": 270, "y": 540, "scale": 0.2, "opacity": 0, "svg": bubble(txt("YOU", 30, "#141218"), w=120, h=80, fill="#C8FF4D"),
         "anim": {"pulse": 0.06, "period": 0.9},
         "keys": [{"at": "says your name", "opacity": 1, "scale": 1.6, "dur": 0.4, "ease": "back", "sfx": "ding"}]}]},
    # 13. Real science: your brain hears your name even asleep.
    {"start": "Because your brain", "bg": "lab", "camera": "push", "transition": "cut",
     "fx": [{"type": "pulse", "x": 270, "y": 560, "r": 200, "period": 1.2, "color": "#7FD1FF"}],
     "objects": [{"id": "brain13", "x": 270, "y": 580, "scale": 1.15, "svg": BRAIN, "anim": {"bob": 6, "period": 2.0}},
                 {"id": "zzz", "x": 400, "y": 420, "opacity": 0, "svg": txt("Z z z", 40, "#7FD1FF"), "anim": {"bob": 8, "period": 1.4},
                  "keys": [{"at": "fast asleep", "opacity": 1, "dur": 0.3}]}]},
    # 14. You follow that voice across the city.
    {"start": "So you follow that voice", "bg": "dusk", "camera": "pan_right", "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "speedlines", "dir": "left", "n": 14, "speed": 1.3}],
     "objects": [{"id": "guide", "x": 300, "y": 540, "scale": 0.7, "svg": bubble(txt("YOU", 30), w=120, h=80, fill="#C8FF4D"),
                  "anim": {"bob": 8, "period": 0.8},
                  "keys": [{"at": "So you follow that voice", "x": 440, "dur": 2.6, "ease": "linear"}]}],
     "actors": [{"id": "hero", "char": "hero", "x": 90, "y": 815, "scale": 1.15, "pose": "run_a", "face": "determined",
                 "keys": [{"at": "So you follow that voice", "x": 330, "dur": 2.6, "cycle": "run", "ease": "linear"}]}]},
    # 15. A quiet kid alone at the back of class.
    {"start": "to a shy kid", "bg": "cool_interior", "camera": "reveal", "focus": "kid", "zoom": 2.2, "transition": "cut",
     "props": DESK(330), "fx": ["dust"],
     "objects": [{"id": "hope", "x": 300, "y": 520, "scale": 0.2, "opacity": 0, "svg": bubble(WAVE, w=100, h=70), "front": True,
                  "anim": {"bob": 5, "period": 1.3},
                  "keys": [{"at": "I hope they", "opacity": 1, "scale": 1.1, "dur": 0.3, "ease": "back"}]}],
     "actors": [{"id": "kid", "char": "leo", "x": 330, "y": 810, "scale": 1.05, "pose": "sit", "face": "sad", "look": -0.3, "flip": True,
                 "keys": [{"at": "I hope they", "face": "neutral", "look": 0.4, "dur": 0.4}]}]},
    # 16. You sit next to him and say hi.
    {"start": "So tomorrow", "bg": "day_park", "camera": "push", "transition": "cut",
     "props": "<rect x='120' y='720' width='300' height='18' rx='6' fill='#8A5A44' stroke='#141218' stroke-width='5'/><rect x='140' y='736' width='14' height='70' fill='#6B4A3A'/><rect x='386' y='736' width='14' height='70' fill='#6B4A3A'/>",
     "fx": [{"type": "clouds", "speed": 8, "opacity": 0.5, "y0": 90, "h": 220}, {"type": "embers", "n": 16, "speed": 0.4, "color": "#FFD27A"}],
     "actors": [{"id": "hero", "char": "hero", "x": 60, "y": 815, "scale": 1.15, "pose": "walk_a", "face": "happy",
                 "keys": [{"at": "So tomorrow", "x": 200, "dur": 1.2, "cycle": "walk"},
                          {"at": "say hi", "cycle": None, "pose": "wave", "dur": 0.15}]},
                {"id": "kid", "char": "leo", "x": 330, "y": 815, "scale": 1.05, "pose": "sit", "face": "neutral", "flip": True,
                 "keys": [{"at": "say hi+0.3", "face": "happy", "pose": "wave", "dur": 0.2}]}]},
    # 17. The planet goes quiet... except one sandwich thought. Loops to the opening Earth.
    {"start": "And for the first time", "bg": "space", "transition": "zoom",
     "fx": ["stars"],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 560},
     "cam": [{"at": "except the guy", "zoom": 1.3, "cx": 300, "cy": 520, "dur": 1.6, "ease": "inout"}],
     "objects": [{"id": "earth17", "x": 270, "y": 580, "svg": earth(), "anim": {"spin": 6}},
                 {"id": "sand17", "x": 370, "y": 410, "scale": 0.2, "opacity": 0, "svg": bubble(SANDWICH), "anim": {"bob": 6, "period": 1.0},
                  "keys": [{"at": "except the guy", "opacity": 1, "scale": 0.95, "dur": 0.35, "ease": "back", "sfx": "pop"}]}]},
]

hud = [
    {"type": "title", "at": 0.05, "until": "Eight billion minds", "small": "WHAT IF YOU COULD", "text": "HEAR EVERY THOUGHT?", "color": "#C8FF4D", "size": 52, "top": 150},
    {"type": "title", "at": "Eight billion minds", "until": "Minute one", "small": "ALL AT ONCE", "text": "8 BILLION MINDS", "color": "#FF6B6B", "size": 58, "top": 150, "captions": True},
    {"type": "marker", "at": "Minute one", "until": "Did I leave", "label": "MINUTE", "text": "1", "sub": "THE BUS: 40 MINDS"},
    {"type": "marker", "at": "Hour one", "until": "Your teacher", "label": "HOUR", "text": "1", "sub": "SCHOOL"},
    {"type": "marker", "at": "Day two", "until": "Normally, your brain", "label": "DAY", "text": "2", "sub": "THE CITY: 3,000,000 MINDS"},
    {"type": "title", "at": "cocktail party effect", "until": "Your power has no filter", "small": "REAL SCIENCE", "text": "COCKTAIL PARTY EFFECT", "color": "#7FD1FF", "size": 46, "top": 150, "captions": True},
    {"type": "marker", "at": "Day five", "until": "You can't sleep", "label": "DAY", "text": "5", "sub": "THE PLANET: 8,000,000,000 MINDS", "color": "#FF6B6B"},
    {"type": "title", "at": "says your name", "until": "Because your brain", "text": "YOUR NAME", "color": "#C8FF4D", "size": 72, "top": 160},
    {"type": "title", "at": "fast asleep", "until": "So you follow that voice", "small": "YOUR BRAIN HEARS YOUR NAME", "text": "EVEN ASLEEP", "color": "#7FD1FF", "size": 62, "top": 150, "captions": True},
    {"type": "title", "at": "the planet goes quiet", "until": "Well", "text": "QUIET.", "color": "#F4F1FF", "size": 96, "top": 170},
]

ep.update({
    "ep": 40,
    "voiceover": "voiceover.wav",
    "accent": "#C8FF4D",
    "show_ep": False,
    "thumbnail": "Day five+0.6",
    "highlights": {"every thought": "green", "eight billion": "amber", "cocktail party effect": "amber", "your name": "green", "sandwich": "amber"},
    "music": [{"track": "music/daybreak.mp3", "at": 0},
              {"track": "music/unknown.mp3", "at": "Then the power spreads"},
              {"track": "music/home.mp3", "at": "So you follow that voice"}],
    "music_db_below_voice": 20,
    "hud": hud,
    "shakes": [{"at": "Your power has no filter", "amp": 12, "dur": 0.45}, {"at": "Day five", "amp": 14, "dur": 0.5}],
    "flashes": [{"at": "says your name", "dur": 0.12, "color": "#fff"}],
    "scenes": scenes,
})
(E / "episode.json").write_text(json.dumps(ep, indent=1, ensure_ascii=False))
print("scenes", len(scenes))
