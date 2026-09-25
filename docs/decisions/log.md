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
| D-014 | 2026-09-24 | **No existing brand to keep.** The old purple AI logo and colours are dropped. Brand identity (wordmark, colour, iconography, illustration) is designed from scratch. | Owner | Answers Q-01. |
| D-015 | 2026-09-24 | **Ian Kuria** (product developer and software engineer) builds and operates AWO with Claude. | Owner | Answers Q-06. Informs the stack choice. |
| D-016 | 2026-09-24 | **Compliance (FAIS, POPIA) is covered by AWO.** Claude doesn't spend time on compliance analysis, but still applies the product rules in CLAUDE.md. | Owner | Answers Q-08. |
| D-017 | 2026-09-24 | **Design tool: Figma.** | Owner | Answers Q-11. Figma connector to be connected. |
| D-018 | 2026-09-24 | **First members:** women and business people who want to understand their finances. The individual and entrepreneur contexts both matter from day one. | Owner | Answers Q-03. |
| D-019 | 2026-09-24 | Round 1 feedback: **A** liked (Home to improve); **B**'s Ask is strong but needs micro-interactions (candidate for Learn); **C** rejected, replaced by a human-centred direction (D). | Owner | See 07-brand-and-motion. |
| D-020 | 2026-09-24 | **Motion-first.** Motion and illustration are part of the brand and the UX, not decoration. | Owner | Principles M1–M6 in 07. |
| D-021 | 2026-09-24 | A **mascot** is allowed in **one area only**, not everywhere. Proposal: Ola, in Learn and Ask only, never on results. | Owner + Joint | Name and scope: Q-26. |
| D-022 | 2026-09-24 | Tier names (Bronze/Silver/Gold/Platinum) are **open to exploration**. | Owner | Q-04 stays open for names. |
| D-023 | 2026-09-24 | Plugins enabled at project scope in `.claude/settings.json`: design, figma, engineering, security-guidance, modern-web-guidance, frontend-design, playwright, context7, skill-creator. | Owner | Every session in this repo gets them. |
| D-024 | 2026-09-24 | Round 2 feedback: combine **A and D** into one direction with more screen variants. **Ola, colours and Learn interactivity were the weakest**; Round 1's Night Oasis (B) looked better than Round 2's. Push further: widgets, stats bars, micro-animation, switches, graphs, layout variations, bento grids, device mock-ups, campaign ads, Play Store assets. Non-generic layouts, visual-first. | Owner | Brief for Round 3 in STATUS. |
| D-025 | 2026-09-24 | Design research needs outside inspiration. Network access for the cloud environment will be widened so Claude can reach design reference sites, photo libraries and Figma. | Owner | See STATUS, "Environment". |
| D-026 | 2026-09-25 | **Claude self-checks every board** before publishing: it renders each board locally with the canvas runtime, screenshots it (clicking through interactive states) and fixes breakage (clipping, overlap, contrast). Fixes cover breakage only, not redesigns. | Owner | Answers T-010 and T-024 (sessions 2 and 3 both recorded it). Tool: `scripts/canvas-preview.mjs`; recipe in 06. |
| D-027 | 2026-09-25 | Round 4 goes ahead as the review proposed: fewer screens, deeper moments. Ian **leans towards Mentor and Circle** but wants to see all three directions before choosing, so Moment 1 is built three ways and the rest of the loop as Mentor + Circle. | Owner | Q-29 stays open until he reacts. |
| D-028 | 2026-09-25 | **Round 4 lost character.** Bring back Round 3's **bold condensed type, colour as big blocks, signature shapes and visual-first layouts**. The target is a **meaningful design language: fun, modern, clean**, where every shape and colour stands for something. Test it first with a **volume test** (the same screens at three volumes) before redoing the flows. | Owner | Reverses Round 4's retirement of heavy condensed type in the app and of the shapes. Claude keeps Round 4's behaviour rules unless Ian says otherwise: no streak counts, no red for a month that went down, no chips over faces. Round 5, doc 11. |
| D-029 | 2026-09-25 | The app is built around **five areas: Home, Learn, Vault, Community, Me**. | Owner | Replaces Round 4's Today, Learn, Circle, You. Feeds the IA (T-032). |
