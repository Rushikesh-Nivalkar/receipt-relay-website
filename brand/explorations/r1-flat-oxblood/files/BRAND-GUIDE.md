# ReceiptRelay — Brand Guide

Built 2026-11-21 under `.claude/rules/design-stack.md` (taste-skill + ui-ux-pro-max + website-standards). Nothing below was hand-picked: the palette, type pairing and mark type came from the taste-skill dealer, using the studio-wide history, and cleared Gate S against every earlier studio brand.

## The mark

One large dot with three smaller dots fanned out on an arc. One receipt, scanned once, is relayed to each provider. The dots sit on an arc, never in a straight row, so the mark can't be read as a "more" menu.

| File | Use |
|---|---|
| `logo-primary.svg` | Main lockup, transparent background |
| `logo-full-colour.svg` | Oxblood on white, with padding |
| `logo-on-ground.svg` | Oxblood on the brand grey ground |
| `logo-knockout.svg` | Grey on oxblood |
| `logo-monochrome.svg` | Single colour, #1A1A1A |
| `logo-icon.svg` | Mark only (favicon, in-app) |
| `logo-social.svg` | 400×400 profile image, grey mark on oxblood, 12% padding |
| `icon-512.svg` | Android launcher source, mark inside a 60% safe zone |
| `tokens.css` | Dealt `:root` design tokens. Keep as printed. |

## Colour (dealt palette `oxblood-grey`)

| Role | Hex | Token |
|---|---|---|
| Primary — oxblood (ink, accent, action) | `#7D0C14` | `--p-ink`, `--p-accent`, `--p-action` |
| Secondary — grey ground | `#E2E2E2` | `--p-bg` |
| Surface | `#D6D6D6` | `--p-surface` |
| Muted text | `#7A4A4E` | `--p-muted` |
| Inverted surface (on oxblood) | `#862323` | `--p-inv-surface` |
| Inverted muted | `#D0B3AF` | `--p-inv-muted` |
| Monochrome | `#1A1A1A` | — |

Accent: this is a two-tone palette, so the accent is oxblood itself. Emphasis comes from inverting (oxblood ground, grey type), never from adding a third hue.

Contrast: oxblood on `#E2E2E2` is about 8.4:1, and on white about 10.9:1 (both WCAG AAA).

Gate S (2026-11-21): accent `#7D0C14`. Closest prior or banned colour is `#FF6B35`, 20° hue apart but 34 lightness points apart, so no clash. **PASS.**

## Type (dealt pairing `instrument`)

| Use | Face | Weight |
|---|---|---|
| Wordmark (outlined to paths) | Instrument Sans, width 96% | 500, tracking −2.8% |
| Display / headings | Instrument Sans | 400–500, tracking −2.8% (−3.6% at hero size) |
| Text | Instrument Sans | 400; 500 for buttons and labels |
| Figures, receipt data, deadlines | DM Mono | 400 / 500 |

Use sentence case everywhere except the brand name, which is always written "ReceiptRelay". Both faces are under the SIL Open Font License; the licence is in `fonts/`.

## Size and clear space

- Minimum lockup width: **120 px** on screen, **30 mm** in print.
- Minimum mark size: **16 px**. The small dots are designed to read at **32 px** and above.
- Clear space: on every side, at least the diameter of the smallest dot × 2. In lockup units that is 17, about 17% of the mark's height.

## Do

- Use oxblood on the grey ground or on white. Use grey on oxblood for inverted panels.
- Keep the arc of three dots to the upper right of the large dot.
- Use DM Mono for amounts, dates and deadline counters in the app and on the site.
- Use the mark alone for the app icon, favicon and social avatar.

## Don't

- Don't line the three dots up in a row or column (it would read as a menu icon).
- Don't recolour the dots individually, add gradients, outlines or shadows, or add a third brand colour.
- Don't use violet or lavender anywhere (taste-skill rule).
- Don't re-type the wordmark in a live font. Use the outlined SVG.
- Don't place the mark on photographs without an oxblood or grey panel behind it.
- Don't draw receipts, zigzag paper edges, coins, dollar signs or shopping carts into the brand. These are category clichés and were rejected at Gate A.
