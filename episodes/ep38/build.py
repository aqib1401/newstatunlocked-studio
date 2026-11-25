import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"
FLOAT = {"shadow": False}


def globe(r=120, top=False):
    """Flat cartoon Earth. top=True: seen from above the North Pole (spins like a merry-go-round)."""
    land = ("<path d='M{a} {b} q30 -40 70 -20 q20 30 -10 60 q-40 20 -60 -40 Z' fill='#5BD27A' stroke='#141218' stroke-width='4'/>"
            "<path d='M{c} {d} q40 -10 50 30 q-20 40 -50 20 q-20 -30 0 -50 Z' fill='#5BD27A' stroke='#141218' stroke-width='4'/>"
            "<path d='M{e} {f} q30 0 40 25 q-30 25 -55 5 Z' fill='#5BD27A' stroke='#141218' stroke-width='4'/>")
    s = r / 120
    land = land.format(a=-80 * s, b=-30 * s, c=20 * s, d=10 * s, e=-30 * s, f=60 * s)
    extra = "<circle r='22' fill='#F4F1FF' stroke='#141218' stroke-width='4'/>" if top else ""
    return (f"<circle r='{r*1.18:.0f}' fill='#5BE7FF' opacity='.12'/>"
            f"<circle r='{r}' fill='#3D7BFF' stroke='{INK}' stroke-width='7'/>{land}{extra}")


def portal(r=90, c1="#B07CFF", c2="#5BE7FF"):
    rings = "".join(f"<circle r='{r*k:.0f}' fill='none' stroke='{c}' stroke-width='{w}' stroke-dasharray='{d}' opacity='.9'/>"
                    for k, c, w, d in [(1.0, c1, 14, "50 22"), (0.8, c2, 10, "34 16"), (0.6, "#F4F1FF", 6, "20 12")])
    return f"<circle r='{r*1.2:.0f}' fill='{c1}' opacity='.15'/>{rings}<circle r='{r*.45:.0f}' fill='#F4F1FF' opacity='.5'/>"


def arrow_h(length=110, col="#FF6B6B", w=12):
    return (f"<path d='M0 0 L{length} 0' stroke='{col}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<path d='M{length-w*1.4} {-w*1.6} L{length+w*1.3} 0 L{length-w*1.4} {w*1.6} Z' fill='{col}' stroke='{INK}' stroke-width='3'/>")


TINY = (f"<circle cx='0' cy='-30' r='9' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/>"
        f"<path d='M0 -21 L0 0 M0 -14 L-10 -24 M0 -14 L10 -4 M0 0 L-7 14 M0 0 L7 14' stroke='#5BA8FF' stroke-width='5' stroke-linecap='round'/>")
BALL = (f"<circle r='26' fill='#F4F1FF' stroke='{INK}' stroke-width='5'/>"
        f"<path d='M0 -10 L10 -3 L6 9 L-6 9 L-10 -3 Z' fill='{INK}'/>"
        f"<path d='M0 -10 L0 -26 M10 -3 L24 -8 M6 9 L14 22 M-6 9 L-14 22 M-10 -3 L-24 -8' stroke='{INK}' stroke-width='3'/>")
FENCE = "".join(f"<rect x='{x}' y='640' width='34' height='170' rx='4' fill='#C98A5A' stroke='{INK}' stroke-width='4'/>" for x in range(0, 540, 44)) + \
    f"<rect x='0' y='680' width='540' height='16' fill='#A86C42' stroke='{INK}' stroke-width='4'/>"
PLANK = f"<rect x='-17' y='-80' width='34' height='160' rx='4' fill='#C98A5A' stroke='{INK}' stroke-width='4'/>"
MGR = (f"<circle r='190' fill='#FFB547' stroke='{INK}' stroke-width='8'/>"
       + "".join(f"<path d='M0 0 L0 -190' stroke='{INK}' stroke-width='6' transform='rotate({a})'/>" for a in range(0, 360, 45))
       + "".join(f"<path d='M0 -190 A190 190 0 0 1 134 -134 L0 0 Z' fill='{c}' transform='rotate({a})' opacity='.9'/>"
                 for a, c in [(0, '#FF6B6B'), (90, '#5BE7FF'), (180, '#C8FF4D'), (270, '#B07CFF')])
       + f"<circle r='36' fill='#F4F1FF' stroke='{INK}' stroke-width='6'/>")
ESCALATOR = (f"<path d='M40 810 L120 810 L380 560 L500 560 L500 600 L400 600 L140 850 L40 850 Z' fill='#8E9AC4' stroke='{INK}' stroke-width='6'/>"
             + "".join(f"<path d='M{150+i*26} {800-i*25} l26 0 l0 -25' stroke='{INK}' stroke-width='4' fill='none'/>" for i in range(9)))
EIFFEL = (f"<g stroke='{INK}' stroke-width='6' fill='none' stroke-linejoin='round'>"
          f"<path d='M180 815 Q240 640 262 330 L278 330 Q300 640 360 815' fill='#8A6A4A' opacity='.9'/>"
          f"<path d='M206 700 L334 700 M228 560 L312 560 M246 440 L294 440'/><path d='M238 815 Q270 740 302 815' fill='#BFE3FF'/>"
          f"<path d='M270 330 L270 280'/></g>")
CROISSANT = (f"<path d='M-50 10 Q-40 -30 0 -32 Q40 -30 50 10 Q30 0 20 -10 Q0 -2 -20 -10 Q-30 0 -50 10 Z' fill='#FFB547' stroke='{INK}' stroke-width='5'/>"
             f"<path d='M-20 -10 L-14 -28 M20 -10 L14 -28' stroke='{INK}' stroke-width='4'/>")
SEA = ("<rect x='0' y='690' width='540' height='60' fill='#3DC8E0' stroke='#141218' stroke-width='4'/>"
       "<rect x='0' y='750' width='540' height='210' fill='#FFE09A' stroke='#141218' stroke-width='4'/>")
PALM = (f"<path d='M430 800 Q420 650 450 560' stroke='#8A5A3A' stroke-width='18' fill='none' stroke-linecap='round'/>"
        f"<g fill='#3DBF6A' stroke='{INK}' stroke-width='4'><path d='M450 560 q-70 -30 -110 20 q60 -10 110 -20 Z'/>"
        f"<path d='M450 560 q60 -40 90 10 q-50 -15 -90 -10 Z'/><path d='M450 560 q-10 -60 -60 -70 q40 30 60 70 Z'/></g>")
PEAK = (f"<path d='M40 1060 L270 760 L500 1160 Z' fill='#E8EEFF' stroke='{INK}' stroke-width='7'/>"
        f"<path d='M270 760 L220 850 L250 840 L270 870 L295 840 L320 850 Z' fill='#FFFFFF' stroke='{INK}' stroke-width='5'/>"
        f"<path d='M270 760 L270 700' stroke='{INK}' stroke-width='5'/><path d='M270 700 L310 712 L270 724 Z' fill='#FF6B6B' stroke='{INK}' stroke-width='3'/>")
MOON = (f"<circle r='200' fill='#C9C6D6' stroke='{INK}' stroke-width='8'/>"
        + "".join(f"<circle cx='{x}' cy='{y}' r='{r}' fill='#A7A3B8' stroke='{INK}' stroke-width='4'/>"
                  for x, y, r in [(-70, -60, 38), (60, 30, 52), (-40, 90, 26), (90, -100, 22), (-120, 30, 18)]))
HELMET = (f"<circle r='120' fill='#BFE3FF' opacity='.45' stroke='{INK}' stroke-width='8'/>"
          f"<path d='M-70 -60 Q-40 -95 10 -100' stroke='#FFFFFF' stroke-width='14' fill='none' stroke-linecap='round' opacity='.8'/>"
          f"<rect x='-110' y='95' width='220' height='40' rx='14' fill='#F4F1FF' stroke='{INK}' stroke-width='7'/>")
MOON_GROUND = (f"<path d='M0 790 Q140 760 280 785 T540 775 L540 960 L0 960 Z' fill='#B9B5C8' stroke='{INK}' stroke-width='6'/>"
               "<ellipse cx='120' cy='850' rx='50' ry='12' fill='#9C98AE'/><ellipse cx='400' cy='880' rx='70' ry='14' fill='#9C98AE'/>")
BEAM = "<rect x='-60' y='-7' width='120' height='14' rx='7' fill='#FFE7A0'/><rect x='-80' y='-16' width='160' height='32' rx='16' fill='#FFD27A' opacity='.25'/>"
SCOPE = (f"<g transform='rotate(-35)'><rect x='-20' y='-24' width='170' height='48' rx='10' fill='#F4F1FF' stroke='{INK}' stroke-width='6'/>"
         f"<rect x='140' y='-32' width='30' height='64' rx='6' fill='#5BA8FF' stroke='{INK}' stroke-width='6'/></g>"
         f"<path d='M10 0 L-30 120 M10 0 L50 120 M10 0 L10 120' stroke='{INK}' stroke-width='6'/>")
LENS_MASK = ("<path d='M0 0 H540 V960 H0 Z M270 330 a230 230 0 1 0 0.1 0 Z' fill='#05040A' fill-rule='evenodd'/>"
             "<circle cx='270' cy='560' r='230' fill='none' stroke='#8E9AC4' stroke-width='22'/>"
             "<circle cx='270' cy='560' r='230' fill='none' stroke='#141218' stroke-width='6'/>"
             "<path d='M270 340 L270 380 M270 740 L270 780 M50 560 L90 560 M450 560 L490 560' stroke='#5BE7FF' stroke-width='4' opacity='.7'/>")
YARD_IN_LENS = ("<rect x='40' y='330' width='460' height='300' fill='#9FE0FF'/><rect x='40' y='630' width='460' height='170' fill='#6BCB5A'/>"
                + "".join(f"<rect x='{x}' y='560' width='26' height='80' rx='3' fill='#C98A5A' stroke='#141218' stroke-width='3'/>" for x in range(60, 500, 36)))
SEPIA = ("<rect x='40' y='330' width='460' height='460' fill='#E8D2A6'/>"
         "<rect x='40' y='680' width='460' height='120' fill='#B89A6A'/>"
         "<rect x='60' y='430' width='120' height='250' fill='#C8AE80' stroke='#5A4630' stroke-width='4'/>"
         "<rect x='360' y='400' width='130' height='280' fill='#C8AE80' stroke='#5A4630' stroke-width='4'/>"
         + "".join(f"<rect x='{x}' y='{y}' width='22' height='30' fill='#5A4630' opacity='.6'/>" for x in (85, 135, 385, 440) for y in (470, 560)))
OLDCAR = ("<rect x='-70' y='-40' width='140' height='40' rx='8' fill='#3A2E22' stroke='#141218' stroke-width='4'/>"
          "<rect x='-40' y='-80' width='80' height='42' rx='6' fill='#3A2E22' stroke='#141218' stroke-width='4'/>"
          "<rect x='-30' y='-72' width='26' height='26' fill='#E8D2A6'/><rect x='6' y='-72' width='26' height='26' fill='#E8D2A6'/>"
          "<circle cx='-42' cy='2' r='20' fill='#141218'/><circle cx='42' cy='2' r='20' fill='#141218'/>"
          "<circle cx='-42' cy='2' r='7' fill='#C8AE80'/><circle cx='42' cy='2' r='7' fill='#C8AE80'/>")
SMOKE = "<circle r='22' fill='#F4F1FF' opacity='.7'/><circle cx='26' cy='-14' r='16' fill='#F4F1FF' opacity='.6'/>"
OLDFOLK = ("<g fill='#5A4630'><circle cx='0' cy='-70' r='12'/><rect x='-12' y='-58' width='24' height='46' rx='8'/>"
           "<rect x='-16' y='-86' width='32' height='8' rx='3'/><rect x='-10' y='-96' width='20' height='12' rx='3'/>"
           "<path d='M-6 -12 L-10 10 M6 -12 L10 10' stroke='#5A4630' stroke-width='6'/></g>")


def star(col="#FFE7A0", r=10):
    return f"<circle r='{r*3}' fill='{col}' opacity='.18'/><path d='M0 {-r*2} L{r*.5} {-r*.5} L{r*2} 0 L{r*.5} {r*.5} L0 {r*2} L{-r*.5} {r*.5} L{-r*2} 0 L{-r*.5} {-r*.5} Z' fill='{col}'/>"


def year_star(year, x, y, col="#FFE7A0"):
    return {"id": f"ys{year}", "x": x, "y": y, "svg": star(col, 8) +
            f"<text y='46' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='26' fill='#F4F1FF' stroke='#141218' stroke-width='2'>{year}</text>",
            "anim": {"pulse": 0.12, "period": 1.3 + (x % 5) * 0.2, "bob": 3}}


OPEN_OBJ = lambda tag: [
    {"id": f"globe{tag}", "x": 270, "y": 600, "svg": globe(150), "anim": {"sway": 4, "period": 3}},
    {"id": f"pA{tag}", "x": 160, "y": 470, "scale": 0.55, "svg": portal(90), "anim": {"spin": 160}},
    {"id": f"pB{tag}", "x": 390, "y": 740, "scale": 0.55, "svg": portal(90, "#5BE7FF", "#C8FF4D"), "anim": {"spin": -160}},
    {"id": f"tiny{tag}", "x": 160, "y": 470, "scale": 1.3, "svg": TINY, "anim": {"bob": 4, "period": 0.9}},
]

scenes = [
    # 1. Earth with two portals, a tiny you blinking from one to the other.
    {"bg": "earth_orbit", "fx": ["stars", {"type": "warp", "x": 270, "y": 600, "n": 50, "speed": 1.2, "color": "#B07CFF"}],
     "cam_start": {"zoom": 1.35, "cx": 270, "cy": 600},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 560, "dur": 2.0, "ease": "out"}],
     "objects": OPEN_OBJ("1")},
    # 2. One blink: you vanish from your backyard.
    {"start": "One blink", "bg": "day_park", "camera": "push", "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "pulse", "x": 230, "y": 660, "r": 120, "period": 0.9, "color": "#B07CFF"}, {"type": "clouds", "speed": 20, "opacity": 0.5}],
     "objects": [{"id": "p2", "x": 230, "y": 680, "scale": 0.0, "svg": portal(110), "anim": {"spin": 200},
                  "keys": [{"at": "One blink", "scale": 1.0, "dur": 0.3, "ease": "back"}]}],
     "actors": [{"id": "hero", "char": "hero", "x": 230, "y": 812, "scale": 1.3, "pose": "wave", "face": "happy",
                 "keys": [{"at": "One blink+0.35", "opacity": 0, "scale": 0.2, "dur": 0.25, "sfx": "swish"},
                          {"at": "exactly where it goes wrong", "opacity": 1, "scale": 1.3, "pose": "shrug", "face": "worried", "dur": 0.3}]}]},
    # 3. The soccer ball test.
    {"start": "You test it", "bg": "dusk", "camera": "zoom_in", "cx": 300, "cy": 700, "zoom": 1.3, "transition": "cut",
     "props": FENCE, "fx": [{"type": "dust", "n": 18, "speed": 0.3, "color": "#FFD27A"}],
     "objects": [{"id": "ball3", "x": 330, "y": 784, "svg": BALL, "anim": {"bob": 3, "period": 0.7},
                  "keys": [{"at": "You send it", "opacity": 0, "scale": 0.2, "dur": 0.25, "sfx": "pop"}]},
                 {"id": "p3", "x": 330, "y": 760, "scale": 0.0, "svg": portal(70), "anim": {"spin": 220},
                  "keys": [{"at": "You send it", "scale": 1.0, "dur": 0.25, "ease": "back"},
                           {"at": "it doesn't just appear", "scale": 0.0, "dur": 0.3}]}],
     "actors": [{"id": "hero", "char": "hero", "x": 160, "y": 812, "scale": 1.3, "pose": "point", "face": "smug",
                 "keys": [{"at": "it doesn't just appear", "face": "shocked", "pose": "idle", "dur": 0.15}]}]},
    # 4. It blasts through a fence on the far side of the planet.
    {"start": "It blasts through", "bg": "city_day", "camera": "static", "transition": "flash",
     "props": FENCE, "fx": [{"type": "speedlines", "dir": "left", "n": 14, "speed": 2.5}],
     "objects": [{"id": "ball4", "x": 620, "y": 720, "scale": 1.2, "svg": BALL, "anim": {"spin": -900},
                  "keys": [{"at": "It blasts through+0.1", "x": -100, "y": 700, "dur": 0.6, "ease": "linear"}]},
                 {"id": "pl1", "x": 280, "y": 725, "svg": PLANK, "front": True,
                  "keys": [{"at": "It blasts through+0.4", "x": 90, "y": 520, "rot": -260, "dur": 0.9, "ease": "out", "arc": 60}]},
                 {"id": "pl2", "x": 324, "y": 725, "svg": PLANK, "front": True,
                  "keys": [{"at": "It blasts through+0.38", "x": 40, "y": 640, "rot": 300, "dur": 0.9, "ease": "out", "arc": 40}]}]},
    # 5. Earth is a giant spinning merry go round.
    {"start": "Because Earth is", "bg": "void", "camera": "pull", "transition": "zoom",
     "fx": [{"type": "rays", "x": 270, "y": 560, "spin": 8, "opacity": 0.12, "color": "#FFB547"}],
     "objects": [{"id": "mgr", "x": 270, "y": 580, "svg": MGR, "anim": {"spin": 90}}]},
    # 6. From above the pole: two sides, opposite arrows.
    {"start": "The ground under you", "bg": "space", "camera": "drift", "transition": "cut",
     "fx": ["stars"],
     "objects": [{"id": "gtop", "x": 270, "y": 560, "svg": globe(150, top=True), "anim": {"spin": 40}},
                 {"id": "arA", "x": 200, "y": 380, "svg": arrow_h(120, "#C8FF4D"), "anim": {"bob": 4, "period": 0.8}},
                 {"id": "arB", "x": 340, "y": 740, "rot": 180, "svg": arrow_h(120, "#FF6B6B"), "opacity": 0, "anim": {"bob": 4, "period": 0.8},
                  "keys": [{"at": "east points the opposite way", "opacity": 1, "dur": 0.3, "sfx": "pop"}]},
                 {"id": "dotA", "x": 270, "y": 410, "svg": TINY, "scale": 1.1},
                 {"id": "dotB", "x": 270, "y": 744, "rot": 180, "svg": TINY, "scale": 1.1, "opacity": 0,
                  "keys": [{"at": "and so is the ground", "opacity": 1, "dur": 0.3}]}]},
    # 7. You arrive moving backwards, twice as fast as a jet.
    {"start": "Jump across", "bg": "sky", "camera": "drift", "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "speedlines", "dir": "right", "n": 16, "speed": 2.4}, {"type": "clouds", "speed": 400, "opacity": 0.6}],
     "objects": [{"id": "jet", "x": 600, "y": 300, "svg": "<path d='M-60 0 L50 -8 L70 0 L50 8 Z M-10 -4 L-30 -40 L0 -4 Z M-10 4 L-30 40 L0 4 Z' fill='#F4F1FF' stroke='#141218' stroke-width='4'/>",
                  "keys": [{"at": "twice as fast", "x": 380, "dur": 1.6, "ease": "out"}]}],
     "actors": [{"id": "hero", "char": "hero", "x": 230, "y": 640, "scale": 1.2, "pose": "fall", "face": "shocked", "rot": -20, **FLOAT,
                 "keys": [{"at": "so you arrive", "x": 160, "rot": 20, "dur": 2.0}]}]},
    # 8. Learn to cheat: stop dead, step off gently like an escalator.
    {"start": "So you learn to cheat", "bg": "cool_interior", "camera": "pan_right", "transition": "cut",
     "props": ESCALATOR, "fx": [{"type": "dust", "n": 14, "speed": 0.3}],
     "actors": [{"id": "hero", "char": "hero", "x": 330, "y": 600, "scale": 1.1, "pose": "idle", "face": "focused", "flip": True,
                 "keys": [{"at": "You stop dead", "pose": "crouch", "dur": 0.15},
                          {"at": "then pop out gently", "x": 140, "y": 812, "pose": "walk_a", "cycle": "walk", "dur": 2.0, "face": "smug"},
                          {"at": "And now nothing", "cycle": None, "pose": "cheer", "face": "happy", "dur": 0.2}]}]},
    # 9. Breakfast in Paris.
    {"start": "Breakfast in Paris", "bg": "city_day", "camera": "tilt_up", "from_y": 640, "to_y": 480, "transition": "whip", "whip_dir": "right",
     "props": EIFFEL, "fx": [{"type": "clouds", "speed": 30, "opacity": 0.5}],
     "objects": [{"id": "cro", "x": 400, "y": 480, "svg": CROISSANT, "anim": {"bob": 10, "sway": 10, "period": 1.4}}]},
    # 10. Lunch on a beach in Brazil.
    {"start": "Lunch on a beach", "bg": "day_park", "camera": "pan_left", "transition": "whip", "whip_dir": "left",
     "props": SEA + PALM, "fx": [{"type": "clouds", "speed": 25, "opacity": 0.6}],
     "actors": [{"id": "hero", "char": "hero", "x": 200, "y": 815, "scale": 1.25, "pose": "sit", "face": "happy"}]},
    # 11. The top of Everest.
    {"start": "A sunset on the top", "bg": "snow", "camera": "drift", "transition": "cut",
     "props": PEAK, "fx": [{"type": "snow", "n": 60, "speed": 2.0}, {"type": "speedlines", "dir": "left", "n": 6, "speed": 1.2}],
     "actors": [{"id": "hero", "char": "hero", "x": 240, "y": 800, "scale": 0.9, "pose": "tired", "face": "worried", "flip": True,
                 "keys": [{"at": "cold enough to freeze", "pose": "hug", "face": "sad", "dur": 0.3}]}]},
    # 12. So you go bigger: the Moon.
    {"start": "So you go bigger", "bg": "void", "camera": "reveal", "cx": 270, "cy": 560, "zoom": 2.2, "transition": "zoom",
     "fx": ["stars", {"type": "dust", "n": 20, "speed": 0.2}],
     "objects": [{"id": "moon", "x": 270, "y": 580, "svg": MOON, "anim": {"spin": 6}}]},
    # 13. Spacesuit first: helmet drops on, alarm edges.
    {"start": "Spacesuit first", "bg": "space", "camera": "push", "transition": "cut",
     "fx": ["stars", {"type": "alarm", "period": 0.9}],
     "objects": [{"id": "helmet", "x": 270, "y": 200, "svg": HELMET, "anim": {"bob": 4, "period": 1.2},
                  "keys": [{"at": "Spacesuit first", "y": 580, "dur": 0.6, "ease": "back", "sfx": "thud"}]}]},
    # 14. Landing in silence, a huge Moon jump, Earth in the sky.
    {"start": "You land in total silence", "bg": "space", "transition": "flash",
     "props": MOON_GROUND, "fx": [{"type": "dust", "n": 10, "speed": 0.15, "color": "#C9C6D6"}],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 600},
     "cam": [{"at": "And Earth hangs", "zoom": 1.6, "cx": 380, "cy": 500, "dur": 1.6, "ease": "inout"}],
     "objects": [{"id": "earth14", "x": 400, "y": 480, "scale": 0.25, "svg": globe(150), "anim": {"sway": 3, "period": 4}}],
     "actors": [{"id": "hero", "char": "hero", "x": 150, "y": 790, "scale": 1.15, "pose": "idle", "face": "happy", **FLOAT,
                 "keys": [{"at": "You jump", "lift": 90, "pose": "jump", "dur": 1.4, "ease": "out"},
                          {"at": "And Earth hangs", "lift": 0, "pose": "point", "face": "shocked", "dur": 1.2, "ease": "inout"}]}]},
    # 15. Light takes time to travel: a beam crawling from Earth.
    {"start": "But this is where", "bg": "void", "camera": "pan_right", "transition": "zoom",
     "fx": ["stars", "glitch"],
     "objects": [{"id": "earth15", "x": 90, "y": 560, "scale": 0.5, "svg": globe(150), "anim": {"sway": 3, "period": 3}},
                 {"id": "beam1", "x": 200, "y": 560, "svg": BEAM, "anim": {"drift": [40, 0]}},
                 {"id": "beam2", "x": 120, "y": 560, "svg": BEAM, "opacity": 0, "anim": {"drift": [40, 0]},
                  "keys": [{"at": "and you don't", "opacity": 1, "dur": 0.2}]},
                 {"id": "tiny15", "x": 200, "y": 560, "svg": TINY, "scale": 1.3, "opacity": 0,
                  "keys": [{"at": "and you don't", "opacity": 1, "x": 470, "dur": 0.15, "sfx": "swish"}]}]},
    # 16. Mars with a telescope.
    {"start": "So you jump to Mars", "bg": "mars", "camera": "push", "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "dust", "n": 30, "speed": 0.6, "color": "#FFB08A"}],
     "objects": [{"id": "scope", "x": 330, "y": 700, "svg": SCOPE},
                 {"id": "earth16", "x": 110, "y": 400, "scale": 0.12, "svg": globe(150), "anim": {"pulse": 0.15, "period": 1.2}}],
     "actors": [{"id": "hero", "char": "hero", "x": 400, "y": 820, "scale": 1.15, "pose": "think", "face": "focused", "flip": True}]},
    # 17. Through the telescope: your backyard, and you, 20 minutes ago.
    {"start": "Point an impossibly", "bg": "void", "camera": "reveal", "cx": 270, "cy": 640, "zoom": 2.0, "transition": "zoom",
     "props": YARD_IN_LENS, "front_props": LENS_MASK, "fx": [{"type": "pulse", "x": 270, "y": 560, "r": 230, "period": 1.6, "color": "#5BE7FF"}],
     "objects": [{"id": "you17", "x": 250, "y": 700, "scale": 2.4, "svg": TINY, "anim": {"bob": 3, "period": 1.2}},
                 {"id": "p17", "x": 250, "y": 660, "scale": 0.0, "svg": portal(40), "anim": {"spin": 200},
                  "keys": [{"at": "about to leave", "scale": 1.0, "dur": 0.4, "ease": "back"}]}]},
    # 18. A star a hundred light years away.
    {"start": "So you keep going", "bg": "space", "camera": "zoom_in", "cx": 300, "cy": 520, "zoom": 1.4, "transition": "flash",
     "fx": [{"type": "warp", "x": 300, "y": 520, "n": 90, "speed": 2.6, "color": "#FFE7A0"}],
     "objects": [{"id": "bigstar", "x": 300, "y": 520, "scale": 0.4, "svg": star("#FFE7A0", 30), "anim": {"spin": 10, "pulse": 0.1, "period": 1.0},
                  "keys": [{"at": "To a star", "scale": 1.6, "dur": 2.5, "ease": "out"}]}]},
    # 19. Through the impossible telescope: a sepia street a century ago.
    {"start": "Through that impossible", "bg": "void", "camera": "static", "transition": "zoom",
     "props": SEPIA, "front_props": LENS_MASK, "fx": [{"type": "dust", "n": 25, "speed": 0.3, "color": "#E8D2A6"}],
     "objects": [{"id": "car", "x": 0, "y": 720, "svg": OLDCAR, "anim": {"bob": 2, "period": 0.3},
                  "keys": [{"at": "old cars", "x": 520, "dur": 6.0, "ease": "linear"}]},
                 {"id": "smoke", "x": 420, "y": 420, "svg": SMOKE, "anim": {"drift": [-14, -30], "pulse": 0.1, "period": 1.0}},
                 {"id": "folk1", "x": 210, "y": 690, "svg": OLDFOLK, "keys": [{"at": "your great great", "x": 300, "dur": 3.0, "ease": "linear"}]},
                 {"id": "folk2", "x": 250, "y": 692, "svg": OLDFOLK, "scale": 0.9, "keys": [{"at": "your great great", "x": 336, "dur": 3.0, "ease": "linear"}]}]},
    # 20. Every star is a window into a different year.
    {"start": "Every star in the sky", "bg": "night_city", "camera": "tilt_up", "from_y": 640, "to_y": 440, "transition": "cut",
     "fx": ["stars"],
     "objects": [year_star(1926, 120, 440), year_star(1969, 300, 420, "#5BE7FF"), year_star(1492, 420, 500, "#FFB547"),
                 year_star(1800, 190, 580, "#C8FF4D"), year_star(2001, 390, 640, "#F4F1FF")]},
    # 21. Loop: back to Earth and the two portals.
    {"start": "So if you could stand", "bg": "earth_orbit", "transition": "zoom",
     "fx": ["stars", {"type": "warp", "x": 270, "y": 600, "n": 50, "speed": 1.2, "color": "#B07CFF"}],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 560},
     "cam": [{"at": "So if you could stand", "zoom": 1.3, "cx": 270, "cy": 600, "dur": 7.0, "ease": "inout"}],
     "objects": OPEN_OBJ("21")},
]

# Tiny "you" blinks from one portal to the other in the opening and in the loop.
scenes[0]["objects"][3]["keys"] = [{"at": 1.4, "opacity": 0, "dur": 0.1}, {"at": 1.55, "x": 390, "y": 740, "dur": 0.05},
                                   {"at": 1.7, "opacity": 1, "dur": 0.1}]
scenes[-1]["objects"][3]["keys"] = [{"at": "which moment", "opacity": 0, "dur": 0.1}, {"at": "which moment+0.15", "x": 390, "y": 740, "dur": 0.05},
                                    {"at": "which moment+0.3", "opacity": 1, "dur": 0.1}]

hud = [
    {"type": "title", "at": 0.05, "until": "One blink", "small": "WHAT IF YOU COULD", "text": "TELEPORT ANYWHERE?", "color": "#C9A8FF", "size": 56, "top": 150},
    {"type": "title", "at": "more than two thousand", "until": "Why?", "small": "ARRIVAL SPEED", "text": "2,000+ KM/H", "color": "#FF6B6B", "size": 74, "top": 150, "captions": True},
    {"type": "note", "at": "The ground under you", "until": "Jump across", "label": "REAL SCIENCE", "text": "Earth's surface spins east at up to 1,670 km/h."},
    {"type": "title", "at": "about a third", "until": "So you go bigger", "small": "TOP OF EVEREST", "text": "1/3 THE OXYGEN", "color": "#5BE7FF", "size": 64, "top": 150, "captions": True},
    {"type": "title", "at": "about fifteen seconds", "until": "You land", "small": "NO SPACESUIT", "text": "15 SECONDS", "color": "#FF6B6B", "size": 84, "top": 150, "captions": True},
    {"type": "title", "at": "up to twenty minutes", "until": "Point an impossibly", "small": "EARTH'S LIGHT TO MARS", "text": "UP TO 20 MIN", "color": "#FFB08A", "size": 70, "top": 150, "captions": True},
    {"type": "title", "at": "You beat your own light", "until": "So you keep going", "text": "YOU BEAT YOUR OWN LIGHT", "color": "#FFE7A0", "size": 44, "top": 160},
    {"type": "title", "at": "a hundred light years", "until": "Through that impossible", "small": "100 LIGHT YEARS AWAY", "text": "EARTH, 1926", "color": "#E8D2A6", "size": 72, "top": 150, "captions": True},
    {"type": "endcard", "at": "which moment would you", "text": "Which moment would you go see?"},
]

ep.update({
    "ep": 38,
    "voiceover": "voiceover.wav",
    "accent": "#C9A8FF",
    "show_ep": False,
    "thumbnail": "It blasts through+0.5",
    "highlights": {"two thousand kilometers": "amber", "merry go round": "green", "about a third": "amber",
                   "fifteen seconds": "amber", "twenty minutes ago": "green", "beat your own light": "green", "a hundred years ago": "amber"},
    "music": [{"track": "music/lost-islands.mp3", "at": 0},
              {"track": "music/now-or-never.mp3", "at": "But this is where"},
              {"track": "music/from-here.mp3", "at": "So you keep going"}],
    "music_db_below_voice": 20,
    "hud": hud,
    "shakes": [{"at": "It blasts through+0.4", "amp": 16, "dur": 0.5}, {"at": "Spacesuit first+0.5", "amp": 8, "dur": 0.3}],
    "flashes": [{"at": "It blasts through+0.4", "dur": 0.12, "color": "#FFFFFF"}, {"at": "You beat your own light", "dur": 0.12, "color": "#FFE7A0"}],
    "sfx": [{"name": "riser", "at": "Point an impossibly", "gain": 0.5}],
    "scenes": scenes,
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
