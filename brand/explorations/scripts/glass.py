"""Glass/radiant mockups of the ReceiptRelay dots mark. Usage: python -I glass.py <out_dir>"""
import sys, os, math
out = sys.argv[1]; os.makedirs(out, exist_ok=True)

CX, CY, BIG = 34.0, 60.0, 25.0
ARC, SMALL, ANG = 48.0, (10.5, 9.5, 8.5), (62, 22, -18)
dots = [(CX, CY, BIG)] + [(CX + ARC * math.cos(math.radians(a)), CY - ARC * math.sin(math.radians(a)), r) for a, r in zip(ANG, SMALL)]
minx = min(x - r for x, y, r in dots); maxx = max(x + r for x, y, r in dots)
miny = min(y - r for x, y, r in dots); maxy = max(y + r for x, y, r in dots)
dx, dy = 50 - (minx + maxx) / 2, 50 - (miny + maxy) / 2
dots = [(x + dx, y + dy, r) for x, y, r in dots]

DEFS = """<defs>
 <radialGradient id="ruby" cx="35%" cy="30%" r="75%">
  <stop offset="0" stop-color="#E0384A"/><stop offset="0.45" stop-color="#A3121E"/>
  <stop offset="0.85" stop-color="#5E0710"/><stop offset="1" stop-color="#3F040A"/></radialGradient>
 <radialGradient id="rubyGlow" cx="50%" cy="50%" r="50%">
  <stop offset="0" stop-color="#E0384A" stop-opacity="0.55"/><stop offset="1" stop-color="#E0384A" stop-opacity="0"/></radialGradient>
 <linearGradient id="spec" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.85"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
 <radialGradient id="caustic" cx="60%" cy="85%" r="45%">
  <stop offset="0" stop-color="#FF8A93" stop-opacity="0.7"/><stop offset="1" stop-color="#FF8A93" stop-opacity="0"/></radialGradient>
 <radialGradient id="frost" cx="35%" cy="30%" r="80%">
  <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.55"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.12"/></radialGradient>
 <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.95"/><stop offset="0.5" stop-color="#FFFFFF" stop-opacity="0.15"/>
  <stop offset="1" stop-color="#FFFFFF" stop-opacity="0.6"/></linearGradient>
 <linearGradient id="tileGrey" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#F4F4F4"/><stop offset="1" stop-color="#D2D2D2"/></linearGradient>
 <radialGradient id="tileOx" cx="30%" cy="20%" r="95%">
  <stop offset="0" stop-color="#B3141F"/><stop offset="0.55" stop-color="#7D0C14"/><stop offset="1" stop-color="#3F040A"/></radialGradient>
 <filter id="shadow" x="-30%" y="-30%" width="160%" height="170%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="2.2"/><feOffset dy="3"/>
  <feComponentTransfer><feFuncA type="linear" slope="0.35"/></feComponentTransfer>
  <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>
</defs>"""

def ruby_dot(x, y, r):
    return (f'<g filter="url(#shadow)"><circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="url(#ruby)"/>'
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="url(#caustic)"/>'
            f'<ellipse cx="{x - r*0.22:.2f}" cy="{y - r*0.45:.2f}" rx="{r*0.58:.2f}" ry="{r*0.34:.2f}" fill="url(#spec)"/>'
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r - 0.6:.2f}" fill="none" stroke="url(#rim)" stroke-width="1.1" opacity="0.55"/></g>')

def frost_dot(x, y, r):
    return (f'<g filter="url(#shadow)"><circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="url(#frost)"/>'
            f'<ellipse cx="{x - r*0.22:.2f}" cy="{y - r*0.45:.2f}" rx="{r*0.58:.2f}" ry="{r*0.32:.2f}" fill="url(#spec)" opacity="0.9"/>'
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r - 0.7:.2f}" fill="none" stroke="url(#rim)" stroke-width="1.4"/></g>')

def tile(fill, glow=True):
    g = f'<circle cx="38" cy="62" r="34" fill="url(#rubyGlow)" filter="url(#soft)"/>' if glow else ""
    return f'<rect x="-14" y="-14" width="128" height="128" rx="30" fill="{fill}"/>{g}'

def icon(variant):
    if variant == "ruby-on-grey":
        body = tile("url(#tileGrey)") + "".join(ruby_dot(*d) for d in dots)
    elif variant == "glass-on-oxblood":
        x, y, r = dots[0]
        body = tile("url(#tileOx)", glow=False) + ruby_dot(x, y, r) .replace("url(#ruby)", "url(#ruby)") + "".join(frost_dot(*d) for d in dots[1:])
        # big dot as frosted glass over a ruby core for depth
        body = tile("url(#tileOx)", glow=False) + f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r*0.62:.2f}" fill="#E0384A" opacity="0.55" filter="url(#soft)"/>' + frost_dot(x, y, r) + "".join(frost_dot(*d) for d in dots[1:])
    else:  # ruby-free (no tile) for lockups
        body = "".join(ruby_dot(*d) for d in dots)
    return body

def svg(vb, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{DEFS}{body}</svg>\n'

for v in ("ruby-on-grey", "glass-on-oxblood"):
    open(os.path.join(out, f"glass-{v}.svg"), "w").write(svg("-14 -14 128 128", icon(v)))
open(os.path.join(out, "glass-mark.svg"), "w").write(svg("0 0 100 100", icon("mark")))
print("ok")
