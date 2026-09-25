# Changelog: the project diary

> **Newest first.** Add an entry with every commit (or a tight group of commits). Say what changed, why, and anything the next session must know. A Claude Code hook blocks `git commit` when this file hasn't been touched; use `SKIP_CHANGELOG=1` only for trivial commits.
>
> Format: `### <short title>` under a date heading, with the commit hash once known, then 1–5 bullets.

## 2026-09-25

### Round 4 published: Moment 1 three ways, the Mentor + Circle loop
- Canvas page **`r4`**, 11 boards (9 interactive), recorded in **`00-discovery/09-round-4.md`**. Ian leans towards Mentor + Circle but wants to see all three (D-027), so the first result reveal is built as **Mentor**, **Journal** and **Circle**, each with a "lower than I hoped" branch.
- The rest of the loop is in Mentor + Circle with three sample members: Today (Naledi), a week's step (Wanjiru, KSh), a check-in where the safety net went down (Amara, £), a dark stokvel lesson with Ola, and being seen by the circle. There is also a hard-moments board (day one, missed week, coming back, offline) and an **"E, tightened"** board (one job per colour, calmer type, one main button, retired patterns).
- **D-026:** Claude now renders and clicks through its own boards before publishing. It caught SVG text that doesn't render, a squashed card and overflow under the tab bar. The gotchas are now in doc 06.
- New photos from nappy.co for emotional range (focused, tired, determined, sixty), plus face crops. The Unsplash connector needs its account email confirmed (T-025).

### Round 3 review: fewer screens, deeper moments
- Rendered all 35 Round 3 boards locally with the canvas runtime and reviewed them as screenshots. Wrote **`00-discovery/08-round-3-review.md`**: keep, cut, improve, three human directions and a Round 4 plan.
- Verdict: E is a coherent brand and Ola works, but the round is broad, not deep. Cut two Homes, the ripple-ring DIVA chart (it reads as "close your rings"), metaphor overload, everyday iris, vanity stats, chips over photos, arches everywhere and more marketing for now.
- Round 4 (T-040 to T-046): five moments with their hard states, three sample members, and Moment 1 in three directions (Mentor, Journal, Circle).
- New open questions **Q-29** (who is AWO to her?) and **Q-30** (is Learn always dark?). Added the local render recipe to doc 06.
- Connectors now live: Figma, Unsplash, Mobbin (needs a paid plan), Fonts, tldraw, Trello, HyperFrames.

### Round 3 published to the canvas (session 2, logged retroactively)
- Session 2 published Round 3 on canvas page `r3` but didn't commit, so it is recorded here. 35 boards: taste board, E foundations, Ola v2, Learn flow, Vault flip cards, Ask, three Homes, DIVA, progress, check-in, community, buddy, settings, three welcomes, components, widgets, six store screenshots, listing, feature graphic, app icon, hero device and four ads. People photos from nappy.co.

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
