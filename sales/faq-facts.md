# ReceiptRelay FAQ facts

The approved facts for every shopper answer, store listing, forum reply and partner talk. Source: `ideaOutput.md` (2026-11-21) and `docs/WEBSITE-PLAN.md` section 5. If a fact is missing here, leave it out. Don't fill the gap.

Status on 2026-11-23: the app is still to be built. The website is built but not public. Testers will come in through the Play internal testing track, and the APK will be published on GitHub Releases. Write about the app in the present tense only once it ships. Until then, write "will" or "is being built".

## The product

| Fact | Approved wording |
|---|---|
| What it is | A free Android app for Australian shoppers that checks one receipt against the rules of Shping, ShopBack and ReceiptJar, then guides you to claim it in each app. |
| Where | Australia only. |
| Platform | Android only. There is no iPhone app yet. |
| Providers at launch | Shping, ShopBack, ReceiptJar. |
| How claiming works | ReceiptRelay hands your receipt to each provider's own app. You submit it there, then tap "I submitted it". |
| ShopBack hand-off | Uses the Android share sheet. |
| Shping and ReceiptJar hand-off | The app saves the receipt file, opens the provider's app and shows the steps. |
| Receipt capture | A camera photo, or a PDF or image shared in. The original file is kept unchanged: no crop, no enhancement, no compression. |
| Store, date, total | You pick the store from a list and type the date and total. There's no OCR. |
| Eligibility results | Eligible, Not eligible (with the rule that failed, for example "over 7 days for Shping"), or Check manually (when a rule is unknown). |
| Duplicate blocking | Each receipt is fingerprinted (SHA-256), so the same file goes to each provider once only. |
| Claim tracker | Not started → Submitted → Pending/Tracked → Confirmed/Paid, or Rejected (with the reason) or Expired. |
| Reminders | A reminder before each provider's deadline. |
| Totals | Totals per provider. |
| AI | None. The rules are fixed code and every result can be explained. |

## Provider rules the app checks (as published by each provider)

| Provider | Max receipt age | Caps | Other | Confidence |
|---|---|---|---|---|
| Shping | 7 days | 2 per store per day; 5 per store per 7 days; 100 per month | Accounts can be flagged below the monthly cap (Shping FAQ) | Published FAQ: https://shping.com/faq/ |
| ShopBack | 28 days | 30 attempts per week per sharing method; a daily per-store cap exists with the number unpublished | One eligible receipt per transaction, whatever the method | Published T&Cs: https://support.shopback.com.au/hc/en-gb/articles/45068630719251-ShopBack-Receipts-Terms-and-Conditions |
| ReceiptJar | **Don't publish a number.** A third-party review says 14 days; this is unconfirmed | Weekly cap; threshold unstated | A repeat shows as "receipt already in ReceiptJar" | No public T&Cs. Check the in-app terms before quoting anything |

Shopper-facing wording for ReceiptJar until its rules are confirmed: "ReceiptJar's rules are in its app. ReceiptRelay shows Check manually where a rule is unconfirmed."

Rules belong to each provider and can change. Each rule file records the provider's terms URL and a review date.

## Stacking (sending one receipt to several apps)

| Fact | Approved wording |
|---|---|
| Basis | We read each provider's published terms and found no clause against sending a genuine receipt to more than one rewards app. |
| Limit | Once per provider, per genuine receipt. Never twice to the same app. |
| What we can't promise | Any provider can change its terms or reject a receipt. ReceiptRelay can't guarantee approval, and its makers aren't lawyers. |
| ShopBack wording to know | ShopBack's fraud definition covers activity meant to "duplicate or artificially obtain rewards". Sending the same purchase to ShopBack twice would be that. Sending it once to ShopBack and once to another app is what we checked the terms for. |
| Don't say | "Allowed by every provider", "approved by ShopBack", "100% safe", "no risk of a ban". |

## Accounts and passwords

| Fact | Approved wording |
|---|---|
| Sign-up | None. There is no account: install, scan, claim. |
| Provider passwords | Never asked for, never stored. |
| Automation | ReceiptRelay never logs in to, scrapes or automates provider apps (no Accessibility Service). |
| Who submits | You do, in each provider's own app. |

## Privacy and security

| Fact | Approved wording |
|---|---|
| Where receipts live | On your phone, encrypted. Receipts aren't uploaded to ReceiptRelay servers. |
| Encryption at rest | Database: SQLCipher. Receipt files: AES-256-GCM (Tink). Keys are held in Android Keystore (StrongBox where the phone has it). |
| In transit | TLS 1.3 with certificate pinning; cleartext traffic is off. |
| Logs | No plaintext logs. |
| Standards | Never write "ISO 27001 certified" or "SOC 2 certified". The most you may write is "built to align with ISO/IEC 27001:2022 and SOC 2 controls", and only if marketing wants that line. Certification would mean an audit that hasn't happened. |

## Ads and money

| Fact | Approved wording |
|---|---|
| Price | Free. There's no paid tier and no ad-free upgrade. |
| Ads | One native ad on the "Submitted" screen after you claim, plus an optional rewarded "support us" ad you choose to watch. |
| No | No banners, no interstitials (full-screen pop-ups). |
| What ads see | The ad code never runs on a receipt screen and never gets receipt data. Receipts are never sold or shared. |
| Consent | Google UMP consent screen, with a non-personalised ads option. |
| Disclosure | A "How we make money" screen in onboarding and in settings, and a page on the website. |
| Referral links | Not decided. If they're ever used, they go on the "How we make money" screen. |
| Rewarded ad reward | Nothing beyond supporting the app is specified. Don't promise a reward. |

## Affiliation

- ReceiptRelay is independent: no affiliation, endorsement or partnership with Shping, ShopBack or ReceiptJar.
- Use provider names in text only. Don't show provider logos until there's written permission (WEBSITE-PLAN section 6, decision 1).
- Link to provider apps on Google Play only, never through APK mirrors.

## Facts never to state (not in the source)

- User counts, download counts, ratings, reviews, testimonials, earnings per user, approval rates or ban rates.
- Any amount per receipt, or average earnings. The one figure in the source is a UK guide's "~£0.50 a week for 5 receipts a week across apps". It's foreign and third-party, so use it only in internal notes.
- Any provider partnership, endorsement or API integration.
- Release dates.
