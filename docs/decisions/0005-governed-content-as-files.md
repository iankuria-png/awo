# ADR 0005: Governed content lives as versioned files in git until the admin app

- **Status:** Proposed (foundation pass, T-120, 13 October 2026). Not in the decision log until Ian decides.
- **Relates to:** D-004 (scoring and interpretation server-side, versioned, auditable), D-009 (admin comes late), D-010 (scoring rules are versioned configuration until the admin app), Q-07, Q-13, Q-14, Q-15, Q-34.

## Context

AWO's most sensitive content is *governed*: starter-check questions and options, scoring methods (rules, weights, thresholds), evidence-confidence rules, the interpretation library, next steps, lessons, Words entries and the Hub's dated facts (Q-41). Every result pins the versions it used, so the content must be versioned, reviewable and reproducible from day one.

The admin app, with its maker-checker approvals (designed on the Round 7 board, Q-34), comes late (D-009). Until then, someone has to author, review and publish this content, and the build has to read it.

## Options

| Option | For | Against |
|---|---|---|
| **A. Files in git** (YAML or JSON with JSON Schemas, plus Markdown or MDX for long text) under `content/`, reviewed by pull request, compiled into versioned, immutable bundles that the API loads or seeds into Postgres | Versioning, diffs, review and an audit trail for free; golden tests run against exactly what ships; works with one person; no admin UI to build first | Non-developers can't edit without help; approvals are GitHub reviews, which a solo account can't enforce (§2 of doc 17); large media must live elsewhere |
| **B. The database from day one**, with a minimal internal editor | Same shape as the final admin app; editors work in a UI | An editor, roles, approvals and audit to build before any member sees anything; review and diffs are ours to build; harder to test deterministically |
| **C. A headless CMS** (for example Payload, self-hosted in South Africa) | A ready editor with drafts and roles | Another service to run; versioning and pinning still ours; scoring rules don't belong in a CMS |

## Proposed decision

**Option A until the admin app (Phase 7), then import.** Specifically:

- `content/` holds one folder per kind (`assessment/`, `scoring/`, `evidence/`, `interpretation/`, `next-steps/`, `lessons/`, `words/`, `facts/`), each file with an `id`, a semantic `version`, a `status` (`draft`, `published`, `retired`), `reviewedBy` and `reviewedOn`, and, for facts, `source` and `checkedOn`.
- A JSON Schema per kind validates every file in CI. A copy check (the `awo-copy-check` skill's rules, run as a script) flags advice, credit, guarantee or eligibility language.
- Publishing is a merge to `main` plus a tag such as `content/scoring/individual@1.0.0`. A published version is never edited; a change is a new version.
- The API loads published bundles at start and stores each bundle's hash with every result, so a result can always be traced to the exact text and rules that made it.
- Everything not yet approved by AWO carries `sample: true` and renders with the "Sample" label (CLAUDE.md).
- When the admin app arrives, the files are imported as the first versions in the database, and the database becomes the source of truth for content. Git keeps the history before that point.

## Consequences

- Content review is a pull request; Ian (or AWO's content owner, Q-07) reviews the diff. Until GitHub can enforce two approvers (doc 17 §2), the maker-checker rule (Q-34) is a habit, recorded in each file's `reviewedBy`.
- Lessons with media keep their media in the asset store (doc 17 §9), referenced by id.
- No member data ever lives in `content/`.

## Data-location note

Content files are AWO's own text, not member data. They live in GitHub (United States) and on the Vultr server in Johannesburg. Nothing personal is stored with them.

## Ian decides

Files in git first (recommended), the database from day one, or a CMS. Also: who reviews governed content (Q-07, Q-34).
