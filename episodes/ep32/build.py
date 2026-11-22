import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())

INK = "#141218"; RIM = "#F2C48D"
CONT = ("<path d='M-70 -62 Q-40 -92 -8 -72 Q10 -42 -20 -22 Q-52 -10 -72 -32 Z' fill='#3FAE6A'/>"
        "<path d='M18 -22 Q60 -42 82 -2 Q72 40 40 52 Q18 32 24 0 Z' fill='#3FAE6A'/>"
        "<path d='M-62 28 Q-32 18 -20 50 Q-30 82 -60 72 Z' fill='#3FAE6A'/>"
        "<path d='M38 -94 Q70 -98 86 -72 Q60 -60 44 -70 Z' fill='#3FAE6A'/>")
GLOBE = f"<circle r='120' fill='#2F6FD6'/>{CONT}<circle r='120' fill='none' stroke='{RIM}' stroke-width='4'/>"
SHADE = "<path d='M0 -120 A120 120 0 0 1 0 120 A70 120 0 0 0 0 -120 Z' fill='#05040F' opacity='.28'/><circle r='128' fill='none' stroke='#7FD1FF' stroke-opacity='.35' stroke-width='8'/>"
EQUATOR = "<ellipse rx='122' ry='16' fill='none' stroke='#C8FF4D' stroke-width='4' stroke-dasharray='10 8'/>"
CAR = f"<rect x='-40' y='-18' width='80' height='26' rx='8' fill='#FF6B6B' stroke='{INK}' stroke-width='3'/><rect x='-22' y='-36' width='44' height='20' rx='6' fill='#FF8E8E' stroke='{INK}' stroke-width='3'/><circle cx='-22' cy='9' r='9' fill='{INK}'/><circle cx='22' cy='9' r='9' fill='{INK}'/>"
TREE = f"<rect x='-7' y='-10' width='14' height='62' fill='#6B4A3A' stroke='{INK}' stroke-width='2'/><circle cx='0' cy='-32' r='34' fill='#3FAE6A' stroke='{INK}' stroke-width='3'/>"
HOUSE = f"<rect x='-42' y='-30' width='84' height='62' fill='#F2C94C' stroke='{INK}' stroke-width='3'/><path d='M-52 -30 L0 -72 L52 -30 Z' fill='#C0504D' stroke='{INK}' stroke-width='3'/><rect x='-10' y='2' width='20' height='30' fill='#6B4A3A'/><rect x='-34' y='-16' width='16' height='14' fill='#BFE3FF'/>"
COW = f"<ellipse rx='34' ry='20' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/><circle cx='-10' cy='-4' r='7' fill='{INK}'/><circle cx='14' cy='6' r='6' fill='{INK}'/><circle cx='38' cy='-10' r='13' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/><path d='M-20 18 L-22 34 M20 18 L22 34' stroke='{INK}' stroke-width='5' stroke-linecap='round'/>"
LEAF = "<path d='M0 -8 Q9 0 0 8 Q-9 0 0 -8 Z' fill='#7BC86C'/>"
WAVE = f"<path d='M-320 80 Q-210 -150 -60 -170 Q50 -178 70 -92 Q26 -116 4 -72 Q-16 -14 90 40 L90 260 L-320 260 Z' fill='#3E8FE0' stroke='#DFF8FF' stroke-width='6'/><path d='M-280 120 Q-180 -40 -70 -60' stroke='#DFF8FF' stroke-opacity='.5' stroke-width='5' fill='none'/>"
SEA = f"<rect x='0' y='700' width='540' height='260' fill='#2F6FD6'/><path d='M0 700 L540 700' stroke='#DFF8FF' stroke-opacity='.6' stroke-width='3'/>"
LIGHTHOUSE = f"<path d='M-22 0 L-14 -150 L14 -150 L22 0 Z' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/><rect x='-16' y='-110' width='32' height='18' fill='#FF6B6B'/><rect x='-18' y='-60' width='36' height='18' fill='#FF6B6B'/><rect x='-20' y='-176' width='40' height='26' fill='#FFE7A0' stroke='{INK}' stroke-width='3'/><path d='M-24 -176 L0 -196 L24 -176 Z' fill='{INK}'/>"
POLE = f"<rect x='-9' y='-200' width='18' height='200' fill='#fff' stroke='{INK}' stroke-width='3'/>" + "".join(f"<path d='M-9 {-190+i*36} L9 {-178+i*36} L9 {-166+i*36} L-9 {-178+i*36} Z' fill='#E0443E'/>" for i in range(5)) + f"<circle cx='0' cy='-208' r='14' fill='#F2C94C' stroke='{INK}' stroke-width='3'/><rect x='12' y='-150' width='110' height='34' rx='6' fill='#6B4A3A' stroke='{INK}' stroke-width='3'/><text x='67' y='-127' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='15' fill='#fff'>NORTH POLE</text>"
MUG = f"<path d='M-10 -12 L10 -12 L8 12 L-8 12 Z' fill='#E46F8E' stroke='{INK}' stroke-width='2'/><path d='M-4 -18 Q0 -26 4 -18' stroke='#fff' stroke-opacity='.7' stroke-width='2' fill='none'/>"
SUN = "<circle r='70' fill='#FFF0C2'/><circle r='120' fill='#FFF0C2' opacity='.22'/><circle r='170' fill='#FFF0C2' opacity='.1'/>"
MOON = "<circle r='40' fill='#E8EEFF'/><circle cx='12' cy='-8' r='8' fill='#C9D2EE'/><circle cx='-14' cy='12' r='6' fill='#C9D2EE'/>"
WATER_BLOB = "<ellipse rx='60' ry='22' fill='#7FD1FF' opacity='.9'/>"
NEWMAP = (f"<circle r='120' fill='#C9985A'/>"
          "<path d='M-120 0 A120 120 0 0 1 120 0 L96 -40 Q0 -20 -96 -40 Z' fill='#2F6FD6'/>"
          "<path d='M-116 -30 A120 120 0 0 1 116 -30 Q0 -55 -116 -30 Z' fill='#2F6FD6'/>"
          "<path d='M-118 26 A120 120 0 0 0 118 26 Q0 50 -118 26 Z' fill='#2F6FD6'/>"
          "<path d='M-90 -6 Q-40 -20 0 -8 Q50 4 90 -10' stroke='#3FAE6A' stroke-width='16' fill='none' stroke-linecap='round'/>"
          f"<circle r='120' fill='none' stroke='{RIM}' stroke-width='4'/>")
BULGE = (f"<ellipse rx='136' ry='112' fill='#2F6FD6'/>{CONT}<ellipse rx='136' ry='112' fill='none' stroke='{RIM}' stroke-width='4'/>")
PAPER = f"<rect x='-70' y='-46' width='140' height='92' rx='4' fill='#F3E6C8' stroke='{INK}' stroke-width='3'/><path d='M-60 -30 L60 -30 M-60 30 L60 30' stroke='#2F6FD6' stroke-width='12'/><path d='M-60 0 Q0 -14 60 0' stroke='#C9985A' stroke-width='22' fill='none'/>"
SPINARC = "<path d='M0 -165 A165 165 0 0 1 143 -82' stroke='#C8FF4D' stroke-width='7' fill='none' stroke-linecap='round'/><path d='M128 -100 L146 -78 L120 -70' stroke='#C8FF4D' stroke-width='7' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"
HAT = "<path d='M-30 6 L30 6 L20 -4 L18 -26 L-18 -26 L-20 -4 Z' fill='#3A3550' stroke='#141218' stroke-width='3'/><rect x='-18' y='-10' width='36' height='6' fill='#FF6B6B'/>"
UMB = "<path d='M-50 0 Q0 -60 50 0 Z' fill='#FF7ACF' stroke='#141218' stroke-width='3'/><path d='M0 0 L0 50 Q0 60 -10 58' stroke='#141218' stroke-width='4' fill='none'/>"
ARROW = "<path d='M-40 0 L30 0 M18 -12 L32 0 L18 12' stroke='#C8FF4D' stroke-width='7' fill='none' stroke-linecap='round' stroke-linejoin='round'/>"

def hero(x, y, scale=1.3, **kw):
    a = {"id": "hero", "char": "hero", "x": x, "y": y, "scale": scale}
    a.update(kw)
    return a

scenes = [
    # 1 cold open: spinning planet, title, then it stops dead
    {"bg": "space", "fx": ["stars"], "cam_start": {"zoom": 1.35, "cx": 270, "cy": 560},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 520, "dur": 2.2, "ease": "out"}],
     "objects": [
        {"id": "globe", "x": 270, "y": 600, "scale": 1.25, "svg": GLOBE, "anim": {"spin": 160},
         "keys": [{"at": "All at once", "stop_anim": True}]},
        {"id": "shade", "x": 270, "y": 600, "scale": 1.25, "front": True, "svg": SHADE}]},
    # 2 you, on the couch, moving without knowing it
    {"start": "Right now", "bg": "warm_interior", "camera": "drift", "fx": [{"type": "speedlines", "dir": "left", "speed": 0.7}],
     "props": f"<rect x='90' y='690' width='250' height='70' rx='18' fill='#6B4A7A' stroke='{INK}' stroke-width='3'/><rect x='90' y='650' width='40' height='110' rx='14' fill='#6B4A7A' stroke='{INK}' stroke-width='3'/><rect x='300' y='650' width='40' height='110' rx='14' fill='#6B4A7A' stroke='{INK}' stroke-width='3'/>",
     "actors": [hero(215, 760, pose="sit", face="bored", keys=[{"at": "you're moving", "face": "shocked", "look": -1, "dur": 0.12}])]},
    # 3 the number
    {"start": "At the equator", "bg": "void", "camera": "zoom_in", "zoom": 1.15, "cy": 600,
     "objects": [
        {"id": "g", "x": 270, "y": 610, "scale": 1.35, "svg": GLOBE + EQUATOR},
        {"id": "arc", "x": 270, "y": 610, "scale": 1.35, "front": True, "svg": SPINARC, "anim": {"spin": 140}},
        {"id": "sh", "x": 270, "y": 610, "scale": 1.35, "front": True, "svg": SHADE},
        {"id": "ar", "x": 270, "y": 790, "front": True, "svg": ARROW, "anim": {"bob": 0, "drift": [0, 0]},
         "keys": [{"at": "spins at", "x": 330, "dur": 0.6, "ease": "out"}]}],
     "captions": True},
    # 4 everything moves together
    {"start": "You just can't feel it", "bg": "sky", "camera": "pan_right",
     "fx": [{"type": "clouds", "speed": 6, "opacity": 0.7}],
     "objects": [
        {"id": "bird", "x": 120, "y": 420, "svg": f"<path d='M-20 0 Q-10 -12 0 0 Q10 -12 20 0' stroke='{INK}' stroke-width='5' fill='none' stroke-linecap='round'/>", "anim": {"drift": [60, -6], "bob": 6, "period": 0.5}}],
     "actors": [hero(250, 860, scale=1.5, shadow=False, pose="cheer", face="happy", lift=0,
                     keys=[{"at": "and you", "pose": "point", "face": "smug", "dur": 0.2}])]},
    # 5 brakes
    {"start": "So when the planet", "bg": "space", "fx": ["stars"], "camera": "static",
     "objects": [
        {"id": "g2", "x": 270, "y": 600, "scale": 1.35, "svg": GLOBE, "anim": {"spin": 220},
         "keys": [{"at": "slams on the brakes", "stop_anim": True}]},
        {"id": "sh2", "x": 270, "y": 600, "scale": 1.35, "front": True, "svg": SHADE}]},
    # 6 the air keeps going
    {"start": "nothing else does", "bg": "sky", "transition": "whip", "camera": "drift",
     "fx": [{"type": "clouds", "speed": 30, "opacity": 0.8}, {"type": "speedlines", "dir": "right", "speed": 1.3}],
     "objects": [{"id": "hat", "x": -60, "y": 560, "svg": HAT, "scale": 1.6, "anim": {"drift": [420, -40], "spin": 300}},
                 {"id": "umb", "x": -200, "y": 700, "svg": UMB, "scale": 1.5, "anim": {"drift": [460, -60], "spin": -200}}]},
    # 7 hurricane winds, city
    {"start": "Winds faster", "bg": "city_day", "camera": "drift", "zoom": 1.1,
     "fx": [{"type": "speedlines", "dir": "right", "speed": 1.6, "n": 30}, {"type": "dust", "n": 50}],
     "objects": [{"id": f"leaf{i}", "x": -40 - i * 70, "y": 520 + (i * 53) % 260, "svg": LEAF, "anim": {"drift": [520, -20], "spin": 400}} for i in range(9)],
     "actors": [hero(170, 812, pose="crouch", face="shocked", flip=True,
                     keys=[{"at": "sweep across", "x": 600, "rot": 30, "lift": 60, "pose": "fall", "dur": 1.8, "ease": "in"}])]},
    # 8 cars, trees, houses (no hero)
    {"start": "Cars, trees", "bg": "city_day", "transition": "flash", "camera": "static",
     "fx": [{"type": "speedlines", "dir": "right", "speed": 1.8, "n": 30}],
     "objects": [
        {"id": "car", "x": -80, "y": 760, "svg": CAR, "scale": 1.3, "keys": [{"at": "Cars", "x": 640, "y": 560, "rot": 540, "dur": 1.6, "ease": "in"}]},
        {"id": "tree", "x": -80, "y": 700, "svg": TREE, "scale": 1.2, "keys": [{"at": "trees", "x": 640, "y": 470, "rot": 400, "dur": 1.6, "ease": "in"}]},
        {"id": "cow", "x": -90, "y": 640, "svg": COW, "scale": 1.2, "keys": [{"at": "even whole", "x": 640, "y": 520, "rot": 300, "dur": 1.5, "ease": "in"}]},
        {"id": "house", "x": -120, "y": 700, "svg": HOUSE, "scale": 1.6, "keys": [{"at": "whole houses", "x": 680, "y": 560, "rot": 200, "dur": 1.7, "ease": "in"}]}]},
    # 9 giant wave
    {"start": "The oceans keep going", "bg": "dusk", "camera": "pull", "props": SEA,
     "front_props": "",
     "objects": [
        {"id": "lh", "x": 400, "y": 720, "svg": LIGHTHOUSE, "scale": 1.2},
        {"id": "wave", "x": -260, "y": 700, "svg": WAVE, "front": True, "scale": 1.4,
         "keys": [{"at": "giant waves", "x": 560, "dur": 2.6, "ease": "inout"}]}],
     "fx": [{"type": "rain", "n": 40, "color": "#DFF8FF"}]},
    # 10 north pole calm
    {"start": "But if you happened", "bg": "snow", "camera": "reveal", "focus": "hero", "zoom": 2.2, "fx": ["snow"],
     "objects": [{"id": "pole", "x": 360, "y": 812, "svg": POLE, "scale": 1.1},
                 {"id": "mug", "x": 0, "y": 0, "svg": MUG, "front": True, "keys": [{"at": 0, "attach": "hero.hand", "dx": 4, "dy": -8}]}],
     "actors": [hero(200, 812, pose="hold", face="bored", keys=[{"at": "barely notice", "face": "smug", "dur": 0.2}])]},
    # 11 speed diagram: equator fast, pole zero
    {"start": "Up there", "bg": "void", "camera": "static",
     "objects": [
        {"id": "g3", "x": 270, "y": 620, "scale": 1.5, "svg": GLOBE + EQUATOR},
        {"id": "sh3", "x": 270, "y": 620, "scale": 1.5, "front": True, "svg": SHADE},
        {"id": "dot", "x": 270, "y": 440, "front": True, "svg": "<circle r='10' fill='#C8FF4D'/>", "anim": {"pulse": 0.3, "period": 0.8}}],
     "fx": [{"type": "pulse", "x": 270, "y": 440, "r": 90, "period": 1.0}]},
    # 12 the sun stops
    {"start": "So you'd watch the sky", "bg": "dusk", "camera": "tilt_up", "from_y": 700, "to_y": 420, "zoom": 1.3,
     "objects": [{"id": "sun", "x": 300, "y": 380, "svg": SUN, "anim": {"pulse": 0.03, "period": 2}}],
     "actors": [hero(170, 812, pose="point", face="neutral", look=0.6, keys=[{"at": "sun stops", "face": "shocked", "pose": "reach_up", "dur": 0.15}])]},
    # 13 six months of day
    {"start": "One side of the Earth", "bg": "desert", "camera": "push", "transition": "zoom",
     "fx": [{"type": "rays", "x": 270, "y": 470, "spin": 6, "opacity": 0.14}, {"type": "embers", "n": 18, "color": "#FFF0C2"}],
     "actors": [hero(280, 820, pose="tired", face="worried", keys=[{"at": "six months of daylight", "pose": "slump", "dur": 0.5}])]},
    # 14 six months of night
    {"start": "The other side freezes", "bg": "snow", "transition": "whip", "camera": "drift",
     "fx": [{"type": "stars", "n": 50}, {"type": "snow", "n": 90, "speed": 2.2}],
     "objects": [{"id": "moon", "x": 400, "y": 330, "svg": MOON}],
     "actors": [hero(250, 815, pose="hug", face="worried", keys=[{"at": "freezes", "pose": "crouch", "dur": 0.4}])]},
    # 15 something stranger: the bulge
    {"start": "And slowly", "bg": "space", "fx": ["stars"], "camera": "zoom_in", "zoom": 1.25, "cy": 560,
     "objects": [
        {"id": "b", "x": 270, "y": 600, "scale": 1.3, "svg": GLOBE, "keys": [{"at": "fat around the middle", "opacity": 0, "dur": 0.4}]},
        {"id": "b2", "x": 270, "y": 600, "scale": 1.3, "opacity": 0, "svg": BULGE, "anim": {"pulse": 0.03, "period": 1.2},
         "keys": [{"at": "fat around the middle", "opacity": 1, "dur": 0.4}]},
        {"id": "w1", "x": 120, "y": 600, "opacity": 0, "front": True, "svg": ARROW.replace("#C8FF4D", "#7FD1FF"), "rot": 180,
         "keys": [{"at": "pushes the oceans", "opacity": 1, "x": 80, "dur": 0.5}]},
        {"id": "w2", "x": 420, "y": 600, "opacity": 0, "front": True, "svg": ARROW.replace("#C8FF4D", "#7FD1FF"),
         "keys": [{"at": "pushes the oceans", "opacity": 1, "x": 460, "dur": 0.5}]}]},
    # 16 water drains to poles
    {"start": "Without the spin", "bg": "void", "camera": "static",
     "objects": [
        {"id": "g4", "x": 270, "y": 600, "scale": 1.5, "svg": GLOBE},
        {"id": "wa", "x": 270, "y": 600, "front": True, "scale": 1.3, "svg": WATER_BLOB, "keys": [{"at": "drains toward", "y": 460, "dur": 1.4}]},
        {"id": "wb", "x": 270, "y": 600, "front": True, "scale": 1.3, "svg": WATER_BLOB, "keys": [{"at": "drains toward", "y": 740, "dur": 1.4}]}]},
    # 17 new world map
    {"start": "Two giant oceans", "bg": "earth_orbit", "fx": ["stars"], "camera": "reveal", "zoom": 1.8, "cy": 520,
     "objects": [{"id": "nm", "x": 270, "y": 520, "scale": 1.5, "svg": NEWMAP, "anim": {"spin": 6}},
                 {"id": "nms", "x": 270, "y": 520, "scale": 1.5, "front": True, "svg": SHADE}]},
    # 18 brand new map, hero holds it
    {"start": "A brand new map", "bg": "cool_interior", "camera": "closeup", "focus": "hero", "zoom": 1.7, "focus_y": 560,
     "objects": [{"id": "paper", "x": 0, "y": 0, "front": True, "svg": PAPER, "scale": 0.8, "keys": [{"at": 0, "attach": "hero.hand", "dx": -10, "dy": -30}]}],
     "actors": [hero(200, 812, pose="hold", face="shocked", flip=True)]},
    # 19 loop: back to the planet from scene 1
    {"start": "So when the Earth stops", "bg": "space", "fx": ["stars"], "camera": "static", "cam_start": {"zoom": 1.0, "cx": 270, "cy": 520},
     "cam": [{"at": "where do you want", "zoom": 1.35, "cx": 270, "cy": 560, "dur": 2.0}],
     "objects": [
        {"id": "gl", "x": 270, "y": 600, "scale": 1.25, "svg": GLOBE, "anim": {"spin": 160}},
        {"id": "shl", "x": 270, "y": 600, "scale": 1.25, "front": True, "svg": SHADE}]},
]

hud = [
    {"type": "title", "at": 0.05, "until": "Not slowly", "small": "WHAT IF THE EARTH", "text": "STOPPED SPINNING?", "top": 150},
    {"type": "title", "at": "seventeen hundred", "until": "You just can't", "small": "SPEED AT THE EQUATOR", "text": "1,670 KM/H", "color": "#C8FF4D", "top": 180, "size": 70, "captions": True},
    {"type": "title", "at": "slams on the brakes", "until": "nothing else does", "text": "STOP.", "color": "#FF6B6B", "size": 110, "top": 180, "sfx": "thud"},
    {"type": "title", "at": "Up there", "until": "So you'd watch", "small": "AT THE POLE", "text": "≈ 0 KM/H", "color": "#C8FF4D", "top": 200, "size": 70, "captions": True},
    {"type": "title", "at": "six months of daylight", "until": "The other side", "text": "6 MONTHS OF DAY", "color": "#FFD27A", "size": 52, "top": 200, "captions": True},
    {"type": "title", "at": "six months of night", "until": "And slowly", "text": "6 MONTHS OF NIGHT", "color": "#9FC2FF", "size": 52, "top": 200, "captions": True},
    {"type": "title", "at": "one huge continent", "until": "A brand new map", "small": "THE NEW EARTH", "text": "2 OCEANS. 1 CONTINENT.", "color": "#7FD1FF", "size": 44, "top": 170, "captions": True},
    {"type": "title", "at": "where do you want", "small": "WHERE DO YOU WANT", "text": "TO BE STANDING?", "color": "#FFD27A", "top": 160},
]

ep.update({
    "scenes": scenes, "hud": hud,
    "shakes": [{"at": "All at once", "amp": 14, "dur": 0.5}, {"at": "slams on the brakes", "amp": 18, "dur": 0.6}],
    "flashes": [{"at": "All at once", "dur": 0.15}],
    "music": [{"track": "music/syntheticity.mp3", "at": 0}, {"track": "music/now-or-never.mp3", "at": "So when the planet"},
              {"track": "music/destiny.mp3", "at": "And slowly"}],
    "highlights": {"seventeen hundred": "green", "nothing else does": "amber", "North Pole": "green", "six months": "amber", "new map": "green"},
    "thumbnail": "slams on the brakes",
    "accent": "#C8FF4D",
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
