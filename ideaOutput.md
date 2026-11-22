# ReceiptRelay — Idea Output

Slug: `receipt-relay` · Created: 2026-11-21 · Idea input: `IdeaInputs/receipt-relay-ideaInput.md`

An Android app for Australian shoppers. Sign up once, scan a receipt once, and get guided through claiming it with each eligible receipt-rewards provider. Each genuine receipt goes to each provider at most once. The MVP covers Shping, ShopBack and ReceiptJar.

## Checkpoint decisions (2026-11-21)

| Question | Decision |
|---|---|
| Go / no-go | **Go.** The user reviewed every provider's terms and found no clause banning upload to multiple platforms. Each provider's own policy is the agreement. |
| Name | **ReceiptRelay** (not yet checked against trademarks or the Play Store) |
| Paid ad-free tier | **No.** The app stays free and earns only from ads. |

Standing constraints:
- Deterministic code only. No AI or ML, including no OCR in the MVP.
- Ads are disclosed in full to users. Use the smallest possible ad footprint while maximising earnings.
- Security target: built to ISO/IEC 27001:2022 and SOC 2 controls, with encryption in transit and at rest and secure credential storage. Certification is a later organisational audit. Never claim "certified" before the audit passes.

---

## Provider research (2026-11-21)

Third-party APK mirrors (apkmirror, apkpure, apkturbo) are **not official** and must never be linked from the app or docs. Google Play only.

| # | Provider | Receipt upload | Pays | Official terms | Google Play |
|---|---|---|---|---|---|
| 1 | Shping | Yes, any store | Shping Points (est. AUD at monthly rate); bank or crypto cash-out | https://shping.com/faq/ | `com.shping` (verify) |
| 2 | ShopBack Receipts | Yes: photo, PDF, share from another app, connected email | AUD Cashback, Tracked → Confirmed | https://support.shopback.com.au/hc/en-gb/articles/45068630719251-ShopBack-Receipts-Terms-and-Conditions | `com.shopback.app` (verify) |
| 3 | ReceiptJar | Yes | Points → gift cards or PayID | In-app only | `com.unocart.unomoney` (verify) |
| 4 | My QV Rewards | Yes, QV products only | Stamps (1 per $5) | https://qvskincare.com.au/qv-rewards/terms-and-conditions.html | `com.ego.myqv` (verify) |
| 5 | Uber Eats Dine Out | In-app, after a booked reservation | Uber Cash (reported 50%, max $50) | https://www.uber.com/au/en/blog/introducing-dine-out | `com.ubercab.eats` |
| 6 | Snapcash | Yes, plus an Instagram post | Up to 100%, $100 cap, plus content fee, paid to PayID | https://snapcash.com.au/terms/ | `com.snapcash.snapcashapp` |
| 7 | Field Agent | Assigned jobs only | Bounty plus reimbursement | AU terms not found | `net.fieldagent` (verify) |
| 8 | SmartSpotter | Assigned jobs only | Job pay | https://smartspotter.com/en-au/terms-and-conditions | Unverified |
| 9 | Google Opinion Rewards | Invite-only receipt tasks | Google Play credit | https://support.google.com/opinionrewards/answer/9333413 | `com.google.android.apps.paidtasks` |
| 10 | Prizecart | Not confirmed | Prize chances | Not found | `app.prizecart.mobile` |

### Rules for the MVP providers (rule-file inputs)

| Rule | Shping | ShopBack | ReceiptJar |
|---|---|---|---|
| Max receipt age | 7 days | 28 days | 14 days (third-party source, unverified) |
| Per-retailer cap | 2/day, 5 per 7 days | Daily cap exists, number not stated | Unknown |
| Global cap | 100/month | 30 attempts/week per sharing method | Weekly cap, threshold not stated |
| Per transaction | — | One eligible receipt per transaction, regardless of method | Repeat = receipt already in ReceiptJar |
| Formats | Image; referral needs full PDF or image | Photo (paper) or PDF (e-receipt) | Photo |

### Flags and unclear wording

- **Shping:** accounts can be flagged below the 100/month cap. The FAQ says "Points" but the store listing says "Coins". The standalone Fair Usage Policy page was not found.
- **ShopBack:** the fraud definition includes activity intended to "duplicate or artificially obtain rewards". The user's review of the terms found no clause against multiple platforms, so the decision is Go. Re-check this wording whenever the terms change.
- **ReceiptJar:** no public T&Cs. Every rule above needs checking against the in-app terms.
- **My QV:** the T&Cs say upload in the app, but one FAQ says email receipts and not upload them in the app.
- **Uber Dine Out:** limited to invited restaurants and some Uber One members. Limits come from forum posts.
- **Snapcash:** requires a public Instagram account with 500+ followers. Melbourne and Cairns only for now.
- **Field Agent / SmartSpotter:** these are job marketplaces. It's unclear whether a job purchase can be claimed elsewhere.
- **Google Opinion Rewards:** Australian access to receipt tasks is unconfirmed.
- **Prizecart:** receipt scanning is unconfirmed. The site says Android is "coming soon", but a Play listing exists.

### Official integrations

| Provider | Partner API / account linking | MVP approach |
|---|---|---|
| Shping | None found | Guided upload: save the file, open the app, follow a checklist |
| ShopBack | None for receipts (public developer docs cover payments only) | Guided upload via the Android share sheet (`ACTION_SEND`) |
| ReceiptJar | None found | Guided upload: save the file, open the app, follow a checklist |

The app must never do any of the following: automate provider apps (Accessibility Service), scrape them, or store provider credentials.

---

## Task 1 — Validation (Paul Graham)

### Core Assumptions
1. Shping, ShopBack and ReceiptJar each accept the same genuine receipt once per provider.
2. Shoppers value a hub that tracks rules, deadlines and caps, even though they still upload in each provider's app.
3. One small native ad slot plus an optional rewarded ad can fund the app.
4. Provider rules can be expressed as deterministic code (age, caps, retailers, formats).

### 3 Fatal Flaws (severity order)
1. **Provider stance on cross-platform receipts.** Any provider could change its terms or deny stacked receipts. There is a precedent: US app Checkout 51 reportedly denies receipts used in other apps. *Mitigation:* each provider's rule file carries its terms URL and a review date, with a terms-change watch list. The app shows each provider's own rules to the user, who makes the submission.
2. **Ad revenue vs compliance cost.** Rough maths: ~24 native impressions per user per month at ~US$3 eCPM (a global vendor figure, not Australian) ≈ $0.07 per user per month. ISO 27001 and SOC 2 audits cost more than that brings in early on. *Mitigation:* go local-first with no receipt data on servers, build to the controls now, and audit later. Never claim "certified" before an audit (Australian Consumer Law).
3. **Thin value over the share sheet.** With no integrations, the app is a smart checklist. *Mitigation:* the value comes from the rule engine, deadline reminders, duplicate blocking and payout tracking. Measure week-2 retention.

### Founder-Market Fit
Strong as a builder: prior Android apps (Rush Flix, RemAura), based in Australia, and has researched every provider's terms personally.

### Problem Validation
A moderate pain for heavy stackers, a vitamin for casual users. Payouts per receipt are small (a UK guide reported ~£0.50/week for 5 receipts a week across apps).

### Brutal Verdict
**PROCEED.** The user confirmed at the checkpoint that no provider has a clause against multiple platforms. The remaining flaws concern economics and positioning, not existence.

## Task 2 — Customer Discovery

### Specific Pain
Each app has different deadlines (7, 14 or 28 days), caps and formats. People miss deadlines, forget a provider, or get rejected after hitting a cap.

### Early Adopter Profile
An Android user on OzBargain or Whirlpool who uses at least 2 of Shping, ShopBack and ReceiptJar and logs 5+ receipts a week.

### 5 Discovery Questions
1. Walk me through what you do with a receipt after you get home.
2. Which apps do you send each receipt to, and in what order?
3. When did you last miss a deadline or get rejected? What happened?
4. How much do you earn from these apps a month?
5. Have you ever been flagged or banned? What did the app say?

### Validation Criteria
- 3 of 5 use 2+ apps per receipt.
- 3 of 5 report a missed deadline or a rejection.
- 3 of 5 accept a small ad in exchange for a free tool.

### Vitamin or Painkiller Verdict
A vitamin for most users, a painkiller for heavy stackers. Launch to heavy stackers first.

## Task 3 — Competitive Landscape

### Current Behaviour of Target Customer
Photograph the receipt, open each app, upload again. No tracking of deadlines, caps or payouts.

### Direct Competitors
No Australian multi-provider receipt hub was found. ReceiptPal (US) markets multiple earning methods, but within a single provider.

### Indirect Competitors
Gallery plus share sheet, spreadsheets, notes apps, and each provider's own app.

### The Real Enemy
The share sheet, plus "I'll do it later".

### Genuine Differentiation
One scan is checked against every provider's rules, with deterministic, explainable results ("Not eligible: over 7 days for Shping"). Deadline reminders, duplicate blocking, local-first privacy, and fully transparent ad funding.

## Task 4 — First 10 Customers

### Where First 10 Are
OzBargain threads on ShopBack, Shping and ReceiptJar (check self-promotion rules first), Whirlpool forums, Australian frugal subreddits, and Facebook saver groups.

### Manual Outreach Approach
Reply to posts about rejections, caps or deadlines. Offer a Play internal-testing invite. No pitch.

### First Message
"Saw your post about ShopBack rejecting a receipt over the cap. I'm building a free Android app that checks one receipt against Shping, ShopBack and ReceiptJar rules and reminds you of each deadline. Want to try the beta and tell me what breaks?"

### Success Criteria
- 10 testers log 5+ receipts each.
- 3+ use it again in week 2 unprompted.
- 0 provider bans among testers.

### Weekly Milestone Plan
- Week 1: find 20 candidates, message 10, recruit 5.
- Week 2: beta; capture friction.
- Week 3: fix.
- Week 4: open beta to 50.

## Task 5 — MVP + 2-Week Launch Plan

### Core Assumption
Shoppers will log one receipt and follow a guided upload to 3 providers if the app tells them eligibility and deadlines instantly.

### Minimum Feature Set
1. **Sign-up:** passkey via Credential Manager, email OTP fallback. No provider credentials, ever.
2. **Capture:** CameraX photo or a shared-in PDF/image. Store the original bytes untouched (no crop, enhance or compress). Hash with SHA-256. The user picks the store from a list and enters the date and total. No OCR.
3. **Eligibility engine:** a pure function over versioned JSON rule files (max age, retailer allow/deny lists, per-retailer day/week caps, monthly cap, minimum spend, formats). Results: Eligible, Not eligible (with the failed rule), or Check manually (unknown rule).
4. **Guided submission:** ShopBack via the share sheet. Shping and ReceiptJar by saving the file to the media store, opening the app, and showing the steps. Then the user taps "I submitted it".
5. **Claim tracker:** Not started → Submitted → Pending/Tracked → Confirmed/Paid | Rejected (reason) | Expired. WorkManager reminds before deadlines. Totals per provider.
6. **Ads:**
   - One native ad on the "Submitted" success screen.
   - An optional rewarded "support us" ad.
   - No banners, no interstitials.
   - The ad SDK never sees receipt screens or data.
   - A "How we make money" screen in onboarding and settings.
   - Google UMP consent, with a non-personalised ads option.
7. **Security:**
   - SQLCipher database.
   - Receipt files encrypted with Tink AES-256-GCM.
   - Keys in Android Keystore (StrongBox where available).
   - TLS 1.3 with certificate pinning, cleartext disabled.
   - No plaintext logs.
   - Do not use Jetpack `security-crypto` (deprecated).

### What Gets Cut
See `remaining-features.md`.

### Test Criteria
- The rule engine passes 100% of fixture tests.
- 10 testers log 5+ receipts each.
- 0 bans.
- Week-2 retention ≥30%.

### Week 1 Plan
- D1: project setup, Room + SQLCipher, Keystore.
- D2: capture, import, hashing.
- D3: rule engine + unit tests.
- D4: 3 provider rule files.
- D5: guided submission.
- D6: claim tracker + reminders.
- D7: internal test with real receipts.

### Week 2 Plan
- D8: passkey sign-up.
- D9: AdMob native slot + UMP consent.
- D10: transparency screen + privacy policy.
- D11: security pass.
- D12: Play internal testing track.
- D13–14: onboard testers, collect feedback.

### Launch Channels
OzBargain, Whirlpool, Australian frugal subreddits, Facebook saver groups.

### Pricing Tiers
Free only, ad-funded. No paid ad-free tier (user decision). Any provider referral links count as extra revenue and must be disclosed on the "How we make money" screen.

### Product Name
**ReceiptRelay** | Slug: `receipt-relay`. Alternatives: StackSnap, OneReceipt, ClaimLoop, ReceiptHub, ScanOnce.

---

## Sources
- Shping FAQ: https://shping.com/faq/
- Shping cash-out: https://shping.com/australias-first-rewards-program-to-offer-cryptocurrency-cash-outs/
- ShopBack Receipts T&Cs: https://support.shopback.com.au/hc/en-gb/articles/45068630719251-ShopBack-Receipts-Terms-and-Conditions
- ShopBack Receipts FAQ: https://support.shopback.com.au/hc/en-gb/articles/45067967029779
- ShopBack developer docs: https://docs.shopback.com/docs/in-store-integrations
- ReceiptJar App Store: https://apps.apple.com/au/app/receiptjar/id1450157256
- ReceiptJar third-party review: https://thechampagnemile.com.au/receiptjar-australia-review/
- QV Rewards T&Cs: https://qvskincare.com.au/qv-rewards/terms-and-conditions.html
- Uber Dine Out: https://www.uber.com/au/en/blog/introducing-dine-out
- Snapcash terms: https://snapcash.com.au/terms/
- SmartSpotter AU terms: https://smartspotter.com/en-au/terms-and-conditions
- Google Opinion Rewards receipts: https://support.google.com/opinionrewards/answer/9333413
- Prizecart: https://reveal.prizecart.app/
- Scrimpr UK multi-app guide: https://scrimpr.co.uk/save-money/receipt-scanning-cashback-apps-uk/
- Checkout 51 Play listing: https://play.google.com/store/apps/details?id=com.c51
- AdMob eCPM Trends: https://support.google.com/admob/answer/14660616
