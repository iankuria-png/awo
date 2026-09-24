# 06 · Tooling, skills and working environment

> **Status:** Draft v0. This is how we'll work together without repeating ourselves.

## Context management: how we avoid repeating ourselves

Each Claude session starts cold. It may run in a fresh cloud container, and conversations get summarised. So **the repo is the memory**:

| File | Role | Updated when |
|---|---|---|
| [`/CLAUDE.md`](../../CLAUDE.md) | Short standing orders: what AWO is, the non-negotiables, where things live, how we work. Loaded automatically every session. | Rarely. Keep it under ~120 lines. |
| [`docs/STATUS.md`](../STATUS.md) | **Where we are right now:** phase, last session, next steps, what we're waiting on. | End of every working session. |
| [`docs/decisions/log.md`](../decisions/log.md) | Every decision, with date and source. The "we already agreed this" record. | Whenever something is decided. |
| [`docs/00-discovery/05-open-questions.md`](05-open-questions.md) | Everything we must *not* invent. | Whenever a question appears or is answered. |
| [`docs/glossary.md`](../glossary.md) | AWO vocabulary, so words mean one thing. | When a term is introduced or changed. |
| `docs/<area>/…` | One topic per document (PRD, design standard, architecture…). | As the work evolves. |

**Rule of thumb:** if we had to explain it twice, it belongs in a doc; if it's a choice, it belongs in the decision log.

## Claude plugins worth enabling (from your org's catalog)

| Plugin | What it gives us | When |
|---|---|---|
| **Design** (Anthropic) | Design critique, design-system management, **accessibility review**, **UX copy**, user-research planning and research synthesis, dev handoff | **Now:** design standard, copy tone, research with real members |
| **Figma** | Build and read Figma files directly: design-system libraries, screens, code connect | **Now, if you use Figma** (Q-11) |
| **Engineering** (Anthropic) | Architecture reviews, testing strategy, documentation, deploy checklists, incident response | Phase 1–2, before and during build |
| **Security Guidance** | Security warnings on edits and diff review on commits (injection, XSS, secrets…) | **When coding starts.** Essential for a finance and personal-data product. |
| Data | Analytics queries and dashboards | Phase 7 (admin analytics) |
| SigNoz | Observability setup, dashboards and alerts | If we choose SigNoz for monitoring |

## Built-in capabilities I'll use

- **Design canvases:** shareable, commentable mockups and wireframes (the direction explorations use this). You can comment directly on a board and I'll pick it up.
- **Data visualisation:** charts for reports and admin analytics, accessible in light and dark themes.
- **PDF / Word / PowerPoint:** report prototypes, stakeholder documents, pitch or partner decks.
- **Code review and security review:** on every meaningful change during build.
- **Session-start hook:** once code exists, so every cloud session installs dependencies and can run tests immediately.

## Project skills we'll write (in `.claude/skills/`, after the standards are agreed)

| Skill | What it does |
|---|---|
| `awo-copy-check` | Scans UI copy, reports and notifications for **advice, credit, guarantee or eligibility language**, plus tone rules (plain, warm, not patronising). |
| `awo-design-review` | Reviews a screen or component against the **design standard and the anti-stereotype rules D1–D12**. |
| `awo-decision` | Records a decision in the log, closes the matching open question and updates STATUS. |
| `awo-handoff` | End-of-session routine: update STATUS, list what changed, list what's next. |

These are deliberately *not* written yet: a skill that encodes rules we haven't agreed would just automate guesses.

## Proposed repository structure

Stack-dependent parts are marked *(later)*.

```
awo/
├── CLAUDE.md                  standing orders for every session
├── README.md
├── docs/
│   ├── README.md              map of all docs
│   ├── STATUS.md              where we are now
│   ├── glossary.md
│   ├── 00-discovery/          this pass
│   ├── product/               PRD, feature map, journeys, IA            (next)
│   ├── design/                design standard, content style, tokens      (next)
│   ├── engineering/           tech stack, architecture, domain, API       (next)
│   ├── governance/            educational language, POPIA, AI policy      (next)
│   ├── operations/            deploy, backup/restore, runbooks            (later)
│   └── decisions/             log.md + ADRs for big technical choices
├── design/                    exported explorations, wireframes, assets   (next)
├── .claude/                   settings, project skills, agents
├── apps/                                                                  (later)
│   ├── web/                   public site + member PWA
│   ├── admin/                 administration app
│   ├── api/                   the one backend
│   └── mobile/                Expo app (phase 8)
├── packages/                                                              (later)
│   ├── contracts/             API schemas and shared types
│   ├── tokens/                design tokens (web and native)
│   ├── ui/                    web component library
│   ├── i18n/                  message catalogues
│   └── config/                lint, tsconfig, test presets
└── infra/                     compose files, Caddy, backups, monitoring  (later)
```

## Working agreements (proposed)

1. **Docs before code.** A feature starts with a short spec in `docs/product/`.
2. **Never invent business rules.** Use clearly labelled sample content and log the gap as an open question.
3. **Small, reviewable changes.** One concern per commit and per PR.
4. **Decisions are written down** the same day.
5. **UK/South African English spelling** in docs and UI ("colour", "behaviour", "personalised"), matching the brief.
6. **Ask when it's yours to decide.** Product rules, brand, compliance and priorities are yours. Implementation details I'll decide, explain and record.
