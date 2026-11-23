# ReceiptRelay positioning

Status: prepared 2026-11-23; unpublished. Frameworks: Corey Haines product marketing context (`product-marketing-context`), Brian Wagner positioning basics (5 questions, competitive map, statement, test). Sources: `ideaOutput.md`, `docs/WEBSITE-PLAN.md` section 5, the built site `src/index.html`. Nothing here goes beyond those facts.

## Product overview

- **One-liner:** Receipt rewards app for Australian shoppers on Android.
- **What it does:** You scan a shopping receipt once. ReceiptRelay checks it against the published rules of Shping, ShopBack and ReceiptJar, hands the original photo to each app you choose, and tracks each claim until it is paid, rejected or expired.
- **Category (the shelf people search):** receipt scanning app, receipt rewards app, receipt cashback tracker.
- **Type:** free Android app, Australia only. iPhone not yet.
- **Business model:** free, funded by one ad on the screen after a submission and an optional rewarded "support us" ad. There is no paid tier, banner or interstitial.

## Target audience

- **Best-fit buyer:** an Android user in Australia who already sends receipts to at least two of Shping, ShopBack and ReceiptJar and logs five or more receipts a week. Often reads OzBargain or Whirlpool.
- **Primary use case:** knowing, for each receipt, which apps it still counts for and how many days are left.
- **Jobs to be done:**
  - Send each receipt to every app it qualifies for, once each.
  - Avoid a rejection for an old receipt or a hit cap.
  - See what each app has paid so far.
- **Not for:** iPhone users (not yet), shoppers outside Australia, anyone who wants the app to log in and upload for them (it never does), casual users with one receipt a month.

## Problems and pain points

- **Core problem:** each app has its own deadline, caps and formats. Shping allows 7 days, 2 receipts a day per store, 5 per store in 7 days and 100 a month. ShopBack allows 28 days and one receipt per purchase. ReceiptJar shows its rules in its own app.
- **What happens today:** a receipt is photographed, then opened in each app in turn, with no record of deadlines, caps or payouts.
- **Cost:** a missed deadline, a forgotten app, a rejection after a cap. Each receipt pays a small amount, so the loss is the habit breaking.
- **Emotional tension:** worry about being flagged; annoyance at doing the same upload three times and still guessing.

## Competitive landscape

| | ReceiptRelay | Each provider's own app | Gallery plus share sheet | Spreadsheet or notes app |
|---|---|---|---|---|
| Best for | Shoppers using two or three receipt apps | Shoppers using one app | Occasional uploads | Heavy stackers who like tracking by hand |
| Approach | One scan, a rule check per app, guided upload, a claim list | Upload and status inside one app | Share the photo to each app from memory | Type each receipt and date in by hand |
| Trade-off | You still submit inside each app; Android only | Knows only its own rules and receipts | Deadlines and duplicates tracked from memory | Manual, easy to fall behind |
| They win when | You use two or more apps | You only use one app | You upload once a fortnight | You want a custom view of earnings |

- **Direct competitors in Australia:** none found in the research (ideaOutput Task 3). ReceiptPal (US) bundles earning methods inside one provider.
- **The real enemy:** the share sheet, and "I'll do it later".
- **Live competitor browsing:** skipped. With no direct Australian competitor, the browser step has nothing to visit; the indirect alternatives above are habits people have.

## Differentiation

- One scan checked against each provider's published rules, with a plain reason on every "no" ("Not eligible: over 7 days for Shping").
- Days-left reminders before each app's deadline.
- A fingerprint on each photo, so the same receipt is caught before it goes to the same app twice.
- Receipts stay on the phone, encrypted. The app never asks for provider passwords and never logs in for you.
- Fixed rules written as code; the check uses no AI.
- The money is disclosed in the app: one ad after you submit, an optional support ad.

## The five questions (Brian Wagner)

1. **Who:** Android shoppers in Australia who send receipts to two or three of Shping, ShopBack and ReceiptJar, five or more a week.
2. **What problem:** three apps, three sets of deadlines and caps; a receipt gets missed, sent late or rejected over a cap. Trigger: a rejection or a lapsed deadline.
3. **How:** a pure rule check over versioned rule files per provider (age, caps, stores, one claim per purchase), then a guided hand-off to each provider's own app, then a status list with reminders.
4. **Why better:** only ReceiptRelay checks one Australian receipt against all three apps' rules at once and keeps the claim list in one place, without touching provider accounts.
5. **So what:** for each receipt you see where it counts and the days left, and each app's paid total sits in one list (Tier 2: a named change; no measured figures exist yet).

## Positioning statement

> For Android shoppers in Australia who send receipts to Shping, ShopBack and ReceiptJar,
> ReceiptRelay is a receipt rewards app
> that checks one scan against each app's published rules and tracks every claim until it pays.
> Each app opened by hand knows only its own rules; ReceiptRelay shows all three side by side,
> with the days left and the reason for every no.

- **One-liner (10 words or fewer):** Scan a receipt once; claim it with each app.
- **Elevator pitch (about 70 words):** ReceiptRelay is a free Android app for Australians who use Shping, ShopBack or ReceiptJar. Take one photo of a shopping receipt and it checks that receipt against each app's published rules: Shping's 7-day limit and caps, ShopBack's 28-day limit and one receipt per purchase. It hands the photo to each app for you to submit, reminds you before deadlines and tracks each claim. Receipts stay on your phone, encrypted.

### Positioning test

| Check | Result |
|---|---|
| Specific | Pass: a named platform, country and three named apps |
| Differentiated | Pass: no Australian multi-provider receipt hub found |
| Credible | Pass with care: the rules quoted are each provider's published rules; ReceiptJar's are unconfirmed and never quoted as numbers |
| Meaningful | Pass for heavy stackers; a vitamin for casual users (ideaOutput Task 2) |
| Memorable | Pass: "scan once, claim with each app" |

## Objections and answers

| Objection | Answer |
|---|---|
| Will sending one receipt to three apps get me banned? | ReceiptRelay shows each app's own published rules and sends a receipt to each app once. The rules belong to each app and can change; you submit under each app's terms. |
| Why give an app my receipts? | They stay on your phone, encrypted. ReceiptRelay has no server copy of them and ad code never runs on a receipt screen. |
| Does it need my Shping or ShopBack login? | No. It never asks for provider passwords. You submit in each app yourself. |
| What's the catch with free? | One ad after you submit a receipt, plus an optional ad you can watch to support the app. |
| Is it on iPhone? | Not yet. Android first, Australia only. |
| Does it read the receipt for me? | No. You pick the store and type the date and total; the rules are fixed code, no AI. |

## Switching forces

- **Push:** a rejection over a cap, a deadline missed by a day, three uploads per receipt.
- **Pull:** one list with days left per app; the reason for each no.
- **Habit:** photographing and sharing from the gallery works well enough.
- **Anxiety:** account flags; a new app holding receipt photos; ads.

## Customer language

- **Words to use:** receipt, claim, deadline, days left, cap, rules, each app, once, on your phone.
- **Words to avoid:** stack hack, beat the system, guaranteed, certified, partner (of any provider), AI, automatic upload, "maximise".
- **Verbatim customer quotes:** none collected yet. The first ten testers' words go here (see `outreach-first-10.md`).

## Voice card

```
Voice: technical-dry (copy-registers.md 2), with the founder's letter (3) for community posts
Pairs: exact, not cold; sure, not loud
Person: "you" for what the shopper gets; "I" in community posts by the developer; the app is the subject of feature lines
Sentences: mostly 8 to 16 words; one long one where it explains the rule check
Humour: none in listings, FAQ or ads; a dry line allowed in microcopy only
House words: receipt, app, claim, rules, days left (same word every time)
Never: virtue words, invented numbers, provider logos, "certified", any promise about bans
```

## Proof points

- **Metrics, customers, testimonials:** none yet. None may be invented.
- **Facts allowed as proof:** the published rules (Shping 7 days, 2 a day per store, 5 per store in 7 days, 100 a month; ShopBack 28 days, one receipt per purchase), free, Android, Australia, on-device encryption, no provider passwords, not affiliated with any provider.

## Goal

- **Primary action:** Download for Android (after release). Before release: join the test.
- **First milestone (ideaOutput Task 4):** 10 testers logging 5 or more receipts each; 3 or more back in week 2 unprompted; 0 provider bans.
