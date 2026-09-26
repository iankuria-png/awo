# Changelog: the project diary

> **Newest first.** Add an entry with every commit (or a tight group of commits). Say what changed, why, and anything the next session must know. A Claude Code hook blocks `git commit` when this file hasn't been touched; use `SKIP_CHANGELOG=1` only for trivial commits.
>
> Format: `### <short title>` under a date heading, with the commit hash once known, then 1–5 bullets.

## 2026-09-26

### Round 8 pulled into the Round 7 board
- Ian: "Pull in Round 8 into the Round 7 board. Do not replace items in the Round 7 board; we just want a full board with all my ideas." All 46 Round 8 boards are now on page `r7` too, as copies named `R7-R8-*`, linked to each other, in Round 8's own rows and section titles. They sit under a heading below Round 7's last row, with a note saying what they are.
- Nothing on Round 7 moved or changed, and page `r8` is unchanged. Checks run: every copy matched the live Round 8 file byte for byte before copying; no copy links back to `R8-`; four copies were rendered.
- This branch fast-forwarded to the Round 8 session's branch (`claude/intelligent-hypatia-ja9g5n`), so the docs remain one history.
- New `design/round-7/pull8.py` refreshes the copies if Round 8 changes.

### Round 8 batch 5: Companies explained and the marketing refresh
- **Companies explained, in Learn** (`design/round-8/companies8.py`), the safe version of Q-36: the path, with a standing line that AWO isn't paid to feature any company and six proposed editorial rules; a Safaricom brief (how M-Pesa came to earn about twice what calls do, what could go wrong, why AWO chose it), using figures from its results for the year to 31 March 2025 and labelled "Sample editorial, Q-36"; and a sample Lagos startup's funding rounds, where the founders own less of something bigger and a valuation isn't money in the bank. No share prices, no buy buttons.
- **Marketing in the Round 8 tabs** (`marketing8.py`): eight store screenshots, the listing (a 77-character short description), a feature graphic, a device hero and six ads, exported at exact size to `design/marketing/round-8/`. No ad names a company. `capture8.mjs` recaptures the screens they're built from, and `python3 marketing8.py specs` lists what to capture.
- New: T-095 (Ian: real companies or made-up ones, and the editorial rules; the store copy, Q-31). Q-31 and Q-36 point to the new boards; doc 14 has the batch and the Safaricom sources. `R8-Learn`'s Companies explained path now opens the new pages.
- The self-check fixed headlines with one word on the last line, a goals ad whose subtitle ran into the pools, and a shop ad whose headline broke into five lines.

### Round 8 batch 4: real stories, the podcast and the feed
- **Stories, in Learn** (`design/round-8/stories8.py`): a Rise story from Wanjiru (read or listen, save for offline, three lessons to keep, the Hub tools she used); the AWO Podcast player (chapters on the scrubber, a synced AI-assisted transcript checked by a person, key lessons, low-data audio on by default, offline); and "My worst money mistake" in three steps, where she chooses how her name shows and approves the edit before anything is published.
- **Community as a feed** (`feed8.py`): "For you" and "Circles"; notes, letters that open in place, milestones where a stone lands and the amount stays hidden, questions to one circle, and member shop cards; three reactions (Cheer, Same here, Taught me) with no public totals; a composer whose milestones come only from real tool actions, with an AI-assisted rule check that sends risky posts to a person; a question thread with a hidden reply; and reporting with a reason. `R8-Feed-Parts` shows all of it side by side.
- New open questions: Q-42 (members' stories: editing, credit, payment) and Q-43 (reaction counts). Q-39 and Q-40 now point to their safe versions. Doc 14 lists what Round 8 hasn't covered yet (T-094).
- The self-check fixed textareas bound the wrong way, a story board 400px too tall, reactions wrapping, a reply box that kept its text, and a parts board that overflowed.

## 2026-09-25

### Round 8 batch 3: the Hub, nine tools, goals and Home
- **The Hub** in two modes, **Me** and **My business** (renamed from "My job" to match Round 7's business Home and to include members without a payslip). Naledi (employed, Johannesburg) opens on Me, and her business tab shows the empty state; Wanjiru (a market stall, Nairobi) opens on My business. One lime "next useful thing", goals as pools, tools grouped by the job they do, Stay safe last.
- **`R8-Tool-Skeleton`:** the six beats, three tools shown beat by beat, the document path (consent, AI reads, she checks, the sum runs, the original is deleted) and four rules.
- **Nine tools** (`design/round-8/tools8.py`, `biz8.py`): payslip decoder, pay-day plan with family support, debt payoff, fee eater, statement insights, price it right, quotes and invoices, and Shop (editor and buyer's page, with products cut from Wanjiru's stall photo). Each is live and ends in a lesson, Words, a goal and, where it fits, a milestone without amounts.
- **Goals studio and Home** (`goals8.py`): eight goal templates with their cost reality (a car's balloon payment, moving out's first month, three checks before investing). Home is Round 7's Home, kept, with several goal pools and a "From the Hub" card.
- Q-35, Q-37 and Q-38 now point to their safe versions. The self-check fixed a too-small tap target, wrapped buttons, false precision, a miscount, a vanished space, dim photos and goals that disagreed between screens (doc 14).

### Round 8 batch 2: the new IA, and Learn with three tabs
- Ian picked the **keystone** for the Hub, in **lime**, and nine tools for batch 3: the kickoff's eight plus the pay-day plan (D-039). The icon board now marks the pick.
- Four new boards on page `r8` (`design/round-8/ia8.py`, `learn8.py`):
  - **`R8-IA`:** the five tabs, what moved where from Round 7, and a live tab bar that turns night on Learn.
  - **`R8-Learn`:** Paths, Words and Stories. The mint pill stretches towards the chosen tab and the content slides in from that side; each tab's shape arrives with it.
  - **`R8-Topic-Shares`:** a five-step explainer (a sample bakery cut into 100 shares), six lessons, words, a Hub tool and a goal, "Before you start", and the standing line that AWO never says what to buy.
  - **`R8-Words-Decoder`:** eight sample words at three depths, by country, with red flags and links into Learn and the Hub. Alias matches are labelled AI-assisted; a missing word can be asked for.
- The self-check found and fixed clipped panes, a squashed button, amounts breaking across lines (every Round 8 board now uses non-breaking spaces in amounts), wrapped lesson times and an unreachable "not in Words" state. Doc 14 has the details.

### Round 8 batch 1: the brief, the research and the Hub's icon
- **Doc 14** (`docs/00-discovery/14-round-8.md`) holds the research and the plan:
  - the 24 benchmark products, each with what AWO takes and what it leaves;
  - local facts for true-to-life samples (2026/27 tax tables, Kenya's SHIF, NSSF and Housing Levy, the new R 2,3 million VAT threshold, remittance costs, family support, retail forex losses, crypto licensing), all to be verified and dated before use;
  - the Hub shortlist, trimmed from 31 tools to 18 and ranked on value, weave, safety and effort; seven tools moved out of the Hub (goal templates, lessons, Words, Me);
  - how each tool is woven into Learn, Words, goals, Community and Me; the Hub page and the six-beat tool skeleton; the new IA; a safe version for each idea that meets a rule.
- **`R8-Hub-Icons`** on the new canvas page `r8` (the canvas now opens there): keystone, dial and market awning, each animated, in a working tab bar, on night, at five sizes and blurred. Claude recommends the keystone. The dial looks like a credit-score gauge (rule D8); the awning says "shop" only.
- The first keystone (a wedge on two legs) read as a little figure at 20px. Five drawings were compared; the arch-crown version replaced it.
- New open question **Q-41**: who keeps the facts behind Hub tools current. T-088 asks Ian to pick the icon and confirm the colour, the first eight tools and a facts owner.
- Generator in `design/round-8/` (`lib8.py`, `icons8.py`, `round8.py`, `layout8.py`). The glossary gains Hub, Words, Paths, Stories, tool, goal and the five post kinds.

### Round 8 briefed: the kickoff prompt
- Ian's next direction is recorded as D-037 and D-038:
  - Learn absorbs the Vault as a tab, and a new centre tab, the Hub, holds tools for employed women and entrepreneurs (tabs: Home, Learn, Hub, Community, Me).
  - Goals of every kind.
  - Learning beyond savings groups (markets, crypto, forex, companies).
  - Real human stories and an AWO podcast.
  - Community as a feed.
- **`docs/handover/2026-09-25-round-8-kickoff.md`** holds:
  - the brief and the proposed IA, with three Hub icon directions;
  - a Hub tool catalogue (12 for jobs, 11 for businesses, 8 for everyone), each with how it's woven in and its guard rail;
  - where the ideas meet the rules;
  - the deliverables, the gotchas, and a kickoff prompt to paste into a new session.
- New open questions Q-35 to Q-40: shops, featured companies, reading members' documents, a DIVA calculator, the podcast, and crypto and forex.
- The render and layout scripts moved out of the scratchpad and into the repo: `scripts/serve-boards.py`, `scripts/board-check.mjs` and `design/round-7/layout7.py`. Doc 06 explains them.

### Round 7 batch 5: AWO Admin (desktop)
- Seven linked admin screens (`design/round-7/admin7.py`), with Cmd+K search and a sidebar showing counts:
  - **Overview:** "Needs you" first (filterable), then what's live, key figures and where members are.
  - **Approvals:** two people with the author excluded, a line-by-line diff, automatic checks, a member preview, and approve or request changes (a note is required).
  - **Scoring:** a draft against the live version, with a preview on 200 test profiles.
  - **Members:** private by default; revealing a number needs a reason and is logged; a data request can be exported.
  - **Moderation:** AI flags and people decide, with keyboard shortcuts and undo.
  - **Lessons and Vault:** a Kanban from draft to published.
  - **Audit log and AI log.**
- Doc 13 now carries the admin guidance Ian asked for: each pattern, which product it's borrowed from, and how AWO uses it. The approval rule stays a proposal (Q-34).

### Round 7 batches 2 and 3: the deeper loop, and entrepreneurs
- **The loop, deeper** (`design/round-7/loop7.py`):
  - **Lesson player:** story cards, Thandi's stokvel as a turning circle, Ola explaining in reviewed words, a quick check with kind feedback, and a finish that waxes the moon.
  - **Compare versions:** pick any two; decreases are grey, never red, and nothing is recalculated.
  - **What if:** safety net runway, and a loan's real cost. Both are labelled as illustrations.
  - **Check an offer:** AI against AWO's red-flag list. It highlights the phrases, never says an offer is safe, and points to the FSCA register.
  - **Report:** a printable one-page DIVA report.
  - **Hard moments:** day one, a late check-in, coming back after weeks, a month that went down, and offline.
- **Entrepreneurs** (`biz7.py`, D-018): a two-minute business profile, a business check with sample questions (stated as learning readiness, not a loan decision), and a business view of Home: this week's business step, her own notebook of money in and out in KSh, a business word and a business lesson.
- Me now links to the report and to "Your business".

### Round 7 batch 1: accounts and the first loop
- Ian picked batches 1, 2, 3 and 5, with phone and social sign-in (D-035, D-036). The admin approval rule is open (Q-34), with a two-person proposal.
- New screens (`design/round-7/auth7.py`), all linked:
  - **Sign-in:** phone number first (formats as she types, with a country sheet), or Google and Apple.
  - **Account setup:** the code screen (six boxes, SMS autofill, a clear error), "about you" (first name, where she lives, currency), and consent in plain words (the optional AI and research switches start off).
  - **The first loop:** the first result reveal (the stones build, and "Reviewed by AWO" sits on the meaning) and choosing a first step with the next 30 days. Reminders are asked for after that step, not before.
  - **Privacy on shared phones:** a PIN lock (enter it twice, fingerprint optional) and a welcome-back unlock.
- Existing screens now link into the flow: the photo welcome, Goals (now step 4 of 4) and the starter check, which ends on the reveal.
- The page is laid out row by row from a small script, so each batch slots in without moving anything by hand.

### Proposal: the screens still to design
- Ian asked which important screens are still missing, starting with sign-in and an AWO Admin dashboard. Doc 13 now lists seven batches in priority order: accounts and the first loop, deeper learning and loop, entrepreneurs, deeper community, AWO Admin, the public website, and later channels. Each notes the open questions it touches. Ian picks the order (T-080).

### Round 7 marketing: the Round 3 pieces Ian flagged
- Ian's screenshots showed three sections: Play Store screenshots, the listing with feature graphic, icon and device hero, and campaign ads, from Rounds 3 and 6. All three now sit on page `r7`. Three Round 3 pieces were still missing, and are now added in Round 7 style: the photo-led Community screenshot (a real photo beside the phone, her answer in her hand), an eighth screenshot for the check-in ("Watch your safety net fill."), and the listing's short and full descriptions with character counts and the store rules they follow.
- Fixed the screen captures: cutting a tall screen to 844px had squashed its sections, most visibly the Community circle cards. The captures now switch off flex shrinking first. Five captures were re-uploaded, and the superseded uploads were deleted.

### Round 7 marketing in Geist, and the full board complete
- Marketing moved to Round 7 (T-076, D-033), built from 2x captures of the Round 7 screens: seven store screenshots (Progress is new), the listing, the feature graphic, a 512 app icon, the device hero, and photo, pool, word and story ads. Exports are in `design/marketing/round-7/`.
- The stepping-stones lockup replaces the Bricolage wordmark everywhere. Corners scale with the canvas (14 becomes 40 at 1080). The hand appears only in members' own words: her answer on the Community screenshot and Amara's line on the story ad.
- Doc 13 now describes the full board: the page's rows, how the screens link, and the choices to check. Generator: `design/round-7/marketing7.py`.

### Round 7 becomes the full board: brand, foundations, new screens, components
- Ian: make Round 7 "a full board which we will use for UI/UX inspo and references", with Round 2's brand boards and Round 3's screens, components and marketing redone in the Round 7 language. He also confirmed the draft: keep Geist and Kalam, and move marketing over (D-033).
- **New screens**, written natively (`design/round-7/screens7.py`): a photo-led welcome, "What brings you here", Your progress (tap a stone to see each version), the 30-day check-in (drag the amount, three questions, a new stone at the end), Your buddy and Settings (switches, with reduce motion and larger text working live). Me links to Progress and Settings; Community links to the buddy.
- **Components** (`kit7.py`): controls and data-and-feedback boards, both live (tabs, choices, switches, the what-if calculator, notices, loading, empty, offline and failed states). Widgets are the Round 6 board in Round 7 type.
- **Brand and foundations** (`brand7.py`): app icon A with the Geist wordmark lockup, the icon family, motion M1 to M6 as live cards, and foundations (colour, shapes, people, space).
- Page `r7` is laid out as a reference: foundations and brand on top, then every screen, linked, then components and widgets. Marketing follows.

### Round 7: Vault, Me and Community redesigned
- Ian's reaction: these three were the weakest (hierarchy, generic, text-heavy; Community less so). They are now written natively in Round 7 style in **`design/round-7/areas7.py`**, not transformed from Round 6. Each screen leads with its area's shape and has one clear job.
- **Vault:** the lime arch is the hero (the word of the week flips to an example). "3 words to practise" opens a short practice deck. Kept words sit in four collections instead of a long list.
- **Me** (1720px down to 1330): a pool hero with "Stage 2 of 4 stages", a small readiness ring and the stepping stones with her face on her stone. Tap a bar in "Your shape" to read about that dimension. Evidence has its own meter, versions are a sparkline, and the full interpretation is collapsed. Results stay typeset.
- **Community:** the question card shows one answer and then hers. Circles are cards with faces and ripples, the post is photo-first, and the event card is dark.
- Recorded as a section in `13-round-7.md`. Ian's unsent draft "Keep Geist, Kalam, move marketing over too" is logged as a **draft** decision (D-033) until he confirms it.

### Round 7: Geist, a hand for special moments, tighter corners
- Ian's brief (D-032): Round 1 Oasis's typeface (Geist), a handwritten face only for special moments, and a more restricted radius. His Round 6 answers, typed in the same screenshot: icon A, keep Home as it is (D-031).
- Canvas page **`r7`**: a **Type and corners** board (Geist's scale, three handwriting candidates with a live switcher, corners 6, 10, 14 and a circle, each beside Round 6), plus the Round 6 screens and components rebuilt by a transform in **`design/round-7/round7.py`**. Content and flows are unchanged, so the pages compare fairly.
- Handwriting appears in six moments: welcome "start here", "Here's where you start.", wins in members' own words, "Done for this week", "You showed up three evenings this week", and her shared answer. Results, AI answers and definitions stay typeset. Kalam is the default; every board has a `hand` Tweak (Q-33).
- Recorded in **`00-discovery/13-round-7.md`**.

### Round 6, batches 2 and 3: components, widgets, marketing, foundations
- **Components** (all live): buttons, the shape tab bar, provenance labels, inputs, switches, feedback states, the five shapes working, people, rows and steps. **Widgets**: a lock screen with no amounts, a home screen with small, medium and large widgets, and notifications written as a person first.
- **Marketing from captures of the Round 6 screens**, so nothing starts stale: six store screenshots (one per area, in its colour), a store listing in our own layout, a feature graphic, two app icon candidates, a device hero, and word-of-the-week, pool and story ads. PNGs are exported to `design/marketing/round-6/`.
- **E foundations at Volume 1**: area colours with their meaning and motion, type, animated shapes, people, motion speeds and radius by rank.
- Recorded in **`00-discovery/12-round-6.md`**. Generator README in `design/round-6/`.

### Round 6, batch 1: the screens at Volume 1 (Clean)
- Ian's Round 5 pick (D-030): Volume 1, with Round 3's Bento and Stories Home structure, Oasis v2 onboarding and Night Oasis's Ask and profile. Fast-forwarded this branch to `claude/exciting-cray-7z7fke`, which holds Round 5, so the docs are one history again.
- Canvas page **`r6`**: Welcome (three slides, each in its area's colour), Starter check (through "working out your profile" to the stage), **Home** (in Ian's order, with stories, a carousel and an expanding step), Learn, Ask Ola, Vault, Community and **Me** (a single readiness arc, evidence kept separate, four tappable dimensions, "explain it more simply" marked AI-assisted, versions as stepping stones). The tab bars link the screens.
- New generator in **`design/round-6/`**, built on Round 5's `lib.py`. Every board was rendered and clicked through before publishing. The checks caught overlapping welcome text, small pager targets, a wrapping button, a clipped version stone and Home content under the tab bar.

### Round 5 published: one language, five areas, three volumes
- Canvas page **`r5`** (opens by default), 4 boards, recorded in **`00-discovery/11-round-5-volume-test.md`**. It answers Ian's Round 4 reaction (D-028, D-029).
- **The language:** each area has a colour and a shape that means one thing and moves one way. Home is evergreen with a pool (money building), Learn is night with a moon (learning, Ola), Vault is lime with an arch (kept words), Community is blush with ripples (people), Me is pool with stepping stones (her stage). The tab icons are the shapes; a tile wears the colour of the area it opens.
- **The volume test:** the same five screens and sample content at Clean, Bold and Playful. Four taps work everywhere: the pool fills, Ola reacts, the Stokvel card flips, Cheer ripples.
- Self-checked every board and state (D-026), including reduce motion; fixes are listed in doc 11. The boards come from a small generator committed in `design/round-5/`, so the shared shapes survive the session.

### Merge: Round 3 and Round 4 histories joined, IDs reconciled; Ian's Round 4 reaction
- Session 3 (Round 3 review, Round 4) branched off before session 2's Round 3 commits, so both sessions reused IDs. Merged `claude/nifty-gauss-7odogg` into this branch and renumbered: the review is now doc **09**, Round 4 doc **10**; session 2's store-copy and Ola-outside-Learn questions are now **Q-31** and **Q-32**; the Mobbin task is **T-028**; the two D-026 entries (same decision) are one. Older diary entries keep their original numbers.
- Dropped session 3's retroactive "Round 3 published" entry: the real Round 3 commits are now in this history.
- **Ian's reaction to Round 4 (T-021):** it lost character. Bring back Round 3's bold condensed type, colour as big blocks, signature shapes and visual-first layouts, as a **meaningful design language: fun, modern, clean** (D-028). Build around five areas: **Home, Learn, Vault, Community, Me** (D-029). Next is a **volume test**: the five areas at three volumes (T-060 to T-062).

### Round 4 published: Moment 1 three ways, the Mentor + Circle loop
- Canvas page **`r4`**, 11 boards (9 interactive), recorded in **`00-discovery/10-round-4.md`**. Ian leans towards Mentor + Circle but wants to see all three (D-027), so the first result reveal is built as **Mentor**, **Journal** and **Circle**, each with a "lower than I hoped" branch.
- The rest of the loop is in Mentor + Circle with three sample members: Today (Naledi), a week's step (Wanjiru, KSh), a check-in where the safety net went down (Amara, £), a dark stokvel lesson with Ola, and being seen by the circle. There is also a hard-moments board (day one, missed week, coming back, offline) and an **"E, tightened"** board (one job per colour, calmer type, one main button, retired patterns).
- **D-026:** Claude now renders and clicks through its own boards before publishing. It caught SVG text that doesn't render, a squashed card and overflow under the tab bar. The gotchas are now in doc 06.
- New photos from nappy.co for emotional range (focused, tired, determined, sixty), plus face crops. The Unsplash connector needs its account email confirmed (T-025).

### Round 3 review: fewer screens, deeper moments
- Rendered all 35 Round 3 boards locally with the canvas runtime and reviewed them as screenshots. Wrote **`00-discovery/09-round-3-review.md`**: keep, cut, improve, three human directions and a Round 4 plan.
- Verdict: E is a coherent brand and Ola works, but the round is broad, not deep. Cut two Homes, the ripple-ring DIVA chart (it reads as "close your rings"), metaphor overload, everyday iris, vanity stats, chips over photos, arches everywhere and more marketing for now.
- Round 4 (T-040 to T-046): five moments with their hard states, three sample members, and Moment 1 in three directions (Mentor, Journal, Circle).
- New open questions **Q-29** (who is AWO to her?) and **Q-30** (is Learn always dark?). Added the local render recipe to doc 06.
- Connectors now live: Figma, Unsplash, Mobbin (needs a paid plan), Fonts, tldraw, Trello, HyperFrames.

### Round 3, batches 5 to 7: remaining E screens, components, widgets, marketing
- **E screens:** interactive 30-day check-in (a slider fills the safety-net pool), community (likes, event reminder), buddy (send a cheer; lessons shared, never amounts), settings with working switches (reduce-motion demo, data stored in South Africa), and three onboarding variants (photo-led, ripple, goal picker).
- **Components:** controls, data and feedback (stat tiles, a what-if calculator, progress forms, notifications, skeletons), and home-screen and lock-screen widgets.
- **Marketing:** six Play Store screenshots, feature graphic, app icon candidate, a device hero (real photo with a real screen composited in), three square ads, a story ad and a simplified listing preview. PNG exports at exact sizes and their sources are in `design/marketing/`; Play specs were checked on 25 Sep 2026.
- New open questions: store name and copy (Q-29), Ola outside Learn and Ask (Q-30). Round 3 is complete on the canvas and waits for Ian's reactions (T-021).

### Round 3, batches 3 and 4: Learn and Ask, E Homes, DIVA, progress
- **Learn flow** (one interactive board): stepping-stone path, story cards with progress bars, quiz with feedback, Ola's celebration, back to an updated path. **Vault flip cards** (flip, filter, save) and **Ask Ola** (suggestion, thinking, sourced answer). All self-checked by clicking through every state.
- **E screens:** bento, timeline and stories Homes; the **DIVA ripple rings** (tap a dimension, evidence shown apart, version label, no gamification); **progress over time** (tooltip, small multiples, effort stats).
- Charts follow the `dataviz` skill; the validator showed the brand colours fail as a categorical palette, so charts use one hue with direct labels.

### Round 3, batches 1 and 2: taste board, Direction E foundations, Ola v2
- Ian answered T-010: **Claude self-checks every board** (D-026). Added `scripts/canvas-preview.mjs`, which renders boards locally with the canvas runtime and screenshots them, including clicked states. The first checks caught a clipped headline, an overlapping animation and a pink cast on Ola.
- **Taste board** (canvas, Round 3 page): 12 references from Play Store listings (Wise, Kuda, Cash App, Monzo, Headspace, Duolingo) and Dribbble (mascots, AI orb, widgets, savings pools, bento), each with the one thing to take. Photography comes from nappy.co (CC0).
- **Direction E foundations:** evergreen, lime, blush, mist, pool and ink for day; Round 1 Night Oasis for Learn and Ask; Bricolage Grotesque + Geist; radius by rank; ripple, pool and stepping-stone motifs; live motion tokens.
- **Ola v2:** a mint-to-iris glass orb with capsule eyes only, squash and stretch, six states. The board is interactive: tap a state.
- New tools this session: Mobbin needs a paid plan, the Unsplash connector needs Ian to confirm his email, and Figma is connected (View seat). Details and tokens in `docs/00-discovery/08-round-3-direction-e.md`.

## 2026-09-24

### Harness: changelog, task list, commit hook, Round 3 handover
- Added this **CHANGELOG** (diary) and **TASKS.md** (the single task list). Ian asked for them so context is never lost and documents don't scatter.
- Added a **PreToolUse hook** (`scripts/hooks/require-changelog.sh`, wired in `.claude/settings.json`) that blocks commits without a changelog update.
- Wrote **`docs/handover/2026-09-24-round-3.md`**: everything learned in session 1 (taste, mistakes, the Round 3 brief, technical gotchas, tokens, a kickoff prompt). Session 1 ended here because the context was nearly full.
- Added `scripts/screenshot.mjs` (headless Chromium capture that works in cloud sessions).
- Slimmed **STATUS.md** to a snapshot that points to TASKS and the handover. `CLAUDE.md` now defines what each doc is for and the commit ritual.

### `20f19e8` STATUS: network resolved; record which inspiration sources work
- Ian widened network access and it worked without a new session. Dribbble, Behance (incl. Pock), Mobbin and Google Play work in headless Chromium. Unsplash, Pexels and Medium are bot-walled.
- Found that **Pock is deep green + acid lime** (not purple as assumed).

### `576c95e` Add a Playwright MCP server that works in cloud sessions
- The plugin Playwright looks for Google Chrome, which isn't in cloud containers. Added `.mcp.json` + `scripts/playwright-mcp.sh` (uses the pre-installed Chromium and pins the proxy CA key), disabled the plugin copy, and approved the server in settings. Tested end to end.

### `4dacd95` Record Round 2 feedback and Round 3 brief; note network blocker
- D-024: combine A + D. Ola, the colours and Learn interactivity were the weakest; Round 1 B looked better. Push for widgets, bento, graphs, mock-ups, ads, Play Store.
- D-025: widen network access for design research.

### `0d304a7` Discovery round 2: owner answers, brand and motion direction, project plugins
- Recorded D-014 to D-023 (no brand to keep, Ian builds, compliance is AWO's, Figma, first members, Round 1 verdicts, motion-first, mascot in one area, tier names open, plugins).
- Added `07-brand-and-motion.md` and rules D13 (no AI-made tells) and D14 (motion with meaning).
- Canvas **Round 2** published: wordmarks, hand-drawn icons, motion board, A v2 (welcome, starter check, home), B as Learn and Ask with Ola, D · Human.
- Enabled 9 plugins at project scope.

### `08f8ca9` Discovery pass: understanding, design direction, open questions, harness
- First pass: discovery docs 01–06, decision log D-001 to D-013, glossary, STATUS, `CLAUDE.md`.
- Canvas **Round 1** published: A · Oasis, B · Night Oasis, C · Editorial Violet (system sheet, Home, DIVA profile each).
