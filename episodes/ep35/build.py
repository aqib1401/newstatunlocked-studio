import json
from pathlib import Path

E = Path(__file__).resolve().parent
ep = json.loads((E / "episode.json").read_text())
INK = "#141218"


def sun(r=110):
    return (f"<circle r='{r*1.9}' fill='#FFB547' opacity='.12'/><circle r='{r*1.45}' fill='#FFD27A' opacity='.22'/>"
            f"<circle r='{r}' fill='#FFC23D' stroke='{INK}' stroke-width='6'/>"
            f"<circle cx='{-r*.3}' cy='{-r*.3}' r='{r*.35}' fill='#FFE7A0' opacity='.8'/>"
            f"<circle cx='{r*.35}' cy='{r*.25}' r='{r*.12}' fill='#F29A2E'/><circle cx='{-r*.2}' cy='{r*.45}' r='{r*.09}' fill='#F29A2E'/>")


def earth(r=46):
    return (f"<circle r='{r}' fill='#2F6FD6' stroke='{INK}' stroke-width='5'/>"
            f"<path d='M{-r*.6} {-r*.3} Q{-r*.2} {-r*.7} {r*.2} {-r*.4} Q{r*.1} 0 {-r*.3} {r*.1} Z' fill='#3FAE6A'/>"
            f"<path d='M{r*.2} {r*.2} Q{r*.6} {r*.1} {r*.55} {r*.5} Q{r*.3} {r*.7} {r*.1} {r*.5} Z' fill='#3FAE6A'/>"
            f"<ellipse cx='{-r*.1}' cy='{r*.05}' rx='{r*.5}' ry='{r*.08}' fill='#fff' opacity='.6'/>")


def moon(r=90, lit=True):
    base = '#E9E4F5' if lit else '#2B2840'
    crat = '#C9C2DD' if lit else '#221F33'
    return (f"<circle r='{r}' fill='{base}' stroke='{INK}' stroke-width='6'/>"
            f"<circle cx='{-r*.3}' cy='{-r*.25}' r='{r*.2}' fill='{crat}'/><circle cx='{r*.35}' cy='{r*.1}' r='{r*.14}' fill='{crat}'/>"
            f"<circle cx='{-r*.05}' cy='{r*.45}' r='{r*.12}' fill='{crat}'/>")


def jupiter(r=120):
    bands = "".join(f"<rect x='{-r}' y='{y}' width='{2*r}' height='{h}' fill='{c}'/>" for y, h, c in
                    [(-r*.7, r*.18, '#C98B5A'), (-r*.35, r*.22, '#E3B98A'), (-r*.05, r*.2, '#B8714A'), (r*.3, r*.16, '#E3B98A'), (r*.55, r*.14, '#C98B5A')])
    return (f"<defs><clipPath id='jc'><circle r='{r}'/></clipPath></defs><circle r='{r*1.5}' fill='#FFD8A8' opacity='.14'/>"
            f"<circle r='{r}' fill='#F0D2A8'/><g clip-path='url(#jc)'>{bands}<ellipse cx='{r*.35}' cy='{r*.42}' rx='{r*.22}' ry='{r*.12}' fill='#D9573E'/></g>"
            f"<circle r='{r}' fill='none' stroke='{INK}' stroke-width='6'/>")


BEACH = (f"<rect x='0' y='690' width='540' height='90' fill='#2E8FC9'/>"
         f"<path d='M0 700 Q40 692 80 700 T160 700 T240 700 T320 700 T400 700 T480 700 T560 700' stroke='#BFE3FF' stroke-width='4' fill='none'/>"
         f"<path d='M0 770 Q140 750 270 765 T540 758 L540 960 L0 960 Z' fill='#F2D49B'/>"
         f"<path d='M0 770 Q140 750 270 765 T540 758' fill='none' stroke='{INK}' stroke-width='4'/>"
         f"<rect x='90' y='800' width='220' height='26' rx='6' fill='#E46F8E' stroke='{INK}' stroke-width='4'/>"
         f"<rect x='90' y='808' width='220' height='8' fill='#F4F1FF'/>"
         f"<path d='M420 820 L400 610' stroke='{INK}' stroke-width='6'/>"
         f"<path d='M320 640 Q400 560 480 610 Z' fill='#FF6B6B' stroke='{INK}' stroke-width='5'/>")
WAVE = f"<path d='M-300 0 Q-260 -10 -220 0 T-140 0 T-60 0 T20 0 T100 0 T180 0 T260 0 T340 0' stroke='#F4F1FF' stroke-width='5' fill='none' opacity='.8'/>"
NIGHT = ("<rect x='0' y='0' width='540' height='692' fill='#05040E'/>"
         + "".join(f"<circle cx='{(i*137) % 540}' cy='{(i*71 + i*i*3) % 660 + 10}' r='{1 + (i % 3)*.6}' fill='#fff' opacity='{.4 + (i % 4)*.15}'/>" for i in range(60)))
NIGHT_SEA = "<rect x='0' y='690' width='540' height='270' fill='#05040E' opacity='.55'/>"
BEAM = "<circle r='12' fill='#FFE7A0'/><circle r='26' fill='#FFE7A0' opacity='.3'/><path d='M-70 0 L-12 0' stroke='#FFE7A0' stroke-width='8' stroke-linecap='round' opacity='.6'/>"
DOTTED_PATH = "<path d='M120 560 L430 560' stroke='#FFE7A0' stroke-width='3' stroke-dasharray='6 12' opacity='.5'/>"
ORBIT = "<ellipse cx='270' cy='560' rx='190' ry='190' fill='none' stroke='#7FD1FF' stroke-width='3' stroke-dasharray='10 12' opacity='.5'/>"
GHOST_SUN = "<circle cx='270' cy='560' r='70' fill='none' stroke='#FFD27A' stroke-width='4' stroke-dasharray='8 10' opacity='.55'/><text x='270' y='570' text-anchor='middle' font-family='Chakra Petch' font-weight='700' font-size='26' fill='#FFD27A' opacity='.7'>GONE</text>"
ICE = (f"<rect x='0' y='0' width='540' height='150' fill='#DDF4FF' stroke='{INK}' stroke-width='5'/>"
       f"<path d='M0 150 L40 170 L90 150 L150 176 L210 150 L280 172 L350 150 L420 170 L480 150 L540 166 L540 150 Z' fill='#DDF4FF' stroke='{INK}' stroke-width='4'/>"
       f"<path d='M60 40 L110 90 M300 30 L340 100 M430 60 L470 90' stroke='#9FD3EE' stroke-width='5'/>"
       "<rect x='0' y='150' width='540' height='200' fill='#06243A' opacity='.35'/>")
VENT = (f"<path d='M-40 0 L-22 -110 L22 -110 L40 0 Z' fill='#4A3A4E' stroke='{INK}' stroke-width='5'/>"
        f"<ellipse cx='0' cy='-110' rx='24' ry='8' fill='#FF8A4C' stroke='{INK}' stroke-width='4'/>")
WORMS = "".join(f"<path d='M{x} 0 Q{x-6} -30 {x+2} -{h}' stroke='#F4F1FF' stroke-width='7' fill='none' stroke-linecap='round'/><circle cx='{x+2}' cy='-{h}' r='9' fill='#E0443E' stroke='{INK}' stroke-width='3'/>"
                for x, h in [(-30, 50), (-12, 66), (8, 58), (26, 44)])
FISH = f"<path d='M-26 0 Q0 -18 22 0 Q0 18 -26 0 Z' fill='#5BE7FF' stroke='{INK}' stroke-width='4'/><path d='M22 0 L38 -12 L38 12 Z' fill='#5BE7FF' stroke='{INK}' stroke-width='4'/><circle cx='-12' cy='-3' r='3' fill='{INK}'/>"
SCARF_TREE = ""

SUN_OBJ = lambda keys, extra=None: dict({"id": "sun", "x": 270, "y": 560, "scale": 1.0, "anim": {"pulse": 0.04, "period": 1.6, "spin": 6},
                                         "svg": sun(), "keys": keys}, **(extra or {}))

scenes = [
    # 1. The Sun, in motion, then POOF.
    {"bg": "void", "fx": ["stars", {"type": "rays", "x": 270, "y": 560, "spin": 10, "opacity": 0.12, "color": "#FFD27A"}],
     "cam_start": {"zoom": 1.25, "cx": 270, "cy": 560},
     "cam": [{"at": 0, "zoom": 1.0, "cx": 270, "cy": 540, "dur": 2.0, "ease": "out"}],
     "objects": [SUN_OBJ([{"at": "Poof", "scale": 0.02, "opacity": 0, "dur": 0.18, "ease": "in", "sfx": "pop"}])]},
    # 2. The beach: nothing happens.
    {"start": "Here's the weird part", "bg": "sky", "camera": "pan_right", "transition": "whip", "whip_dir": "right",
     "props": BEACH, "fx": [{"type": "clouds", "speed": 8, "opacity": 0.5, "y0": 100, "h": 300}],
     "objects": [{"id": "wave", "x": 270, "y": 730, "svg": WAVE, "anim": {"drift": [18, 0], "bob": 3, "period": 2.4}}],
     "actors": [{"id": "hero", "char": "hero", "x": 200, "y": 800, "scale": 1.1, "pose": "sit", "face": "happy",
                 "keys": [{"at": "and the sky stays blue", "pose": "wave", "face": "happy", "dur": 0.35}]}]},
    # 3. Light's trip from Sun to Earth.
    {"start": "because sunlight takes", "bg": "space", "camera": "static", "fx": ["stars"],
     "props": DOTTED_PATH,
     "objects": [{"id": "s3", "x": 90, "y": 560, "scale": 0.55, "svg": sun(), "anim": {"pulse": 0.05, "period": 1.4}},
                 {"id": "e3", "x": 455, "y": 560, "svg": earth(34), "anim": {"spin": 12}},
                 {"id": "beam", "x": 150, "y": 560, "svg": BEAM, "front": True,
                  "keys": [{"at": "because sunlight takes", "x": 150, "dur": 0.01}, {"at": "eight minutes", "x": 415, "dur": 2.6, "ease": "linear"}]}]},
    # 4. Gravity is on the same delay: Earth circling an empty spot.
    {"start": "Even gravity", "bg": "void", "camera": "zoom_in", "zoom": 1.15, "cx": 270, "cy": 560, "transition": "zoom",
     "fx": ["stars", {"type": "pulse", "x": 270, "y": 560, "r": 200, "period": 1.6, "color": "#FFD27A"}],
     "props": ORBIT + GHOST_SUN,
     "objects": [{"id": "orb", "x": 270, "y": 560, "svg": f"<g transform='translate(190 0)'>{earth(30)}</g>", "anim": {"spin": 55}}]},
    # 5. Minute eight: the sky goes black at the beach.
    {"start": "Then minute eight hits", "bg": "sky", "camera": "drift", "transition": "cut",
     "props": BEACH,
     "objects": [{"id": "night", "x": 0, "y": 0, "opacity": 0, "svg": NIGHT,
                  "keys": [{"at": "The sky goes black", "opacity": 1, "dur": 0.08}]},
                 {"id": "nsea", "x": 0, "y": 0, "opacity": 0, "front": True, "svg": NIGHT_SEA,
                  "keys": [{"at": "The sky goes black", "opacity": 1, "dur": 0.08}]},
                 {"id": "wave5", "x": 270, "y": 730, "svg": WAVE, "anim": {"drift": [-14, 0], "bob": 3, "period": 2.4}}],
     "actors": [{"id": "hero", "char": "hero", "x": 210, "y": 805, "scale": 1.25, "pose": "sit", "face": "happy", "look": 0.5,
                 "keys": [{"at": "The sky goes black", "pose": "reach_up", "face": "shocked", "dur": 0.12},
                          {"at": "in an instant+0.5", "pose": "stand", "face": "worried", "dur": 0.3}]}]},
    # 6. The Moon goes dark.
    {"start": "and the Moon vanishes", "bg": "earth_orbit", "camera": "closeup", "focus_y": 420, "zoom": 1.2, "transition": "none",
     "fx": [{"type": "stars", "n": 40, "speed": 0.4}],
     "objects": [{"id": "moonlit", "x": 270, "y": 420, "svg": moon(), "anim": {"bob": 6, "period": 3},
                  "keys": [{"at": "vanishes too+0.2", "opacity": 0, "dur": 0.6}]},
                 {"id": "moondark", "x": 270, "y": 420, "svg": moon(lit=False), "anim": {"bob": 6, "period": 3}}]},
    # 7. Earth flies off in a straight line.
    {"start": "Earth lets go", "bg": "space", "camera": "pan_left", "transition": "whip", "whip_dir": "left",
     "fx": [{"type": "speedlines", "dir": "left", "speed": 1.4}, "stars"],
     "objects": [{"id": "e7", "x": 150, "y": 560, "scale": 1.6, "svg": earth(46), "anim": {"spin": 20},
                  "keys": [{"at": "flies off", "x": 340, "dur": 4.0, "ease": "in"}]}]},
    # 8. Look up: Jupiter still shining.
    {"start": "But look up", "bg": "space", "camera": "push", "transition": "flash",
     "fx": [{"type": "rays", "x": 250, "y": 600, "spin": 5, "opacity": 0.1, "color": "#FFD8A8"}],
     "objects": [{"id": "jup", "x": 250, "y": 600, "scale": 0.85, "svg": jupiter(), "anim": {"pulse": 0.03, "period": 2.0},
                  "keys": [{"at": "glows for over an hour", "opacity": 0.35, "dur": 2.5}]}]},
    # 9. Day seven: frozen planet.
    {"start": "Day seven", "bg": "snow", "camera": "push", "transition": "cut",
     "fx": [{"type": "snow", "n": 110, "speed": 1.3}],
     "actors": [{"id": "hero", "char": "hero", "x": 230, "y": 805, "scale": 1.25, "pose": "tired", "face": "worried",
                 "keys": [{"at": "below freezing", "pose": "hug", "face": "shocked", "dur": 0.2}]}]},
    # 10. Under the ice, life keeps going.
    {"start": "But that ice works", "bg": "underwater", "camera": "tilt_down", "from_y": 360, "to_y": 620, "zoom": 1.25, "transition": "cut",
     "props": ICE, "fx": [{"type": "bubbles", "n": 30, "speed": 0.8}, {"type": "embers", "n": 18, "speed": 0.6, "color": "#FF8A4C"}],
     "objects": [{"id": "vent", "x": 290, "y": 822, "svg": VENT},
                 {"id": "worms", "x": 200, "y": 822, "svg": WORMS, "anim": {"sway": 6, "period": 2.2}},
                 {"id": "worms2", "x": 380, "y": 822, "svg": WORMS, "anim": {"sway": 7, "period": 1.8}},
                 {"id": "fish", "x": 120, "y": 640, "svg": FISH, "anim": {"drift": [22, 0], "bob": 6, "period": 1.6}}]},
    # 11. Sunlight on your face, right now.
    {"start": "And the sunlight on your face", "bg": "sky", "camera": "closeup", "focus": "hero", "zoom": 2.0, "focus_y": 700, "transition": "flash",
     "props": BEACH, "fx": [{"type": "rays", "x": 420, "y": 230, "spin": 8, "opacity": 0.16, "color": "#FFF3D0"}],
     "actors": [{"id": "hero", "char": "hero", "x": 200, "y": 805, "scale": 1.3, "pose": "sit", "face": "happy", "look": 0.6,
                 "keys": [{"at": "eight minutes ago", "face": "shocked", "dur": 0.15}]}]},
    # 12. Loop: the Sun again, flickering.
    {"start": "So it could already be gone", "bg": "void", "transition": "zoom",
     "fx": ["stars", {"type": "rays", "x": 270, "y": 560, "spin": 10, "opacity": 0.12, "color": "#FFD27A"}],
     "cam_start": {"zoom": 1.0, "cx": 270, "cy": 540},
     "cam": [{"at": "So it could", "zoom": 1.25, "cx": 270, "cy": 560, "dur": 4.0, "ease": "inout"}],
     "objects": [SUN_OBJ([], {"id": "sun2", "anim": {"pulse": 0.04, "period": 1.6, "spin": 6, "flicker": 0.25}})]},
]

hud = [
    {"type": "title", "at": 0.05, "until": "Here's the weird part", "small": "WHAT IF THE SUN", "text": "VANISHED?", "color": "#FFD27A", "top": 150},
    {"type": "title", "at": "eight minutes and twenty", "until": "Even gravity", "small": "SUNLIGHT'S TRIP TO EARTH", "text": "8 MIN 20 S", "color": "#FFD27A", "size": 72, "top": 150, "captions": True},
    {"type": "marker", "at": "Then minute eight", "until": "The sky goes black", "label": "MINUTE", "text": "8"},
    {"type": "title", "at": "borrowed sunlight", "until": "Earth lets go", "small": "MOONLIGHT IS JUST", "text": "BORROWED SUNLIGHT", "color": "#C9D2EE", "size": 50, "top": 150, "captions": True},
    {"type": "title", "at": "thirty kilometers", "until": "But look up", "small": "EARTH FLIES OFF AT", "text": "30 KM/S", "color": "#7FD1FF", "size": 76, "top": 150, "captions": True},
    {"type": "title", "at": "still shining", "until": "Day seven", "small": "JUPITER IS", "text": "STILL SHINING", "sub": "FOR OVER AN HOUR", "color": "#FFD8A8", "size": 58, "top": 150, "captions": True},
    {"type": "marker", "at": "Day seven", "until": "Earth's average", "label": "DAY", "text": "7"},
    {"type": "title", "at": "left the Sun", "until": "So it could", "small": "THE LIGHT ON YOUR FACE IS", "text": "8 MINUTES OLD", "color": "#FFD27A", "size": 64, "top": 150, "captions": True},
]

ep.update({
    "ep": 35,
    "voiceover": "voiceover.wav",
    "accent": "#FFD27A",
    "show_ep": False,
    "thumbnail": "The sky goes black+0.4",
    "highlights": {"eight minutes": "amber", "black": "amber", "thirty kilometers": "green", "over an hour": "green", "minute eight": "amber"},
    "music": [{"track": "music/lost-islands.mp3", "at": 0},
              {"track": "music/unknown.mp3", "at": "Then minute eight"},
              {"track": "music/remember.mp3", "at": "But that ice works"}],
    "music_db_below_voice": 20,
    "hud": hud,
    "shakes": [{"at": "The sky goes black", "amp": 16, "dur": 0.5}, {"at": "Earth lets go", "amp": 10, "dur": 0.4}],
    "flashes": [{"at": "Poof", "dur": 0.15, "color": "#FFE7A0"}, {"at": "The sky goes black", "dur": 0.1, "color": "#fff"}],
    "scenes": scenes,
})
(E / "episode.json").write_text(json.dumps(ep, indent=1))
print("scenes", len(scenes))
