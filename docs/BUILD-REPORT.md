# ReceiptRelay Website — Build Report (2026-11-21)

**GATE: PASS** (taste-skill `gate.mjs`, round 3 of 3), with 1 waiver.

## Waiver

| Check | Where | Reason |
|---|---|---|
| `cut-text` | `.dg-node--tile` captions in the #rules lanes diagram, at 390 (and 1024 in a quick run) | The diagram kit places each caption under its tile by design (`diagram.css .dg-cap { top: 100% + 10px }`). Every label reads whole in the crops. The phone frame was raised to 880px so nothing is clipped. |

## The deal (built as dealt)

- **Kind:** software (consumer fintech app). `data-type=software`, `site-kind=software`.
- **Palette:** `blush-sage-slate` (user pick #20). Slate ground, ink, olive action, with the surface ground on #claims.
- **Pairing:** `instrument` (Instrument Sans + DM Mono). Radius `round`. Buttons `pill`. Lit ground `sage`.
- **Hero:** `triptych`. Headline on the left, a UI collage (3 sets, crossfading every 2.8s) in the middle, the button on the right.
- **Nav, close, footer:** `nav-mega` · `close-type` · `footer-statement` · rhythm `space`.
- **Effect:** `fluted-glass` (dealt with `--slots band`) in the one `[data-visual]` frame (#rules), behind the lanes diagram.
- **Moments:** `word-highlight` (#how statement) and `line-carries-colour` (#claims, from base to surface).
- **Logo:** the client's own files (flat lockup in the nav and footer, glass icon in the hero and FAQ), per BRAND-GUIDE R7.

## Voice card

Technical-dry: exact and plain. "You" is for what the shopper gets, and the product is the subject of each feature line. No humour in the hero or FAQ. House words: receipt, app, claim, rules.

## Checks

| Check | Result |
|---|---|
| copy-lint | 0 FAIL. 1 WARN fixed ("within N days" read as a response promise, reworded to "N-day limit"). 1 contrast frame and 1 negation run kept, both within budget. |
| layout `check.mjs` (1440, 1024, 820, 768, 390) | No findings after the phone action bar was added. |
| consistency (full run, then quick runs) | 0 open FAIL besides the waived diagram captions. WARNs kept: fragment rows cut under their fades (by design), section gaps at the tablet, nav-label length. |
| gate | PASS |
| perf | Not run separately. The gate's checker covered image weight, and the page has no photographs. |

## Fixes made during checks

- **Text contrast:** body text moved from grey to ink (#app paragraph, #claims card text) to reach 7:1.
- **Headings:** #claims h2 now names the thing ("Claim tracker for every receipt"); a card title was reworded.
- **Visuals:** the FAQ got the glass app icon (it was the last text-only section); a hidden collage set's icon was replaced with a rules card.
- **Diagram icons:** resolved with `icons.mjs scan` (ui:receipt, ui:search, ui:file-text, ui:globe).
- **Tablet:** #claims cards take the full row there (this fixed the "hole").
- **Phone:** action bar added (nav overflow fixed); the wide close button's padding reduced (overflow at 320); the rules frame is 880px tall and the section is two screens (`--hm: 2`); the legal links were moved into the company block (off-grid).

## Assumed facts and stand-ins

- **UI mock data** (stores, dates, totals, days left, "$38 from 11 claims") is illustrative content inside the drawn app frames. It is not presented as a statistic.
- **Contact:** `mailto:hello@receiptrelay.example` is a stand-in. The client must supply a real address.
- **Domain:** not set. `site.config.json` has `siteUrl: http://localhost:4173`. Until it holds a real domain, the build omits the canonical link and og:url, and `robots.txt` disallows crawling.
- **Download:** links to `download.html`, which links to GitHub Releases on this repo. No release exists yet.
- **Photographs:** none used. One live-search candidate was rejected (it showed faces and readable third-party brands).

## Still to do

- Set the real domain in `site.config.json` and rebuild.
- Publish the first APK release (GitHub Releases) with its SHA-256 checksum.
- Replace the `.example` email.
- Confirm ReceiptJar's in-app rules. The site currently says "rules shown in its app".
- Run code-reviewer, compliance-reviewer (ads disclosure, privacy wording) and the qa-agent pass before any public deploy.
