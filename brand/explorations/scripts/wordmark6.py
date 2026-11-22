"""Option 6 refinement: inverse-gradient border (light bottom -> dark top), painted under the fill.
Usage: python -I wordmark6.py <font.ttf> <out_dir>"""
import sys, os, importlib.util
fp, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("wo", os.path.join(here, "wordmark_opts.py"))
sys.argv = [sys.argv[0], fp, os.path.join(out, "_wo")]; wo = importlib.util.module_from_spec(spec); spec.loader.exec_module(wo)
b3 = wo.b3
EDGE = """<defs>
<linearGradient id="eInk" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#9AA5AC"/><stop offset="0.5" stop-color="#4A535A"/><stop offset="1" stop-color="#050506"/></linearGradient>
<linearGradient id="eOlive" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#B4C496"/><stop offset="0.5" stop-color="#55663C"/><stop offset="1" stop-color="#0E120A"/></linearGradient>
</defs>"""
def layer(d, fill, edge, w, filt):
    s = f'<g filter="url(#{filt})">'
    if w: s += f'<path d="{d}" fill="none" stroke="url(#{edge})" stroke-width="{w*2}" stroke-linejoin="round"/>'
    return s + f'<path d="{d}" fill="{fill}"/><path d="{d}" fill="url(#tShine)"/></g>'
(a, b), W0 = wo.words(600, ["Receipt", "Relay"])
VARS = [("Current 6 (no border)", 0, 0), ("Border on Relay only — fine", 0, 0.7), ("Border on both — fine", 0.7, 0.7),
        ("Border on both — medium", 1.1, 1.1), ("Border on both — strong", 1.6, 1.6)]
html = ['<html><body style="margin:0;padding:18px;background:#f4f4f2;font:14px system-ui">']
for i, (name, wa, wb) in enumerate(VARS, 1):
    body = layer(a, "url(#tInk)", "eInk", wa, "tDrop") + layer(b, "url(#tOlive)", "eOlive", wb, "tGlow")
    W = int(W0 + 30); H = 148
    for bg, suf in (("url(#rrTile)", ""), ("#FFFFFF", "-white")):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">{b3.DEFS}{wo.TXT_DEFS}{EDGE}'
               f'<rect width="{W}" height="{H}" rx="20" fill="{bg}"/><g transform="translate(14 24)">{b3.glass()}{body}</g></svg>\n')
        open(os.path.join(out, f"e{i}{suf}.svg"), "w").write(svg)
    html.append(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:14px;background:#fff;border:1px solid #ddd;border-radius:14px;padding:10px 14px">'
                f'<div style="font:800 34px system-ui;width:44px;text-align:center">{i}</div><img src="e{i}.svg" width="520"><img src="e{i}-white.svg" width="330"><div style="font-weight:600;width:150px">{name}</div></div>')
# zoom strip of option 4 for detail
html.append('<div style="background:#fff;border:1px solid #ddd;border-radius:14px;padding:10px 14px"><b>Zoom of 4 (edge detail)</b><br><div style="width:1000px;height:230px;overflow:hidden"><img src="e4.svg" style="width:2000px;margin-left:-640px;margin-top:-60px"></div></div>')
open(os.path.join(out, "sheet.html"), "w").write("".join(html) + "</body></html>"); print("ok")
