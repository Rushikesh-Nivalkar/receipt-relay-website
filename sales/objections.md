# Shopper objections and answers

Who this is for: the first testers. They're Android users on OzBargain, Whirlpool, Australian frugal subreddits and Facebook saver groups who use at least two of Shping, ShopBack and ReceiptJar (ideaOutput Task 2 and Task 4).

Method: ai-sales-team `sales-objections`, adapted. ReceiptRelay is free, so every answer here is about trust. Each objection gets:
- what it usually means
- one **Acknowledge, Bridge, Close** answer
- a short forum reply
- a follow-up question
- the proof we're allowed to use
- when to stop

The skill's Feel-Felt-Found frame is **not used**. Its "felt" and "found" parts need real users and real results, and we have neither yet. Every fact here comes from `faq-facts.md`.

Rules for every reply:
- Before posting a link in a community, check that community's rules on self-promotion.
- Say plainly that you're the developer.
- Offer the beta. Don't pitch.

---

## 1. "Won't I get banned for sending one receipt to several apps?"

**What it means:** This is the biggest fear. People in these groups have read stories of accounts being flagged.

**Acknowledge:** That's the right thing to ask first. An account ban costs more than any receipt is worth.

**Bridge:** We read each provider's published terms and found no clause against sending a genuine receipt to more than one rewards app. The app sends each receipt **once per app** and blocks a second send of the same file to the same app. It also checks the published caps before you submit: Shping allows 2 per store a day, 5 per store over 7 days and 100 a month, and ShopBack allows one receipt per purchase.

**Close:** We can't promise a provider will never change its rules or reject a receipt. Each provider's own terms are the final word, and the app links to them. Want to try the beta on a few receipts and tell me if anything looks off?

**Forum reply:** "Fair worry. We read Shping's and ShopBack's published terms and found nothing against using a genuine receipt in more than one app. The app sends each receipt to each app once, never twice, and checks their caps first (Shping: 2 per store a day, 100 a month). Their terms are the final word, and the app links to them."

**Follow-up question:** "Have you been flagged before? What did the app say?" (This is discovery question 5, and the answer is worth recording.)

**Proof allowed:** The published rules above and the once-per-provider block. Nothing else.

**When to stop:** If they'd rather wait for a provider to confirm in writing, respect that. Note them for when a reply comes back (`provider-emails.md`).

## 2. "I already just share the photo to each app."

**What it means:** The share sheet works for them. This is the real competitor (Task 3).

**Acknowledge:** It does work, and you'll still submit in each app with ReceiptRelay too.

**Bridge:** The difference shows up before and after the share. Shping wants receipts within 7 days and ShopBack within 28. The app works out which deadline applies, reminds you before it passes, and tells you why a receipt won't qualify ("over 7 days for Shping") before you waste an upload. Then it tracks each claim until it's paid or rejected.

**Close:** If you've never missed a deadline or hit a cap, you may not need it. If you have, try it on this week's receipts.

**Forum reply:** "You still share it, the app just tells you where it counts first: Shping's 7 days, ShopBack's 28, the caps. It reminds you before a deadline and tracks each claim to paid."

**Follow-up question:** "When did you last miss a deadline or get a rejection?"

**When to stop:** If they use only one app, they aren't the early adopter. Thank them and move on.

## 3. "Does it want my ShopBack or Shping password?"

**What it means:** They expect a scraper or a bot.

**Acknowledge:** Good question. An app that wanted those passwords would be a real risk.

**Bridge:** ReceiptRelay never asks for provider passwords and never stores them. It doesn't log in to, scrape or automate other apps. It hands your receipt to each app, and you submit it there yourself.

**Close:** ReceiptRelay itself has no account and no sign-in either.

**Forum reply:** "No. It never asks for those passwords or logs in for you. It hands the receipt to each app and you tap submit there."

**Proof allowed:** the passwords and automation rows in `faq-facts.md`.

## 4. "Free app, so you're selling my receipts."

**What it means:** It's a reasonable guess. Many free apps make money from data.

**Acknowledge:** That's how a lot of free apps work, so it's worth asking.

**Bridge:** ReceiptRelay makes money from ads only: one ad after you submit and an optional "support us" ad. Receipts stay on your phone, encrypted, and aren't uploaded to our servers. The ad code never runs on a receipt screen and never gets receipt data. Receipts are never sold or shared.

**Close:** The "How we make money" screen in the app lays all of this out before you start.

**Forum reply:** "Ads only. One after you submit, plus an optional one you can watch to support it. Receipts stay encrypted on your phone and the ad code never sees them. Nothing is sold."

**Follow-up question:** "Would one small ad after each submission put you off?" (This tests validation criterion 3.)

## 5. "It'll be full of ads."

**Acknowledge:** Ad-heavy apps are tiring, especially ones you open every day.

**Bridge:** There's one native ad, on the "Submitted" screen after you claim. There are no banners and no full-screen pop-ups. A second ad is optional and only plays if you choose it. You can pick non-personalised ads on the consent screen.

**Close:** There's no paid version to upsell you either. It's free, and that's the whole model.

**Forum reply:** "One ad, after you submit. No banners, no pop-ups. The other one only plays if you choose it."

## 6. "Do I need an account?"

**Acknowledge:** Fair question. Plenty of apps ask for one they don't need.

**Bridge:** ReceiptRelay has no account and no sign-up. Install it, scan a receipt, claim. Nothing is uploaded, because there is no server to upload to.

**Close:** Your receipts stay on the phone, encrypted. Delete the app and they are gone.

**Forum reply:** "No account, no sign-up, no email. It runs on the phone."

## 7. "It's tiny money. Not worth another app."

**What it means:** For a casual user, this is a vitamin (Task 2). They're probably right.

**Acknowledge:** For a receipt or two a week, the share sheet is probably enough, and I'd say so.

**Bridge:** It's built for people who log five or more receipts a week across two or three apps. That's where deadlines, caps and lost claims add up.

**Close:** If that's you, the beta is free. If not, no hard feelings.

**When to stop:** Fewer than 5 receipts a week, or only one app. Don't push.

## 8. "An APK from GitHub? Why not the Play Store?"

**What it means:** Installing outside the Play Store feels risky. They're right to check.

**Acknowledge:** Installing from outside the Play Store deserves care.

**Bridge:** The download page lists the release, its SHA-256 checksum so you can check the file, and the install steps. Testers can also join through the Play internal testing track. A public Play Store listing will come later.

**Close:** If you'd rather wait for the Play Store, that's a sensible choice.

**Don't:** Link any APK mirror, for ReceiptRelay or for a provider.

## 9. "Is this made by ShopBack (or Shping, or ReceiptJar)?"

**Acknowledge:** It's good to know who's behind an app before you install it.

**Bridge:** No. ReceiptRelay is an independent app, made in Australia, with no affiliation to Shping, ShopBack or ReceiptJar and no endorsement from them. It works alongside their apps, using the rules they publish.

**Close:** Your rewards and payouts stay with each provider, in your account there.

## 10. "Does it read the receipt for me?"

**Acknowledge:** Auto-reading would save typing.

**Bridge:** Not in this version. It has no AI and no text scanning. You pick the store and type the date and total, which takes a few seconds, and the rules check is exact. Your photo is kept unchanged, so each provider gets the original.

**Close:** If typing turns out to be the main friction, tell us in the beta.

## 11. "What if a provider changes its rules?"

**Acknowledge:** They do change them, and that's what catches people out.

**Bridge:** Each provider's rules live in a file that records the provider's terms link and the date we last checked it. When a rule is unknown, the app says Check manually. ReceiptJar starts that way, because its rules are only in its app.

**Close:** Spotted a rule change? Email us and we'll update the file.

## 12. "No iPhone?"

**Bridge:** Android first, and Australia only. An iPhone version may come later, but it has no date.

**When to stop:** Thank them. Don't collect emails for an iPhone waitlist unless the user approves one.

---

## Two points to make before anyone asks

Put these into the onboarding screens, the website FAQ and the first forum post:

1. **Once per app, by their rules.** "Each receipt goes to each app once, and only if it meets that app's published rules." This answers objections 1 and 11 before they come up.
2. **How it's paid for.** "One ad after you submit. Receipts stay encrypted on your phone. No provider passwords, ever." This answers objections 3, 4 and 5.

## Recording answers (beta)

Log each conversation against the Task 2 validation criteria:
- uses 2+ apps per receipt (Y/N)
- has missed a deadline or had a rejection (Y/N)
- would accept a small ad (Y/N)
- has been flagged or banned (Y/N, and what was said)

Publish these numbers as proof only with the user's approval.
