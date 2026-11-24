import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"


def brain(r=1.0, glow="#C8FF4D"):
    s = lambda v: round(v * r, 1)
    return (f"<circle r='{s(150)}' fill='{glow}' opacity='.10'/><circle r='{s(115)}' fill='{glow}' opacity='.14'/>"
            f"<path d='M{s(-95)} {s(10)} Q{s(-110)} {s(-60)} {s(-55)} {s(-80)} Q{s(-30)} {s(-115)} {s(15)} {s(-95)} "
            f"Q{s(70)} {s(-110)} {s(90)} {s(-55)} Q{s(125)} {s(-10)} {s(90)} {s(35)} Q{s(85)} {s(80)} {s(30)} {s(75)} "
            f"Q{s(0)} {s(100)} {s(-35)} {s(75)} Q{s(-90)} {s(75)} {s(-95)} {s(10)} Z' fill='#F59AC0' stroke='{INK}' stroke-width='6'/>"
            f"<path d='M{s(0)} {s(-95)} Q{s(-10)} {s(-20)} {s(5)} {s(70)}' stroke='{INK}' stroke-width='5' fill='none'/>"
            f"<path d='M{s(-70)} {s(-40)} Q{s(-40)} {s(-30)} {s(-50)} {s(0)} M{s(-60)} {s(40)} Q{s(-30)} {s(30)} {s(-20)} {s(50)} "
            f"M{s(40)} {s(-60)} Q{s(60)} {s(-30)} {s(40)} {s(-10)} M{s(70)} {s(20)} Q{s(40)} {s(30)} {s(50)} {s(55)}' stroke='#C9578A' stroke-width='5' fill='none' stroke-linecap='round'/>"
            f"<path d='M{s(-60)} {s(-60)} L{s(-30)} {s(-20)} L{s(-45)} {s(-15)} L{s(-15)} {s(25)}' stroke='{glow}' stroke-width='5' fill='none' stroke-linecap='round'/>"
            f"<path d='M{s(55)} {s(-70)} L{s(30)} {s(-25)} L{s(50)} {s(-20)} L{s(25)} {s(30)}' stroke='{glow}' stroke-width='5' fill='none' stroke-linecap='round'/>")


def clock(r=110, color="#F4F1FF"):
    ticks = "".join(f"<rect x='-3' y='{-r+10}' width='6' height='{18 if i % 3 == 0 else 10}' fill='{INK}' transform='rotate({i*30})'/>" for i in range(12))
    return (f"<circle r='{r+14}' fill='#FFD27A' opacity='.15'/><circle r='{r}' fill='{color}' stroke='{INK}' stroke-width='8'/>{ticks}"
            f"<rect x='-5' y='{-r*.5}' width='10' height='{r*.55}' rx='5' fill='{INK}' transform='rotate(-60)'/>"
            f"<rect x='-4' y='{-r*.72}' width='8' height='{r*.77}' rx='4' fill='{INK}' transform='rotate(40)'/><circle r='10' fill='{INK}'/>")


HAND = lambda r=110: f"<rect x='-2.5' y='{-r*.85}' width='5' height='{r*.95}' rx='2' fill='#FF6B6B'/><circle r='6' fill='#FF6B6B'/>"
BALL = (f"<circle r='26' fill='#F4F1FF' stroke='{INK}' stroke-width='5'/><path d='M0 -10 L10 -3 L6 9 L-6 9 L-10 -3 Z' fill='{INK}'/>"
        f"<path d='M0 -10 L0 -25 M10 -3 L24 -8 M6 9 L14 21 M-6 9 L-14 21 M-10 -3 L-24 -8' stroke='{INK}' stroke-width='3'/>")
BULLET = (f"<path d='M-30 -9 L14 -9 Q34 -9 40 0 Q34 9 14 9 L-30 9 Z' fill='#E0B14A' stroke='{INK}' stroke-width='4'/>"
          f"<rect x='-30' y='-9' width='14' height='18' fill='#B8863A' stroke='{INK}' stroke-width='4'/>"
          "<path d='M-40 -4 L-70 -4 M-40 4 L-62 4' stroke='#F4F1FF' stroke-width='3' opacity='.6'/>")
BOARD = (f"<rect x='60' y='450' width='300' height='170' rx='8' fill='#24493A' stroke='{INK}' stroke-width='6'/>"
         "<path d='M90 500 L200 500 M90 540 L250 540 M90 580 L170 580' stroke='#E8F3EC' stroke-width='5' opacity='.7' stroke-linecap='round'/>"
         f"<rect x='40' y='720' width='190' height='14' rx='5' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/>")
DESK = f"<rect x='300' y='735' width='200' height='14' rx='5' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/><rect x='310' y='749' width='10' height='60' fill='#4A3328'/><rect x='480' y='749' width='10' height='60' fill='#4A3328'/>"
PLAN = ("<rect x='-95' y='-70' width='190' height='140' rx='22' fill='#F4F1FF' stroke='#141218' stroke-width='5'/>"
        "<path d='M-20 70 L-35 95 L5 70 Z' fill='#F4F1FF' stroke='#141218' stroke-width='5'/>"
        + "".join(f"<rect x='-75' y='{-52+i*24}' width='18' height='16' rx='3' fill='{c}'/><rect x='-50' y='{-48+i*24}' width='{w}' height='8' rx='4' fill='#9A94B8'/>"
                  for i, (c, w) in enumerate([('#C8FF4D', 110), ('#7FD1FF', 90), ('#FFD27A', 120), ('#FF6B6B', 70), ('#C8FF4D', 100)])))
WORD_HE = "<text x='0' y='0' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='54' fill='#FFD27A' stroke='#141218' stroke-width='3'>HEL…</text>"
LID = lambda top: (f"<rect x='-400' y='{-560 if top else 0}' width='800' height='560' fill='#07060D'/>"
                   f"<path d='M-400 {0 if top else 0} Q0 {50 if top else -50} 400 0' fill='#07060D' stroke='#2A2640' stroke-width='6'/>")
BUS = (f"<rect x='-120' y='-60' width='240' height='100' rx='16' fill='#FFC23D' stroke='{INK}' stroke-width='6'/>"
       + "".join(f"<rect x='{-104+i*52}' y='-46' width='40' height='34' rx='5' fill='#BFE3FF' stroke='{INK}' stroke-width='4'/>" for i in range(4))
       + f"<rect x='-120' y='5' width='240' height='10' fill='#E39A1E'/><circle cx='-70' cy='42' r='20' fill='#3A3448' stroke='{INK}' stroke-width='5'/><circle cx='70' cy='42' r='20' fill='#3A3448' stroke='{INK}' stroke-width='5'/>")
SNAIL = (f"<path d='M-40 10 Q-40 -4 -20 -4 L30 -4 Q44 -4 46 10 Z' fill='#C9D2EE' stroke='{INK}' stroke-width='4'/>"
         f"<circle cx='0' cy='-22' r='24' fill='#C98B5A' stroke='{INK}' stroke-width='4'/><path d='M0 -22 m-12 0 a12 12 0 1 0 12 -12' stroke='{INK}' stroke-width='3' fill='none'/>")
BLUEPRINT = ("<g stroke='#5BE7FF' stroke-width='3' fill='none' opacity='.9'>"
             + "".join(f"<rect x='{x}' y='{y}' width='{w}' height='{h}'/>" for x, y, w, h in
                       [(-200, -60, 60, 160), (-130, -140, 70, 240), (-50, -200, 60, 300), (20, -110, 80, 210), (110, -170, 60, 270), (180, -40, 40, 140)])
             + "".join(f"<path d='M{x} {y} h{w}'/>" for x, y, w in [(-130, -100, 70), (-130, -60, 70), (-50, -150, 60), (-50, -90, 60), (20, -60, 80), (110, -120, 60), (110, -60, 60)])
             + "<path d='M-240 100 L240 100'/></g>")
SUN = (f"<circle r='70' fill='#FFB547' opacity='.18'/><circle r='44' fill='#FFC23D' stroke='{INK}' stroke-width='5'/>")
STREAK = "<path d='M-500 0 Q0 -260 500 0' stroke='#FFE7A0' stroke-width='16' fill='none' opacity='.55' stroke-linecap='round'/>"
SWITCH = (f"<rect x='-80' y='-130' width='160' height='260' rx='26' fill='#E9E4F5' stroke='{INK}' stroke-width='7'/>"
          f"<rect x='-38' y='-90' width='76' height='180' rx='38' fill='#2B2840' stroke='{INK}' stroke-width='5'/>"
          "<text x='0' y='-102' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='22' fill='#141218'>×1000</text>"
          "<text x='0' y='122' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='22' fill='#141218'>×1</text>")
KNOB = f"<circle r='32' fill='#C8FF4D' stroke='{INK}' stroke-width='6'/>"
BED = (f"<rect x='250' y='690' width='260' height='70' rx='12' fill='#7FA3E8' stroke='{INK}' stroke-width='5'/>"
       f"<rect x='250' y='640' width='26' height='130' rx='6' fill='#6B4A3A' stroke='{INK}' stroke-width='4'/>"
       f"<rect x='280' y='672' width='70' height='26' rx='10' fill='#F4F1FF' stroke='{INK}' stroke-width='4'/>"
       "<circle cx='110' cy='520' r='60' fill='#FFD27A' opacity='.18'/>"
       f"<rect x='100' y='560' width='20' height='200' fill='#4A3A4E'/><path d='M80 520 L140 520 L125 470 L95 470 Z' fill='#FFD27A' stroke='{INK}' stroke-width='4'/>")
EARTHSPAN = "<circle cx='270' cy='1700' r='1100' fill='#2F6FD6' stroke='#141218' stroke-width='6'/>"
BAR = lambda w, c: f"<rect x='0' y='-14' width='{w}' height='28' rx='14' fill='{c}' stroke='{INK}' stroke-width='4'/>"

BRAIN_OBJ = lambda i: {"id": i, "x": 270, "y": 540, "scale": 1.15, "svg": brain(), "anim": {"pulse": 0.05, "period": 0.5, "bob": 6}}

scenes = [
    # 1. The brain, racing.
    {"bg": "void", "fx": [{"type": "warp", "x": 270, "y": 540, "n": 80, "speed": 2.2, "color": "#C8FF4D"}, {"type": "pulse", "x": 270, "y": 540, "r": 260, "period": 0.6, "color": "#C8FF4D"}],
     "cam_start": {"zoom": 1.3, "cx": 270, "cy": 540},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 540, "dur": 1.8, "ease": "out"}],
     "objects": [BRAIN_OBJ("brain1")]},
    # 2. One second = seventeen minutes: a clock whose second hand barely crawls.
    {"start": "Every second of your life", "bg": "future_city", "camera": "zoom_in", "zoom": 1.2, "cx": 270, "cy": 560, "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "rays", "x": 270, "y": 560, "spin": 4, "opacity": 0.12, "color": "#FFD27A"}, "dust"],
     "objects": [{"id": "clk", "x": 270, "y": 560, "scale": 1.3, "svg": clock()},
                 {"id": "hand", "x": 270, "y": 560, "scale": 1.3, "svg": HAND(), "anim": {"spin": 1.2}}]},
    # 3. Teacher opens her mouth; you plan the whole weekend.
    {"start": "Your teacher opens her mouth", "bg": "cool_interior", "camera": "push", "props": BOARD + DESK,
     "objects": [{"id": "plan", "x": 380, "y": 520, "scale": 0.0, "svg": PLAN, "anim": {"bob": 5, "period": 1.4},
                  "keys": [{"at": "in that gap", "scale": 0.9, "dur": 0.4, "ease": "back", "sfx": "pop"}]}],
     "actors": [{"id": "teach", "char": "extra", "shirt": "#E46F8E", "x": 140, "y": 808, "scale": 1.2, "pose": "point", "face": "neutral"},
                {"id": "hero", "char": "hero", "x": 400, "y": 808, "scale": 1.15, "pose": "sit", "face": "focused", "flip": True,
                 "keys": [{"at": "minute by minute", "face": "smug", "dur": 0.2}]}]},
    # 4. A football drifts in like a soap bubble.
    {"start": "A football flies", "bg": "day_park", "camera": "pan_left", "transition": "cut",
     "fx": [{"type": "bubbles", "n": 14, "speed": 0.3}],
     "objects": [{"id": "ball", "x": 520, "y": 560, "svg": BALL, "anim": {"spin": 8, "bob": 6, "period": 2.2},
                  "keys": [{"at": "A football flies", "x": 440, "dur": 0.4}, {"at": "drifts in", "x": 330, "y": 600, "dur": 3.2, "ease": "linear"}]}],
     "actors": [{"id": "hero", "char": "hero", "x": 260, "y": 812, "scale": 1.3, "pose": "idle", "face": "bored",
                 "keys": [{"at": "like a soap bubble", "x": 170, "pose": "shrug", "face": "smug", "dur": 0.5}]}]},
    # 5. A bullet, overtaken by a walker.
    {"start": "Even a bullet", "bg": "city_day", "camera": "static", "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "speedlines", "dir": "right", "n": 6, "speed": 0.3}],
     "objects": [{"id": "bul", "x": 150, "y": 560, "scale": 1.9, "svg": BULLET, "anim": {"bob": 2, "period": 1.2},
                  "keys": [{"at": "Even a bullet", "x": 240, "dur": 4.0, "ease": "linear"}]}],
     "actors": [{"id": "walker", "char": "extra", "shirt": "#7FD1FF", "x": 60, "y": 815, "scale": 1.0, "pose": "walk_a",
                 "keys": [{"at": "Even a bullet", "x": 430, "dur": 4.0, "cycle": "walk", "ease": "linear"}]}]},
    # 6. The catch: reveal the hero in the lab.
    {"start": "But there's a catch", "bg": "lab", "camera": "reveal", "focus": "hero", "zoom": 2.3, "transition": "flash",
     "fx": ["glitch", {"type": "pulse", "x": 270, "y": 600, "r": 200, "period": 1.4, "color": "#FF6B6B"}],
     "actors": [{"id": "hero", "char": "hero", "x": 270, "y": 830, "scale": 1.35, "pose": "idle", "face": "worried",
                 "keys": [{"at": "your own body", "pose": "think", "face": "shocked", "dur": 0.15}]}]},
    # 7. Brain fast, body slow: brain racing, snail crawling.
    {"start": "Your brain is fast", "bg": "void", "camera": "pan_right", "transition": "cut",
     "fx": [{"type": "speedlines", "dir": "left", "speed": 2.0}],
     "objects": [{"id": "brain7", "x": 270, "y": 470, "scale": 0.8, "svg": brain(), "anim": {"pulse": 0.06, "bob": 10, "period": 0.4}},
                 {"id": "snail", "x": 150, "y": 720, "scale": 1.5, "svg": SNAIL, "anim": {"drift": [6, 0], "bob": 1, "period": 2}}]},
    # 8. Lifting your arm: eight long minutes.
    {"start": "Your muscles still move", "bg": "warm_interior", "camera": "closeup", "focus": "hero", "zoom": 1.6, "transition": "cut",
     "objects": [{"id": "clk8", "x": 400, "y": 480, "scale": 0.45, "svg": clock(), "anim": {"sway": 2, "period": 3}},
                 {"id": "hand8", "x": 400, "y": 480, "scale": 0.45, "svg": HAND(), "anim": {"spin": 90}}],
     "actors": [{"id": "hero", "char": "hero", "x": 230, "y": 808, "scale": 1.3, "pose": "idle", "face": "determined",
                 "keys": [{"at": "so lifting your arm", "pose": "reach_up", "face": "tired", "dur": 3.0, "ease": "linear"}]}]},
    # 9. One blink: eyelids close on the night city.
    {"start": "One blink is", "bg": "night_city", "camera": "drift", "transition": "none", "fx": ["stars"],
     "objects": [{"id": "lidT", "x": 270, "y": 0, "svg": LID(True), "front": True,
                  "keys": [{"at": "One blink", "y": 420, "dur": 0.9, "ease": "inout"}]},
                 {"id": "lidB", "x": 270, "y": 960, "svg": LID(False), "front": True,
                  "keys": [{"at": "One blink", "y": 460, "dur": 0.9, "ease": "inout"}]}]},
    # 10. Mia says hello: the word crawls toward you.
    {"start": "When your best friend Mia", "bg": "dusk", "camera": "push", "transition": "cut",
     "fx": [{"type": "clouds", "speed": 3, "opacity": 0.4, "y0": 120, "h": 260}],
     "objects": [{"id": "word", "x": 150, "y": 560, "svg": WORD_HE, "anim": {"bob": 4, "period": 1.6},
                  "keys": [{"at": "that one word", "x": 290, "dur": 3.5, "ease": "linear"}]}],
     "actors": [{"id": "mia", "char": "mia", "x": 120, "y": 815, "scale": 1.2, "pose": "wave", "face": "happy"},
                {"id": "hero", "char": "hero", "x": 400, "y": 815, "scale": 1.2, "pose": "idle", "face": "bored", "flip": True}]},
    # 11. Frozen to everyone watching; a whole afternoon inside.
    {"start": "And to everyone watching", "bg": "cool_interior", "camera": "pull", "transition": "cut",
     "props": BOARD,
     "fx": [{"type": "pulse", "x": 370, "y": 520, "r": 120, "period": 1.2, "color": "#C8FF4D"}],
     "objects": [{"id": "think", "x": 370, "y": 500, "scale": 0.0, "svg": f"<circle r='80' fill='#BFE3FF' stroke='{INK}' stroke-width='5'/><g transform='scale(.5)'>{SUN}</g>",
                  "keys": [{"at": "while inside your head", "scale": 0.85, "dur": 0.4, "ease": "back"}]},
                 {"id": "tsun", "x": 320, "y": 520, "svg": "<circle r='14' fill='#FFC23D' stroke='#141218' stroke-width='3'/>", "opacity": 0,
                  "keys": [{"at": "while inside your head+0.3", "opacity": 1, "dur": 0.2}, {"at": "a whole afternoon", "x": 420, "y": 500, "dur": 1.5, "arc": 40}]}],
     "actors": [{"id": "e1", "char": "extra", "shirt": "#FFB547", "x": 110, "y": 810, "scale": 1.1, "pose": "point", "face": "shocked"},
                {"id": "e2", "char": "extra", "shirt": "#7FD1FF", "x": 200, "y": 810, "scale": 1.0, "pose": "shrug", "face": "worried"},
                {"id": "hero", "char": "hero", "x": 360, "y": 810, "scale": 1.2, "pose": "stand", "face": "neutral", "flip": True}]},
    # 12. Brain: 2% of body, 20% of energy, over Earth's curve.
    {"start": "Here's the weird part", "bg": "earth_orbit", "camera": "zoom_in", "zoom": 1.15, "cx": 270, "cy": 520, "transition": "zoom",
     "fx": ["stars", {"type": "embers", "n": 26, "speed": 1.2, "color": "#FFD27A"}],
     "objects": [{"id": "brain12", "x": 270, "y": 520, "scale": 1.0, "svg": brain(glow="#FFD27A"), "anim": {"pulse": 0.06, "period": 0.8, "spin": 0, "bob": 5}}]},
    # 13. Ten-minute bus ride lasts a week.
    {"start": "So you stop talking", "bg": "city_day", "camera": "pan_left", "transition": "whip", "whip_dir": "right",
     "fx": [{"type": "clouds", "speed": 2, "opacity": 0.5, "y0": 100, "h": 280}],
     "objects": [{"id": "bus", "x": 160, "y": 760, "svg": BUS, "anim": {"bob": 2, "period": 0.6},
                  "keys": [{"at": "A ten minute bus ride", "x": 215, "dur": 4.0, "ease": "linear"}]},
                 {"id": "snail13", "x": 380, "y": 800, "scale": 0.9, "svg": SNAIL, "anim": {"drift": [-3, 0]}}]},
    # 14. A city designed in your mind.
    {"start": "You design a whole city", "bg": "future_city", "camera": "tilt_up", "from_y": 700, "to_y": 480, "zoom": 1.3, "transition": "zoom",
     "fx": [{"type": "rays", "x": 270, "y": 600, "spin": 7, "opacity": 0.12, "color": "#5BE7FF"}, {"type": "dust", "n": 30, "color": "#5BE7FF"}],
     "objects": [{"id": "bp", "x": 270, "y": 620, "scale": 0.1, "opacity": 0.2, "svg": BLUEPRINT, "anim": {"flicker": 0.15},
                  "keys": [{"at": "You design", "scale": 1.0, "opacity": 1, "dur": 2.5, "ease": "out"}]}]},
    # 15. One year, a thousand years: the sun streaks like a strobe.
    {"start": "In one year", "bg": "sky", "camera": "static", "transition": "flash",
     "fx": [{"type": "clouds", "speed": 90, "opacity": 0.6, "y0": 140, "h": 380}, "glitch"],
     "props": STREAK,
     "objects": [{"id": "sun15", "x": 270, "y": 980, "svg": "<g transform='translate(0 -520)'>" + SUN + "</g>", "anim": {"spin": 260}}]},
    # 16. Alone among statues: one goodnight hug lasts an hour.
    {"start": "But you live them alone", "bg": "warm_interior", "camera": "closeup", "focus": "hero", "zoom": 1.5, "focus_y": 640, "transition": "cut",
     "props": BED, "fx": [{"type": "dust", "n": 24, "speed": 0.2, "color": "#FFD27A"}],
     "actors": [{"id": "mom", "char": "mom", "x": 230, "y": 808, "scale": 1.3, "pose": "hug", "face": "happy"},
                {"id": "hero", "char": "hero", "x": 310, "y": 808, "scale": 1.1, "pose": "hug", "face": "sad", "flip": True}]},
    # 17. The switch.
    {"start": "One night, you find out", "bg": "space", "camera": "push", "transition": "flash",
     "fx": ["stars", {"type": "pulse", "x": 270, "y": 560, "r": 220, "period": 1.3, "color": "#C8FF4D"}],
     "objects": [{"id": "sw", "x": 270, "y": 560, "scale": 1.2, "svg": SWITCH, "anim": {"bob": 4, "period": 2.4}},
                 {"id": "knob", "x": 270, "y": 488, "scale": 1.2, "svg": KNOB, "front": True, "anim": {"pulse": 0.08, "period": 0.7}}]},
    # 18. Keep it: Mia grows up while you watch.
    {"start": "Keep it, and you", "bg": "night_city", "camera": "pan_right", "transition": "cut", "fx": ["stars", {"type": "snow", "n": 40, "speed": 0.4}],
     "actors": [{"id": "hero", "char": "hero", "x": 140, "y": 812, "scale": 1.15, "pose": "stand", "face": "sad"},
                {"id": "mia", "char": "mia", "x": 340, "y": 812, "scale": 0.95, "pose": "idle", "face": "happy", "flip": True,
                 "keys": [{"at": "watching Mia grow up", "scale": 1.35, "dur": 3.5, "ease": "linear"},
                          {"at": "one slow blink", "face": "neutral", "dur": 0.6}]}]},
    # 19. Switch it off: ordinary, together.
    {"start": "Switch it off, and", "bg": "day_park", "camera": "pull", "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "confetti", "n": 50}],
     "actors": [{"id": "hero", "char": "hero", "x": 160, "y": 815, "scale": 1.2, "pose": "walk_a", "face": "happy",
                 "keys": [{"at": "Switch it off, and", "x": 260, "dur": 3.0, "cycle": "walk", "ease": "linear"}, {"at": "everyone you love", "cycle": None, "pose": "cheer", "face": "happy"}]},
                {"id": "mia", "char": "mia", "x": 60, "y": 815, "scale": 1.2, "pose": "walk_a", "face": "happy",
                 "keys": [{"at": "Switch it off, and", "x": 120, "dur": 3.0, "cycle": "walk", "ease": "linear"}, {"at": "everyone you love", "cycle": None, "pose": "wave"}]},
                {"id": "mom", "char": "mom", "x": 400, "y": 815, "scale": 1.25, "pose": "wave", "face": "happy", "flip": True}]},
    # 20. Loop: the racing brain again.
    {"start": "Which one do you choose", "bg": "void", "transition": "zoom",
     "fx": [{"type": "warp", "x": 270, "y": 540, "n": 80, "speed": 2.2, "color": "#C8FF4D"}, {"type": "pulse", "x": 270, "y": 540, "r": 260, "period": 0.6, "color": "#C8FF4D"}],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 540},
     "cam": [{"at": "Which one", "zoom": 1.3, "cx": 270, "cy": 540, "dur": 4.0, "ease": "inout"}],
     "objects": [BRAIN_OBJ("brain20")]},
]

hud = [
    {"type": "title", "at": 0.05, "until": "Every second", "small": "WHAT IF YOUR BRAIN", "text": "RAN 1,000x FASTER?", "color": "#C8FF4D", "size": 56, "top": 150},
    {"type": "title", "at": "would feel like", "until": "Your teacher", "small": "ONE SECOND FEELS LIKE", "text": "17 MINUTES", "color": "#FFD27A", "size": 74, "top": 150, "captions": True},
    {"type": "title", "at": "slower than you walk", "until": "But there's a catch", "small": "A BULLET MOVES", "text": "SLOWER THAN YOU", "color": "#FF6B6B", "size": 58, "top": 150, "captions": True},
    {"type": "note", "at": "Your brain is fast", "until": "Your muscles still", "label": "THE CATCH", "text": "Brain ×1000. Body ×1."},
    {"type": "title", "at": "One blink is", "until": "When your best friend", "small": "ONE BLINK", "text": "5 MINUTES OF DARK", "color": "#C9D2EE", "size": 54, "top": 150, "captions": True},
    {"type": "compare", "at": "only two percent", "until": "So you stop talking", "label": "YOUR BRAIN · REAL SCIENCE", "a": ["Of your weight", "2%", 0.1], "b": ["Of your energy", "20%", 1.0]},
    {"type": "title", "at": "In one year", "until": "But you live them alone", "small": "ONE YEAR FEELS LIKE", "text": "1,000 YEARS", "color": "#FFD27A", "size": 76, "top": 150, "captions": True},
    {"type": "endcard", "at": "Which one do you choose", "text": "Keep it or switch it off?", "a": "KEEP IT", "b": "SWITCH OFF"},
]

ep.update({
    "ep": 36,
    "voiceover": "voiceover.wav",
    "accent": "#C8FF4D",
    "show_ep": False,
    "thumbnail": "drifts in like a soap bubble",
    "highlights": {"thousand times faster": "green", "seventeen minutes": "amber", "eight long minutes": "amber",
                   "five minutes": "amber", "a fifth": "green", "a week": "amber", "a thousand": "green"},
    "music": [{"track": "music/daybreak.mp3", "at": 0},
              {"track": "music/ominosity.mp3", "at": "But there's a catch"},
              {"track": "music/a-memory-away.mp3", "at": "But you live them alone"}],
    "music_db_below_voice": 20,
    "hud": hud,
    "shakes": [{"at": "But there's a catch", "amp": 12, "dur": 0.4}, {"at": "In one year", "amp": 10, "dur": 0.4}],
    "flashes": [{"at": "One night, you find out", "dur": 0.12, "color": "#C8FF4D"}],
    "sfx": [{"name": "riser", "at": "Here's the weird part", "gain": 0.6}],
    "scenes": scenes,
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
