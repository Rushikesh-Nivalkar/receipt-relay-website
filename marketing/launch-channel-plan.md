# Launch channel plan

Status: prepared, nothing posted. The website stays local (no domain) and the app is not built. Every step below starts only when its gate is met. Frameworks: Brian Wagner (signal first, one-to-one outreach, follow-up with something new, a clean exit) and Corey Haines launch strategy (owned, rented and borrowed channels; internal, alpha, beta, launch).

## Gates before any outreach

| Gate | Needed for | State on 2026-11-23 |
|---|---|---|
| G1: a test build installs and checks a real receipt | Any tester invite | Not built |
| G2: ReceiptJar rules confirmed in its app | Any post that names ReceiptJar limits | Open (never quote a number) |
| G3: real contact email | Every post and listing | `.example` stand-in |
| G4: privacy page live on a real domain | Store listing, public posts | No domain |
| G5: compliance review of ads disclosure and privacy wording | Public launch posts | Not run |
| G6: moderator answer for each community (below) | Posting in that community | Not asked |

## Channels (ORB)

| Type | Channel | Role | When |
|---|---|---|---|
| Owned | Website (`/`, `/download`, `/privacy`) | Explains the app, hosts the APK link and the ads disclosure | After G4 |
| Owned | Tester email list (testers only, opt-in) | Release notes, week-2 check-in | From the first tester |
| Rented | Google Play listing | Main install path once listed | After internal testing |
| Rented | OzBargain, Whirlpool, Reddit, Facebook saver groups | Find the first testers; answer questions | Phase by phase, below |
| Borrowed | Australian money-saving blogs and newsletters that review receipt apps | A review once the app is public | After launch, only on invitation or pitch with no payment |

## Community rules (check on the day; rules change)

| Community | What its rules say | How ReceiptRelay takes part |
|---|---|---|
| OzBargain | Declare any relationship with a business up front in the post body; posting as a customer while being the owner is sockpuppeting, which can also breach the Competition and Consumer Act; site operators may not post comments promoting their own site; store reps apply through the Talk With a Moderator forum | Ask in Talk With a Moderator first, with the disclosure wording and the free app. No deal post for your own app unless a moderator says yes. In threads, answer rule questions; mention the app only when asked, with "Disclosure: I'm building this app" |
| Whirlpool | The forum rules were not readable in research; most AU forums ban advertising without permission | Read the forum's own rules page and ask a moderator before any mention. Default: answer questions with no link |
| Reddit (Australian money and frugal subreddits) | Each subreddit sets its own self-promotion rule in its sidebar; some have a weekly self-promotion thread | Read each sidebar before posting. Use a weekly self-promotion thread where one exists; ask the moderators by modmail where it does not. Reply to rule questions without a link unless asked |
| Facebook saver and cashback groups | Each group's admins set the rules, usually "no promotion without admin approval" | Message the admins first with the disclosure and a test invite offer. Post only with written approval, once |

Rules for every channel:

- Always disclose: "I'm the developer" in the first line, every time.
- No sockpuppets, no friends posting as customers, no paid upvotes, no fake reviews.
- No referral links to any provider in community posts.
- No promise about bans, earnings or "stacking".
- Provider names in text only, never their logos.

## Phases

### Phase 1: internal test (after G1)

- Install on the developer's own phone and two or three people known personally.
- Log real receipts for a week. Fix anything that blocks a claim.

### Phase 2: first 10 testers (after G1, G2, G3, G6 for the channel used)

Weekly plan from ideaOutput Task 4:

| Week | Action | Measure |
|---|---|---|
| 1 | Find 20 people posting about rejections, caps or deadlines; message 10; recruit 5 | Replies, testers joined |
| 2 | Testers use the app; capture friction in their words | Receipts logged per tester |
| 3 | Fix what testers hit | Issues closed |
| 4 | Open the test to 50 | Week-2 return |

Outreach rule (Brian Wagner): every first message names the signal (the post the person wrote). Without a post to point at, send nothing. Scripts: `outreach-first-10.md`.

Success for this phase: 10 testers logging 5 or more receipts each; 3 or more back in week 2 unprompted; 0 provider bans.

### Phase 3: open test (after G4, G5)

- Put the website on its domain. Publish the APK release with its SHA-256 checksum.
- One post per approved community, on different days, each written for that community (drafts: `social-posts.md`).
- Answer every reply within that day.

### Phase 4: Google Play launch (after Play review)

- Store listing: `play-store-listing.md`.
- Update the website's download page to the Play link.
- Tell testers first by email, then one launch post per approved community.

## What to measure

- Receipts logged per tester per week.
- Week-2 return rate (target 30% or more, ideaOutput Task 5).
- Rejections reported by testers and the rule that failed.
- Any provider account flag among testers (target 0). One flag pauses outreach until the cause is known.

## Stop rules

- A provider changes its terms on multi-app receipts: stop posting, update the rule files, tell testers.
- A moderator says no: no further posts in that community.
- A tester reports a ban: pause outreach and review the rules for that provider.
