"""Dimensional wordmark options for ReceiptRelay (glass mark + treated text). Numbered sheet.
Usage: python -I wordmark_opts.py <InstrumentSans.ttf> <out_dir>"""
import sys, os, importlib.util
font_path, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
spec = importlib.util.spec_from_file_location("b3", os.path.join(os.path.dirname(__file__), "build_logo3.py"))
sys.argv = [sys.argv[0], font_path, os.path.join(out, "_tmp")]; b3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b3)
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

def words(weight, parts, size=60, x0=118, base=72, track=-0.028):
    f = instantiateVariableFont(TTFont(font_path), {"wght": weight, "wdth": 96}, inplace=False)
    gs, cmap, hm, upm = f.getGlyphSet(), f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm
    sc = size / upm; x = 0.0; res = []
    for text in parts:
        pen = SVGPathPen(gs)
        for ch in text:
            g = cmap[ord(ch)]; gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x0 + x * sc, base))); x += hm[g][0] + track * upm
        res.append(pen.getCommands())
    return res, x0 + x * sc

TXT_DEFS = """<defs>
<linearGradient id="tInk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4A535A"/><stop offset="0.55" stop-color="#1C1C1C"/><stop offset="1" stop-color="#0B0C0D"/></linearGradient>
<linearGradient id="tOlive" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8FA36A"/><stop offset="0.48" stop-color="#3B4A2A"/><stop offset="0.52" stop-color="#2C3620"/><stop offset="1" stop-color="#151A0F"/></linearGradient>
<linearGradient id="tFrost" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.95"/><stop offset="0.5" stop-color="#E9EEF1" stop-opacity="0.75"/><stop offset="1" stop-color="#8E9BA4" stop-opacity="0.85"/></linearGradient>
<linearGradient id="tChrome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.42" stop-color="#C9D2D8"/><stop offset="0.5" stop-color="#6E7B84"/><stop offset="0.62" stop-color="#AEB9C0"/><stop offset="1" stop-color="#E6EBEE"/></linearGradient>
<linearGradient id="tShine" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.6"/><stop offset="0.45" stop-color="#FFFFFF" stop-opacity="0.08"/><stop offset="0.46" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
<filter id="tDrop" x="-5%" y="-30%" width="110%" height="170%"><feGaussianBlur in="SourceAlpha" stdDeviation="1.6"/><feOffset dy="2.4"/><feComponentTransfer><feFuncA type="linear" slope="0.35"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="tPress" x="-5%" y="-30%" width="110%" height="170%">
 <feOffset in="SourceAlpha" dy="1.2" result="o1"/><feFlood flood-color="#FFFFFF" flood-opacity="0.55"/><feComposite in2="o1" operator="in" result="lite"/>
 <feOffset in="SourceAlpha" dy="-1" result="o2"/><feFlood flood-color="#000000" flood-opacity="0.35"/><feComposite in2="o2" operator="in" result="dark"/>
 <feMerge><feMergeNode in="lite"/><feMergeNode in="dark"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="tGlow" x="-10%" y="-40%" width="120%" height="180%"><feGaussianBlur in="SourceAlpha" stdDeviation="5"/><feOffset dy="4"/><feComponentTransfer><feFuncA type="linear" slope="0.28"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>"""

def text_layer(d, fill, filt=None, rim=None, shine=True):
    f = f' filter="url(#{filt})"' if filt else ""
    s = f'<g{f}><path d="{d}" fill="{fill}"/>'
    if shine: s += f'<path d="{d}" fill="url(#tShine)"/>'
    pass  # rim stroke removed: exposes variable-font overlap contours
    return s + "</g>"

OPTS = []
# 1 satin ink: gradient + shine + soft drop
(d,), w = words(560, ["ReceiptRelay"]); OPTS.append(("Satin ink", text_layer(d, "url(#tInk)", "tDrop"), w))
# 2 olive glass text
(d,), w = words(600, ["ReceiptRelay"]); OPTS.append(("Olive glass", text_layer(d, "url(#tOlive)", "tGlow", rim="#FFFFFF"), w))
# 3 two-tone: Receipt olive glass + Relay frosted glass (mirrors core + satellites)
(a, b), w = words(600, ["Receipt", "Relay"]); OPTS.append(("Olive + frosted (matches mark)", text_layer(a, "url(#tOlive)", "tGlow", rim="#FFFFFF") + text_layer(b, "url(#tFrost)", "tGlow", rim="#FFFFFF", shine=False), w))
# 4 letterpress on slate
(d,), w = words(600, ["ReceiptRelay"]); OPTS.append(("Letterpress", text_layer(d, "#2C3620", "tPress", shine=False), w))
# 5 frosted chrome
(d,), w = words(620, ["ReceiptRelay"]); OPTS.append(("Frosted chrome", text_layer(d, "url(#tChrome)", "tGlow", rim="#5C6870", shine=False), w))
# 6 two-tone: Receipt satin ink + Relay olive glass
(a, b), w = words(600, ["Receipt", "Relay"]); OPTS.append(("Ink + olive glass", text_layer(a, "url(#tInk)", "tDrop") + text_layer(b, "url(#tOlive)", "tGlow", rim="#FFFFFF"), w))

html = ['<html><body style="margin:0;padding:18px;background:#f4f4f2;font:14px system-ui">']
for i, (name, body, w) in enumerate(OPTS, 1):
    W = int(w + 28); H = 148
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">{b3.DEFS}{TXT_DEFS}'
           f'<rect width="{W}" height="{H}" rx="20" fill="url(#rrTile)"/>'
           f'<g transform="translate(14 24)">{b3.glass()}{body}</g></svg>\n')
    fn = f"w{i}.svg"; open(os.path.join(out, fn), "w").write(svg)
    svgw = svg.replace(f'<rect width="{W}" height="{H}" rx="20" fill="url(#rrTile)"/>', f'<rect width="{W}" height="{H}" rx="20" fill="#FFFFFF"/>')
    open(os.path.join(out, f"w{i}-white.svg"), "w").write(svgw)
    html.append(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:14px;background:#fff;border:1px solid #ddd;border-radius:14px;padding:10px 14px">'
                f'<div style="font:800 34px system-ui;width:44px;text-align:center">{i}</div>'
                f'<img src="{fn}" width="470"><img src="w{i}-white.svg" width="300"><div style="font-weight:600">{name}</div></div>')
html.append("</body></html>")
open(os.path.join(out, "sheet.html"), "w").write("".join(html)); print("ok", len(OPTS))
