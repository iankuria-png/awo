# 13 · Round 7: Geist, a hand, and tighter corners

> **Status:** Published on canvas page `r7` (Round 7), 25 Sep 2026. Every board was rendered and clicked through locally before publishing (D-026). Generator: [`design/round-7/`](../../design/round-7/README.md).
> **Ian's brief (D-032):** "Experiment with this typeface (Round 1's Oasis board, Geist), only a few handwritten fonts for those special moments, and a more restricted border radius."
> **Carried in from Round 6 (D-031):** app icon A (stepping stones); Home stays as it is.
> **Update, same day:** Ian found Vault, Me and Community the weakest. They were redesigned natively; see [Vault, Me and Community, redesigned](#vault-me-and-community-redesigned).
> **Then:** Round 7 became the full reference board (D-034), with Geist and Kalam confirmed and marketing moved over (D-033); see [Round 7 as the full board](#round-7-as-the-full-board).

## How it was built

Round 7 is the Round 6 screens with three changes applied as a transform. The content, flows and interactions are identical, so the two pages compare fairly.

| Change | Round 6 | Round 7 |
|---|---|---|
| Display type | Bricolage Grotesque 800, condensed to 82% | **Geist 600**, tracking −0.045em, at 86% of the old sizes. Geist already carried the body text |
| Handwriting | none | **Kalam** by default. Nanum Pen Script and Delicious Handrawn are a Tweak on every board |
| Corners | seven radii (16 to 44) plus pills | **6, 10, 14 and a circle**. Bars and tracks get 2px ends |

## The special moments (the only handwriting in the app)

| Screen | Moment | Whose voice |
|---|---|---|
| Welcome | "start here", with an arrow to the first stepping stone | AWO |
| Starter check | "Here's where you start." above the first stage | AWO, at a milestone |
| Home | Each win's story text | The member's own words |
| Home | "Done for this week. Nicely done!" when the step is finished | AWO, at a milestone |
| Learn | "You showed up three evenings this week." | AWO |
| Community | Her answer to the week's question, once shared | Her own words |
| Vault | "See you tomorrow." at the end of a practice round | AWO, at a milestone |
| Check-in | "One month, kept." when the 30-day check-in is done | AWO, at a milestone |
| Marketing | Her answer on the Community store screenshot; Amara's line on the story ad | Members' own words |

**These stay typeset on purpose:**
- **Me:** results, scores and stages.
- **Ask:** anything Ola or AI writes. Handwriting would pass machine text off as a person's.
- **Vault:** definitions.

**The rules:**
- Handwriting is only for someone's own words or AWO's short note at a real milestone.
- Never for numbers, buttons or instructions.
- Never under 20px.
- At most one line on a screen.
- Always real text, so it can be read aloud and translated.
- `font-size-adjust` keeps the three candidate faces at the same apparent size, so switching faces doesn't reflow layouts.

## The corners

| Radius | Used for |
|---|---|
| 6 | Chips, tags, small controls, the tail corner of a speech bubble |
| 10 | Buttons (no more pills), inputs, list rows, tab pills |
| 14 | Cards, bento tiles, hero blocks, sheets |
| Circle | Faces, dots, story rings and the five shapes. The pool stays a capsule |

## Choices for Ian to check

- **Which hand** (Q-33)?
  - **Kalam:** the most legible at 20 to 30px; warm, grown-up.
  - **Nanum Pen Script:** most like a real note, but loose.
  - **Delicious Handrawn:** a bold marker, better for ads than the app.
- **Geist in marketing:** the store screenshots and ads are still Round 6 (Bricolage). Moving them is a regenerate once the type is settled.
- **Buttons are no longer pills.** With 10px corners they read more "tool", less "toy". Round 1's Oasis board used pills, so that's worth a look.
- **Candidates rejected:** Caveat (seen everywhere) and Playpen Sans (reads as a font, not a hand). The Fonts connector only suggests commercial faces, and the canvas loads Google Fonts only.

## Self-check notes

All ten boards rendered without broken bindings, text under 12px or touch targets under 44px. The transform keeps circles and rings round: an element stays a circle when it is square or sized to fill its parent. One label wrapped on the type board and was shortened.

## Vault, Me and Community, redesigned

**Ian's reaction:** "These three pages are currently the weakest in terms of hierarchy, design and overall UI/UX. They look a bit generic and text-heavy (Community is not that bad)."

**What was wrong:** each screen was a stack of white cards and text rows with the same weight. Nothing led, so the eye had nowhere to land. The area's shape (arch, stepping stones, ripples) was barely there, so the screens could have belonged to any app.

**The fix:** each screen now opens with its area's shape doing a job, has one thing to do, and pushes detail one tap deeper. They are written natively in Round 7 style (`design/round-7/areas7.py`) rather than transformed from Round 6, because the layouts changed as well as the styling.

| Screen | Leads with | Then | Moved out of sight |
|---|---|---|---|
| **Vault** | The word of the week on a lime **arch** card: word, how to say it, one line of meaning. "See an example" flips it | An evergreen strip, "3 words to practise, about two minutes", opens a practice deck: show the meaning, then "Not yet" or "I knew it". It ends with "Three words, practised." and the handwritten "See you tomorrow." | The long list of words. Kept words sit in four **collections** (Saving together, Borrowing, Business, Sending home) shown as stacked-card tiles; open one to see its words |
| **Me** | A pool block: **Stage 2** big, "of 4 stages", a small readiness ring, and the **stepping stones** with her face on stone 2. One sentence, "Learning readiness, not a credit score.", and a Sample label | "Your shape": four bars. Tap one to read a sentence about it, with its DIVA name and weight. Evidence gets its own card and meter, separate from the score. "Your versions" is a sparkline with the next check-in dashed | The full interpretation, behind "What this means, in full", with "Explain it more simply" labelled AI-assisted. The screen is 1330px tall (was 1720) |
| **Community** | The week's question on blush, with one answer from Thandi, then hers, handwritten once shared | "Your circles" as swipeable cards with faces, ripples and "2 new" (Safety net opens Round 4's "being seen" moment). A photo-first story from Wanjiru with Cheer | A dark event card with "Remind me" closes the screen |

Unchanged: the rules. Results, scores and AI text stay typeset; the hand appears once per screen at most; evidence stays separate from the score.

**Self-check:** all three boards rendered with no broken bindings, no text under 12px and no touch targets under 44px. The Me heading was reworked after the first render: "Stage 2 of 4" in one line was too wide, so it became "Stage 2" with "of 4 stages" beside it.

## Round 7 as the full board

**Ian's brief (D-034):** "Let's add these pages and components to the Round 7 artifact, now made to fit our Round 7 design language. I want Round 7 to be a full board, which we will use for UI/UX inspiration and references." His screenshots showed Round 2's brand boards (wordmark, icons, motion) and Round 3's screens, components and marketing. In the same message he confirmed: keep Geist and Kalam, and move marketing over (D-033).

**The page, top to bottom:**

| Row | Boards |
|---|---|
| Foundations and brand | Type and corners, Foundations (colour, shapes, people, space), Brand (app icon A, the wordmark in Geist), Icons, Motion (M1 to M6, live) |
| The app | Welcome (photo-led), Welcome (three slides), What brings you here, Starter check, Home, Learn, Ask, Vault, Community, Me |
| Inside the areas | Your progress, the 30-day check-in, Your buddy, Settings |
| Components and widgets | Components (controls), Data and feedback, Widgets |
| Marketing | Eight store screenshots (Community is photo-led; the check-in is new), the listing with descriptions and store rules, the feature graphic, the 512 icon, the device hero and four ads |

**The screens link up:**
- The photo-led welcome leads to "What brings you here", then the starter check.
- Me opens Progress (from "Your versions") and Settings.
- Progress opens the check-in, which ends back on Me.
- Community opens the buddy (her face, top right).

**Choices worth checking:**
- **Progress:** each version is a stone, rising with readiness. Tap one to see its date and value. "What moved" shows the old value pale and the gain dark. Evidence keeps its own meter.
- **The check-in:**
  - The pool fills as she drags the amount.
  - Answering "Not this time" gets "Thanks for saying so. It still counts as a check-in."
  - At the end a new lime stone appears with her face on it, and the hand says "One month, kept."
  - It shows no new score. Scoring happens on the server, so the new version appears on Me.
- **The buddy:** the shared goal shows lessons only, never amounts.
- **Settings:** reduce motion and larger text work live, in the rows themselves.
- **Controls:**
  - Switches have a 10px track and a 6px thumb.
  - Radios stay circles; checkboxes are squares with 6px corners.
  - Warnings and deleting use wine, never red.
- **Brand:**
  - App icon A stays as chosen.
  - The lockup is the stones mark beside "awo" in Geist 600. It is a working lockup while the wordmark stays open (Q-25).
  - The mark stops at 20px, where the stones merge.
- **Icons:** they stay geometric. Round 2 drew them by hand, but in Round 7 the hand belongs to people's words.
- **Motion:** M1 to M6 are live cards. Turning reduce motion on pauses every loop on the board.
- **Marketing:**
  - Everything is built from 2x captures of the Round 7 screens.
  - Corners scale with the canvas: 14 at phone width becomes 40 at 1080.
  - The hand appears only in members' own words.
  - Exports are in `design/marketing/round-7/`.

**Self-check:** every new board was rendered and clicked through, with no broken bindings, no text under 12px and no touch targets under 44px. The renders caught and fixed these problems:
- a tooltip covering a stone;
- a cramped amount chip;
- a flat check-in ending (it now adds a new stone);
- the Learn tab label vanishing on a light bar;
- the buddy link crowding the Community title;
- the photo ad's headline running under the photo;
- 256-colour exports banding the photos.

## Screens still to design (proposal, for Ian to prioritise)

Ian asked which other screens matter, starting with sign-in and an admin dashboard. The list below comes from the core loop, the IA in [02](02-product-shape.md) and the open questions. It is ordered by what blocks a first release.

| Batch | Screens | Why now | Open questions it touches |
|---|---|---|---|
| **Accounts and the first loop** | Sign up, verify (code or link), sign in, recover access, consent and privacy, country and currency, notification priming; then the first result reveal and "choose your first step" | Nobody gets into the app without these, and "What next? One step" is the loop's third beat | Q-18 (email or phone), Q-04, Q-05 |
| **Learning and the loop, deeper** | Lesson player (story cards, quiz, finish), the DIVA report and comparing two versions, a what-if simulator, "Check an offer", the hard moments (missed check-in, coming back, a month that went down, offline, errors, day one) | Learn has a hub but no lesson; Me has versions but no report; the hard moments shape trust | Q-26 |
| **Entrepreneurs** | Business profile, venture assessment, a business view of Home | D-018: individuals and entrepreneurs matter from day one, and nothing is designed for them yet | Assessment content is AWO's to supply |
| **Community, deeper** | A question thread, the composer, a circle's page, reporting a post, events | Moderation starts here; members need a way to flag scams | Q-32 |
| **AWO Admin (desktop)** | Overview, members and data requests, interpretation library (versions and approvals), scoring versions (read-only diff, publish), content review, moderation queue, AI log, audit log | Sequenced late (D-009), but designing it now shapes the data model and the "server-side, versioned, auditable" promise | Who approves what, and how many people sign off |
| **Public website** | Home, how DIVA works, a public Vault term page, for entrepreneurs, diaspora, privacy | The public Vault is the search entry point | Q-31 |
| **Later channels** | A WhatsApp check-in and a USSD menu drawn from the same question graph | Proves "one question graph, many renderers" | D-009 |

## Batches 1, 2, 3 and 5 (D-036)

Ian picked accounts and the first loop, the deeper loop, entrepreneurs and AWO Admin, "so that you can focus completely on great world-class UI/UX". Sign-in is phone first, with Google and Apple (D-035).

| Batch | Screens | Choices worth checking |
|---|---|---|
| **Accounts and the first loop** | Sign in, the code, about you, consent, the result reveal, choosing a first step, reminders, a PIN lock, welcome back | Phone first: there's no password. Consent keeps its optional switches off. Reminders are asked for after the first step, when she knows what they're for. A PIN because phones get shared. The reveal carries no burst: results are not prizes. |
| **The loop, deeper** | Lesson player, compare versions, what-if, check an offer, the one-page report, hard moments | Ola speaks reviewed lesson text, so it is labelled "Reviewed by AWO", not AI. "Check an offer" never says an offer is safe and points to the FSCA register. Decreases are grey. The what-if tools are labelled as illustrations. |
| **Entrepreneurs** | Business profile, business check, business Home | The check's questions are samples, and it says it is not a loan or credit decision. The notebook holds her own notes, not bank data. |
| **AWO Admin** | Overview, approvals, scoring, members, moderation, lessons and Vault, audit and AI log | See the guidance below. |

## AWO Admin: the patterns, and why

Ian asked for guidance on approvals and for a world-class dashboard. These patterns come from tools that small teams trust with serious data.

| Pattern | Borrowed from | On AWO Admin |
|---|---|---|
| **Inbox first** | Linear, GitHub notifications | The overview opens on "Needs you", with one clear action per row. The charts come after. |
| **Two people for results (maker-checker)** | Banking's four-eyes rule, GitHub pull-request reviews | Interpretation text and scoring need two approvals, and the author can't approve their own change. The reviewer sees a line-by-line diff, automatic checks (plain words, no advice words, complete), where it shows, and a preview. "Request changes" needs a note. |
| **One reviewer for teaching content** | Content platforms (draft, review, publish) | Lessons and Vault words need one reviewer. AI drafts stay labelled until a person rewrites and approves them. Only published content says "Reviewed by AWO". |
| **Preview before publish** | Vercel preview deployments | A scoring draft runs against 200 fixed, made-up test profiles and shows who would move stage. Real members are never used, and past results never change. |
| **Private by default** | Stripe, Okta | Lists show first names and member IDs. Amounts never appear. Revealing a phone number needs a reason, is logged, and shows in her own history. |
| **Keyboard first** | Linear, Superhuman | Cmd+K jumps anywhere. The moderation queue has single keys: K keep, H hide, R remove, J and K to move. |
| **AI flags, people decide** | Trust and safety teams | Every AI flag says why. The weekly "flags a person agreed with" figure tunes the flags, not the speed. |
| **Everything leaves a trail** | Audit logs in regulated software | The audit log can't be edited or deleted. The AI log keeps every output with the source it was allowed to use. |

**The approval rule is still a proposal (Q-34):** two people for results text and scoring, and one for lessons and words. The team roles (owner, content lead, community, support) are samples too.

## Round 8, on the Round 7 board

Ian asked for one full board with all his ideas, without replacing anything on Round 7. Every Round 8 board ([14](14-round-8.md)) is now also on page `r7`, as copies named `R7-R8-*`, below Round 7's last row, in Round 8's own rows. The copies link to each other. Page `r8` is unchanged. `design/round-7/pull8.py` refreshes the copies.

## The DIVA score in the marketing

Ian noticed the marketing never named the DIVA score. It does now, in both sets (Round 7's and Round 8's), on the first store screenshot, the listings, the feature graphics, the heroes and a new square ad each ("What's your DIVA score?"). The rule the copy follows: the score always says what it is, readiness to learn and never a credit score, and it is never put next to loans, credit or eligibility. The app still labels the number "Readiness" under "Your DIVA profile"; Q-44 asks whether both should say "DIVA score".

## The board, grouped by topic

Ian then asked for the board to be grouped by what the screens are, not by when they were made. Page `r7` now has 14 sections, top to bottom:

| Section | What's in it |
|---|---|
| Foundations, brand and the app's structure | Type and corners, foundations, brand, icons, motion; the Hub's icon and the five tabs (Round 8) |
| Onboarding | The photo-led welcome, the three slides, sign in, the code, about you, consent, goals, the starter check, the reveal, the first step, reminders, the PIN and welcome back |
| Home | Round 7's Home, Round 8's Home with several goals, the business Home, the goals studio and the hard moments |
| Learn | Both Learn tabs, the lesson player, the shares topic, the Vault, the word decoder and Ask |
| Learn: stories and companies | A Rise story, the AWO Podcast, "My worst money mistake", Companies explained, a company brief and a startup's rounds |
| The Hub, for a job | The tool skeleton, the Hub, the five Me tools, the what-if simulator and "Check an offer" |
| Business | The business profile and check, the Hub in business mode, pricing, invoices and Shop |
| Community | Round 7's Community, the buddy, the feed in parts, the feed, the composer and a thread |
| Me | Me, progress, the check-in, comparing versions, the report and settings |
| Components and widgets | Controls, data and feedback, widgets |
| AWO Admin | The seven desktop screens |
| Marketing (three sections) | Store screenshots, the listing set and ads, each with Round 7's row above Round 8's |

Round 8's copies keep their files and links; their titles end in "(Round 8)". `design/round-7/group7.py` reapplies the grouping and stops if any board on the page isn't in a section.

