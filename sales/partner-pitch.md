# Partner pitch: ReceiptRelay

Audience:
- **Primary:** the partnership or product teams at Shping, ShopBack and ReceiptJar.
- **Secondary:** an advertiser, or an ad network contact, asking about the single ad slot.

Length: 11 slides, about 12 minutes plus questions.

Built as slides: `sales/deck/partner-deck.html`, rendered to `sales/deck/partner-deck.pdf` and `sales/deck/png/slide-NN.png`.

How this adapts the agent's 12-slide sales deck (`.claude/agents/sales-agent.md`):
- **Business model:** there are no pricing tiers. The app is free, with ads only, by user decision.
- **Market size:** dropped. The source has no sourced TAM/SAM/SOM, and invented market figures break the facts-only rule.
- **Traction:** says plainly that the app is pre-launch.
- **The ask:** it's for written policy confirmation and a supported hand-off.
- **Demo slide:** dropped until the app is built. Slide 5 shows the hand-off in words.

Every fact comes from `faq-facts.md`. Every figure that's an assumption is labelled as one.

Narrative check: problem (2) → why now (3) → solution (4–5) → proof (6–7, design facts only, no metrics) → ask (10–11).

---

## Slide 1: Title

- Asset: `brand/logo-glass-lockup-transparent.svg` on the slate ground (glass tier, at least 240 px wide).
- **Headline:** ReceiptRelay. Receipt rewards app for Australian shoppers.
- **Sub-line:** One receipt, checked against Shping, ShopBack and ReceiptJar rules, claimed in each provider's own app.
- **Footer line:** Rushi Nivalkar, independent developer · Partner conversation, November 2026

**Speaker notes:** Thank them for the time. Say up front that ReceiptRelay is an independent Android app with no provider affiliation, and that you're here to ask for guidance. The meeting has two goals: to confirm how they want shoppers to use their programme alongside others, and to ask whether there's a supported way to open their upload screen.

## Slide 2: Who we are, today

- An independent Android app for Australia.
- **Pre-launch.** The app is being built, and testers will come in through the Play internal testing track.
- No users, revenue or partnerships yet.
- Not affiliated with or endorsed by Shping, ShopBack or ReceiptJar.

**Speaker notes:** Be plain about the stage. There are no numbers to show, and you won't invent any. Talking to them before launch is the point: you'd rather build it the way their programme wants than fix it afterwards.

## Slide 3: The shopper's problem

- Each programme sets its own receipt age:
  - Shping: 7 days
  - ShopBack: 28 days
  - ReceiptJar: rules in its app
- Each sets its own caps:
  - Shping: 2 per store a day, 5 per store over 7 days, 100 a month
  - ShopBack: one receipt per purchase
- Shoppers who use more than one app miss deadlines, forget an app, or upload after hitting a cap and get rejected.
- **Why now:** these shoppers already juggle several receipt apps by hand. Nothing in Australia tracks the rules across them. (We found no Australian multi-provider receipt hub.)

**Speaker notes:** These are the rules as each provider publishes them. Ask them to correct anything that's out of date, because getting it right is the point. Rejections that come from timing and caps waste the shopper's effort and the provider's review time alike.

## Slide 4: What ReceiptRelay does

1. **Captures once.** A photo, or a shared PDF or image. The original file is kept unchanged: no crop, enhancement or compression.
2. **Checks the published rules.** The result is Eligible, Not eligible with the reason, or Check manually when a rule is unknown. These are fixed rules, with no AI.
3. **Hands off and tracks.** The shopper submits in your app. ReceiptRelay reminds them before deadlines and tracks each claim to Paid, Rejected or Expired.

**Speaker notes:** The shopper picks the store and types the date and total. There's no OCR. The check runs on your published rules: age, caps, retailers and formats. When we don't know a rule, it says so.

## Slide 5: How the hand-off works

| Provider | Today's hand-off |
|---|---|
| ShopBack | Android share sheet into the ShopBack app |
| Shping | Saves the file, opens the Shping app, shows the steps |
| ReceiptJar | Saves the file, opens the ReceiptJar app, shows the steps |

- The shopper submits it themselves, in your app, under your terms.
- ReceiptRelay never asks for or stores provider passwords, and never logs in for the shopper.
- It never automates or scrapes your app (no Accessibility Service).

**Speaker notes:** We found no public partner API or account linking for any of the three. ShopBack's public developer docs cover payments only. So the hand-off is as plain as it gets. If you have a deep link or intent that opens your upload screen, that would replace "open the app and follow the steps".

## Slide 6: What it is designed to do for your programme

- Checks your published age limit and caps **before** the shopper uploads.
- Sends each receipt to each provider **once**. A SHA-256 fingerprint blocks the same file going to the same provider twice.
- Passes on the original file, untouched.
- Sends the shopper to **your** app to submit, where your review and your rewards apply.

**Speaker notes:** These are design facts. There are no results yet. We have no data yet, and you'll get no figures until we do. The aim is fewer submissions that break your rules on timing, caps or repeats. If there are rules we've missed, we want them in the rule file.

## Slide 7: Data and privacy

- Receipts stay on the shopper's phone, encrypted:
  - SQLCipher database
  - AES-256-GCM files
  - keys in Android Keystore
- Receipts aren't uploaded to our servers. The ad code never runs on a receipt screen and never gets receipt data.
- TLS 1.3 with certificate pinning, and no plaintext logs.
- Built towards ISO/IEC 27001:2022 and SOC 2 controls. **Not certified.** No audit has been done.

**Speaker notes:** Say "not certified" out loud, so nobody takes it away as a claim. Stress that nothing about their shoppers or their receipts reaches ReceiptRelay servers or an ad network.

## Slide 8: How it is funded

- Free. There's no paid tier, by choice.
- One native ad on the "Submitted" screen, plus an optional rewarded "support us" ad. No banners or interstitials.
- Google UMP consent, with a non-personalised option. A "How we make money" screen in onboarding and settings.
- **Assumption (no results yet):** about 24 native impressions per user a month at about US$3 eCPM. That eCPM is a global vendor figure; Australian rates are unknown. This comes to about US$0.07 per user a month.

**Speaker notes:** This slide is here so they know the business model doesn't depend on their data. The revenue line is a rough planning assumption, labelled as one. Don't present it as a forecast.

## Slide 9: For advertisers, the one slot

- **Placement:** the "Submitted" screen, just after a shopper finishes a claim.
- **Audience:** Australian Android shoppers who use receipt-rewards apps.
- **Served by:** AdMob at launch, with consent through Google UMP.
- **Targeting:** never on receipt data. The slot has no access to receipts.
- Direct sponsorship of the slot is an open question for later.

**Speaker notes:** Use this slide only with an advertiser or a network. Skip it with providers. There's no audience size or click rate to quote yet. Offer to share real figures after the beta, with the user's approval.

## Slide 10: What we are asking for

1. **Written confirmation** that a genuine receipt may be submitted once to your programme even if the shopper also submits it to other programmes.
2. **The current rules** (age, caps, formats, retailers) and a contact or page to watch for changes.
3. **A supported entry point,** if one exists: a deep link or intent to your receipt upload screen, a share target, or an API.
4. **Guidance on your name and logo.** Until you say yes, we use your name in text only, with a "not affiliated" line.
5. *(Optional; for the user to decide.)* Whether you run a referral programme that's open to us. If you do, we'd disclose it on the "How we make money" screen.

**Speaker notes:** Item 1 is the one that matters. If their answer is no, or "only through us", the rule file changes and the shopper is told before submitting. Ask who owns each item, and write it down.

## Slide 11: Next step

- A 20-minute call with whoever owns receipt policy, or a written reply to the five questions.
- On request: a beta build or a screen walk-through once it exists.
- Contact: Rushi Nivalkar, ReceiptRelay. Reply to the email this deck came with.

**Speaker notes:** Close on one action. Offer to update the rules within a week of any reply, and to remove their programme from the app if they'd rather not be included.

---

## Pre-emptive points (built into the slides)

1. **"Are you encouraging duplicate claims?"** Slide 6: once per provider, the original file, the shopper submits in your app, and your caps are checked before upload.
2. **"What do you do with our shoppers' data?"** Slides 7 and 8: receipts stay on the phone, the ad code never sees them, and revenue comes from ads only.

## Objections a provider may raise

ABC method; facts only.

| Objection | Acknowledge | Bridge | Close |
|---|---|---|---|
| "We don't allow receipts used elsewhere." | Thank you, that's exactly what we need to know. | The rule file will mark your programme so shoppers see it before they submit. | Could you point us to the clause, or confirm it in writing, so we quote it exactly? |
| "This looks like a tool for gaming us." | That's a reasonable worry about any helper app. | It submits nothing itself, holds no passwords, and checks your caps and once-per-receipt rule before upload. | Would a look at the beta's rule check settle it? |
| "No API for you." | Understood. | The share sheet and "open the app" work without one. | Is there a public deep link to the upload screen we may use? |
| "Don't use our name." | Understood, it's your name. | We'd stop listing your programme. | Should we remove it, or describe it with no name? |
| "How many users do you have?" | It's a fair question. | We're pre-launch, with none yet. That's why we're asking before launch. | Can we come back with beta figures? |
