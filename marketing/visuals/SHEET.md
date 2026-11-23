# Visual options (pick by number)

Contact sheet: `SHEET.png`. Built only from `brand/` files and the dealt tokens (`brand/tokens.css`, palette `blush-sage-slate`, Roboto + Roboto Mono as the Android system-font stand-ins (font change 2026-11-23)). HTML sources in `src/`, rendered to PNG with Playwright and Chrome. No AI image generation. Nothing posted.

| # | File | Size | Use | Ground | Logo tier |
|---|---|---|---|---|---|
| 1 | `01-feature-slate-lockup.png` | 1024 x 500 | Google Play feature graphic | Slate `#A6B3BC` | Glass lockup, 400 px wide |
| 2 | `02-feature-olive-knockout.png` | 1024 x 500 | Google Play feature graphic, or a cover image | Olive `#2C3620` | Flat knockout lockup |
| 3 | `03-feature-slate-rules.png` | 1024 x 500 | Google Play feature graphic showing the rule check | Slate | Flat primary lockup |
| 4 | `04-square-rules.png` | 1080 x 1080 | Instagram or Facebook post (launch or explainer C1) | Slate | Glass lockup, 300 px wide |

Notes:

- Options 3 and 4 name the providers in text, so each carries the "not affiliated" line. No provider logos anywhere.
- The rule card shows published rules only (7-day and 28-day limits; ReceiptJar "check in app"). No earnings figures, no mock totals.
- Option 2 holds the brand line; it is the one figure of speech for that piece.
- To re-render: `python src/render.py src` (Python Playwright + Chrome); it writes the PNGs here, and `00-sheet.png` is renamed to `SHEET.png`.
