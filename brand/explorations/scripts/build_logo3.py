"""ReceiptRelay final logo (option 20: blush-sage-slate + hub dots). Flat master + glass expression.
Usage: python -I build_logo3.py <InstrumentSans.ttf> <out_dir>"""
import sys, os, math
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

font_path, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
SLATE, SLATE_HI, SLATE_LO = "#A6B3BC", "#B8C3CA", "#97A5AF"
OLIVE, OLIVE_HI, OLIVE_LO = "#2C3620", "#7A8C5E", "#151A0F"
INK, PALE, MONO, WHITE = "#1C1C1C", "#E3E2DA", "#1A1A1A", "#FFFFFF"

# hub: centre dot + 3 dots at 90/210/330 deg, fitted to 92-unit box centred in 100
raw = [(50, 50, 22)] + [(50 + 37 * math.cos(math.radians(a)), 50 - 37 * math.sin(math.radians(a)), 10.5) for a in (90, 210, 330)]
x0 = min(x - r for x, y, r in raw); x1 = max(x + r for x, y, r in raw)
y0 = min(y - r for x, y, r in raw); y1 = max(y + r for x, y, r in raw)
s = 92 / max(x1 - x0, y1 - y0)
DOTS = [((x - (x0 + x1) / 2) * s + 50, (y - (y0 + y1) / 2) * s + 50, r * s) for x, y, r in raw]

def flat(fill):
    return "".join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}"/>' for x, y, r in DOTS)

DEFS = f"""<defs>
<radialGradient id="rrCore" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="{OLIVE_HI}"/><stop offset="0.5" stop-color="{OLIVE}"/><stop offset="1" stop-color="{OLIVE_LO}"/></radialGradient>
<radialGradient id="rrGlow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{OLIVE}" stop-opacity="0.45"/><stop offset="1" stop-color="{OLIVE}" stop-opacity="0"/></radialGradient>
<radialGradient id="rrFrost" cx="35%" cy="28%" r="80%"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.75"/><stop offset="0.55" stop-color="{INK}" stop-opacity="0.28"/><stop offset="1" stop-color="{INK}" stop-opacity="0.55"/></radialGradient>
<linearGradient id="rrSpec" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.9"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
<linearGradient id="rrRim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.95"/><stop offset="0.5" stop-color="#FFFFFF" stop-opacity="0.1"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.55"/></linearGradient>
<linearGradient id="rrTile" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SLATE_HI}"/><stop offset="1" stop-color="{SLATE_LO}"/></linearGradient>
<filter id="rrSh" x="-40%" y="-40%" width="180%" height="190%"><feGaussianBlur in="SourceAlpha" stdDeviation="2.2"/><feOffset dy="3"/><feComponentTransfer><feFuncA type="linear" slope="0.3"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="rrBlur"><feGaussianBlur stdDeviation="6"/></filter>
</defs>"""

def glass():
    (bx, by, br), rest = DOTS[0], DOTS[1:]
    g = f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{br*1.35:.1f}" fill="url(#rrGlow)" filter="url(#rrBlur)"/>'
    g += (f'<g filter="url(#rrSh)"><circle cx="{bx:.2f}" cy="{by:.2f}" r="{br:.2f}" fill="url(#rrCore)"/>'
          f'<ellipse cx="{bx-br*.22:.2f}" cy="{by-br*.45:.2f}" rx="{br*.58:.2f}" ry="{br*.34:.2f}" fill="url(#rrSpec)"/>'
          f'<circle cx="{bx:.2f}" cy="{by:.2f}" r="{br-.6:.2f}" fill="none" stroke="url(#rrRim)" stroke-width="1.1" opacity=".55"/></g>')
    for x, y, r in rest:
        g += (f'<g filter="url(#rrSh)"><circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="url(#rrFrost)"/>'
              f'<ellipse cx="{x-r*.22:.2f}" cy="{y-r*.45:.2f}" rx="{r*.56:.2f}" ry="{r*.3:.2f}" fill="url(#rrSpec)"/>'
              f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r-.7:.2f}" fill="none" stroke="url(#rrRim)" stroke-width="1.4"/></g>')
    return g

font = instantiateVariableFont(TTFont(font_path), {"wght": 500, "wdth": 96}, inplace=False)
gs, cmap, hmtx, upm = font.getGlyphSet(), font.getBestCmap(), font["hmtx"], font["head"].unitsPerEm
def word(text, size, x0, base, track=-0.028):
    sc = size / upm; pen = SVGPathPen(gs); x = 0.0
    for ch in text:
        gname = cmap[ord(ch)]
        gs[gname].draw(TransformPen(pen, (sc, 0, 0, -sc, x0 + x * sc, base)))
        x += hmtx[gname][0] + track * upm
    return pen.getCommands(), x * sc
WD, WW = word("ReceiptRelay", 58, 116, 70)
LW = int(116 + WW + 4)

def svg(vb, body, defs=False, title="ReceiptRelay"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{title}"><title>{title}</title>'
            f'{DEFS if defs else ""}{body}</svg>\n')
def lockup(mark, text, bg=None, pad=0, defs=False):
    w, h = LW + 2 * pad, 100 + 2 * pad
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return svg(f"0 0 {w} {h}", f'{b}<g transform="translate({pad} {pad})">{mark}<path d="{WD}" fill="{text}"/></g>', defs)
def square(size, frac, mark, bg_fill, defs=False, rx=0):
    sc = size * frac / 100; off = (size - size * frac) / 2
    return svg(f"0 0 {size} {size}", f'<rect width="{size}" height="{size}" rx="{rx}" fill="{bg_fill}"/>'
               f'<g transform="translate({off:.1f} {off:.1f}) scale({sc:.3f})">{mark}</g>', defs)

files = {
    # flat master system
    "logo-primary.svg": lockup(flat(OLIVE), INK),
    "logo-full-colour.svg": lockup(flat(OLIVE), INK, bg=WHITE, pad=24),
    "logo-on-ground.svg": lockup(flat(OLIVE), INK, bg=SLATE, pad=24),
    "logo-knockout.svg": lockup(flat(PALE), PALE, bg=OLIVE, pad=24),
    "logo-monochrome.svg": lockup(flat(MONO), MONO),
    "logo-icon.svg": svg("0 0 100 100", flat(OLIVE)),
    "favicon.svg": svg("0 0 100 100", flat(OLIVE)),
    "icon-monochrome.svg": svg("0 0 100 100", flat(MONO)),          # Android 13+ themed icon source
    # glass expression
    "logo-glass-lockup.svg": lockup(glass(), INK, bg=SLATE, pad=24, defs=True),
    "logo-glass-icon.svg": square(512, 0.66, glass(), "url(#rrTile)", defs=True, rx=112),
    "icon-512.svg": square(512, 0.60, glass(), "url(#rrTile)", defs=True),        # launcher (platform masks it)
    "logo-social.svg": square(400, 0.76, glass(), "url(#rrTile)", defs=True),     # 12% padding
}
for n, d in files.items():
    open(os.path.join(out, n), "w", encoding="utf-8").write(d)
print("dots", [(round(x, 1), round(y, 1), round(r, 1)) for x, y, r in DOTS], "lockup", LW)
