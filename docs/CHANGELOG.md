# Changelog: the project diary

> **Newest first.** Add an entry with every commit (or a tight group of commits). Say what changed, why, and anything the next session must know. A Claude Code hook blocks `git commit` when this file hasn't been touched; use `SKIP_CHANGELOG=1` only for trivial commits.
>
> Format: `### <short title>` under a date heading, with the commit hash once known, then 1–5 bullets.

## 2026-09-25

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
