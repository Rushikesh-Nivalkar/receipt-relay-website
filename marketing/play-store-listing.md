# Google Play listing draft

Status: draft only. The app is not built and there is no Play listing yet. Character counts were checked with a script (see `GENERATION-LOG.md`).

## App name (30 characters at most)

ReceiptRelay: Receipt Rewards (29 characters)

Alternates:

- ReceiptRelay: Receipt Tracker (29)
- ReceiptRelay: Receipt Claims (28)

Google Play's metadata policy keeps "free", "best", "#1", other brands' names and emoji out of the title, so the provider names live in the descriptions only.

## Short description (80 characters at most)

Scan a receipt once. Check Shping, ShopBack and ReceiptJar rules and deadlines. (79 characters)

Alternates:

- Scan a receipt once. See Shping and ShopBack rules, deadlines and claims. (73)
- Scan a receipt once, check each receipt app's rules and track every claim. (74)
- One receipt scan, checked against Shping, ShopBack and ReceiptJar rules. (72)

## Full description (4,000 characters at most; plain text for Play)

ReceiptRelay is a receipt rewards app for shoppers in Australia. Scan a shopping receipt once. ReceiptRelay checks it against the published rules of Shping, ShopBack and ReceiptJar, shows where it counts and how many days are left, and guides each claim into that app.

HOW IT WORKS
1. Take a photo of your receipt, or share in a PDF or image. Pick the store and type the date and total.
2. ReceiptRelay checks the receipt against each app's rules and shows the result for each one: eligible, not eligible with its reason, or check in the app.
3. Send it to each app. ShopBack opens through Android's share screen. For Shping and ReceiptJar, the photo is saved to your gallery and the steps are shown on screen.
4. Mark it sent. The claim stays in your list until it is paid, rejected or expired.

THE RULES IT CHECKS
Shping: 7-day limit, 2 receipts a day per store, 5 per store in 7 days, 100 a month.
ShopBack: 28-day limit, one receipt per purchase.
ReceiptJar: its rules are shown in the ReceiptJar app.
Each app sets its own rules and can change them. ReceiptRelay shows the rules it checks for each app.

CLAIM TRACKING
Every receipt sits in one list with its store, date and total. A reminder goes out before a receipt gets too old for an app. Each photo gets a fingerprint, so the same receipt is caught before it goes to the same app twice. Mark a claim paid and ReceiptRelay keeps the running total for each app, month by month.

YOUR RECEIPTS STAY ON YOUR PHONE
Receipt photos and the details you enter are stored on your phone, encrypted. ReceiptRelay never asks for your Shping, ShopBack or ReceiptJar password and never logs in for you. You submit in each app, under that app's own terms.

HOW THE APP IS PAID FOR
ReceiptRelay is free. It shows one ad after you submit a receipt, and an optional ad you can watch to support the app. No banners, no pop-ups. Ads are served by Google AdMob, which asks for your consent where the law requires it. Ad code never runs on a receipt screen and never receives receipt data. The full details are on the "How we make money" screen in the app.

FIXED RULES
The rule check is code written from each app's published rules: receipt age, daily and weekly caps, stores and one claim per purchase. There is no AI and no guessing, and every no comes with its reason.

GOOD TO KNOW
Australia only. Android only for now; there is no iPhone app yet.
ReceiptRelay does not read the receipt for you: you choose the store and type the date and total.
ReceiptRelay is not affiliated with Shping, ShopBack or ReceiptJar. Product names are trademarks of their owners.

## What's new (first release)

First release. Checks receipts against Shping, ShopBack and ReceiptJar rules, guides each upload and tracks each claim with reminders.

## Store settings to choose (decisions for the user)

| Setting | Draft | Why |
|---|---|---|
| Category | Shopping | Finance adds financial-feature declarations the app does not need; the user decides |
| Contains ads | Yes | One native ad after a submission and an optional rewarded ad |
| In-app purchases | No | No paid tier (checkpoint decision) |
| Target age | 18 and over | Keeps the app outside the Families policy; receipt reward apps pay money out |
| Countries | Australia only | Rules are for Australian providers |
| Contact email | Needed | The site still uses a `.example` address |
| Privacy policy URL | Needed | Waits for a real domain; the policy text is `src/privacy.html` |

## Graphics checklist

| Asset | Size | Source |
|---|---|---|
| App icon | 512 x 512 PNG | `brand/icon-512.svg` (glass tier) |
| Feature graphic | 1024 x 500 PNG | `marketing/visuals/` options 1 to 3 (choose one) |
| Phone screenshots | 2 to 8, 9:16 | From the built app only; none exist yet. Mock data in screenshots must look like mock data (no earnings figures) |

## Data safety form notes (must match the facts)

Play counts data as "collected" only when it leaves the device. Fill the form from the shipped build and the SDK versions on the day; the notes below are the starting point.

| Question | Draft answer | Basis |
|---|---|---|
| Receipt photos, store, date, total | Not collected | Stored on the phone, encrypted, never uploaded to ReceiptRelay servers (privacy page) |
| Provider usernames or passwords | Not collected | The app never asks for them |
| Data shared with provider apps | Not declared as sharing by ReceiptRelay | The user sends the photo to each app through Android; Play treats a user-started transfer as not shared. Re-check against Google's current definition |
| Ads SDK (Google AdMob) | Collected and shared for advertising, analytics and fraud prevention: device or other IDs; app interactions; diagnostics; approximate location if the SDK version collects it | Take the exact list from Google's AdMob data-disclosure page for the SDK version in the build |
| Encrypted in transit | Yes | TLS for every network call (MVP security list) |
| Can users request deletion | Yes: deleting a receipt or the app removes the data on the phone | Privacy page |
| Account sign-up | None (decided 2026-11-23) | No account, so no email collected and no account-deletion link needed |
| Independent security review | Leave blank | Never state ISO 27001 or SOC 2 certification before an audit passes |

## Listing checks

- Provider names appear only to describe which apps' rules are checked, with the "not affiliated" line in the description.
- No ratings, user counts, earnings figures or testimonials.
- The ReceiptJar limit is never given as a number until confirmed in its app.
- The listing says what the app does not do (no iPhone, no receipt reading, no logging in).
