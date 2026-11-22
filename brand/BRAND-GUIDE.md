# ReceiptRelay — Brand Guide

**Version R7, final, approved 2026-11-21.**
- Mark: option **20** (palette `blush-sage-slate`, hub dots).
- Wordmark: option **6** with border **2** ("Receipt" in satin ink; "Relay" in olive glass with a fine edge that darkens towards the top).
- Built under `.claude/rules/design-stack.md` (taste-skill + ui-ux-pro-max + website-standards). Rounds R0–R6 are in `explorations/`, and the reasons for each change are in `.claude/design-history/logo-agent-changelog.md`.
- Overview image: `brand-overview.png`.

## The mark

One central dot with three satellites at 90°, 210° and 330°: your receipt in the middle, relayed to each of the three providers around it.

There are two tiers, and they must match:

| Tier | Mark | Wordmark | Use for |
|---|---|---|---|
| **Glass expression** | Solid olive-glass core, frosted glass satellites, soft glow and shadow | "Receipt" in satin ink + "Relay" in olive glass, with an inverse-gradient edge on "Relay" | App icon, store listing, website header and hero, social, decks |
| **Flat master** | Solid dots, one colour | Flat Instrument Sans 500 | Favicon (≤32 px), print, monochrome, Android themed icon, legal, small UI |

Never mix the tiers: no glass mark with a flat wordmark, and no flat mark with the glass wordmark.

### Files

| File | Tier | Use |
|---|---|---|
| `logo-glass-lockup.svg` | glass | Lockup on a rounded slate panel |
| `logo-glass-lockup-white.svg` | glass | Lockup on white |
| `logo-glass-lockup-transparent.svg` | glass | Lockup over slate, sage or blush website grounds |
| `logo-glass-icon.svg` | glass | 512 rounded-tile icon (store, website) |
| `icon-512.svg` | glass | Square launcher source; the platform masks it (mark in a 60% safe zone) |
| `logo-social.svg` | glass | 400×400 avatar, 12% padding |
| `logo-primary.svg` | flat | Olive mark + ink wordmark, transparent background |
| `logo-full-colour.svg` / `logo-on-ground.svg` | flat | On white / on slate |
| `logo-knockout.svg` | flat | Pale `#E3E2DA` on olive |
| `logo-monochrome.svg` | flat | `#1A1A1A` |
| `logo-icon.svg` / `favicon.svg` | flat | Mark only |
| `icon-monochrome.svg` | flat | Android 13+ themed-icon source |
| `tokens.css` | — | Dealt `:root` tokens. Keep as printed. |

## Colour (dealt palette `blush-sage-slate`)

| Role | Hex | Token |
|---|---|---|
| Ground — slate blue-grey | `#A6B3BC` | `--p-bg` |
| Surface | `#B2BDC5` | `--p-surface` |
| Ink | `#1C1C1C` | `--p-ink` |
| Muted ink | `#38424A` | `--p-muted` |
| Accent / action — deep olive | `#2C3620` | `--p-accent`, `--p-action` |
| Text on olive | `#E3E2DA` | `--p-accent-ink` |
| Sage field | `#B7C8BE` | palette field |
| Blush field | `#D6C4B8` | palette field |
| Olive glass ramp | `#7A8C5E` → `#2C3620` → `#151A0F` | expression only |
| Olive edge (Relay) | `#B4C496` (bottom) → `#55663C` → `#0E120A` (top) | expression only |
| Ink satin (Receipt) | `#4A535A` → `#1C1C1C` → `#0B0C0D` | expression only |
| Glass tile | `#B8C3CA` → `#97A5AF` | expression only |

Contrast: ink on slate is about 8:1, and pale on olive about 9.8:1 (both AAA).

**Status colours are separate from the brand.** Approved, pending and rejected claims each use an icon plus a label. Olive never means "success", and the brand has no red.

## Type (dealt pairing `instrument`)

| Use | Face | Weight |
|---|---|---|
| Wordmark (outlined to paths) | Instrument Sans, width 96% | 600 in the glass tier, 500 in the flat tier; tracking −2.8% |
| Headings | Instrument Sans | 400–500 |
| Body | Instrument Sans | 400; 500 for buttons and labels |
| Amounts, dates, days left | DM Mono | 400 / 500 |

Use sentence case everywhere. The brand name is always "ReceiptRelay". Both faces are under the SIL Open Font License; the licence is in `fonts/`.

## Size and clear space

- Glass tier: lockup **≥ 240 px** wide, icon **≥ 48 px**.
- Flat tier: lockup ≥ 120 px wide, mark ≥ 16 px.
- Clear space: one satellite diameter on every side.

## Do

- Use the glass tier wherever the brand is the hero; use the flat tier everywhere small or single-colour.
- On the website, use the palette's flat fields: slate, sage and blush as soft blocks, one per chapter, with deep olive for the close.
- Use DM Mono for every number a shopper cares about.

## Don't

- Don't rotate the hub; the single satellite is always on top.
- Don't join the dots with lines (that makes it a share icon).
- Don't use the glass tier under 48 px, or on busy photographs.
- Don't stroke the outlined wordmark on top of its fill: the overlap contours show. The edge is always painted under the fill.
- Don't add red, orange or violet, or use olive to mean "success".
- Don't draw receipts, coins, dollar signs or carts into the brand.

## Recorded trade-offs

- Olive `#2C3620` is close in hue to RemAura's moss `#4A5240`. This was the user's pick (#20), and the brands still read differently: ReceiptRelay leads with slate, RemAura with moss and cream.
- The flat hub can read as a person glyph. The glass tier reduces this. Satellites always stay equal in size and smaller than the core.
