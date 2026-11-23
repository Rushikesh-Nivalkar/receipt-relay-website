# First 10 users: outreach messages

Status: drafts; nothing sent yet. Send only after gates G1, G2, G3 and the community's moderator answer (G6) in `launch-channel-plan.md`. Structure (Brian Wagner, cold outreach): a named signal, one reason to talk, one easy question, a follow-up with something new, a clean exit. Every message opens with the disclosure.

How to use: each message below is written for one kind of post. Change the app, the store and the detail to match the post you are answering. If there is no post to point at, do not send a message.

## 1. Reply to a post about a rejection over a cap

> Disclosure: I'm the developer of a free Android app for this. Saw your post about ShopBack turning down a receipt. ShopBack takes one receipt per purchase, and Shping caps each store at 2 a day and 5 in 7 days, which catches a lot of people. I'm building ReceiptRelay to check a receipt against Shping, ShopBack and ReceiptJar rules before you upload. Would you try the test build and tell me what breaks?

## 2. Reply to a post about a missed deadline

> Disclosure: I'm building an Android app for this. Your post about missing the Shping window is the exact case I'm working on: Shping allows 7 days, ShopBack 28. ReceiptRelay keeps each receipt in a list with the days left for each app and sends a reminder before the deadline. It's free and I'm looking for ten testers in Australia. Interested?

## 3. Reply to a thread asking which receipt apps people use

> Disclosure: I'm the developer of ReceiptRelay, so weigh this accordingly. The hard part with these apps is the different limits: 7 days and 28 days, plus Shping's per-store caps. I'm building a free Android app that shows those limits for each receipt and tracks each claim. Happy to share a test build if anyone wants to try it.

## 4. Direct message after someone asks for the test build

> Thanks for putting your hand up. Here's what testing looks like:
>
> 1. Install the test build from the link in this message (Android only).
> 2. Scan your receipts as normal for two weeks, five or more a week if you can.
> 3. Send each one to the apps you already use, through ReceiptRelay.
> 4. Tell me anything that is wrong, slow or confusing, in any words.
>
> The app is free. It shows one ad after you submit a receipt; your receipts stay on your phone, encrypted, and it never asks for your Shping or ShopBack password. You submit in each app under that app's terms, so follow their rules as usual.

## 5. Follow-up on day 7 (only with something new)

> Quick one: a new test build is out with the fixes testers asked for in week one, listed in its release notes. How many receipts have you logged so far, and did any of them get rejected?

(Send only when a new build with real fixes has shipped.)

## 6. Week-2 check-in (the discovery questions)

> You're two weeks in, thanks for sticking with it. Five short questions, answer any you like:
>
> 1. What do you do with a receipt after you get home?
> 2. Which apps do you send each receipt to, and in what order?
> 3. When did you last miss a deadline or get a rejection? What happened?
> 4. Roughly how much do these apps pay you a month?
> 5. Has any app ever flagged your account? What did it say?
>
> Your words go straight into the next build.

## 7. Exit message (day 21, no reply)

> Last message from me on this. If ReceiptRelay is the wrong fit, no problem at all; uninstalling removes every receipt from the phone. If you ever want the next build, reply here and I'll send it.

## Moderator and admin requests (send before any post)

### OzBargain: Talk With a Moderator

> Hi mods. I'm building ReceiptRelay, a free Android app that checks a receipt against Shping, ShopBack and ReceiptJar published rules and tracks each claim. It has one ad after a submission and no referral links. I'd like to ask for ten testers from the community. Is a forum post allowed, and is "Disclosure: I'm the developer" in the first line the right wording? Happy to follow whatever you prefer.

### Whirlpool, a subreddit, or a Facebook group admin

> Hi. I'm the developer of ReceiptRelay, a free Android app for Australians who use Shping, ShopBack or ReceiptJar. It checks each receipt against those apps' published rules and tracks each claim. May I post once to ask for testers, with the disclosure in the first line and no referral links? If not, I won't post.

## Tracking sheet (keep it private, outside this repo)

Columns: date, community, post answered, message number, reply, joined test, receipts logged, week-2 return, issues raised. No personal details beyond a forum handle.
