"""Palette x dot-arrangement matrix in the A+B mix glass style.
Usage: python -I glass_matrix.py <out_dir>"""
import sys, os, math
out = sys.argv[1]; os.makedirs(out, exist_ok=True)

# Palettes from taste-skill library (Gate S PASS, no red/violet/near-black ground)
PAL = {
 "cobalt-on-sand":   dict(tile=("#F0E8D8", "#D9CCB2"), hi="#5A7FE6", mid="#062B8A", lo="#021649", frost="#062B8A", ink="#062B8A"),
 "white-mint-tiles": dict(tile=("#FFFFFF", "#E9ECEA"), hi="#F2FFF8", mid="#A1FFCB", lo="#2FAE72", frost="#232323", ink="#232323"),
 "olive-on-bone":     dict(tile=("#F3F2EE", "#DEDCD5"), hi="#8FA34A", mid="#38450F", lo="#1C2307", frost="#38450F", ink="#38450F"),
 "orange-field-black": dict(tile=("#FF9147", "#F2660A"), hi="#56687A", mid="#050F16", lo="#000000", frost="#050F16", ink="#050F16"),
 "blush-sage-slate":  dict(tile=("#B8C3CA", "#97A5AF"), hi="#7A8C5E", mid="#2C3620", lo="#151A0F", frost="#1C1C1C", ink="#1C1C1C"),
 "poster-chapters":  dict(tile=("#EFEADF", "#D8D0BE"), hi="#7DEB98", mid="#18BC42", lo="#0A5E21", frost="#1A1A1A", ink="#1A1A1A"),
}

def arc(cx, cy, R, big, smalls, angs):
    return [(cx, cy, big)] + [(cx + R * math.cos(math.radians(a)), cy - R * math.sin(math.radians(a)), r) for a, r in zip(angs, smalls)]
ARR = {
 "D1 fan":     arc(34, 60, 48, 25, (10.5, 9.5, 8.5), (62, 22, -18)),
 "D2 overlap": arc(42, 56, 29, 27, (11.5, 10.5, 9.5), (72, 30, -12)),
 "D3 relay":   [(30, 66, 24), (59, 41, 11.5), (77, 26, 9), (90, 14, 7)],
 "D4 hub":     [(50, 50, 22)] + [(50 + 37 * math.cos(math.radians(a)), 50 - 37 * math.sin(math.radians(a)), 10.5) for a in (90, 210, 330)],
}
def centre(d):
    x0 = min(x - r for x, y, r in d); x1 = max(x + r for x, y, r in d)
    y0 = min(y - r for x, y, r in d); y1 = max(y + r for x, y, r in d)
    s = min(1.0, 92 / max(x1 - x0, y1 - y0))
    return [((x - (x0 + x1) / 2) * s + 50, (y - (y0 + y1) / 2) * s + 50, r * s) for x, y, r in d]

def defs(p, k):
    return f"""<defs>
<radialGradient id="core{k}" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="{p['hi']}"/><stop offset="0.5" stop-color="{p['mid']}"/><stop offset="1" stop-color="{p['lo']}"/></radialGradient>
<radialGradient id="glow{k}" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{p['mid']}" stop-opacity="0.45"/><stop offset="1" stop-color="{p['mid']}" stop-opacity="0"/></radialGradient>
<radialGradient id="frost{k}" cx="35%" cy="28%" r="80%"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.75"/><stop offset="0.55" stop-color="{p['frost']}" stop-opacity="0.28"/><stop offset="1" stop-color="{p['frost']}" stop-opacity="0.55"/></radialGradient>
<linearGradient id="spec{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.9"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
<linearGradient id="rim{k}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.95"/><stop offset="0.5" stop-color="#FFFFFF" stop-opacity="0.1"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.55"/></linearGradient>
<linearGradient id="tile{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p['tile'][0]}"/><stop offset="1" stop-color="{p['tile'][1]}"/></linearGradient>
<filter id="sh{k}" x="-40%" y="-40%" width="180%" height="190%"><feGaussianBlur in="SourceAlpha" stdDeviation="2.2"/><feOffset dy="3"/><feComponentTransfer><feFuncA type="linear" slope="0.3"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="blur{k}"><feGaussianBlur stdDeviation="6"/></filter>
</defs>"""

def solid(x, y, r, k):
    return (f'<g filter="url(#sh{k})"><circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="url(#core{k})"/>'
            f'<ellipse cx="{x-r*.22:.2f}" cy="{y-r*.45:.2f}" rx="{r*.58:.2f}" ry="{r*.34:.2f}" fill="url(#spec{k})"/>'
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r-.6:.2f}" fill="none" stroke="url(#rim{k})" stroke-width="1.1" opacity=".55"/></g>')
def frost(x, y, r, k):
    return (f'<g filter="url(#sh{k})"><circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="url(#frost{k})"/>'
            f'<ellipse cx="{x-r*.22:.2f}" cy="{y-r*.45:.2f}" rx="{r*.56:.2f}" ry="{r*.3:.2f}" fill="url(#spec{k})"/>'
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r-.7:.2f}" fill="none" stroke="url(#rim{k})" stroke-width="1.4"/></g>')

def icon(pn, an, k):
    p = PAL[pn]; d = centre(ARR[an]); (bx, by, br), rest = d[0], d[1:]
    body = (f'<rect x="-14" y="-14" width="128" height="128" rx="30" fill="url(#tile{k})"/>'
            f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{br*1.35:.1f}" fill="url(#glow{k})" filter="url(#blur{k})"/>'
            + solid(bx, by, br, k) + "".join(frost(x, y, r, k) for x, y, r in rest))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-14 -14 128 128">{defs(p, k)}{body}</svg>\n'


NOTE = {"cobalt-on-sand":"Recommended. Trust blue, warm sand.","white-mint-tiles":"Fresh, but low contrast.","olive-on-bone":"Close to RemAura moss.","orange-field-black":"Orange = red risk.","blush-sage-slate":"Muted, wedding/studio feel.","poster-chapters":"Money-green cliché."}
DOTN = {"D1 fan":"Fan","D2 overlap":"Overlap","D3 relay":"Relay trail","D4 hub":"Hub"}
html=['<html><body style="margin:0;padding:18px;background:#fafafa;font:14px system-ui">']
n=0;k=0
for pn in PAL:
    p=PAL[pn]
    sw="".join(f'<span style="display:inline-flex;align-items:center;margin-right:10px"><span style="width:22px;height:22px;background:{c};border:1px solid #0003;margin-right:4px;display:inline-block"></span>{c}</span>' for c in (p["tile"][0],p["mid"],p["ink"]))
    html.append(f'<div style="margin:6px 0 4px;font-weight:700;font-size:16px">{pn} <span style="font-weight:400;color:#555">— {NOTE[pn]}</span></div><div style="margin-bottom:6px;font-size:12px">{sw}</div><div style="display:flex;gap:14px;margin-bottom:14px">')
    for an in ARR:
        n+=1;k+=1;fn=f"n{n}.svg"
        open(os.path.join(out,fn),"w").write(icon(pn,an,k))
        html.append(f'<div style="text-align:center;background:#fff;border:1px solid #ddd;border-radius:12px;padding:8px 10px;width:150px"><div style="font:800 26px system-ui;color:#111">{n}</div><img src="{fn}" width="104"><div style="display:flex;justify-content:center;align-items:center;gap:6px"><img src="{fn}" width="32"><span style="font-size:12px;color:#444">{DOTN[an]}</span></div></div>')
    html.append('</div>')
html.append('</body></html>')
open(os.path.join(out,"sheet.html"),"w").write("".join(html)); print("ok",n)
