# ReceiptRelay Website — Build Plan (from the approved logo)

For: ui-agent (builder), marketing-agent (copy), sales-agent (download objections), qa-agent (gate), devops-agent (deploy).
Source of truth: `.claude/rules/design-stack.md`, `brand/BRAND-GUIDE.md` (R7), `ideaOutput.md`.
Status: **PLAN — not built.** Dealt 2026-11-21. Deals are recorded in `.taste-skill/` and `.claude/design-history/history.json`; do not re-deal.

---

## 1. Skills each agent must invoke (in order, strict)

| Agent | Step | Skills (read the SKILL.md files and the references they name) |
|---|---|---|
| marketing-agent | Copy first (taste §4 step 2) | claude-mem → caveman → model-router → **design-stack.md** → **design-taste-frontend** (`copy.md`, `copy-voice.md`, `copy-registers.md`, `copy-moves.md`) → **ui-ux-pro-max** → **website-standards** → marketing-corey-haines → claude-seo |
| ui-agent | Plan, build, check | claude-mem → caveman → model-router → **design-stack.md** → **design-taste-frontend** (`layout-v4.md`, `sections.md`, `sections-library.md`, `system.md`, `cards.md`, `motion.md`, `moments.md`, `photos.md`, `icons.md`, `diagrams.md`, `perf.md`) → **ui-ux-pro-max** (UX/a11y data) → **website-standards** → vercel-v0-sdk → claude-seo |
| sales-agent | Download page objections, FAQ facts | claude-mem → caveman → model-router → **design-stack.md** → **design-taste-frontend** (`copy.md`) → **ui-ux-pro-max** → **website-standards** → ai-sales-team |
| qa-agent | Finish gate | claude-mem → caveman → model-router → **design-stack.md** → **design-taste-frontend** (`gate.md`) → **ui-ux-pro-max** → **website-standards** → browser-use |
| devops-agent | Deploy (static export) | its own list + github-actions-skill. Releases: APK as GitHub Releases on this repo. |

If any of the three bold skills is not read, the step has not started. The completion report lists all three.

## 2. The deal (fixed — build exactly this)

- **Plan line 1 — kind:** `software` (consumer fintech app). Meta: `data-type="software"`, `page-type=software`, `site-kind=software`.
- **Plan line 2 — deal:**
  - **Palette:** `blush-sage-slate`. Its slate, sage and blush soft fields and one deep-olive close mirror the logo's frosted satellites around an olive core. The calm, unhurried grounds suit a money tool that needs to read as trustworthy rather than loud.
  - **Pairing:** `instrument` (Instrument Sans + DM Mono). Radius: `round` (consumer app).
  - **Hero:** `triptych` (dealt; `--has ui,photo`). Headline on the left, collage in the middle (sets crossfade every 2.8 s with a pause disc), one large button on the right line.
  - **Moments (2):** `word-highlight` (statement) and `line-carries-colour` (section transition).
  - **Nav:** `nav-mega` · **Footer:** `footer-statement` · **Close:** `close-type` · **Rhythm:** `space` · **Buttons:** `pill`.
  - **Effect (tech allows one):** none dealt yet. If wanted, deal it per `effects-usage.md`. Do not hand-pick a glass shader; the glass belongs to the logo.
- **Tokens:** `brand/tokens.css`, the `:root` block exactly as printed.
- **Head font link:** see `brand/tokens.css` source (Google Fonts: Instrument Sans wdth,wght 75..100,400..700 + DM Mono 400;500).

## 3. Logo use on the site

| Place | Asset | Why |
|---|---|---|
| Nav (about 140–180 px wide) | `logo-primary.svg` (flat) | Under 240 px, the glass tier rule applies (flat only) |
| Hero collage, set 1 | Phone frame showing the app with `logo-glass-icon.svg` as the launcher icon | The glass expression is the hero material |
| Close (olive block) | `logo-knockout.svg` mark only, large, beside the close type | Pale on olive |
| Favicon | `favicon.svg` + 32 px PNG | Flat tier |
| `og:image` / share | `logo-social.svg` rendered to `share.jpg` via `shoot.mjs` | Glass tier |
| Download page | `logo-glass-lockup-transparent.svg` over the sage field | Glass tier at ≥ 240 px |

## 4. Screens (one section per screen, taste house rules)

Each section's `--h` is 1 or 2. Ground order follows the palette note: soft fields, one per chapter, with olive for the close.

| # | id | Ground | One idea | Picture (kind) | Screens | Moment |
|---|---|---|---|---|---|---|
| 1 | hero | slate `#A6B3BC` | Receipt rewards app for Australian shoppers: scan once, claim with each provider | Triptych collage: (a) phone with the scan screen and glass icon, (b) eligibility card with three provider rows, (c) a licensed photo of a hand holding a supermarket receipt (`photos.mjs`), (d) a claim tracker card (UI) | 1 | Hero entrance (`data-enter`); collage loop |
| 2 | statement | sage `#B7C8BE` | "Scan once. See where it counts. Claim it yourself." | Type | 1 | **word-highlight** |
| 3 | eligibility | slate | Deterministic rules: age, caps, retailers. Every "no" comes with its reason | `app-frame`: live HTML eligibility screen (Shping 7 days · ShopBack 28 days · ReceiptJar 14 days, DM Mono, a reason line on the failed one) + diagram card "one input → three lanes" (`diagrams.md` hub preset, mirrors the logo) | 2 | — |
| 4 | tracking | blush `#D6C4B8` | Every claim tracked until it pays; reminders before deadlines | UI cards: status list (Submitted → Pending → Paid), a "days left" counter in DM Mono, card loop 2.5–4 s | 1 | **line-carries-colour** (enters the blush ground) |
| 5 | money | sage | How ReceiptRelay makes money: one ad after you submit, an optional "support us" ad, never your receipts | Type + one still UI card showing the ad slot labelled "Ad" | 1 | — |
| 6 | privacy | slate | Receipts stay on your phone, encrypted; no provider passwords, ever | A context photo (`photos.mjs`, a phone on a kitchen bench) + a short list | 1 | — |
| 7 | close | olive `#2C3620` | Large type: "One receipt. Every claim." + pill "Download for Android" | Knockout mark | 1 | — |
| — | footer | `footer-statement` | Legal line, privacy, "not affiliated with Shping, ShopBack or ReceiptJar", photo credits line | — | — | — |

The main action is **Download for Android**. It links to `https://github.com/Rushikesh-Nivalkar/receipt-relay-website/releases/latest` (the APK is published there). Until the first release exists, the button goes to a `/download` page that says when it ships. No dead links (the gate checks).

## 5. Copy fact sheet (only these facts; nothing invented)

- Australia only. Android only (iOS later).
- MVP providers: Shping, ShopBack, ReceiptJar. The app checks each provider's published rules:
  - Shping: 7 days; 2 per retailer per day; 5 per retailer per 7 days; 100 per month.
  - ShopBack: 28 days; one receipt per transaction.
  - ReceiptJar: 14 days (to confirm from the in-app terms before publishing; else omit the number).
- Guided upload: ReceiptRelay hands your receipt to each provider's own app. It never logs in for you, never automates provider apps, and never stores provider passwords.
- No AI. The rules are fixed and explainable.
- Free. Funded by one ad after a submission plus an optional rewarded "support us" ad. No banners or pop-ups. Receipts are never sold, shared or shown to ad networks.
- Security: data on the device, encrypted at rest; TLS in transit. **Never write "ISO 27001 certified" or "SOC 2 certified".** Write "built to align with" only if marketing wants it.
- Not affiliated with any provider.
- Copy rules: `copy.md`. The h1 names the category and the buyer. One hard fact on screen one. A noun in every heading. Buttons are a verb plus an object. Run `copy-lint.mjs` on the draft `.md` before building.

## 6. Open decisions (ask the user before building)

1. **Provider logos.** taste rule 7 wants real icons, but showing Shping, ShopBack and ReceiptJar logos can imply partnership. Default: names in text only, plus the "not affiliated" footer line, until written permission exists.
2. **Domain.** Canonical domain is TBD (it goes in `og:url` and `canonical`). Use the GitHub Pages or Vercel URL until then.
3. **Effect.** Deal one tech effect, or none? Default: none. The glass in the logo is the visual signature.

## 7. Build and check sequence (ui-agent)

Run every command from `projects/receipt-relay-website/`. `T = .claude/skills/design-taste-frontend` (an absolute path to master-root).

1. **Stack.**
   - Next.js `output: 'export'` per website-standards, with the taste kit copied to `public/assets` (taste §4 step 0).
   - Build and launch a copy at `D:\dev\receipt-relay-website`: robocopy NAS → D:\dev, because UNC paths can't run npm `.bin` scripts.
2. **Arm the gate** (taste §4 step 1):
   `node T/scripts/gate.mjs --start out/index.html --root out --kind software --category "receipt rewards app" --primary "Download for Android"`
3. **Copy draft** → `docs/copy.md` → `node T/scripts/copy-lint.mjs docs/copy.md --kind software`.
4. **Photos:** `node T/scripts/photos.mjs search ...` for hero photo (c) and the privacy photo. Credits go in one footer line.
5. **Build sections 1–7** to their `sections-library.md` recipes. Paste UI from `assets/ui/*/fragment.html` and rewrite every word. The diagram uses `data-diagram="hub"` with the provider labels.
6. **Icons:** `node T/scripts/icons.mjs scan out/index.html --out public/assets/icons --colour`.
7. **Checks** (foreground, one at a time, ≤ 10 min each):
   - `consistency.mjs` at 1440, 1024, 820, 768 and 390
   - `layout/check.mjs` at all 5 sizes
   - `shoot.mjs`
   - `perf.mjs`
   - then `gate.mjs out/index.html --root out` until `GATE: PASS` (3 rounds at most)
8. **SEO** (claude-seo): sitemap.xml, robots.txt, canonical, Open Graph, Twitter card, and JSON-LD `SoftwareApplication` with `operatingSystem: Android` and `offers.price: 0`.
9. **Report:** taste §4 step 7 format, written to `docs/BUILD-REPORT.md`.
10. **Then:** code-reviewer → compliance-reviewer (ads disclosure, privacy policy, no certification claims) → qa-agent gate → devops deploy.

## 8. Pages

- `/`: the 7 screens above.
- `/download`: release notes, APK link, SHA-256 checksum, "how to install an APK" steps, a Play Store note ("coming later").
- `/privacy`: privacy policy (Australian Privacy Principles; on-device data; AdMob + UMP consent; what the ads SDK can and can't see).
- `/how-we-make-money`: the full ads disclosure (mirrors the in-app screen).

---

## Build deviations (2026-11-21/23, recorded at build)

- **Stack:** a static site from the taste-skill starter instead of a Next.js export. taste-skill wins conflicts, and its default for an empty folder is static; the marketing site has no app logic. `site.config.json` + `scripts/build.mjs` handle the domain placeholder (localhost for now).
- **Grounds:** taste-skill allows only base, surface and inverse grounds. The per-section sage and blush fields were dropped; #claims uses the surface ground for the line-carries-colour moment.
- **Photographs:** none. The only live-search candidate showed faces and readable third-party brands and was rejected. UI and the client's glass icon carry the page (allowed for software).
- **Sections as built:** hero (triptych) → #app (app-frame) → #how (word-highlight) → #rules (split + fluted-glass + lanes diagram) → #claims (features 2x2, line-carries-colour) → #faq (money, privacy, credentials, stacking, iPhone) → footer.closing (close-type, footer-statement). The money and privacy content moved into the FAQ and into `privacy.html#ads`.
- **Effect:** `fluted-glass`, dealt at the user's request ("get the animation in, can it later if not wanted"). To remove it, delete `data-fx="fluted-glass"` from the #rules frame.
