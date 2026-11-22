"""ReceiptRelay logo v2 (taste deal: oxblood-grey + Instrument Sans, mark: dots).
Usage: python -I build_logo2.py <InstrumentSans.ttf> <out_dir> <concept:A|B|C>"""
import sys, os, math
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

font_path, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
OX, GROUND, INK, WHITE = "#7D0C14", "#E2E2E2", "#1A1A1A", "#FFFFFF"

# --- mark: one large dot + three smaller dots fanned on an arc (one scan -> three providers)
CX, CY, BIG = 34.0, 60.0, 25.0
ARC, SMALL = 48.0, (10.5, 9.5, 8.5)
ANG = (62, 22, -18)  # degrees, y up
dots = [(CX, CY, BIG)] + [(CX + ARC * math.cos(math.radians(a)), CY - ARC * math.sin(math.radians(a)), r)
                          for a, r in zip(ANG, SMALL)]
minx = min(x - r for x, y, r in dots); maxx = max(x + r for x, y, r in dots)
miny = min(y - r for x, y, r in dots); maxy = max(y + r for x, y, r in dots)
dx, dy = 50 - (minx + maxx) / 2, 50 - (miny + maxy) / 2
dots = [(x + dx, y + dy, r) for x, y, r in dots]

def mark(fill, accent=None):
    return "".join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{(accent if (accent and i) else fill)}"/>'
                   for i, (x, y, r) in enumerate(dots))

font = instantiateVariableFont(TTFont(font_path), {"wght": 500, "wdth": 96}, inplace=False)
gs, cmap, hmtx, upm = font.getGlyphSet(), font.getBestCmap(), font["hmtx"], font["head"].unitsPerEm

def word(text, size, x0, base, track=-0.028):
    s = size / upm; pen = SVGPathPen(gs); x = 0.0
    for ch in text:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x0 + x * s, base)))
        x += hmtx[g][0] + track * upm
    return pen.getCommands(), x * s

WD, WW = word("ReceiptRelay", 58, 114, 70)
LW = int(114 + WW + 4)

def svg(w, h, body, bg=None):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="ReceiptRelay">'
            f"<title>ReceiptRelay</title>{b}{body}</svg>\n")

def lockup(fill, text, bg=None, pad=0):
    t = f' transform="translate({pad} {pad})"' if pad else ""
    return svg(LW + 2 * pad, 100 + 2 * pad, f'<g{t}>{mark(fill)}<path d="{WD}" fill="{text}"/></g>', bg)

def square(size, frac, fill, bg):
    sc = size * frac / 100; off = (size - size * frac) / 2
    return svg(size, size, f'<g transform="translate({off:.1f} {off:.1f}) scale({sc:.3f})">{mark(fill)}</g>', bg)

files = {
    "logo-primary.svg": lockup(OX, OX),
    "logo-full-colour.svg": lockup(OX, OX, bg=WHITE, pad=24),
    "logo-on-ground.svg": lockup(OX, OX, bg=GROUND, pad=24),
    "logo-knockout.svg": lockup(GROUND, GROUND, bg=OX, pad=24),
    "logo-monochrome.svg": lockup(INK, INK),
    "logo-icon.svg": svg(100, 100, mark(OX)),
    "logo-social.svg": square(400, 0.76, GROUND, OX),   # 12% padding each side
    "icon-512.svg": square(512, 0.60, GROUND, OX),      # launcher icon (platform mask safe zone)
}
for n, d in files.items():
    open(os.path.join(out, n), "w", encoding="utf-8").write(d)
print("dots:", [(round(x, 1), round(y, 1), r) for x, y, r in dots], "lockup", LW)
