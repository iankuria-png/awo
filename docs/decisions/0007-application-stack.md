# ADR 0007: The application stack

- **Status:** Proposed, **for Ian to decide** (the stack is his call). Foundation pass, T-120, 13 October 2026.
- **Relates to:** doc 04 (the leaning stack), D-002, D-035 (phone sign-in), D-043 (Vultr, Johannesburg), Q-09, Q-10, Q-17; ADRs 0001, 0005, 0006, 0008.

## Context

Doc 04 leaned to TypeScript end to end: Next.js for the public pages and the member PWA, a standalone API (Fastify or Hono) with a Zod contract published as OpenAPI, Postgres with Drizzle, pg-boss for jobs, Better Auth, and Expo later. This ADR checks each leaning against the state of the tools on **13 October 2026** (npm registry, official docs and release pages; full notes in doc 17 §8) and sets out the choices. It recommends; Ian decides.

## The leanings, checked

| Layer | Leaning | Today | Risk to weigh | Alternative |
|---|---|---|---|---|
| Web | Next.js | **16.4.0** (MIT). Self-hosting is first-class in its docs; image optimisation works under `next start`; the Build Adapters API is stable since 16.2 | A fast patch cadence (security releases in December 2025; another due 14 October 2026). PWA support needs Serwist 9.5 (with a separate Turbopack package) | Expo web for one codebase: not yet credible for an SEO-friendly PWA (its API routes are beta, its server components experimental, and PWA support is manual) |
| API | Fastify or Hono, with a Zod contract and OpenAPI | Fastify **5.12.7** (v6 in alpha); Hono **4.13.13** (v5 in release candidate); **oRPC 1.15.6** emits OpenAPI 3.2 from typed procedures | Both majors move within months: pin versions | oRPC gives typed clients and an OpenAPI document from one definition; tRPC's OpenAPI support is still alpha |
| Validation | Zod | **4.6.7**, v4 stable since July 2025 | — | Valibot |
| Database | PostgreSQL | **18.6** | — | — |
| ORM | Drizzle | **0.45.4**; 1.0 has been in release candidates since April 2026 | Adopting 0.45 now means a migration to 1.0 later | **Prisma 7** (no Rust engine since November 2025; Prisma 8 is in release candidate); **Kysely** 0.29 (a query builder, SQL-first) |
| Jobs | pg-boss | **12.38.0**, needs Postgres 13+ | Changes behaviour within minor versions: pin it | Graphile Worker 0.18 |
| Auth | Better Auth | **1.7.7**; has a phone-number plugin with OTP, Google and Apple sign-in, and an Expo client | Joined Vercel in July 2026 (it says it stays framework-agnostic); about 40 security advisories so far, one critical in September 2026; **AWO writes the SMS sender and the rate limiting** | Auth.js (now maintenance only); a self-hosted identity server (Ory, Keycloak, Zitadel) is heavier to run |
| SMS for the sign-in code | Not chosen | Twilio Verify about $0.1355 per SMS to South Africa plus $0.05 per success; Clickatell processes personal data in AWS Ireland; no provider checked confirmed storage in South Africa | Every SMS path sends phone numbers abroad: it needs a data-location decision | **WhatsApp authentication messages**: $0.0095 each to South Africa (Meta's rate card from 1 October 2026), about a fourteenth of Twilio's SMS price, but through Meta |
| Native (later) | Expo | SDK **57** (React Native 0.86, the New Architecture only) | EAS builds run on Google Cloud with no stated region (no member data in builds); the Expo push service is US-based (avoidable by sending through FCM and APNs directly) | A PWA only, for longer |
| UI primitives | Radix, shadcn-style | Radix still active; **Base UI 1.0** shipped December 2025 and became shadcn/ui's default in July 2026 | — | React Aria |
| Styling | Tailwind | **4.3.3** | NativeWind's stable release is still on Tailwind 3 (v5 is a release candidate), so web and native would build tokens differently | Plain CSS variables from the tokens package |
| PDF | HTML to PDF on the server | Playwright's `page.pdf` (already a test dependency) or Gotenberg 8.37 | — | `@react-pdf/renderer` |
| i18n | ICU messages | `react-intl` 12, Lingui 6.9, next-intl 4.14 all handle ICU | — | — |
| Tests | Vitest, Playwright | Vitest **5.0.4**, Playwright **1.64.0**, Storybook **10.6.2** | Vitest 5 needs Node 22.12+ | — |

## Recommendation (Claude's)

Keep doc 04's shape, with four adjustments:

1. **Next.js 16** for the member PWA and public pages, self-hosted with `next start` behind Caddy.
2. **A standalone API with oRPC on Hono or Fastify** (oRPC can sit on either), so the contract, the typed client and the OpenAPI document come from one definition. If Ian prefers plain REST handlers, Fastify 5 with `@fastify/swagger` is the most settled choice.
3. **Postgres 18 with Drizzle**, accepting the 1.0 migration later; or **Kysely** if Ian wants SQL first and fewer moving parts. Prisma is now a sound choice too; it's a matter of taste.
4. **Better Auth** with its phone-number plugin, pinned and watched for advisories, with **AWO's own sender behind an interface** so SMS and WhatsApp providers can be swapped once the data-location decision is made.

Everything else as doc 04: pg-boss, Zod 4, Tailwind 4, Base UI or Radix primitives with owned components, Vitest, Playwright, Storybook, HTML-to-PDF on the server. Pin exact versions; let Dependabot or Renovate propose updates weekly.

## What Ian decides

1. The stack as a whole (this ADR), or changes to it.
2. **Web first or native first** (Q-10): it decides which app is built in Phase 2 and which token outputs come first.
3. The SMS or WhatsApp provider for the sign-in code, with its data-location note (a paid service).
4. The AI posture (Q-09), before any AI feature ships.

## Data-location note

All runtime pieces above are self-hosted on Vultr in Johannesburg except: the SMS or WhatsApp provider (phone numbers leave South Africa with every provider checked), push notifications (Google's and Apple's services, unavoidable for push), and, if native, Expo's build service (no member data). Each gets a row in the data-location register.
