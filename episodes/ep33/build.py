import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"

def clock(hand_id=False):
    face = (f"<circle r='120' fill='#F4F1FF' stroke='{INK}' stroke-width='8'/>"
            f"<circle r='104' fill='none' stroke='#C9D2EE' stroke-width='3'/>"
            + "".join(f"<rect x='-4' y='-108' width='8' height='{22 if i % 3 == 0 else 12}' fill='{INK}' transform='rotate({i*30})'/>" for i in range(12))
            + f"<rect x='-6' y='-70' width='12' height='70' rx='6' fill='{INK}' transform='rotate(-60)'/>"
            + f"<circle r='10' fill='{INK}'/>")
    return face
HAND = "<rect x='-3' y='-100' width='6' height='112' rx='3' fill='#FF6B6B'/><circle r='7' fill='#FF6B6B'/>"
HOURGLASS = (f"<path d='M-60 -100 L60 -100 L60 -88 Q60 -30 8 0 Q60 30 60 88 L60 100 L-60 100 L-60 88 Q-60 30 -8 0 Q-60 -30 -60 -88 Z' fill='#BFE3FF' fill-opacity='.35' stroke='{INK}' stroke-width='6'/>"
             "<path d='M-44 -78 L44 -78 Q30 -30 0 -4 Q-30 -30 -44 -78 Z' fill='#F2C94C'/>"
             "<path d='M-46 96 L46 96 Q40 60 0 46 Q-40 60 -46 96 Z' fill='#F2C94C'/>"
             f"<rect x='-72' y='-112' width='144' height='16' rx='6' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/>"
             f"<rect x='-72' y='96' width='144' height='16' rx='6' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/>")
SAND = "<rect x='-3' y='-2' width='6' height='48' fill='#F2C94C'/>"
SUN = "<circle r='70' fill='#FFF0C2'/><circle r='120' fill='#FFF0C2' opacity='.22'/><circle r='170' fill='#FFF0C2' opacity='.1'/>"
BEAM = "<path d='M0 -14 L330 -50 L330 50 L0 14 Z' fill='#FFF0C2' opacity='.35'/>"
BLACK = "<rect x='-400' y='-600' width='800' height='1200' fill='#000'/>"
BUBBLE = "<circle r='120' fill='#7FD1FF' fill-opacity='.10' stroke='#7FD1FF' stroke-opacity='.8' stroke-width='4' stroke-dasharray='14 10'/>"
PHONE = f"<rect x='-16' y='-28' width='32' height='56' rx='6' fill='#2B2840' stroke='{INK}' stroke-width='3'/><rect x='-12' y='-22' width='24' height='40' rx='3' fill='#7FD1FF'/>"
BALL = f"<circle r='16' fill='#FF8E3C' stroke='{INK}' stroke-width='3'/><path d='M-16 0 Q0 -8 16 0 M0 -16 Q-8 0 0 16' stroke='{INK}' stroke-width='2' fill='none'/>"
DROP = "<path d='M0 -9 Q6 0 4 5 Q0 9 -4 5 Q-6 0 0 -9 Z' fill='#BFE3FF' stroke='#5BA8E6' stroke-width='1.5'/>"
SPLASH = "<path d='M-8 0 L-3 -6 M8 0 L3 -6 M0 -2 L0 -9' stroke='#BFE3FF' stroke-width='2'/>"
FLOWER = (f"<path d='M0 0 Q-6 120 4 260' stroke='#3FAE6A' stroke-width='8' fill='none'/>"
          + "".join(f"<ellipse cx='0' cy='-34' rx='18' ry='34' fill='#FF7ACF' stroke='{INK}' stroke-width='3' transform='rotate({a})'/>" for a in range(0, 360, 60))
          + f"<circle r='18' fill='#F2C94C' stroke='{INK}' stroke-width='3'/>")
BIRD = (f"<ellipse rx='40' ry='22' fill='#3FAE6A' stroke='{INK}' stroke-width='4'/>"
        f"<circle cx='34' cy='-14' r='17' fill='#3FAE6A' stroke='{INK}' stroke-width='4'/><circle cx='40' cy='-18' r='4' fill='{INK}'/>"
        f"<path d='M50 -14 L110 -6 L50 -8 Z' fill='{INK}'/>"
        f"<path d='M-4 -14 Q-30 -110 -70 -120 Q-40 -60 -20 -16 Z' fill='#9BE7C4' stroke='{INK}' stroke-width='3' opacity='.95'/>"
        f"<path d='M-34 6 L-80 30 L-60 4 Z' fill='#2C8A52' stroke='{INK}' stroke-width='3'/>"
        f"<ellipse cx='10' cy='10' rx='20' ry='10' fill='#E0443E'/>")
BOLT = ("<path d='M60 -300 L-10 -120 L50 -110 L-40 80 L20 85 L-60 300' stroke='#FFFDE8' stroke-width='16' fill='none' stroke-linejoin='round' stroke-linecap='round'/>"
        "<path d='M60 -300 L-10 -120 L50 -110 L-40 80 L20 85 L-60 300' stroke='#B79CFF' stroke-opacity='.5' stroke-width='40' fill='none' stroke-linejoin='round'/>"
        "<path d='M-10 -120 L-90 -40 M-40 80 L-120 140' stroke='#FFFDE8' stroke-width='8' fill='none'/>")
SHELVES = "".join(
    f"<rect x='{x}' y='{y}' width='150' height='12' fill='#6B4A3A' stroke='{INK}' stroke-width='2'/>"
    + "".join(f"<rect x='{x+4+i*18}' y='{y-58+(i%3)*6}' width='15' height='{58-(i%3)*6}' fill='{c}' stroke='{INK}' stroke-width='2'/>" for i, c in enumerate(['#E46F8E','#7FD1FF','#F2C94C','#3FAE6A','#B79CFF','#FF8E3C','#E46F8E','#7FD1FF']))
    for x in (40, 350) for y in (470, 560, 650, 740))
BOOK = f"<rect x='-22' y='-8' width='44' height='16' rx='2' fill='#E46F8E' stroke='{INK}' stroke-width='2'/>"
CAR = f"<rect x='-40' y='-18' width='80' height='26' rx='8' fill='#FF6B6B' stroke='{INK}' stroke-width='3'/><rect x='-22' y='-36' width='44' height='20' rx='6' fill='#FF8E8E' stroke='{INK}' stroke-width='3'/><circle cx='-22' cy='9' r='9' fill='{INK}'/><circle cx='22' cy='9' r='9' fill='{INK}'/>"
PLANE = (f"<path d='M-90 0 Q-90 -14 -70 -14 L80 -14 Q100 -14 106 0 Q100 14 80 14 L-70 14 Q-90 14 -90 0 Z' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/>"
         f"<path d='M-10 0 L-40 50 L-20 50 L30 0 Z' fill='#C9D2EE' stroke='{INK}' stroke-width='3'/><path d='M-80 -10 L-96 -44 L-80 -44 L-60 -12 Z' fill='#C9D2EE' stroke='{INK}' stroke-width='3'/>")
CLOUD = "<g fill='#F4F1FF' opacity='.9'><circle cx='-30' r='26'/><circle cx='0' cy='-12' r='32'/><circle cx='34' r='24'/><rect x='-56' y='0' width='114' height='22' rx='11'/></g>"
ROAD = "<rect x='0' y='800' width='540' height='60' fill='#3A3550'/><path d='M0 830 L540 830' stroke='#F2C94C' stroke-width='4' stroke-dasharray='30 22'/>"
HEART = "<path d='M0 40 C-90 -20 -60 -100 0 -60 C60 -100 90 -20 0 40 Z' fill='#E0443E' stroke='#141218' stroke-width='6'/><path d='M-40 -50 Q-30 -66 -14 -60' stroke='#FF9C9C' stroke-width='8' fill='none' stroke-linecap='round'/>"
ECG = "<path d='M-260 0 L-80 0 L-60 -40 L-40 50 L-20 -90 L0 30 L20 0 L260 0' stroke='#C8FF4D' stroke-width='6' fill='none' stroke-linejoin='round'/>"
SHOE = f"<path d='M-26 0 L-26 -16 Q-10 -18 0 -8 L26 -4 Q30 6 24 8 L-26 8 Z' fill='#E46F8E' stroke='{INK}' stroke-width='3'/>"
ROOF = f"<rect x='0' y='760' width='540' height='200' fill='#2B2840'/><rect x='0' y='752' width='540' height='12' fill='#3A3550' stroke='{INK}' stroke-width='2'/>"
GLOBE = ("<circle r='120' fill='#2F6FD6'/>"
         "<path d='M-70 -62 Q-40 -92 -8 -72 Q10 -42 -20 -22 Q-52 -10 -72 -32 Z' fill='#3FAE6A'/>"
         "<path d='M18 -22 Q60 -42 82 -2 Q72 40 40 52 Q18 32 24 0 Z' fill='#3FAE6A'/>"
         "<path d='M-62 28 Q-32 18 -20 50 Q-30 82 -60 72 Z' fill='#3FAE6A'/>"
         "<circle r='120' fill='none' stroke='#F2C48D' stroke-width='4'/>"
         "<path d='M0 -120 A120 120 0 0 1 0 120 A70 120 0 0 0 0 -120 Z' fill='#05040F' opacity='.28'/>")
DIGI = (f"<rect x='-150' y='-60' width='300' height='120' rx='14' fill='#0B0A14' stroke='#7FD1FF' stroke-width='5'/>"
        "<text x='0' y='26' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='76' fill='#7FD1FF'>07:00</text>")

def hero(x, y, scale=1.3, **kw):
    a = {"id": "hero", "char": "hero", "x": x, "y": y, "scale": scale}
    a.update(kw)
    return a

def extra(i, x, y, pose, shirt, scale=1.15, flip=False):
    return {"id": f"x{i}", "char": "extra", "x": x, "y": y, "scale": scale, "pose": pose, "shirt": shirt, "flip": flip, "face": "neutral"}

def clock_objs(prefix, stop_at=None, restart=False):
    hand = {"id": prefix + "h", "x": 270, "y": 560, "scale": 1.5, "front": True, "svg": HAND, "anim": {"spin": 240}}
    if stop_at:
        hand["keys"] = [{"at": stop_at, "stop_anim": True}]
    return [{"id": prefix + "c", "x": 270, "y": 560, "scale": 1.5, "svg": clock()}, hand]

# rain-tunnel drops: hero walks x 60 -> 470 over 4.0 s from "Each drop you pass"
WALK0, WALKD = 60, 4.0
tunnel_drops = []
for i in range(30):
    x = 40 + (i * 37) % 470
    y = 520 + (i * 61) % 250
    t = max(0.0, (x - WALK0) / (470 - WALK0) * WALKD)
    tunnel_drops.append({"id": f"td{i}", "x": x, "y": y, "svg": DROP, "scale": 1.3, "anim": {"pulse": 0.08, "period": 0.9 + (i % 4) * 0.2},
                         "keys": [{"at": f"Each drop you pass+{t:.2f}", "y": 815, "dur": 0.35, "ease": "in", "opacity": 0.3}]})
frozen_rain = "".join(f"<g transform='translate({20 + (i*53) % 520} {380 + (i*97) % 420}) scale(1.2)'>{DROP}</g>" for i in range(60))

scenes = [
    # 1 cold open: the clock races, then stops dead
    {"bg": "void", "fx": [{"type": "rays", "x": 270, "y": 560, "spin": 10, "opacity": 0.12}],
     "cam_start": {"zoom": 1.3, "cx": 270, "cy": 560},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 540, "dur": 2.2, "ease": "out"}],
     "objects": clock_objs("a", stop_at="stops dead")},
    # 2 the frozen street, you walk through it
    {"start": "except you", "bg": "city_day", "camera": "pan_right", "transition": "flash",
     "actors": [extra(1, 90, 815, "walk_a", "#E46F8E"), extra(2, 380, 815, "run_b", "#F2C94C", flip=True),
                extra(3, 455, 815, "wave", "#7FD1FF", scale=1.05),
                hero(150, 815, face="smug", keys=[{"at": "except you", "x": 300, "dur": 2.4, "cycle": "walk"},
                                                  {"at": "But every", "cycle": None, "pose": "idle"}])]},
    # 3 the bill: an hourglass draining
    {"start": "But every second", "bg": "space", "fx": ["stars"], "camera": "zoom_in", "zoom": 1.2, "cy": 560,
     "objects": [{"id": "hg", "x": 270, "y": 560, "scale": 1.6, "svg": HOURGLASS, "anim": {"sway": 3, "period": 3}},
                 {"id": "sand", "x": 270, "y": 580, "scale": 1.6, "svg": SAND, "anim": {"flicker": 0.4, "period": 0.2}}]},
    # 4 light stops too: pitch black
    {"start": "the catch the movies", "bg": "void", "camera": "drift",
     "objects": [{"id": "sun", "x": 110, "y": 520, "svg": SUN, "anim": {"pulse": 0.04, "period": 1.6}},
                 {"id": "beam", "x": 150, "y": 520, "svg": BEAM, "anim": {"flicker": 0.2, "period": 0.5},
                  "keys": [{"at": "light would stop", "stop_anim": True}]},
                 {"id": "blk", "x": 270, "y": 480, "front": True, "opacity": 0, "svg": BLACK,
                  "keys": [{"at": "pitch black", "opacity": 1, "dur": 0.25}]}]},
    # 5 the cheat: your arm's-length bubble
    {"start": "So your power cheats", "bg": "cool_interior", "camera": "push", "transition": "zoom",
     "fx": [{"type": "pulse", "x": 230, "y": 680, "r": 170, "period": 1.4, "color": "#7FD1FF"}],
     "objects": [{"id": "bub", "x": 230, "y": 680, "scale": 1.4, "front": True, "svg": BUBBLE, "anim": {"spin": 20}}],
     "actors": [hero(230, 810, pose="point", face="happy", keys=[{"at": "arm's length", "pose": "reach_up", "dur": 0.2}])]},
    # 6 statues in the park (no hero)
    {"start": "Everything else turns", "bg": "day_park", "camera": "pan_left",
     "fx": [{"type": "dust", "n": 25, "speed": 0.3}],
     "objects": [{"id": "fris", "x": 270, "y": 560, "svg": "<ellipse rx='26' ry='8' fill='#FF6B6B' stroke='#141218' stroke-width='3'/>"}],
     "actors": [extra(4, 110, 818, "throw", "#3FAE6A"), extra(5, 420, 818, "jump", "#B79CFF", flip=True), extra(6, 300, 818, "run_a", "#F2C94C")]},
    # 7 phone an inch above the floor
    {"start": "Your phone hangs", "bg": "warm_interior", "camera": "closeup", "focus": "hero", "zoom": 1.6, "focus_y": 660,
     "objects": [{"id": "ph", "x": 330, "y": 790, "rot": -30, "svg": PHONE, "anim": {"bob": 2, "period": 1.5},
                  "keys": [{"at": "pluck it", "attach": "hero.hand", "dx": 0, "dy": -10, "rot": 0, "sfx": "swish"}]}],
     "actors": [hero(220, 808, pose="crouch", face="shocked", keys=[{"at": "pluck it", "pose": "hold", "face": "smug", "dur": 0.15}])]},
    # 8 the ball that freezes as it leaves your reach
    {"start": "You throw a ball", "bg": "day_park", "camera": "static", "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "pulse", "x": 150, "y": 640, "r": 120, "period": 1.3, "color": "#7FD1FF"}],
     "objects": [{"id": "ball", "x": 150, "y": 640, "svg": BALL, "anim": {"spin": 360},
                  "keys": [{"at": "You throw a ball+0.3", "x": 290, "y": 560, "dur": 0.4, "ease": "out"},
                           {"at": "it freezes", "stop_anim": True, "sfx": "click"}]}],
     "actors": [hero(140, 818, pose="throw_back", face="determined", keys=[{"at": "You throw a ball+0.25", "pose": "throw", "dur": 0.12},
                                                                       {"at": "it freezes", "face": "shocked", "dur": 0.1}])]},
    # 9 frozen rain over the city (no hero)
    {"start": "Outside", "bg": "city_day", "camera": "tilt_down", "from_y": 420, "to_y": 620, "zoom": 1.3,
     "props": frozen_rain, "fx": [{"type": "dust", "n": 30, "speed": 0.2, "color": "#DFF8FF"}]},
    # 10 your dry tunnel through the rain
    {"start": "Each drop you pass", "bg": "night_city", "camera": "pan_right",
     "objects": tunnel_drops,
     "actors": [hero(WALK0, 812, face="happy", keys=[{"at": "Each drop you pass", "x": 470, "dur": WALKD, "ease": "linear", "cycle": "walk"},
                                                     {"at": "A hummingbird", "cycle": None}])]},
    # 11 hummingbird stuck mid-flap (no hero)
    {"start": "A hummingbird", "bg": "dusk", "camera": "zoom_in", "zoom": 1.25, "cx": 250, "cy": 560, "transition": "zoom",
     "fx": [{"type": "dust", "n": 30, "speed": 0.3, "color": "#FFE7A0"}],
     "objects": [{"id": "fl", "x": 360, "y": 560, "scale": 1.3, "svg": FLOWER, "anim": {"sway": 2, "period": 4}},
                 {"id": "hb", "x": 190, "y": 540, "scale": 1.5, "svg": BIRD}]},
    # 12 frozen lightning (no hero)
    {"start": "Then you find", "bg": "night_city", "camera": "tilt_up", "from_y": 700, "to_y": 460, "zoom": 1.25,
     "fx": [{"type": "stars", "n": 30}],
     "objects": [{"id": "bolt", "x": 300, "y": 520, "svg": BOLT, "anim": {"flicker": 0.25, "period": 0.15}}]},
    # 13 a week in the library
    {"start": "And you get bolder", "bg": "cool_interior", "camera": "drift", "props": SHELVES,
     "objects": [{"id": f"bk{i}", "x": 270, "y": 790 - i * 18, "opacity": 0, "front": True, "svg": BOOK.replace('#E46F8E', c),
                  "keys": [{"at": f"every book+{i*0.35:.2f}", "opacity": 1, "dur": 0.15, "y": 760 - i * 18}]}
                 for i, c in enumerate(['#E46F8E', '#7FD1FF', '#F2C94C', '#3FAE6A', '#B79CFF', '#FF8E3C'])],
     "actors": [hero(170, 808, pose="sit", face="focused", look=0.6)]},
    # 14 a month walking across a country, past frozen cars and planes
    {"start": "You freeze it for a month", "bg": "desert", "camera": "pan_left", "transition": "whip",
     "props": ROAD,
     "objects": [{"id": "car1", "x": 120, "y": 812, "svg": CAR, "scale": 1.2},
                 {"id": "car2", "x": 420, "y": 830, "svg": CAR.replace('#FF6B6B', '#7FD1FF').replace('#FF8E8E', '#BFE3FF'), "scale": 1.2},
                 {"id": "cl", "x": 360, "y": 430, "svg": CLOUD, "scale": 1.4},
                 {"id": "pl", "x": 300, "y": 420, "svg": PLANE, "scale": 1.1}],
     "actors": [hero(470, 800, scale=0.9, flip=True, face="happy",
                     keys=[{"at": "You freeze it for a month", "x": 60, "dur": 5.0, "ease": "linear", "cycle": "walk"}])]},
    # 15 your clock keeps running: heartbeat (no hero)
    {"start": "But your bubble keeps", "bg": "lab", "camera": "closeup", "zoom": 1.4, "cx": 270, "cy": 560, "transition": "flash",
     "fx": [{"type": "pulse", "x": 270, "y": 540, "r": 160, "period": 0.8, "color": "#FF6B6B"}],
     "objects": [{"id": "heart", "x": 270, "y": 560, "scale": 1.6, "svg": HEART, "anim": {"pulse": 0.12, "period": 0.8}},
                 {"id": "ecg", "x": 270, "y": 740, "svg": ECG, "anim": {"drift": [-40, 0]}}]},
    # 16 hair grows, shoes stop fitting
    {"start": "Your hair grows", "bg": "warm_interior", "camera": "push",
     "objects": [{"id": "shoe", "x": 260, "y": 800, "svg": SHOE, "scale": 1.4,
                  "keys": [{"at": "Your shoes", "x": 400, "y": 640, "rot": 300, "arc": 90, "dur": 0.7, "sfx": "boing"}]}],
     "actors": [hero(210, 808, pose="shrug", face="worried",
                     keys=[{"at": "Your hair", "scale": 1.36, "dur": 1.0}, {"at": "Your shoes", "pose": "facepalm", "scale": 1.42, "dur": 0.3}])]},
    # 17 Mia stays eleven, you keep growing
    {"start": "Your best friend Mia", "bg": "day_park", "camera": "static", "transition": "whip",
     "fx": [{"type": "clouds", "speed": 4, "opacity": 0.5}],
     "actors": [{"id": "mia", "char": "mia", "x": 330, "y": 818, "scale": 1.15, "flip": True, "pose": "wave", "face": "happy"},
                hero(170, 818, scale=1.15, face="neutral",
                     keys=[{"at": "you're fifteen", "scale": 1.35, "dur": 0.6, "face": "worried"},
                           {"at": "Then twenty", "scale": 1.55, "dur": 0.6, "face": "sad", "pose": "slump"}])]},
    # 18 alone on a rooftop with your secret years
    {"start": "You've lived whole", "bg": "night_city", "camera": "reveal", "focus": "hero", "zoom": 2.2,
     "props": ROOF, "fx": [{"type": "stars", "n": 60}],
     "actors": [hero(220, 762, pose="sit", face="sad", look=0.5)]},
    # 19 the strangest part: Earth glitches (no hero)
    {"start": "And here's the strangest", "bg": "earth_orbit", "camera": "zoom_in", "zoom": 1.2, "cy": 520,
     "fx": ["stars", "glitch"],
     "objects": [{"id": "g", "x": 270, "y": 540, "scale": 1.4, "svg": GLOBE, "anim": {"spin": 8}}]},
    # 20 everyone frozen, including you; one figure walks
    {"start": "If someone else", "bg": "city_day", "camera": "pull", "transition": "flash",
     "actors": [extra(7, 90, 815, "walk_b", "#E46F8E"),
                {"id": "stranger", "char": "extra", "x": 470, "y": 815, "scale": 1.1, "shirt": "#2B2840", "flip": True, "face": "smug",
                 "keys": [{"at": "If someone else", "x": 300, "dur": 4.0, "ease": "linear", "cycle": "walk"}]},
                hero(190, 815, pose="walk_a", face="happy")]},
    # 21 every clock agrees (no hero)
    {"start": "every clock on Earth", "bg": "future_city", "camera": "drift",
     "fx": [{"type": "pulse", "x": 270, "y": 520, "r": 200, "period": 1.2, "color": "#7FD1FF"}],
     "objects": [{"id": "digi", "x": 270, "y": 520, "scale": 1.2, "svg": DIGI, "anim": {"flicker": 0.15, "period": 1.0}}]},
    # 22 loop: the opening clock, racing, then stopped
    {"start": "So maybe someone", "bg": "void", "fx": [{"type": "rays", "x": 270, "y": 560, "spin": 10, "opacity": 0.12}],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 540},
     "cam": [{"at": "just did", "zoom": 1.3, "cx": 270, "cy": 560, "dur": 1.6}],
     "objects": clock_objs("z", stop_at="end:just did")},
]

hud = [
    {"type": "title", "at": 0.05, "until": "One snap", "small": "WHAT IF YOU COULD", "text": "FREEZE TIME?", "color": "#7FD1FF", "top": 150},
    {"type": "title", "at": "pitch black", "until": "So your power", "text": "PITCH BLACK", "color": "#F4F1FF", "size": 80, "top": 220},
    {"type": "title", "at": "about five times hotter", "until": "And you get bolder", "small": "LIGHTNING", "text": "5x HOTTER THAN THE SUN", "color": "#FFD27A", "size": 34, "top": 160, "captions": True},
    {"type": "marker", "at": "for a whole week", "until": "You freeze it for a month", "label": "FROZEN FOR", "text": "1 WEEK"},
    {"type": "title", "at": "a hundred thousand", "until": "Your hair grows", "small": "YOUR HEART, EVERY DAY", "text": "100,000 BEATS", "color": "#FF6B6B", "size": 64, "top": 170, "captions": True},
    {"type": "title", "at": "Then twenty", "until": "You've lived whole", "small": "MIA: 11", "text": "YOU: 20", "color": "#FFD27A", "size": 72, "top": 170},
    {"type": "title", "at": "end:just did", "text": "SNAP.", "color": "#7FD1FF", "size": 110, "top": 180, "sfx": "thud"},
]

ep.update({
    "scenes": scenes, "hud": hud,
    "shakes": [{"at": "stops dead", "amp": 14, "dur": 0.5}, {"at": "Then you find", "amp": 12, "dur": 0.4}, {"at": "end:just did", "amp": 14, "dur": 0.4}],
    "flashes": [{"at": "stops dead", "dur": 0.15}, {"at": "Then you find", "dur": 0.12, "color": "#E8E0FF"}],
    "music": [{"track": "music/the-forest-awakes.mp3", "at": 0},
              {"track": "music/leaving-millie-live-piano.mp3", "at": "But your bubble keeps"},
              {"track": "music/deeper.mp3", "at": "And here's the strangest"}],
    "highlights": {"pitch black": "amber", "arm's length": "green", "dry tunnel": "green", "five times hotter": "amber",
                   "a hundred thousand": "amber", "secret years": "green", "you'd never know": "amber"},
    "thumbnail": "every raindrop",
    "accent": "#7FD1FF",
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
