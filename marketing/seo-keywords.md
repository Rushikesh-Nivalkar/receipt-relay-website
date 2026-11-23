# SEO keyword list for the website

Status: prepared for when the site gets a domain. Today `robots.txt` blocks crawling and there is no canonical URL, which is correct while the site stays local. Method: claude-seo planning (business type: app landing site), keywords from the fact sheet and the words testers are expected to use. No keyword tool was available, so there are no search volumes or difficulty scores here; measure them in Google Search Console or Keyword Planner before writing new pages.

## Rules

- Provider names (Shping, ShopBack, ReceiptJar) are used only to describe the rules ReceiptRelay checks, on informational pages, each with the "not affiliated" line. Never in the page title as if ReceiptRelay were the provider, never in ad keywords bidding on their brands.
- No page about earnings or "how to make money from receipts" with figures.
- FAQ schema brings no Google rich result for commercial sites (since August 2023); keep `SoftwareApplication` JSON-LD (`operatingSystem: Android`, `offers.price: 0`), already planned.

## Primary keywords (the home page)

| Keyword | Intent | Page |
|---|---|---|
| receipt rewards app australia | find an app | `/` |
| receipt scanning app australia | find an app | `/` |
| receipt cashback app australia | find an app | `/` |
| receipt tracker app android | find an app | `/` |
| scan receipts for rewards | find an app | `/` |

Current home page title: "ReceiptRelay: receipt rewards app for Australian shoppers" (57 characters). Keep it.

Current meta description (152 characters) reads well; keep it. Alternative if it is ever cut for length (142 characters): "Scan a receipt once. ReceiptRelay checks it against Shping, ShopBack and ReceiptJar rules, tracks each claim and reminds you before deadlines."

## Secondary keywords (rule questions; a future "receipt app rules" page)

| Keyword | Intent | Page |
|---|---|---|
| shping receipt limit | rule question | `/rules` (future) |
| shping receipts per day | rule question | `/rules` |
| shping 7 day receipt | rule question | `/rules` |
| shopback receipt time limit | rule question | `/rules` |
| shopback receipts one per purchase | rule question | `/rules` |
| receiptjar receipt rules | rule question | `/rules` (only after the in-app rules are confirmed) |
| can i upload the same receipt to multiple apps | rule question | `/rules`, answered with "each app's own terms decide; send once to each app" |
| receipt rejected shopback | problem | `/rules` |

The `/rules` page would hold one table: each app, its time limit, caps, the source link to its own terms and the date the rule was last checked. It must say the rules belong to each app and can change.

## Long-tail keywords (FAQ and download page)

| Keyword | Page |
|---|---|
| receipt app that doesn't need my password | `/` FAQ |
| receipt app privacy encrypted on phone | `/privacy` |
| free receipt app with no subscription | `/` FAQ (ads line) |
| how to install apk android australia | `/download` |
| receiptrelay | every page (brand) |
| receipt relay app | every page (brand) |

## Words to keep out of titles and headings

stacking hack, make money fast, guaranteed cashback, best receipt app, official Shping app, ShopBack partner.

## Page checklist when the domain is set

1. Set `siteUrl` in `site.config.json`, rebuild, check the canonical, `og:url`, sitemap and that `robots.txt` now allows crawling.
2. Write a meta description each for `/download` and `/privacy` (the home page has one).
3. Submit the sitemap in Google Search Console; check indexing after a week.
4. Build `/rules` only when each rule has a source link and a check date.
