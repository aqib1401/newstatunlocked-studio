import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"


def disk(r=150, hot="#FFB547", warm="#FF6B3D"):
    """Swirling accretion disk seen face-on (spins nicely with anim.spin)."""
    rings = ""
    for i, (rr, col, w, dash) in enumerate([(r * 1.0, warm, r * .16, "40 26"), (r * .84, hot, r * .12, "60 18"),
                                            (r * .70, "#FFE7A0", r * .08, "30 14"), (r * .60, "#FFF6D8", r * .04, "18 10")]):
        rings += f"<circle r='{rr:.1f}' fill='none' stroke='{col}' stroke-width='{w:.1f}' stroke-dasharray='{dash}' opacity='.9'/>"
    return f"<circle r='{r*1.25:.1f}' fill='{hot}' opacity='.10'/><circle r='{r*1.1:.1f}' fill='{warm}' opacity='.12'/>{rings}"


def core(r=150):
    return (f"<circle r='{r*.56:.1f}' fill='#FFF6D8' opacity='.9'/>"
            f"<circle r='{r*.5:.1f}' fill='#000' stroke='{INK}' stroke-width='4'/>")


def bh(id_, x, y, r, spin=40, front=False, keys=None, scale=1.0):
    """Two objects: spinning disk + static black core."""
    d = {"id": id_ + "_d", "x": x, "y": y, "scale": scale, "svg": disk(r), "anim": {"spin": spin}}
    c = {"id": id_ + "_c", "x": x, "y": y, "scale": scale, "svg": core(r), "anim": {"pulse": 0.02, "period": 1.6}}
    if keys:
        d["keys"] = [dict(k) for k in keys]
        c["keys"] = [dict(k) for k in keys]
    return [d, c]


def stick(h=1.0, w=1.0, col="#5BA8FF"):
    """Simple stick figure stretched vertically by h and squeezed by w (feet at y=0)."""
    hy = -170 * h
    return (f"<g stroke='{INK}' stroke-width='{7*w:.1f}' stroke-linecap='round' fill='none'>"
            f"<path d='M0 {hy+34*h:.0f} L0 {-70*h:.0f}' stroke='{col}' stroke-width='{18*w:.1f}'/>"
            f"<path d='M0 {-70*h:.0f} L{-18*w:.0f} 0 M0 {-70*h:.0f} L{18*w:.0f} 0'/>"
            f"<path d='M0 {hy+50*h:.0f} L{-30*w:.0f} {hy+100*h:.0f} M0 {hy+50*h:.0f} L{30*w:.0f} {hy+100*h:.0f}'/></g>"
            f"<ellipse cx='0' cy='{hy+16*h:.0f}' rx='{22*w:.0f}' ry='{22*h:.0f}' fill='#F4F1FF' stroke='{INK}' stroke-width='5'/>")


def arrow(length=80, col="#FF6B6B", w=10):
    return (f"<path d='M0 0 L0 {length}' stroke='{col}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<path d='M{-w*1.6} {length-w*1.4} L0 {length+w*1.2} L{w*1.6} {length-w*1.4} Z' fill='{col}' stroke='{INK}' stroke-width='3'/>")


TUBE = (f"<path d='M-150 -40 L60 -34 L60 34 L-150 40 Z' fill='#F4F1FF' stroke='{INK}' stroke-width='6'/>"
        f"<path d='M-150 -40 L-170 -46 L-170 46 L-150 40 Z' fill='#D8D2EA' stroke='{INK}' stroke-width='5'/>"
        f"<rect x='-110' y='-18' width='120' height='36' rx='8' fill='#5BA8FF' stroke='{INK}' stroke-width='4'/>"
        f"<path d='M60 -22 L92 -14 L92 14 L60 22 Z' fill='#C8FF4D' stroke='{INK}' stroke-width='5'/>")
PASTE = (f"<path d='M0 -10 Q60 -26 120 -6 T240 -4 T330 6' stroke='{INK}' stroke-width='26' fill='none' stroke-linecap='round'/>"
         "<path d='M0 -10 Q60 -26 120 -6 T240 -4 T330 6' stroke='#F4F1FF' stroke-width='16' fill='none' stroke-linecap='round'/>"
         "<path d='M0 -10 Q60 -26 120 -6 T240 -4 T330 6' stroke='#5BE7FF' stroke-width='5' fill='none' stroke-linecap='round'/>")
SINK = (f"<rect x='0' y='640' width='540' height='26' fill='#C9D2EE' stroke='{INK}' stroke-width='5'/>"
        f"<rect x='20' y='666' width='500' height='150' fill='#8E9AC4' stroke='{INK}' stroke-width='5'/>"
        f"<rect x='150' y='380' width='240' height='200' rx='14' fill='#BFE3FF' stroke='{INK}' stroke-width='6' opacity='.9'/>"
        "<path d='M180 410 L230 460 M300 400 L360 470' stroke='#FFFFFF' stroke-width='8' opacity='.6' stroke-linecap='round'/>")
NOODLE = ("<path d='M0 -230 C160 -230 230 -100 200 20 C170 140 40 170 -40 120 C-110 70 -100 -20 -30 -40 C20 -54 50 -10 30 20' "
          "stroke='#141218' stroke-width='20' fill='none' stroke-linecap='round'/>"
          "<path d='M0 -230 C160 -230 230 -100 200 20 C170 140 40 170 -40 120 C-110 70 -100 -20 -30 -40 C20 -54 50 -10 30 20' "
          "stroke='#5BA8FF' stroke-width='11' fill='none' stroke-linecap='round'/>")
RULER = (f"<path d='M0 0 L300 0' stroke='#F4F1FF' stroke-width='5' stroke-dasharray='14 10'/>"
         f"<path d='M0 -18 L0 18 M300 -18 L300 18' stroke='#F4F1FF' stroke-width='5'/>"
         "<text x='150' y='-24' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='38' fill='#FFD27A' stroke='#141218' stroke-width='2'>1,000+ KM</text>")
POP = "<circle r='22' fill='#FF6B6B' opacity='.35'/><circle r='9' fill='#FF6B6B'/>"
HULL = (f"<rect x='0' y='0' width='540' height='960' fill='#2A2840'/>"
        f"<circle cx='300' cy='470' r='190' fill='#05040A' stroke='#8E9AC4' stroke-width='26'/>"
        f"<circle cx='300' cy='470' r='190' fill='none' stroke='{INK}' stroke-width='6'/>"
        + "".join(f"<circle cx='{300+212*c:.0f}' cy='{470+212*s:.0f}' r='7' fill='#C9D2EE' stroke='{INK}' stroke-width='3'/>"
                  for c, s in [(1, 0), (0, 1), (-1, 0), (0, -1), (.707, .707), (-.707, .707), (.707, -.707), (-.707, -.707)])
        + f"<rect x='0' y='760' width='540' height='200' fill='#3A3756' stroke='{INK}' stroke-width='5'/>"
        "<rect x='40' y='120' width='80' height='14' rx='7' fill='#5BE7FF' opacity='.6'/><rect x='40' y='150' width='50' height='14' rx='7' fill='#C8FF4D' opacity='.6'/>")
WIN_STARS = "".join(f"<circle cx='{x}' cy='{y}' r='{r}' fill='#F4F1FF' opacity='.8'/>" for x, y, r in
                    [(190, 360, 2), (380, 330, 2.5), (420, 540, 2), (210, 590, 1.5), (300, 300, 1.5), (450, 430, 2)])
TINY = (f"<circle cx='0' cy='-30' r='9' fill='#F4F1FF' stroke='{INK}' stroke-width='3'/>"
        f"<path d='M0 -21 L0 0 M0 -14 L-10 -4 M0 -14 L10 -4 M0 0 L-7 14 M0 0 L7 14' stroke='#5BA8FF' stroke-width='5' stroke-linecap='round'/>")
REDGLOW = "<circle r='26' fill='#FF3D3D' opacity='.55'/>"


def clock(r=110):
    ticks = "".join(f"<rect x='-3' y='{-r+10}' width='6' height='{18 if i % 3 == 0 else 10}' fill='{INK}' transform='rotate({i*30})'/>" for i in range(12))
    return (f"<circle r='{r+14}' fill='#FFD27A' opacity='.15'/><circle r='{r}' fill='#F4F1FF' stroke='{INK}' stroke-width='8'/>{ticks}"
            f"<rect x='-5' y='{-r*.5}' width='10' height='{r*.55}' rx='5' fill='{INK}' transform='rotate(-60)'/><circle r='10' fill='{INK}'/>")


HAND = lambda r=110: f"<rect x='-3' y='{-r*.85}' width='6' height='{r*.95}' rx='3' fill='#FF6B6B'/><circle r='7' fill='#FF6B6B'/>"
SUN = "<circle r='80' fill='#FFB547' opacity='.2'/><circle r='52' fill='#FFC23D' stroke='#141218' stroke-width='5'/>"
ARROWS = "".join(f"<g transform='rotate({a}) translate(0 -260)'>{arrow(110, '#5BE7FF', 9)}</g>" for a in range(0, 360, 45))

FLOAT = {"shadow": False}

scenes = [
    # 1. Opening: the black hole swirling, a tiny you drifting toward it.
    {"bg": "void", "fx": ["stars", {"type": "warp", "x": 270, "y": 560, "n": 60, "speed": 1.4, "color": "#FFD27A"}],
     "cam_start": {"zoom": 1.35, "cx": 270, "cy": 560},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 540, "dur": 2.0, "ease": "out"}],
     "objects": bh("bh1", 270, 600, 150, spin=50) + [
         {"id": "tiny1", "x": 420, "y": 440, "scale": 1.2, "svg": TINY, "anim": {"spin": 25, "bob": 4, "period": 1.5},
          "keys": [{"at": "You get two tries", "x": 340, "y": 520, "scale": 0.7, "dur": 4.0, "ease": "in"}]}]},
    # 2. Attempt one: a small black hole hanging over Earth's curve.
    {"start": "Attempt one", "bg": "earth_orbit", "camera": "reveal", "cx": 270, "cy": 560, "zoom": 2.0, "transition": "whip", "whip_dir": "right",
     "fx": ["stars", {"type": "pulse", "x": 270, "y": 560, "r": 160, "period": 1.2, "color": "#FF6B3D"}],
     "objects": bh("bh2", 270, 560, 80, spin=90)},
    # 3. Feet first: you drift down toward it.
    {"start": "You drift toward it", "bg": "space", "camera": "drift", "transition": "cut",
     "fx": ["stars", {"type": "speedlines", "dir": "left", "n": 8, "speed": 0.6}],
     "objects": bh("bh3", 270, 760, 110, spin=80),
     "actors": [{"id": "hero", "char": "hero", "x": 270, "y": 560, "scale": 1.1, "pose": "idle", "face": "neutral", **FLOAT,
                 "keys": [{"at": "feet first", "y": 600, "face": "worried", "dur": 1.6, "ease": "in"}]}]},
    # 4. The stretch, as a diagram: feet pulled far harder than head.
    {"start": "Gravity at your feet", "bg": "lab", "camera": "push", "transition": "cut",
     "fx": [{"type": "speedlines", "dir": "right", "n": 5, "speed": 0.4}],
     "objects": [
         {"id": "st1", "x": 270, "y": 700, "svg": stick(1.0, 1.0), "anim": {"bob": 3, "period": 1.2},
          "keys": [{"at": "your body stretches", "opacity": 0, "dur": 0.15}]},
         {"id": "st2", "x": 270, "y": 720, "opacity": 0, "svg": stick(1.6, 0.7), "anim": {"bob": 3, "period": 1.2},
          "keys": [{"at": "your body stretches", "opacity": 1, "dur": 0.15}, {"at": "longer and thinner", "opacity": 0, "dur": 0.15}]},
         {"id": "st3", "x": 270, "y": 745, "opacity": 0, "svg": stick(2.3, 0.45), "anim": {"bob": 3, "period": 1.2},
          "keys": [{"at": "longer and thinner", "opacity": 1, "dur": 0.15}]},
         {"id": "aHead", "x": 150, "y": 330, "svg": arrow(40, "#C8FF4D", 8), "anim": {"bob": 3, "period": 0.8}},
         {"id": "aFeet", "x": 150, "y": 600, "svg": arrow(150, "#FF6B6B", 12), "anim": {"bob": 6, "period": 0.5}}]},
    # 5. Like toothpaste: a tube squeezing on the bathroom sink.
    {"start": "like toothpaste", "bg": "warm_interior", "camera": "zoom_in", "zoom": 1.25, "cx": 270, "cy": 600, "transition": "whip", "whip_dir": "left",
     "props": SINK, "fx": [{"type": "dust", "n": 20, "speed": 0.2, "color": "#FFD27A"}],
     "objects": [{"id": "tube", "x": 235, "y": 610, "rot": -8, "svg": TUBE, "anim": {"sway": 2, "period": 0.6}},
                 {"id": "paste", "x": 327, "y": 600, "scale": 0.05, "svg": PASTE,
                  "keys": [{"at": "like toothpaste+0.2", "scale": 0.6, "dur": 1.4, "ease": "out", "sfx": "swish"}]}]},
    # 6. Spaghettification: a noodle of you spiralling in.
    {"start": "Scientists really call", "bg": "space", "camera": "static", "transition": "zoom",
     "fx": ["stars", {"type": "rays", "x": 270, "y": 600, "spin": 10, "opacity": 0.10, "color": "#FFB547"}],
     "objects": bh("bh6", 270, 600, 110, spin=70) + [
         {"id": "noodle", "x": 270, "y": 600, "scale": 1.0, "svg": NOODLE, "front": True, "anim": {"spin": 70},
          "keys": [{"at": "and it tears you apart", "scale": 0.3, "opacity": 0, "dur": 1.2, "ease": "in"}]}]},
    # 7. Torn apart a thousand kilometers out: a ruler from the edge.
    {"start": "more than a thousand kilometers", "bg": "earth_orbit", "camera": "pan_right", "transition": "flash",
     "fx": ["stars", {"type": "pulse", "x": 420, "y": 520, "r": 90, "period": 0.8, "color": "#FF6B6B"}],
     "objects": bh("bh7", 90, 520, 55, spin=100) + [
         {"id": "ruler", "x": 120, "y": 520, "svg": RULER},
         {"id": "pop", "x": 420, "y": 520, "svg": POP, "anim": {"pulse": 0.2, "period": 0.5}}]},
    # 8. Attempt two: the giant at the center of the galaxy fills the frame.
    {"start": "So, attempt two", "bg": "void", "camera": "pull", "transition": "zoom",
     "fx": ["stars", {"type": "embers", "n": 30, "speed": 0.8, "color": "#FFD27A"}],
     "objects": bh("bh8", 270, 580, 230, spin=18)},
    # 9. Same pull on head and feet: you float calmly in one piece.
    {"start": "It's so huge", "bg": "space", "camera": "pan_left", "transition": "cut",
     "fx": ["stars", {"type": "dust", "n": 26, "speed": 0.3, "color": "#FFD27A"}],
     "actors": [{"id": "hero", "char": "hero", "x": 250, "y": 690, "scale": 1.3, "pose": "idle", "face": "neutral", **FLOAT,
                 "keys": [{"at": "this time you stay", "pose": "cheer", "face": "happy", "dur": 0.3}]}],
     "objects": [{"id": "aH9", "x": 380, "y": 400, "svg": arrow(60, "#C8FF4D", 8), "anim": {"bob": 3, "period": 1.0}},
                 {"id": "aF9", "x": 380, "y": 560, "svg": arrow(66, "#C8FF4D", 8), "anim": {"bob": 3, "period": 1.0}}]},
    # 10. The point of no return: a vast glowing edge, you tiny against it.
    {"start": "You cross the edge", "bg": "earth_orbit", "camera": "reveal", "cx": 270, "cy": 520, "zoom": 2.4, "transition": "flash",
     "fx": ["stars", {"type": "pulse", "x": 270, "y": 900, "r": 300, "period": 1.6, "color": "#FFB547"}],
     "props": "<circle cx='270' cy='1350' r='820' fill='#FFE7A0' opacity='.25'/><circle cx='270' cy='1350' r='790' fill='#000' stroke='#FFF6D8' stroke-width='10'/>",
     "objects": [{"id": "tiny10", "x": 270, "y": 520, "scale": 1.6, "svg": TINY, "anim": {"spin": 12, "bob": 4, "period": 2},
                  "keys": [{"at": "you barely feel", "y": 580, "dur": 2.0, "ease": "in"}]}]},
    # 11. Your friend at the spaceship window.
    {"start": "But your friend", "bg": "cool_interior", "camera": "push", "transition": "whip", "whip_dir": "right",
     "props": HULL + WIN_STARS,
     "objects": bh("bh11", 300, 520, 70, spin=60) + [
         {"id": "tiny11", "x": 300, "y": 440, "scale": 0.9, "svg": TINY, "anim": {"bob": 2, "period": 2}}],
     "actors": [{"id": "mia", "char": "mia", "x": 120, "y": 812, "scale": 1.25, "pose": "point", "face": "shocked", "flip": False}]},
    # 12. Through the window: you slow, redden, dim, freeze.
    {"start": "To her, you slow down", "bg": "cool_interior", "camera": "closeup", "focus_y": 470, "zoom": 1.9, "transition": "none",
     "props": HULL + WIN_STARS,
     "objects": bh("bh12", 300, 520, 70, spin=60) + [
         {"id": "red12", "x": 300, "y": 452, "opacity": 0, "svg": REDGLOW,
          "keys": [{"at": "turning red", "opacity": 1, "dur": 0.8}, {"at": "then dim", "opacity": 0.3, "dur": 1.0}]},
         {"id": "tiny12", "x": 300, "y": 440, "scale": 0.9, "svg": TINY,
          "keys": [{"at": "To her, you slow down", "y": 452, "dur": 4.0, "ease": "out"},
                   {"at": "then dim", "opacity": 0.25, "dur": 1.2}]}],
     "actors": [{"id": "mia", "char": "mia", "x": 140, "y": 812, "scale": 1.25, "pose": "think", "face": "worried"}]},
    # 13. Inside: still falling, and every direction points to the center.
    {"start": "You're actually still falling", "bg": "void", "camera": "drift", "transition": "zoom",
     "fx": [{"type": "warp", "x": 270, "y": 560, "n": 90, "speed": 2.4, "color": "#5BE7FF"}, "glitch"],
     "objects": [{"id": "arrows", "x": 270, "y": 560, "scale": 0.0, "svg": ARROWS, "anim": {"spin": -14},
                  "keys": [{"at": "every direction", "scale": 1.0, "dur": 0.6, "ease": "back", "sfx": "pop"}]},
                 {"id": "dot", "x": 270, "y": 560, "svg": "<circle r='16' fill='#F4F1FF'/><circle r='34' fill='#5BE7FF' opacity='.25'/>", "anim": {"pulse": 0.25, "period": 0.6}}],
     "actors": [{"id": "hero", "char": "hero", "x": 270, "y": 470, "scale": 0.7, "pose": "fall", "face": "shocked", **FLOAT,
                 "keys": [{"at": "every direction", "x": 120, "y": 360, "scale": 0.55, "dur": 0.8}]}]},
    # 14. Like going back to yesterday: the sun runs backward, the clock unwinds.
    {"start": "so trying to escape", "bg": "dusk", "camera": "tilt_up", "from_y": 620, "to_y": 480, "zoom": 1.25, "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "clouds", "speed": -60, "opacity": 0.5, "y0": 120, "h": 300}],
     "objects": [{"id": "sun14", "x": 120, "y": 700, "svg": SUN, "keys": [{"at": "so trying to escape", "x": 400, "y": 300, "dur": 3.5, "arc": 80}]},
                 {"id": "clk14", "x": 270, "y": 560, "scale": 0.0, "svg": clock()},
                 {"id": "hand14", "x": 270, "y": 560, "scale": 0.0, "svg": HAND(), "anim": {"spin": -320},
                  "keys": [{"at": "go back to yesterday", "scale": 1.0, "dur": 0.4, "ease": "back"}]}]},
    # 15. Loop: back to the opening black hole; one minute, then the toothpaste problem.
    {"start": "How long do you get inside", "bg": "void", "transition": "zoom",
     "fx": ["stars", {"type": "warp", "x": 270, "y": 560, "n": 60, "speed": 1.4, "color": "#FFD27A"}],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 540},
     "cam": [{"at": "How long", "zoom": 1.3, "cx": 270, "cy": 560, "dur": 6.0, "ease": "inout"}],
     "objects": bh("bh15", 270, 600, 150, spin=50) + [
         {"id": "tiny15", "x": 420, "y": 440, "scale": 1.2, "svg": TINY, "anim": {"spin": 25, "bob": 4, "period": 1.5}}]},
]
# The clock face appears with its hand.
scenes[13]["objects"][1]["keys"] = [{"at": "go back to yesterday", "scale": 1.0, "dur": 0.4, "ease": "back"}]

hud = [
    {"type": "title", "at": 0.05, "until": "You get two tries", "small": "WHAT IF YOU FELL INTO", "text": "A BLACK HOLE?", "color": "#FFD27A", "size": 66, "top": 150},
    {"type": "title", "at": "Attempt one", "until": "You drift toward", "small": "ATTEMPT 1 · 10 SUNS", "text": "60 KM WIDE", "color": "#FF8A5B", "size": 72, "top": 150, "captions": True},
    {"type": "title", "at": "Scientists really call", "until": "more than a thousand", "text": "SPAGHETTIFICATION", "color": "#5BE7FF", "size": 48, "top": 160, "captions": True},
    {"type": "title", "at": "So, attempt two", "until": "It's so huge", "small": "ATTEMPT 2 · CENTER OF THE GALAXY", "text": "4,000,000 SUNS", "color": "#FFD27A", "size": 62, "top": 150, "captions": True},
    {"type": "note", "at": "It's so huge", "until": "You cross the edge", "label": "REAL SCIENCE", "text": "Head and feet: almost the same pull."},
    {"type": "title", "at": "the point of no return", "until": "But your friend", "small": "THE EVENT HORIZON", "text": "NO RETURN", "color": "#FFF6D8", "size": 80, "top": 150, "captions": True},
    {"type": "title", "at": "About one minute", "until": "end:anyway", "small": "TIME LEFT INSIDE", "text": "ABOUT 1 MINUTE", "color": "#C8FF4D", "size": 64, "top": 150, "captions": True},
]

ep.update({
    "ep": 37,
    "voiceover": "voiceover.wav",
    "accent": "#FFD27A",
    "show_ep": False,
    "thumbnail": "Scientists really call+0.8",
    "highlights": {"sixty kilometers": "amber", "spaghettification": "green", "four million": "amber",
                   "point of no return": "amber", "freeze at the edge forever": "green", "About one minute": "green"},
    "music": [{"track": "music/syntheticity.mp3", "at": 0},
              {"track": "music/deeper.mp3", "at": "You drift toward it"},
              {"track": "music/fate.mp3", "at": "So, attempt two"}],
    "music_db_below_voice": 20,
    "hud": hud,
    "shakes": [{"at": "and it tears you apart", "amp": 16, "dur": 0.5}, {"at": "You cross the edge", "amp": 10, "dur": 0.4}],
    "flashes": [{"at": "and it tears you apart", "dur": 0.15, "color": "#FF6B6B"}, {"at": "the point of no return", "dur": 0.12, "color": "#FFF6D8"}],
    "sfx": [{"name": "riser", "at": "You're actually still falling", "gain": 0.6}],
    "scenes": scenes,
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
