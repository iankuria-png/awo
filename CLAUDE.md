# AWO: standing orders for Claude

AWO (African Wealth Oasis) is a financial **education, intelligence and community** platform for African women in Southern Africa and the diaspora. Its core loop: *Where am I? (DIVA profile) → What does it mean? (governed interpretation) → What next? (one step) → 30-day check-in → progress.*

## Start every session here

1. Read [`docs/STATUS.md`](docs/STATUS.md) (the snapshot) and the latest file in [`docs/handover/`](docs/handover/) if STATUS points to one.
2. Read [`docs/TASKS.md`](docs/TASKS.md) (what to do) and the top of [`docs/CHANGELOG.md`](docs/CHANGELOG.md) (what just happened).
3. Skim [`docs/decisions/log.md`](docs/decisions/log.md) before proposing anything that might already be decided.
4. Check [`docs/00-discovery/05-open-questions.md`](docs/00-discovery/05-open-questions.md) before filling a gap yourself.
5. Use [`docs/glossary.md`](docs/glossary.md) vocabulary exactly.

**Owner and builder:** Ian Kuria, product developer and software engineer (D-015). Designs in Figma.

**Current phase: 0 · Discovery.** Documentation, design direction and harness only. **No product code** until the owner says so.

## Non-negotiables: product

- **Educational scope only.** No personalised investment advice, credit decisions, investment execution, capital pooling or investor matching. Copy uses *learn / understand / explore*, never *you should buy / switch / invest in*.
- **DIVA scoring and interpretation are server-side, deterministic, versioned and auditable.** Results are immutable; recalculation creates a new version. Clients get only what they need to display.
- **Evidence confidence is separate** from the readiness score.
- **Categories describe educational readiness.** Never imply creditworthiness, suitability, eligibility or guaranteed outcomes.
- **AI never** computes or adjusts scores, picks categories, writes interpretations outside the governed library, or recommends financial products or providers. AI output is always labelled and logged.
- **Never invent business rules.** Use visibly labelled *sample* content and log the gap as an open question.
- **Data location matters** (POPIA). Production and backups live in South Africa; every external service needs a data-location note. Compliance analysis itself is AWO's (D-016): don't spend time on it.

## Non-negotiables: design

- **Global craft, local truth.** Benchmark against the best global products. Africa appears in *substance* (names, currencies, stokvels/chamas, real money lives), never as *decoration* (ethnic patterns, continent maps, safari/sunset palettes, "tribal" fonts, flag colours).
- Rules D1–D14 in [`docs/00-discovery/03-design-direction.md`](docs/00-discovery/03-design-direction.md) apply to every screen. D13: no AI-made tells (cream grounds, all-caps eyebrows, "A · B · C" meta strings, fake numbering).
- **Motion-first** (D-020): motion answers a touch, shows progress or marks a win (M1–M6 in [`07-brand-and-motion.md`](docs/00-discovery/07-brand-and-motion.md)). Always respect reduce-motion.
- The mascot (Ola, working name) lives **only** in Learn and Ask, never on DIVA results.
- Mobile-first for mid-range Android on patchy data. WCAG 2.2 AA. Touch targets of 44px or more.
- Provenance is visible: *Reviewed by AWO* · *AI-assisted* · *Sample*.

## How we work

- **Docs are the memory.** Each has one job, so nothing gets scattered:

  | Doc | Job |
  |---|---|
  | `docs/STATUS.md` | Snapshot: phase, current focus, pointers (short) |
  | `docs/TASKS.md` | The single task list (Now / Waiting on Ian / Next / Later / Done) |
  | `docs/CHANGELOG.md` | The diary: one entry per commit, newest first |
  | `docs/decisions/log.md` | Every decision, with source |
  | `docs/00-discovery/05-open-questions.md` | Everything we must not invent |
  | `docs/handover/` | Only when a session ends mid-stream: a full context transfer |
  | Topic docs (`docs/00-discovery/`, later `product/`, `design/`, `engineering/`…) | Durable knowledge, one topic per file |

  Don't create ad-hoc files. New material extends one of these, or goes in a folder listed in `docs/README.md`.
- **Every commit ritual:** add a CHANGELOG entry and update TASKS. Update STATUS if the focus changed, and the decision log or open questions if they changed. A hook (`scripts/hooks/require-changelog.sh`) **blocks `git commit` without a CHANGELOG change**; prefix with `SKIP_CHANGELOG=1` only for trivial commits.
- **Ask when it's the owner's call** (product rules, brand, compliance, priorities). Decide implementation details yourself, explain them, and record the important ones.
- **End of session (or near the context limit):** update STATUS, and if work is mid-stream write a handover in `docs/handover/` (taste, mistakes, next steps, gotchas, kickoff prompt).
- **Spelling:** UK/South African English ("colour", "behaviour", "personalised", "organisation").
- **Git:** small, focused commits with clear messages. Never commit secrets or real member data.

## Where things live

```
docs/00-discovery/   understanding, product shape, design direction, tech leanings, open questions, tooling, brand and motion
docs/decisions/      log.md (+ ADRs for big technical choices)
docs/glossary.md     AWO vocabulary
docs/STATUS.md       snapshot         docs/TASKS.md      task list       docs/CHANGELOG.md  diary
docs/handover/       session handovers
scripts/             screenshot.mjs, canvas-preview.mjs (self-check boards), playwright-mcp.sh, hooks/require-changelog.sh
design/marketing/    marketing PNGs: Round 3 drafts, and round-6/ built from the live screens
design/round-5/      generator for the Round 5 canvas boards (shared shapes, icons, Ola, tab bars)
design/round-6/      generator for Round 6 (the app at Volume 1); design/round-7/ transforms it (Geist, handwriting, corners)
.claude/settings.json  plugins, MCP approval, the changelog hook      .mcp.json  Playwright server
```

Design explorations live on the [AWO Direction Explorations canvas](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9) (pages Round 1 to Round 7).

Planned (not yet created): `docs/product/`, `docs/design/`, `docs/engineering/`, `docs/governance/`, `docs/operations/`, `apps/`, `packages/`, `infra/`. See [`docs/00-discovery/06-tooling-and-harness.md`](docs/00-discovery/06-tooling-and-harness.md).
