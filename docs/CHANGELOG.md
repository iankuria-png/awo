# Changelog: the project diary

> **Newest first.** Add an entry with every commit (or a tight group of commits). Say what changed, why, and anything the next session must know. A Claude Code hook blocks `git commit` when this file hasn't been touched; use `SKIP_CHANGELOG=1` only for trivial commits.
>
> Format: `### <short title>` under a date heading, with the commit hash once known, then 1–5 bullets.

## 2026-09-25

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
