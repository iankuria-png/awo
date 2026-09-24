# Tasks: the single task list

> Update with **every commit**: move items between sections, add new ones, and close finished ones with the date. IDs are stable; never renumber. Owner is **Claude** or **Ian**. Details live in the linked docs, not here.

## Now: Round 3 (brief in [handover](handover/2026-09-24-round-3.md) §5)

| ID | Task | Owner | Notes |
|---|---|---|---|
| T-010 | Ask Ian whether Claude should self-check renders (screenshots of its own work) | Claude | Handover §7 |
| T-011 | **Taste board**: capture about 30 real references (Dribbble, Behance, Mobbin, Play Store), curate 10–12 into a canvas board with "what to take" | Claude | Delegate crawling to a subagent to save context |
| T-012 | **Direction E (A + D)** foundations board: palette, type, shapes, people, motion tokens | Claude | Starting palette in handover §5 |
| T-013 | E screens: bento Home, timeline Home, story Home, DIVA result reveal (ripple rings), progress graphs, interactive check-in, community, buddy, settings with switches, onboarding variants | Claude | Non-generic layouts; minimal copy |
| T-014 | **Ola v2**: glowing-orb character in Round 1 Night Oasis colours, 5 states | Claude | Replaces the droplet |
| T-015 | **Interactive Lesson Player** (path → story cards → quiz → celebration) + flip cards; Learn home redesign | Claude | Real state machine, `is_interactive` |
| T-016 | **Components and widgets** boards: stats bar, switches, sliders, segmented controls, charts, notifications, skeletons, home and lock-screen widgets | Claude | Charts per the `dataviz` skill |
| T-017 | **Marketing**: device hero shot, square and story ads, Play Store feature graphic (1024×500), store screenshots, simplified listing preview | Claude | Also export real PNGs to `design/marketing/` |
| T-018 | Publish Round 3 on a new canvas page `r3`, in batches | Claude | Handover §7 canvas rules |

## Waiting on Ian

| ID | Task | Notes |
|---|---|---|
| T-020 | Connect the **Figma connector** (claude.ai/customize/connectors), then start a new session | Unlocks building the library in Figma |
| T-021 | React to Round 2 / Round 3 | Q-02 |
| T-022 | Answer the open questions when ready (non-blocking) | Q-04, Q-05, Q-07, Q-09, Q-10, Q-25, Q-26, Q-27 |
| T-023 | Optional: add an **Unsplash API key** as an environment secret | Unlocks photo search for real people |

## Next (after Round 3 converges)

| ID | Task | Owner |
|---|---|---|
| T-030 | Design Standard v1 (tokens, type, colour, icons, motion, components, states, content style) | Claude |
| T-031 | Brand identity v1: wordmark, app icon, icon set, Ola; Figma library | Claude + Ian |
| T-032 | PRD v1 + feature map + IA (member, public, admin) | Claude |
| T-033 | Wireframes, then a clickable prototype of the priority journey; plan 5–8 member tests | Claude + Ian |
| T-034 | Tech stack ADR, architecture and domain docs | Claude + Ian |
| T-035 | Implementation plan (phased, with milestones) | Claude |
| T-036 | Project skills: `awo-copy-check`, `awo-design-review`, `awo-decision`, `awo-handoff` | Claude |

## Later

| ID | Task |
|---|---|
| T-050 | Session-start hook to install dependencies once code exists |
| T-051 | Enable `typescript-lsp`, PR review agents and `data` plugins when code exists |

## Done

| ID | Task | Done |
|---|---|---|
| T-001 | Discovery docs 01–06, decision log, glossary, STATUS, CLAUDE.md | 2026-09-24 |
| T-002 | Canvas Round 1 (A, B, C) | 2026-09-24 |
| T-003 | Canvas Round 2 (brand, icons, motion, A v2, B Learn and Ask, D Human) + doc 07 | 2026-09-24 |
| T-004 | Enable project plugins | 2026-09-24 |
| T-005 | Resolve network access for design research | 2026-09-24 |
| T-006 | Playwright MCP that works in cloud sessions + `scripts/screenshot.mjs` | 2026-09-24 |
| T-007 | Round 3 handover, changelog, task list, commit hook | 2026-09-24 |
