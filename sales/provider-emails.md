# Provider emails: Shping, ShopBack, ReceiptJar

**Drafts only. Nothing has been sent.** The user decides whether and when to send each one (see "Before sending").

How these were written: ai-sales-team `sales-outreach`, Framework 1 (Observation → Connection → Ask), applied to a partnership request:
- one ask per email
- plain text, under 170 words
- no bold, no emojis, no exclamation marks
- a subject line of 4 to 7 words
- an easy way to say no

The five-email cold sequence is cut to **one email plus one follow-up**. We're asking these teams for a policy answer, so a breakup sequence would be the wrong tone.

Facts come from `faq-facts.md`. Each provider's rules are quoted as that provider publishes them.

## Where to send (found 2026-11-23; inboxes unverified)

| Provider | Best route found | Notes |
|---|---|---|
| Shping | The brand-media contact ("Book a demo") at https://shping.com/shping-brand-media/, or Shping on LinkedIn (https://www.linkedin.com/company/shping) | No partnerships email was found. The brand-media route is aimed at FMCG brands, so ask them to pass it to whoever owns receipt policy. |
| ShopBack | The "Talk to our partnerships team" link at https://corporate.shopback.com/partnerships, or https://business.shopback.com/au | help@shopback.com.au (from ShopBack's Credit Guide) is for customer enquiries, so use it only if the partnerships form fails. |
| ReceiptJar | hello@receiptjar.com | The only address found, from a developer reply on the App Store listing (https://apps.apple.com/au/app/receiptjar/id1450157256). No partnerships page was found. |

Sign-off: these drafts end with the developer's name only. Send them from the address you want replies to go to. The website's contact address is still to be set (`hello@receiptrelay.example` is a stand-in).

---

## 1. Shping

**Subject A:** Question about Shping receipt rules
**Subject B:** Shping receipts and other rewards apps

Hello Shping team,

Your FAQ sets clear receipt rules: 7 days from purchase, 2 receipts per store a day, 5 per store over 7 days, and 100 a month.

I'm building ReceiptRelay, an independent Android app for Australian shoppers who use more than one receipt-rewards app. It checks a receipt against each app's published rules, then opens that app so the shopper submits it themselves. It never asks for Shping passwords and never automates your app. It has no affiliation with Shping.

Before launch, I'd like to get your rules right. Could someone confirm in writing that a genuine receipt may be submitted once to Shping even if the shopper also submits it to another rewards programme? It would also help to know where your Fair Usage Policy lives, and whether there's a supported link that opens your receipt upload screen.

If this belongs with another team, I'd be grateful for a pointer to the right person.

Thank you,
Rushi Nivalkar
ReceiptRelay

---

## 2. ShopBack

**Subject A:** ShopBack Receipts policy question
**Subject B:** Sharing receipts into ShopBack Receipts

Hello ShopBack partnerships team,

ShopBack Receipts already accepts receipts shared from another app, within 28 days and one eligible receipt per transaction.

I'm building ReceiptRelay, an independent Android app for Australian shoppers who use more than one receipt-rewards app. It checks a receipt against each app's published rules and then uses the Android share sheet to hand it to ShopBack, where the shopper submits it. It never asks for ShopBack passwords and never automates your app. It has no affiliation with ShopBack.

Your terms describe fraud as activity meant to "duplicate or artificially obtain rewards". Could someone confirm in writing that a genuine receipt submitted once to ShopBack, and also to another rewards programme, is outside that definition? It would also help to know the per-store daily cap, and whether sharing into ShopBack is the hand-off you prefer.

If another team owns this, a pointer would be much appreciated.

Thank you,
Rushi Nivalkar
ReceiptRelay

---

## 3. ReceiptJar

**Subject A:** ReceiptJar receipt rules question
**Subject B:** Checking ReceiptJar rules before launch

Hello ReceiptJar team,

I couldn't find ReceiptJar's receipt rules published outside the app, so I'm writing to ask directly.

I'm building ReceiptRelay, an independent Android app for Australian shoppers who use more than one receipt-rewards app. It checks a receipt against each app's rules, then opens that app so the shopper submits it themselves. It never asks for ReceiptJar passwords and never automates your app. It has no affiliation with ReceiptJar.

Could someone share the current rules: the maximum receipt age, the weekly cap, and the accepted formats? And could you confirm in writing whether a genuine receipt may be submitted once to ReceiptJar even if the shopper also submits it to another rewards programme? Until I hear from you, the app tells shoppers to check ReceiptJar's in-app terms.

If you'd rather ReceiptJar wasn't included, tell me and I'll leave it out.

Thank you,
Rushi Nivalkar
ReceiptRelay

---

## One follow-up (each provider, 10 business days after, only if there's no reply)

**Subject:** Re: [the original subject]

Hello again,

Just following up on my note about receipt rules. A one-line answer on whether a genuine receipt may go once to your programme as well as to another one would be enough for now. If this has reached the wrong team, a pointer would help.

Thank you,
Rushi Nivalkar

(Under 75 words. After this, stop. Mark that provider's rule file "unconfirmed by provider", and keep showing its published rules.)

---

## Before sending (user decisions)

1. **Timing.** Send now (before the build), or once the beta exists? Sending now risks an early "no" before there's anything to show. Sending later risks building something a provider rejects. Recommendation: send now. The question is about policy, and the answer changes the rule files.
2. **What a "no" means.** If a provider says receipts used elsewhere aren't allowed, do you drop that provider, or keep it and warn shoppers before they submit?
3. **Referral programmes.** Should you ask about them at all? If you do, it becomes ad-adjacent revenue that has to be disclosed.
4. **Reply address.** Which address do you send from? It should match the address the website will use.
5. **Record replies.** Save every written answer (date, sender, wording) beside each rule file. The rule file's review date and source should point to it.
