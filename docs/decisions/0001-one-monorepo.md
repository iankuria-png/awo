# ADR 0001: One monorepo, with pnpm workspaces and Turborepo

- **Status:** Proposed (foundation pass, T-120, 13 October 2026). Not in the decision log until Ian decides.
- **Relates to:** D-001 (a new repository), D-015 (Ian builds it with Claude); doc 04's leaning; doc 17 §2 and §3.

## Context

AWO will have several apps (the member PWA and public pages, the API, later AWO Admin and an Expo app) sharing contracts, tokens, scoring, content and messages. One person builds it, with Claude sessions that start cold and read the repository as their memory. Every extra repository is another place a session has to be pointed at, another CI and another set of versions to keep in step.

## Options

| Option | For | Against |
|---|---|---|
| **A. One monorepo: pnpm workspaces and Turborepo** | One place for docs, design, content and code; shared packages without publishing; one CI; one clone per session; atomic changes across the API and its clients. Turborepo recommends `apps/` and `packages/` and caches tasks. Most strong open-source TypeScript monorepos use it (cal.com, documenso, formbricks, shadcn/ui, create-t3-turbo, Expo itself) | One repo's CI runs more than it needs to without filters; Expo needs care in a monorepo (now mostly automatic) |
| **B. One monorepo with Nx** | Stronger module-boundary rules, code generators | More concepts and configuration for one person; the boundary rule can be had with a lint plugin |
| **C. Several repositories** (API, web, mobile, design system) | Each small and independent | Contracts and tokens must be published and versioned; changes span repos; a session sees only part of the picture; more CI and more secrets |

## Proposed decision

**Option A.** With the tools as they stand on 13 October 2026 (checked on the npm registry and the projects' docs):

- **pnpm 12** with workspaces and **catalogs** (one version of each shared dependency, set in `pnpm-workspace.yaml`), pinned through `packageManager` or `devEngines` in the root `package.json`, since Node no longer ships Corepack from version 25.
- **Turborepo 2.11** for the task graph (`build`, `lint`, `typecheck`, `test`) and its cache.
- **Node 24 LTS** now, moving to **Node 26** once it becomes LTS (28 October 2026).
- **TypeScript 7** (the native compiler, stable since 8 July 2026), with the TypeScript 6 alias for tools that still need its programmatic API.
- **Biome 2.5** for formatting and most linting; ESLint 10 only where a plugin needs it (for example Expo's or a module-boundary rule).
- **lefthook** for local git hooks, **knip** for unused code and dependencies.
- No Changesets: nothing is published, and the CHANGELOG ritual records changes.
- Expo (when it comes) with pnpm's default isolated installs, which Expo supports from SDK 54; `node-linker=hoisted` only if a native module breaks.

The stack inside the apps (Next.js or not, Fastify or Hono, and so on) is a separate decision (ADR 0007).

## Consequences

- The repo's root gains `package.json`, `pnpm-workspace.yaml`, `turbo.json` and a `packages/config` (or `tooling/`) folder for shared presets, in the setup pass's first code step, and only with Ian's go.
- CI uses Turborepo's filters so a docs-only pull request skips the code tasks.
- Every session can run the whole check suite with one command (`pnpm check`).

## Data-location note

The repository lives on GitHub, which stores data in the United States; GitHub offers data residency only on Enterprise Cloud (EU, Australia, Japan), with no South African region. The repo holds code, docs, governed content and synthetic fixtures only: **never member data and never a production database dump.**

## Ian decides

One monorepo (recommended) or several; Turborepo (recommended) or Nx.
