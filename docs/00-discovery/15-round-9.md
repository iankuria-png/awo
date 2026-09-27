# 15 · Round 9: connecting the pieces, and everything around the app

> **Status:** All six batches published, 27 Sep 2026, and waiting on Ian's reactions. Round 9 lives on the **Round 7 board** (D-042): every board is in its topic section, beside the screens it changes, marked "(Round 9)". There is no separate Round 9 page any more.
> **Ian's brief (D-041):** Build these, in batches, end to end with world-class UI and UX: the 30-day loop as one flow; sharing to WhatsApp; help and support, plus one search; Hub tools 10 to 18; a stokvel or chama record book; desktop and tablet layouts, a WhatsApp check-in and a USSD menu; components (sheets and dialogs, toasts, a date picker, file upload, loading placeholders, a two-currency input) and an empty-state set; emails; print (an A5 flyer and a workshop slide template); mockups in real places; social (carousels, WhatsApp status cards, podcast art); and merchandise (a money notebook, a check-in calendar or magnet, stickers, pins, a tote bag and ambassador T-shirts).
> **Language:** Round 7's, as Round 8 used it: Geist for all type, Kalam only in someone's own words or AWO's short note at a real milestone, corners 6, 10 and 14 and a circle, one colour and shape per area, and the Round 8 tab bar (Home, Learn, Hub, Community, Me).
> **Generator:** [`design/round-9/`](../../design/round-9/README.md).

## The batches

| Batch | What it holds | State |
|---|---|---|
| 1. The loop as one flow | The flow board; the reminder on the lock screen; notifications; what changed; this month's step; a milestone and sharing it; three WhatsApp status cards; one search; help; reporting a problem | Published |
| 2. The rest of the Hub | All tools; sending money home; a loan's real cost and "explain my agreement"; is it worth it; two job offers; business setup; what I own and owe; the retirement pulse; a savings-group record book | Published |
| 3. Other channels and sizes | Home and the DIVA profile on a computer; Learn on a tablet; the check-in on WhatsApp and USSD; one question in every channel | Published |
| 4. Components | Sheets and dialogs, toasts, a date picker, file upload, loading placeholders, a two-currency input; empty states made from the five shapes | Published |
| 5. Around the app | Emails; an A5 flyer and workshop slides; mockups in real places; carousels, status cards, podcast art | Published |
| 6. Merchandise | A money-in-and-out notebook; a check-in calendar or magnet; stickers and pins; a tote bag; ambassador T-shirts | Published |

## Batch 1: the 30-day loop, end to end

Each screen of the loop existed, but nobody had looked at them in order. Laid out as one flow (`R9-Loop-Flow`), six gaps showed, and batch 1 closes them.

| Gap | What closes it | Board |
|---|---|---|
| The check-in ended on Me, where nothing said what had changed | **What changed:** version 4, the DIVA score and its change, what moved in each area against where September was, and the reason in reviewed words. A preview switch shows a month that went down: the decreases are grey, and the reason is kind ("Your safety net paid for the car repair. That's what it's for.") | `R9-What-Changed` |
| There was a first step, but no step for each month after it | **This month's step:** last month's step recapped, four reviewed steps for her focus (one suggested), a payday reminder, and the next 30 days | `R9-Next-Step` |
| A reminder disappeared once it was swiped away | **Notifications:** the check-in stays on top until she does it; replies, cheers, the word of the week and method changes in one list, filtered by her money or her circles. Home gets a bell with the count | `R9-Notifications`, `R8-Home` |
| Milestones stayed inside the app | **A milestone, and sharing it:** four check-ins in a row, a live preview of the card, her first name on or off, and amounts, score and stage locked off. Share to her circle, WhatsApp status or chat, or save the image | `R9-Milestone` |
| Missing a month had no kind way out | **The reminder** on the lock screen: Start, Tonight, or Skip a month ("Nothing is lost"). No amounts, ever, on the lock screen | `R9-Lock-Reminder` |
| Help and search had no home | **One search** across Words, lessons, tools, circles and help, with filters and a kind "nothing found" that offers Ola. **Help** by topic, "Is AWO giving me advice?" first, a person to talk to, and a scam warning. **Report a problem** with a screenshot whose amounts are hidden by default | `R9-Search`, `R9-Help`, `R9-Help-Report` |

The check-in (Round 7's) now ends on "See what changed", so the loop runs without a break.

**Three WhatsApp status cards** (1080 by 1920): a milestone, the word of the week and a Rise story. They are how AWO travels in her world, and they test the privacy rules: no amounts, no score, no stage, and a member's words only in her own hand.

**Choices worth checking:**
- The milestone is about showing up (four check-ins in a row), never the score. Results still get no burst.
- The score in the sample moves by one point while the area she worked on moves by five. What changed leads with that, so a small number doesn't read as failure.
- "Stage 3 starts at 65" uses the sample stage boundaries from AWO Admin; the real ones are AWO's.
- Sharing opens WhatsApp with the image; AWO never learns who views it.

**Open:** Q-46 asks what a member may share outside AWO. The proposal is milestones about showing up and learning, never amounts, the DIVA score or the stage.

## Batch 2: the rest of the Hub

The Hub's "All 18 tools" button went nowhere; it now opens **All tools** (`R9-Hub-All`), grouped by the job each tool does and filtered by Me or My business, with the new ones marked. Every new tool keeps the six beats of the tool skeleton, and each is linked from the Hub.

| Tool | Sample | The one plain result | Choices worth checking |
|---|---|---|---|
| **Sending money home** (`R9-Tool-Remit`) | Amara, a nurse in London, sending to her mother in Harare | How much arrives with each of her two quotes, and what each really costs: the fee plus what is hidden in the rate | She types the quotes; AWO never names, ranks or links a provider. A quote with no fee can cost the most. The mid-market rate is a dated sample |
| **A loan's real cost, and explain my agreement** (`R9-Tool-Loan`) | Naledi, R 8 000 over 12 months | Everything she would pay back, split into what she borrows, interest and fees; the same over another term | The agreement is read by AI against a list AWO reviews: lines worth asking about, with the question to ask. It never says whether to sign. "Or save for it" shows the saving route |
| **Two job offers** (`R9-Tool-Offers`) | R 18 500 basic against R 21 000 cost to company | What reaches her each month under each offer, and what goes into her pension, kept apart | Switches for the medical aid she would pay and the commute. The rest (the work, the people) is hers to weigh |
| **Retirement pulse** (`R9-Tool-Pension`) | Naledi, 31, R 42 000 in her fund | What her fund might pay each month, in today's money | An illustration with three growth rates, never a promise. Notes the two-pot system as a dated fact |
| **What I own and owe** (`R9-Tool-Owe`) | Her pools and stokvel against her debts | The gap, with and without her pension | Private, never used for the DIVA score (sample policy). Below zero is framed as normal while paying debt down |
| **Is it worth it?** (`R9-Tool-Worth`) | Wanjiru and a second-hand sewing machine | Weeks until it pays for itself, with the slow weeks as a switch | Bars stay grey until the machine has paid for itself |
| **Business setup checklist** (`R9-Tool-Setup`) | Kenya or South Africa | Steps done, and the next one | Every fact is dated (Q-41); "general guidance, not tax advice" |
| **Savings group book** (`R9-Group-Book`) | Kopano stokvel: 10 members, R 500 each, the pot on the 5th | Who has paid, whose turn it is, and the payout order | AWO never holds, moves or promises the money, and says so on the screen. The group's rules are in its own words. A gentle WhatsApp reminder, and the month's record to share. Waits on Q-45 |

## Batch 3: other sizes and channels

| Board | What it shows | Choices worth checking |
|---|---|---|
| **Home, on a computer** (`R9-Desktop-Home`) | The five areas down the side (each in its own colour when chosen), then search, notifications and help. Three columns: this month's step and goals; the DIVA profile and the Hub's next useful thing; wins, the circle's question and the next lesson. Below: the next 30 days, and where she left off | A wide screen shows more at once, never more per card: every card is the phone's, placed side by side |
| **Your DIVA profile, on a computer** (`R9-Desktop-Me`) | Stage, score and what it means beside the four areas and the versions line; compare and the PDF report one click away | The September marker stays on each bar |
| **Learn, on a tablet** (`R9-Tablet-Learn`) | A rail, the path's lessons, and the lesson itself side by side, in Learn's night colours, with Ola | Arrow keys move between cards |
| **The check-in on WhatsApp** (`R9-WhatsApp-Checkin`) | Three questions as reply buttons and a list of five amounts, then a link to what changed | "Only you and AWO see your answers"; HELP and STOP; she can delete the chat. A sample of the channel (Q-21) |
| **The check-in on USSD** (`R9-USSD`) | A feature phone to dial through, every screen with its character count, and the SMS that follows | 160 characters a screen, numbers only, three questions because sessions are short. No amounts or score by SMS |
| **One question, every channel** (`R9-One-Question`) | The question written once (its label, five answers, what it feeds, its rules) and drawn four ways: app, web, WhatsApp and USSD | Doc 02's "one question graph, many renderers", made visible |

## Batch 4: components and empty states

Two boards of live components, each working inside a phone-width frame with the rules it follows (`R9-Comp-Overlays`, `R9-Comp-Inputs`), and ten empty states (`R9-Empty-States`).

| Component | The rules it follows |
|---|---|
| **Bottom sheet** | For a short task or a choice without leaving the screen. A handle, a title, one main button; tap outside or drag down to close; focus moves in and back |
| **Are you sure?** | Only before something that can't be undone. The safe choice is the main button; the deletion comes second, in wine. It says what goes and what stays ("The R 1 900 stays where it is") |
| **Toasts** | One line at the bottom, gone after six seconds. Undo shows the time left. Offline and errors say what happens next; never red |
| **Date picker** | Weeks start on Monday. Her own dates are marked: payday, check-in, the stokvel pot. Quick picks. Every day is a 44-pixel target |
| **File upload** | Empty, reading, done and failed. Says where it is read and when it is deleted; a failure offers typing it in |
| **Two currencies** | Rand, pound, dollar, shilling and pula, for members at home and abroad. The rate and its date always show, called a sample; never says where to change money |
| **Loading placeholders** | The shape of what is coming, so nothing jumps; a slow shimmer, still with reduce motion; only after half a second |

**Empty states** are drawn from each area's shape: the pool waits for its first drop, a moon for a saved lesson, the Hub's keystone hovers over its arch, the circle's ripple is quiet, the stones wait for the next step. There is one each for search, notifications, offline, a new savings group and an error. Each says what to do next, with one button.

## Batch 5: around the app

Everything here follows one rule from batch 1, carried off the phone: **no email, print or shared image shows an amount, the DIVA score or the stage** (Q-47 asks Ian to confirm it for email and print). Each piece has one main action and says what AWO isn't.

**Three emails** (`R9-Email-Welcome`, `R9-Email-Reminder`, `R9-Email-Summary`), each shown on a computer (600 wide), on a phone in a light or dark mail app (the phone scrolls), and as it appears in her inbox, with the subject and preview counted.

| Email | When | What it does | Choices worth checking |
|---|---|---|---|
| **Welcome** | A few minutes after she joins | "Your first step is ready", three things to try this week, what AWO is and isn't, and a scam warning: AWO never asks for a PIN, password or payment | If she stopped halfway through the first check, it asks her to finish instead (a switch on the board) |
| **Check-in reminder** | Her check-in day, at her time, only if she hasn't checked in | The same three choices as the lock screen: start, tonight, or skip with nothing lost; last month's step without its amount; what happens next | Email reminders are her choice; a push reminder is the default (sample) |
| **Monthly summary** | The 1st, for the month before | Counts what she did (lessons, words, steps, cheers), the four-in-a-row streak, "your profile has a new version", the words she saved, what's coming | A quiet month gets no email, never a "we miss you" |

In a dark mail app the green band stays, the page goes night and the button turns lime, so the app has nothing to invert.

**Print.** The **A5 flyer** (`R9-Flyer-A5`) has one front for each audience (church groups, campuses, stokvel meetings) and one back: the loop as three questions, what AWO isn't, and lines for the organiser to write her group, time, place and name by hand. A switch shows it photocopied in black and white. The QR code is real and scannable but only says "AWO sample QR code. The real link is still to come." The **workshop slides** (`R9-Workshop-Slides`) are eight layouts with speaker notes (title, today's three questions, a big idea, a money word, talk in pairs, a story, try it, close) and rules for whoever presents: nobody shares an amount out loud, and no bank, product or provider is named as the one to choose.

**The app in real places**, each a stock photo (or a drawn table) with a live screen, and what the place asks of the design:

| Place | The condition to try | What it changed or confirmed |
|---|---|---|
| **A market stall** (`R9-Place-Stall`), Wanjiru in Nairobi | Full sun | Amounts at 7:1 contrast; a sale added in one tap; the notebook works offline; an eye to hide amounts from customers (proposed) |
| **A commute** (`R9-Place-Commute`), Amara in London | The Underground, no signal | Saved words and downloaded lessons work offline; "where you live" gives her the UK example |
| **A kitchen table** (`R9-Place-Table`), Naledi's printed September report, with her own note in pen | Photocopied | Labels carry the meaning, not colour; the page says what the score is; a "My notes" box next (proposed) |
| **A lock screen** (`R9-Place-Lock`), in a real hand | A dark room | Four words say what it is, then how long; Tonight and Skip work from the notification |

**Social.** Two carousels at 1080 by 1350, each with its caption and alt text for every slide: **the DIVA score, explained** (what it looks at, the stage, "It is not a credit score", how it changes) and **before you sign for a loan** (four lines to find, with the same sample loan as the Hub's tool, and a sample line of agreement wording). Two more **status cards**: this week's question in the circles, and a two-second quiz (which loan costs more in all). **The AWO Podcast** gets cover art (Learn's moon in lime on night, checked down to 55 pixels) and episode tiles, each guest in the same arch.

**Choices worth checking:**
- The quiz card and the loan carousel show sample loan amounts. They are general examples, never a member's own money, and match the Hub's loan tool.
- The mockups are composites and say so on the board. Real photography of members, with their consent, is still to come (the Unsplash account is waiting on T-025).
- Podcast guests are samples; real guests would sign a release that says where their story and photo appear.

## Batch 6: merchandise

Things members and ambassadors hold, wear and stick on the fridge. The five shapes do the branding; Africa is in who uses them and what they say, never in patterns, maps or flag colours.

| Piece | What it is | Choices worth checking |
|---|---|---|
| **Money in and out** (`R9-Notebook`) | The Hub's business notebook on paper, A6: a cover with a label she fills in, a week to a spread (each day's in and out, the week's sums, what sold twice, what happened), a month page with bars she colours in by hand, and a back cover pointing to the app. Wanjiru's sample week matches her notebook in the app (KSh 25 700 in, KSh 10 000 out); a switch shows the blank pages | The currency is written once a week, so one book works in any country. Given or sold, and printed where (Q-48) |
| **The check-in on the fridge** (`R9-Checkin-Magnet`) | A magnet with twelve stones, January to December, ticked by hand (tap them), and "My check-in day" written in marker. Beside it, a year she prints from the app: her next twelve check-ins and the dates she added (her stokvel), Monday-first | The magnet is the same for everyone. The printed year shows dates only, because it hangs where everyone can see it |
| **Stickers and pins** (`R9-Stickers-Pins`) | The five shapes as die-cut stickers and 25 mm enamel pins, each in its area's colour, plus word stickers ("I checked in", "Ask me about AWO", the word of the week) | Silver or black nickel; gold reads as luxury. No sticker shows a number |
| **A tote bag** (`R9-Tote`) | Heavy cotton in evergreen, night or mist, printed with the stones ("One step at a time") or the five shapes ("Money, understood."); an inside pocket for the notebook | No natural-canvas cream. One or two colours, for a local screen printer |
| **Ambassador T-shirts** (`R9-Tshirts`) | Front: the mark, small. Back: "Ask me about AWO". A name badge says what an ambassador can do (show the app, run a workshop) and can't (give financial advice, ask for a PIN or money) | The shirt never says "Ask me about your money". There is no ambassador programme yet (Q-48) |

**Open:** Q-48 asks whether AWO will have ambassadors, what they may say and hand out, and whether merchandise is given or sold, and made where.
