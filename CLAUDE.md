# AWO: standing orders for Claude

AWO (African Wealth Oasis) is a financial **education, intelligence and community** platform for African women in Southern Africa and the diaspora. Its core loop: *Where am I? (DIVA profile) → What does it mean? (governed interpretation) → What next? (one step) → 30-day check-in → progress.*

## Start every session here

1. Read [`docs/STATUS.md`](docs/STATUS.md): the current phase, what's next, and what we're waiting on.
2. Skim [`docs/decisions/log.md`](docs/decisions/log.md) before proposing anything that might already be decided.
3. Check [`docs/00-discovery/05-open-questions.md`](docs/00-discovery/05-open-questions.md) before filling a gap yourself.
4. Use [`docs/glossary.md`](docs/glossary.md) vocabulary exactly.

**Current phase: 0 · Discovery.** Documentation, design direction and harness only. **No product code** until the owner says so.

## Non-negotiables: product

- **Educational scope only.** No personalised investment advice, credit decisions, investment execution, capital pooling or investor matching. Copy uses *learn / understand / explore*, never *you should buy / switch / invest in*.
- **DIVA scoring and interpretation are server-side, deterministic, versioned and auditable.** Results are immutable; recalculation creates a new version. Clients get only what they need to display.
- **Evidence confidence is separate** from the readiness score.
- **Categories describe educational readiness.** Never imply creditworthiness, suitability, eligibility or guaranteed outcomes.
- **AI never** computes or adjusts scores, picks categories, writes interpretations outside the governed library, or recommends financial products or providers. AI output is always labelled and logged.
- **Never invent business rules.** Use visibly labelled *sample* content and log the gap as an open question.
- **Data location matters** (POPIA). Production and backups live in South Africa; every external service needs a data-location note.

## Non-negotiables: design

- **Global craft, local truth.** Benchmark against the best global products. Africa appears in *substance* (names, currencies, stokvels/chamas, real money lives), never as *decoration* (ethnic patterns, continent maps, safari/sunset palettes, "tribal" fonts, flag colours).
- Rules D1–D12 in [`docs/00-discovery/03-design-direction.md`](docs/00-discovery/03-design-direction.md) apply to every screen.
- Mobile-first for mid-range Android on patchy data. WCAG 2.2 AA. Touch targets of 44px or more.
- Provenance is visible: *Reviewed by AWO* · *AI-assisted* · *Sample*.

## How we work

- **Docs are the memory.** If something is explained twice, it goes in a doc. If it's a choice, it goes in the decision log.
- **Ask when it's the owner's call** (product rules, brand, compliance, priorities). Decide implementation details yourself, explain them, and record the important ones.
- **End of session:** update `docs/STATUS.md` (done, next, waiting on).
- **Spelling:** UK/South African English ("colour", "behaviour", "personalised", "organisation").
- **Git:** small, focused commits with clear messages. Never commit secrets or real member data.

## Where things live

```
docs/00-discovery/   understanding, product shape, design direction, tech leanings, open questions, tooling
docs/decisions/      log.md (+ ADRs for big technical choices)
docs/glossary.md     AWO vocabulary
docs/STATUS.md       current state
```

Planned (not yet created): `docs/product/`, `docs/design/`, `docs/engineering/`, `docs/governance/`, `docs/operations/`, `design/`, `apps/`, `packages/`, `infra/`. See [`docs/00-discovery/06-tooling-and-harness.md`](docs/00-discovery/06-tooling-and-harness.md).
