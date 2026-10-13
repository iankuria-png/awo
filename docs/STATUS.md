# Status

**Phase:** 0 · Discovery (design exploration; no product code yet)
**Current focus:** **The foundation pass (T-120)**, on the branch `docs/foundation-blueprint`: research and a blueprint for the repo, folder structure, practices, docs, context, the design system, tools, assets and the Claude harness, in [17-foundation.md](00-discovery/17-foundation.md). Step 1, the audit, is written; research and the blueprint come next. Nothing is built until Ian approves. Round 9 and the Brand system page still wait on Ian's reactions (T-102, T-108 to T-112, T-116).
**Last updated:** 2026-10-13, session 5 (the foundation pass: the audit)

## Start here

- **[17-foundation.md](00-discovery/17-foundation.md):** the foundation pass, in progress. Its brief is [handover/2026-10-13-foundation-kickoff.md](handover/2026-10-13-foundation-kickoff.md).

0. **[16-brand-system-brief.md](00-discovery/16-brand-system-brief.md):** AWO's suggested brand system for Instagram and LinkedIn, and where it differs from the app (Q-49). **[15-round-9.md](00-discovery/15-round-9.md):** Round 9 as it is built, batch by batch. Before it, **[14-round-8.md](00-discovery/14-round-8.md):** Round 8 as it's built: research, the ranked Hub shortlist, the new IA, the safe versions and the Hub's icon. The brief behind it is [handover/2026-09-25-round-8-kickoff.md](handover/2026-09-25-round-8-kickoff.md).
1. **[13-round-7.md](00-discovery/13-round-7.md):** Round 7 (type, handwriting, corners). It sits on **[12-round-6.md](00-discovery/12-round-6.md)**, Round 6 as built. The language itself (a colour and a shape per area) is in [11](00-discovery/11-round-5-volume-test.md).
2. **[TASKS.md](TASKS.md):** Ian reacts to Round 8 (T-093) and decides whether briefs may name real companies (T-095, Q-36); what's left of Round 8 is T-094. Ian's Round 7 reactions (T-075, T-085) and the facts owner (T-092, Q-41) are still open.
3. **[CHANGELOG.md](CHANGELOG.md):** what happened, commit by commit. The latest entries explain the branch merge and the renumbering.
4. **Round history:** [11](00-discovery/11-round-5-volume-test.md) Round 5, [08](00-discovery/08-round-3-direction-e.md) Round 3 (Direction E tokens, Ola v2, sources and tools), [09](00-discovery/09-round-3-review.md) the review of Round 3, [10](00-discovery/10-round-4.md) Round 4 as built.
5. Background: the [Round 3 handover](handover/2026-09-24-round-3.md) (taste, mistakes to avoid, canvas gotchas).

## Snapshot

- **Design canvas:** [AWO Direction Explorations](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9), pages Round 1 to Round 8 and Brand system (opens on Brand system). Round 7 is the reference board, and holds every Round 8 board and all of Round 9 too, grouped by topic in 20 sections (onboarding, the loop, Home, Learn, the Hub, Community, Me, other channels, components, Admin, around the app, marketing, merchandise and more).
- **Direction:** **E** (A + D: evergreen, lime, blush, mist, pool; Bricolage Grotesque + Geist; Night Oasis for Learn and Ask; Ola v2 orb). Round 4 made the flows deeper but flattened the look; Ian wants Round 3's bold condensed type, colour blocks, signature shapes and visual-first layouts back, as a **meaningful design language: fun, modern, clean** (D-028). The app has five tabs: **Home, Learn, Hub, Community, Me** (D-037); the Vault lives on as Words inside Learn.
- **Environment:** the network is open for design research; browse with headless Chromium (`scripts/screenshot.mjs` or the Playwright MCP). Connectors: Figma (View seat), Unsplash (needs its account email confirmed), Fonts, tldraw, Trello, HyperFrames; Mobbin needs a paid plan. Claude self-checks boards with `scripts/canvas-preview.mjs` (D-026; recipe in [06](00-discovery/06-tooling-and-harness.md#reviewing-canvas-boards-locally-render-recipe)).
- **Hosting:** Vultr in Johannesburg (D-043), with nothing deployed yet. What the region offers and the data-location notes are in [04](00-discovery/04-technical-leanings.md#hosting-vultr-in-johannesburg); what's left is T-119.
- **Branches:** `main` is the default (D-044); work happens on branches named by type and topic, such as `docs/foundation-kickoff`. GitHub's default setting still points at the old session branch until Ian switches it (T-121).
- **Decisions:** D-001 to D-044 in [decisions/log.md](decisions/log.md). **Open questions:** [05-open-questions.md](00-discovery/05-open-questions.md) (non-blocking; newest are Q-34 to Q-50).
