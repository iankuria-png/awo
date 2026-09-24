# Decision log

> One line per decision. Big technical choices with real trade-offs also get an ADR file (`NNNN-short-title.md`) linked from here.
> **Source** says where the decision came from: *Brief* (the original product brief), *Owner* (you, in conversation), or *Joint* (agreed together).

| ID | Date | Decision | Source | Notes |
|---|---|---|---|---|
| D-001 | 2026-09-24 | Build AWO from scratch in a new repository. The previous stack is background, not a requirement. | Brief | |
| D-002 | 2026-09-24 | Production runs on **AWO-owned, self-managed VPS infrastructure in South Africa**. | Brief | Data location applies to storage, backups and integrations. |
| D-003 | 2026-09-24 | **Scope is educational.** No personalised investment advice, credit decisions, investment execution, capital pooling or investor matching. | Brief | Pending compliance review (Q-08). |
| D-004 | 2026-09-24 | **DIVA scoring, classification and interpretation run on the backend**, and are deterministic, versioned, reproducible and auditable. Clients receive only what they need to present a result. | Brief | |
| D-005 | 2026-09-24 | **AI is kept separate** from deterministic scoring and governed interpretation. It must not invent scores, financial advice or unapproved explanations. | Brief | Use cases to be defined. See 02-product-shape. |
| D-006 | 2026-09-24 | Evidence confidence is **separate from** the readiness score. | Brief | |
| D-007 | 2026-09-24 | Launch language: **English**. | Owner | Architecture still localisation-ready. |
| D-008 | 2026-09-24 | Access is **free** for now. | Owner | |
| D-009 | 2026-09-24 | Admin app, WhatsApp and USSD are **sequenced late**. | Owner | |
| D-010 | 2026-09-24 | Scoring mappings and thresholds will become **configurable in the admin app** (late phase). Until then they live as versioned configuration. | Owner | |
| D-011 | 2026-09-24 | Design is **global-first**: no stereotyped "African" visual tropes. Africa shows up in substance, not decoration. | Owner | Rules D1–D12 in 03-design-direction, to be ratified. |
| D-012 | 2026-09-24 | This pass is **discovery only**: documentation, design direction and harness, with no product code. | Owner | |
| D-013 | 2026-09-24 | Starter questions may be **reinvented**; a questionnaire is acceptable but shouldn't feel like one. | Owner | See Q-12. |
