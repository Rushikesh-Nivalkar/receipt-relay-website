"""ReceiptRelay FINAL brand files (R7): flat master (build_logo3) + glass expression with wordmark 6/2
(Receipt = satin ink, Relay = olive glass + fine inverse-gradient border). Usage: python -I build_final.py <font.ttf> <brand_dir>"""
import sys, os, importlib.util
fp, out = sys.argv[1], sys.argv[2]; here = os.path.dirname(__file__)
def load(name, argv):
    spec = importlib.util.spec_from_file_location(name, os.path.join(here, name + ".py")); sys.argv = argv
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
b3 = load("build_logo3", ["x", fp, out])                       # writes flat master + glass icons into brand dir
w6 = load("wordmark6", ["x", fp, os.path.join(here, "..", "wm6tmp")])
wo = w6.wo
(a, b), W0 = wo.words(600, ["Receipt", "Relay"])
body = w6.layer(a, "url(#tInk)", "eInk", 0, "tDrop") + w6.layer(b, "url(#tOlive)", "eOlive", 0.7, "tGlow")
W = int(W0 + 30); H = 148
def lock(bg, rx):
    rect = f'<rect width="{W}" height="{H}" rx="{rx}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="ReceiptRelay"><title>ReceiptRelay</title>'
            f'{b3.DEFS}{wo.TXT_DEFS}{w6.EDGE}{rect}<g transform="translate(14 24)">{b3.glass()}{body}</g></svg>\n')
for name, bg, rx in (("logo-glass-lockup.svg", "url(#rrTile)", 20), ("logo-glass-lockup-white.svg", "#FFFFFF", 0), ("logo-glass-lockup-transparent.svg", None, 0)):
    open(os.path.join(out, name), "w", encoding="utf-8").write(lock(bg, rx))
print("final ok", W, H)
