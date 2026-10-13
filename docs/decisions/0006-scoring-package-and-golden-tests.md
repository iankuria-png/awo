# ADR 0006: Scoring is an isolated, pure package with golden tests

- **Status:** Proposed (foundation pass, T-120, 13 October 2026). Not in the decision log until Ian decides.
- **Relates to:** D-004, D-005, D-006, D-010; doc 04's domain map (Assessment, Scoring, Evidence, Interpretation); ADR 0005; Q-13, Q-14, Q-15.

## Context

The DIVA score, the stage, evidence confidence and the selected interpretation blocks must be deterministic, versioned, reproducible and auditable (D-004). They are where a bug hurts most: a wrong stage tells a woman something untrue about herself, and a silent change rewrites history. AI must never compute or adjust them (D-005).

## Proposed decision

1. **A package of pure functions**, `packages/scoring`, with no I/O, no clock, no randomness and no database: `score(method, responses) → result`, `confidence(rules, provenance) → level`, `interpret(library, result) → blockIds`. Inputs and outputs are typed with schemas shared through `packages/contracts`.
2. **Methods are data, not code.** A scoring method is a published file from `content/scoring/` (ADR 0005) with a semantic version. The package interprets it. A change in weights is a new method version; a change in how the package interprets methods is a new package version, and both are recorded on every result.
3. **Golden tests.** `packages/scoring/golden/<method>@<version>/` holds fixtures: a set of made-up profiles (the Round 7 admin board's "200 test profiles", all synthetic) and the exact expected result for each (score, stage, dimension scores, confidence, block ids). CI fails on any difference. Updating a golden file needs a new method version or an explicit, reviewed note in the pull request saying why the old expectation was wrong.
4. **Property tests** (for example with `fast-check`) check invariants across random inputs: the score stays in 0 to 100, the stage is monotonic in the score, the same input always gives the same output, and confidence never changes the score (D-006).
5. **The preview from the admin board** ("who would move stage") is the golden set run against a draft method: the same code, so it can be built long before the admin app, as a script.
6. **Only the API calls the package.** Clients receive the result to display, never the method (D-004). The package is never published or bundled into a client.
7. **Immutability is enforced in the database too:** results are insert-only, and a check-in creates a new version that points to the one it supersedes.

## Alternatives

- **Scoring inside the API's service layer.** Simpler at first, but it mixes I/O with rules and makes golden tests slower and leakier.
- **A rules engine** (for example JSON Logic). Flexible, but harder to read, test and diff than a small typed interpreter of AWO's own method format. Worth revisiting only if AWO's methods outgrow simple weighted rules.

## Consequences

- Sample rules (Q-13) can be coded and tested now, clearly labelled, and swapped for AWO's real ones without touching the engine.
- The package's coverage target is 100% of branches; that is cheap for pure functions and it matters here.

## Data-location note

The fixtures are synthetic, never real members. Real responses and results live only in Postgres in Johannesburg.

## Ian decides

Whether this shape stands, and who supplies and approves the real methods (Q-13 to Q-15, Q-34).
