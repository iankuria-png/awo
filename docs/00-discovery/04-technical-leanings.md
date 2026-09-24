# 04 · Technical leanings: stack, domain, phases

> **Status:** Draft v0. These are **leanings, not decisions.** The biggest input still missing is *who will build and operate this with me* (Q-06). A stack a small team can't run is the wrong stack, however elegant.

## Constraints that shape everything

- **One backend, many channels:** web, PWA, iOS, Android, WhatsApp, USSD and admin.
- **Proprietary scoring and interpretation run on the server only.** They must be deterministic, versioned, reproducible and auditable.
- **AWO-owned, self-managed VPS in South Africa.** Data location matters for storage, backups and every third-party integration.
- **Small team:** operational simplicity beats cleverness. Fewer moving parts, boring technology.
- **Low connectivity:** a light client, an offline-aware PWA and server-rendered public pages.

## Leaning stack

| Layer | Leaning | Why | Main alternative |
|---|---|---|---|
| Language | **TypeScript end to end** | One language across web, mobile, API and shared contracts. Largest hiring pool. | — |
| Repo | **pnpm workspaces + Turborepo monorepo** | Shared contracts, tokens and i18n across apps. One place for context. | Separate repos |
| API | **Standalone Node service (Fastify or Hono) with a Zod-defined, OpenAPI-published contract** | Many channels need one explicit API, and scoring stays private behind it. | Next.js server actions (couples the API to one web app) |
| Database | **PostgreSQL** + **Drizzle** (SQL-first migrations) | Relational domain, append-only history, auditability. Drizzle keeps SQL visible. | Prisma |
| Jobs | **pg-boss** (queue inside Postgres) | Check-in reminders, PDFs and emails with no Redis to operate. | BullMQ + Redis |
| Auth | **Better Auth** (self-hosted, Postgres) | Email/password, magic links, 2FA for admins, roles, phone OTP later. We own the data. | Keycloak or Ory (heavier) |
| Web | **Next.js** (public site + member PWA) · **Tailwind** · **Radix primitives with owned components (shadcn-style)** | Server rendering for search engines on public pages. Mature PWA story. Continuity with the previous stack's UI layer. | Astro (public) + Vite SPA (app) |
| Admin | **Separate app on its own origin** | Tighter access (2FA, IP allowlist), isolated from the member app. | Route group inside web |
| Mobile (later) | **Expo / React Native** | Shares contracts, API client, tokens, i18n and domain logic. UI stays native per platform. | Flutter; or PWA only for longer |
| Reports | **Server-rendered PDF** (HTML → PDF) | Governed text stays on the server, consistent output across devices. | Client-side jsPDF (previous stack) |
| i18n | **ICU MessageFormat** + versioned content translations in the database | Plurals and gender done right. Content translations need approval workflows. | — |
| Storage | **S3-compatible object storage on the VPS** (evaluate Garage / SeaweedFS / MinIO's current licensing), or filesystem + backups at first | Private files stay in South Africa. | SA-region cloud storage |
| Infra | **Docker Compose + Caddy** (auto-TLS) · CI deploys via **GitHub Actions** (or Kamal) | Repeatable, rollback-able, understandable by one person. | Coolify / Dokploy (self-hosted PaaS) |
| Backups | **pgBackRest or WAL-G** to a *second South African location*, with **scheduled restore drills** | A backup you haven't restored is a hope, not a backup. | — |
| Observability | Uptime checks + error tracking (self-hosted GlitchTip/Sentry-compatible) + logs (Grafana/Loki) — or **SigNoz** self-hosted | Know before members tell us. | Hosted SaaS (data-location review needed) |
| AI | **Provider-agnostic AI gateway module.** Versioned prompts, retrieval over governed content, full logging and evaluation sets. Claude is the default candidate. | Keeps AI swappable and auditable, and keeps personal data minimised. | — (Q-09 decides residency posture) |
| Testing | **Vitest** · **Playwright** e2e · **golden tests for scoring** (fixtures → expected result per method version) | Scoring and permissions are where bugs hurt most. | — |

**Why not self-hosted Supabase (the previous backend)?** It's familiar and viable. But self-hosting its full stack means operating many services on one VPS, and our critical logic (scoring, governance, audit, multi-channel) would live in our own API anyway. **If your team knows Supabase well, that changes the calculation.** See Q-06.

## Domain map (bounded contexts)

```
Identity & Access ─ users, sessions, roles, consents, legal-document versions
Member Profile    ─ individual profile, business profile, country / diaspora context
Assessment        ─ definitions (versioned, draft → published → retired), questions, options,
                    sessions, responses + INPUT PROVENANCE (self-reported | behavioural | derived,
                    channel, timestamp, member-confirmed)
Scoring           ─ scoring methods (versioned rules + weights), RESULTS (immutable, versioned,
                    supersedes-chain), dimension scores, category
Evidence          ─ EVIDENCE CONFIDENCE per result (kept separate from the score)
Interpretation    ─ governed library (blocks, versions, approval workflow),
                    result → selected blocks (pinned versions), next-step mapping
Journey           ─ next steps, 30-day check-ins, schedules, progress vs own baseline
Learning          ─ Academy (paths, modules, lessons, quizzes, weekly actions), Vault (terms, saves)
Community         ─ posts, comments, reactions, prompts, reports, moderation actions
Buddy             ─ pairings, shared goals, weekly check-ins, messages, lifecycle
Opportunities     ─ informational content, categories, discovery rules (TBD)
Channels          ─ notification preferences, templates, deliveries (email, push, WhatsApp, USSD)
Reporting         ─ member reports (PDF), aggregate admin analytics, exports
AI                ─ gateway, prompt versions, retrieval sources, logs, evaluations
Audit             ─ append-only log of privileged actions and content changes
```

**The heart of it, as a sentence:** *a member's responses (each with provenance) are scored by a specific scoring-method version into an immutable result; that result gets an evidence-confidence rating and a set of pinned, governed interpretation blocks plus one next step; a later check-in creates a new result version, never an edit.*

## Phased delivery (high level)

| Phase | Outcome |
|---|---|
| **0 · Discovery** *(now)* | Shared understanding, design direction, decisions, harness, open questions answered |
| **1 · Design foundation** | Design standard + tokens, IA, wireframes, clickable prototype of the priority journey, **tested with 5–8 real women** |
| **2 · Core platform + priority journey** | Monorepo, API, auth, consent, profiles, assessment engine, scoring, interpretation, next step, check-in, history, PDF report, member PWA, public site basics, minimal content admin, SA VPS deploy with backups and monitoring |
| **3 · Learning** | Academy + Vault (public Vault pages for search) |
| **4 · Community** | Community, moderation, accountability buddy |
| **5 · Venture** | Venture assessment and business learning |
| **6 · AI** | Grounded features from the AI map, in order of risk |
| **7 · Admin expansion** | Assessment configuration, scoring thresholds, interpretation versions, translations, audit tooling |
| **8 · Native apps** | Expo iOS and Android, store submission |
| **9 · Opportunities + localisation** | Once content rules and languages are defined |
| **10 · WhatsApp, then USSD** | On the shared API and question graph |
| **Separate scope** | Live financial-data connections (open finance / account aggregation) |

The order of phases 3–6 is open for discussion. For example, "Explain my result more simply" only needs governed text, so it could arrive early in phase 2 as a differentiator.
