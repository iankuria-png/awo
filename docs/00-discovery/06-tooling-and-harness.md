# 06 · Tooling, skills and working environment

> **Status:** Draft v0. This is how we'll work together without repeating ourselves.

## Context management: how we avoid repeating ourselves

Each Claude session starts cold. It may run in a fresh cloud container, and conversations get summarised. So **the repo is the memory**:

| File | Role | Updated when |
|---|---|---|
| [`/CLAUDE.md`](../../CLAUDE.md) | Short standing orders: what AWO is, the non-negotiables, where things live, how we work. Loaded automatically every session. | Rarely. Keep it under ~120 lines. |
| [`docs/STATUS.md`](../STATUS.md) | **Snapshot:** phase, focus, where to start. | When the focus changes. |
| [`docs/TASKS.md`](../TASKS.md) | **The single task list.** | Every commit. |
| [`docs/CHANGELOG.md`](../CHANGELOG.md) | **The diary**, one entry per commit. Enforced by a commit hook. | Every commit. |
| [`docs/handover/`](../handover/) | Full context transfer when a session ends mid-stream. | Near the context limit. |
| [`docs/decisions/log.md`](../decisions/log.md) | Every decision, with date and source. The "we already agreed this" record. | Whenever something is decided. |
| [`docs/00-discovery/05-open-questions.md`](05-open-questions.md) | Everything we must *not* invent. | Whenever a question appears or is answered. |
| [`docs/glossary.md`](../glossary.md) | AWO vocabulary, so words mean one thing. | When a term is introduced or changed. |
| `docs/<area>/…` | One topic per document (PRD, design standard, architecture…). | As the work evolves. |

**Rule of thumb:** if we had to explain it twice, it belongs in a doc; if it's a choice, it belongs in the decision log.

## Claude plugins: installed (D-023)

These are enabled at **project scope** in [`.claude/settings.json`](../../.claude/settings.json), with their marketplaces declared there, so every new session of this repo (local or cloud) loads them automatically.

| Plugin | Marketplace | What it gives us |
|---|---|---|
| **design** | knowledge-work-plugins | Design critique, design-system management, accessibility review, UX copy, user research, research synthesis, handoff |
| **figma** | knowledge-work-plugins | Build and read Figma files: libraries, screens, design-to-code, code connect. **Needs the Figma connector** (below). |
| **engineering** | knowledge-work-plugins | Architecture, system design, testing strategy, documentation, deploy checklists |
| **security-guidance** | knowledge-work-plugins | Security warnings on edits and review of diffs (injection, XSS, secrets…) |
| **modern-web-guidance** | knowledge-work-plugins | Current web platform best practices |
| **frontend-design** | claude-plugins-official | Distinctive, non-templated visual design. Its critique shaped Round 2 (rule D13). |
| ~~playwright~~ | claude-plugins-official | Disabled: it launches Google Chrome, which cloud sessions don't have. Replaced by the project server below. |
| **context7** | claude-plugins-official | Up-to-date library documentation lookup while building |
| **skill-creator** | claude-plugins-official | Write and test our own project skills |

The design and engineering plugins also bundle optional connectors (Slack, Linear, Notion, Asana, Atlassian…). They stay idle unless you sign in.

**Connectors (connected 2026-09-25):** Figma, Unsplash (photo search), Fonts, tldraw, Trello and HyperFrames. Mobbin is connected but needs a paid plan to return results. Connectors are read when a session starts.

**Playwright (browser automation):** a project MCP server in [`.mcp.json`](../../.mcp.json), launched by [`scripts/playwright-mcp.sh`](../../scripts/playwright-mcp.sh). In cloud sessions it uses the pre-installed Chromium and pins the egress proxy's CA key, so TLS stays verified. On a laptop it uses Playwright's defaults. We use it for inspiration research (the sites block plain `curl`), visual checks and, later, end-to-end tests.

**Later, when code exists:** `typescript-lsp` (code intelligence), `pr-review-toolkit` or `code-review` (PR review agents), and `data` (admin analytics).

## Reviewing canvas boards locally (render recipe)

Review boards as rendered screenshots, never from source. This is how the [Round 3 review](08-round-3-review.md) was done.

1. **Fetch** the canvas with the Artifact tool (`read`, then `path` for each `project/*.dc.html`, `project/canvas.json` and `artifact-type/dc-runtime.js`). Fetch image assets by their `/_blob/<id>` asset ids.
2. **Serve** the folder locally with `dc-runtime.js` exposed as `project/support.js` and each asset at `/_blob/<id>` (a few lines of Node or Python).
3. **Screenshot** each board at its exact root size with the pre-installed Chromium and the proxy SPKI pin (as in `scripts/screenshot.mjs`). Wait about 1.5 s for fonts and first motion.
4. **Contact sheets** (Pillow) make it quick to compare many boards at once.
5. **Delegate** the fetching and rendering to a subagent; it saves context.

Keep everything in the scratchpad. Don't commit `dc-runtime.js` or the renders.

## Motion and illustration tooling

See [07-brand-and-motion § Tooling](07-brand-and-motion.md#tooling-for-motion-and-illustration): Rive (Ola and other interactive characters), Lottie/dotLottie (illustrative loops), Motion (web transitions), React Native Reanimated and Skia (native), and Figma for design and prototyping.

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
| `awo-design-review` | Reviews a screen or component against the **design standard and rules D1–D14** (anti-stereotype, anti-template, motion). |
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
