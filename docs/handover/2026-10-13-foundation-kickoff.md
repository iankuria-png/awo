# Foundation kickoff: the repo, our practices, our docs, context, the design system, tools, assets and skills

> **What this is:** the brief and kickoff prompt for the foundation pass (T-120). Before any product code, Ian wants to agree how AWO is laid out and how we work. This pass researches and proposes; it builds nothing. Paste the prompt at the end into a new session.

## Where we are (13 Oct 2026)

- **Phase 0, after nine rounds of design.** The **Round 7 board** (canvas page `r7`) is the reference for UI and UX (D-034). It also holds every Round 8 and Round 9 board, grouped by topic in about 20 sections (D-042).
- **A second brand system is on the table.** AWO's suggested social brand (doc 16) differs from the app's language. Which one leads is still open (Q-49).
- **Leanings, not decisions:**
  - the stack, domain map and phases (doc 04);
  - the repo tree, plugins, project skills and the memory system (doc 06);
  - motion tooling (doc 07).
- **Already decided:**
  - **Data, scoring and AI:** production stays in South Africa (D-002) on Vultr in Johannesburg (D-043). Scoring is server-side and versioned (D-004), and scoring rules stay versioned configuration until there's an admin app (D-010).
  - **People and tools:** Ian builds it with Claude (D-015). Ian designs in Figma (D-017). Plugins are set at project scope (D-023). Claude self-checks every board (D-026).
  - **The app:** sign-in is phone first (D-035). It launches in English (D-007), it's free (D-008), and admin, WhatsApp and USSD come late (D-009).
- **What the repo holds:**
  - `docs/`: the memory system;
  - `design/`: generators for Rounds 5 to 9 and the brand page, plus marketing exports, about 22 MB;
  - `scripts/`: rendering, checking and exporting boards, and the changelog hook;
  - `.claude/settings.json`: eight plugins and the hook;
  - `.mcp.json`: the Playwright server.

**What hurts today.** These need checking; they aren't conclusions yet.
- **Branches.** GitHub's default branch was a session branch (`claude/nifty-gauss-7odogg`), and session branches drifted apart and were merged by hand. Ian has since chosen `main` as the default and branches named by type and topic (D-044).
- **The memory docs are too big.**
  - STATUS is meant to be a short snapshot, and it isn't.
  - TASKS has 15 items waiting on Ian.
  - The CHANGELOG grows by about a screen a day.
- **Binary files are in git.** About 22 MB of PNG exports and photos live in the repository.
- **The design isn't a system yet.** It lives as Python generators that write canvas HTML, which is good for exploring. But there's no tokens file, no component inventory, and nothing in Figma.

## Ian's brief (his words, tidied)

> Let's discuss how we lay the foundation: our repo, the folder structure, our practices, our MDs, how we manage context and handovers, our design (the Round 7 board, from our design exploration), the tools we'll use, the assets we need, and the skills and plugins that are relevant. In this pass, research and lay out the full project.

## The questions this pass answers

For each area, work out three things. First, what the best teams do today (researched, with sources and dates). Second, what fits one builder working with Claude. Third, a recommendation, the alternatives, and what Ian decides.

**1. The repository**
- One repository or several? Doc 04 leans to a pnpm and Turborepo monorepo.
- Branches: `main` is the default, and branches are named by type and topic (D-044). Still to propose:
  - protection for `main`;
  - how each branch reaches `main` (a pull request per pass, squash or merge);
  - tags and releases;
  - what happens to the old session branches (`claude/…`).
- Binary assets: Git LFS, a separate asset store, or exports kept out of git.
- Licence, CODEOWNERS, issue and pull-request templates, and a security policy. Secrets never go in the repository; a Vultr API key belongs in the session's secrets.

**2. The folder structure**
- The whole tree, with one line on each folder's job: `docs/`, `design/`, `apps/`, `packages/`, `content/`, `infra/`, `.claude/`.
- Where governed content lives before an admin app exists. This covers questions, scoring configuration, interpretation blocks, lessons and Words entries. It could be versioned files with schemas and review, or the database from day one (D-010).
- How doc 04's domain map becomes packages or modules. Scoring stays isolated and has golden tests.
- What happens to `design/round-5` to `round-9` and `design/brand`: archive them, keep them for exploring, or fold them into the design system.

**3. Our practices**
- A definition of done for a doc, a design, a component and a feature. It covers:
  - WCAG 2.2 AA and reduce motion;
  - the copy check (education only);
  - a data-location note;
  - tests;
  - the CHANGELOG entry.
- Git and review: commit style, pull-request size, code review (by people and by Claude) and security review.
- CI covers:
  - lint, types, unit tests and end-to-end tests;
  - accessibility (axe) and visual regression;
  - performance budgets for mid-range Android on patchy data, and bundle size;
  - golden tests for scoring.
- Versioning for scoring methods, the interpretation library, content and the app. ADRs for the big choices.
- A register of every external service with its data location (POPIA), kept current.
- Secrets and environments.

**4. Our docs (the memory)**
- Each doc's job: CLAUDE.md, STATUS, TASKS, CHANGELOG, the decision log, open questions, the glossary, handovers and the topic docs. Keep, merge, split or retire each one?
- Size budgets and archiving (for example, the CHANGELOG by month, and finished tasks moved out).
- A CLAUDE.md for each app or package, with imports and path-scoped rules if Claude Code supports them today (check its current docs).
- The first documents and templates for the planned folders:
  - `product/`: the PRD and feature specs;
  - `design/`: the design standard;
  - `engineering/`: architecture and ADRs;
  - `governance/`: educational language and the AI policy;
  - `operations/`: runbooks.
- Once code exists, does TASKS.md stay the single task list, or move to GitHub Issues and Projects (or Trello, which is connected)? This is Ian's call.

**5. Context and handovers**
- How a cold session gets up to speed in minutes: the reading order, the snapshot, and the kickoff-prompt pattern.
- Parallel sessions: one branch each, how they merge, and how the default branch stays the truth.
- When to write a handover and what goes in it (taste, mistakes, next steps, gotchas, a kickoff prompt), and when not to.
- Claude Code features:
  - skills;
  - subagents for research, to save context;
  - hooks: SessionStart to install dependencies (T-050), and the changelog hook;
  - memory and compaction;
  - canvas comments and pull-request comments as inputs.
- What to automate (for example an `awo-handoff` skill) and what stays a habit.

**6. Our design, from the Round 7 board**
- **Inventory the board's sections** and sort what's a pattern from what's a one-off. The sections cover:
  - foundations, the five tabs and their shapes, and every screen;
  - components and widgets, including Round 9's sheets, dialogs, toasts, date picker, file upload, loading states, two currencies and empty states;
  - motion M1 to M6;
  - AWO Admin and marketing.
- **Outline Design Standard v1** (T-030, T-048):
  - tokens: colour roles (including night for Learn), the Geist and Kalam scales, corners 6, 10 and 14 plus a circle, spacing, elevation, motion durations and easings, and the area shapes;
  - components with their states;
  - content style (plain words, education only) and iconography (a 2px line on a 24 grid);
  - illustration and Ola (Rive), photography (Q-27) and accessibility.
- **A token architecture** in the W3C design tokens (DTCG) format:
  - three layers: primitives, then semantic roles, then component tokens;
  - built for the web (CSS variables, Tailwind) and React Native;
  - a night mode (Q-30), and a brand layer that can take Q-49's answer without a redesign.
- **The path and the source of truth:**
  - from the canvas (exploring) to Figma (Ian designs there, D-017; check what the current seat allows);
  - then to a tokens package, a component library and Storybook, and on to the app;
  - and where the canvas stays useful: reviews, quick explorations and the self-check.
- **What blocks Design Standard v1:** Q-49 (which brand leads), Q-25 (the wordmark), Q-26 (Ola), Q-30 (theme logic) and Ian's Round 7 reaction (T-075).

**7. Tools.** Recommend each with a data-location note:
- **Design:** Figma, Rive, Lottie and the canvas.
- **Code:** editors, GitHub and Actions.
- **Runtime:** doc 04's leanings, checked against today's versions. That covers Next.js, Expo, Fastify or Hono, Postgres with Drizzle, and pg-boss. It also covers Better Auth with phone sign-in (D-035) and an SMS provider.
- **Operations on Vultr in Johannesburg:**
  - Docker Compose and Caddy;
  - backups (Q-50);
  - monitoring and error tracking;
  - privacy-friendly analytics.
- **Content, email and work:** content and translation; email (Q-17, Q-47); project management.

Prefer boring, self-hostable, well-documented tools. Flag anything that would send member data outside South Africa.

**8. Assets.** Inventory what exists: exports, photos, icons and fonts. Then list what a build needs:
- **Brand files:** the wordmark and app icon in every size (Android adaptive icons, iOS, the PWA and favicons).
- **Icons and shapes:** the icon set as SVG, plus the area shapes and the keystone.
- **Motion:** Ola (Rive) and the Lottie loops.
- **Fonts:** Geist and Kalam, with their licences and self-hosting.
- **Photography:** with licences and consent (Q-27).
- **Templates:** store, social, email and PDF.
- **Sample data:** sample members such as Naledi and Wanjiru, as fixtures.

For each asset, say where it lives, its format, its owner and its licence.

**9. Skills, plugins, subagents, hooks and MCP servers**
- **Plugins:** review the eight enabled plugins (D-023), and say what to keep, add or drop now that the build is near. Candidates include `typescript-lsp`, code review, PR review, `data`, and whatever the marketplaces offer today.
- **Project skills (T-036):** `awo-copy-check`, `awo-design-review`, `awo-decision` and `awo-handoff`. Add what the rounds taught: render, check and publish canvas boards; make a scoring change with golden tests; review content. Write their specs (when each runs, its steps, its checks), not the skills themselves, unless Ian says go.
- **Subagents** worth defining in `.claude/agents/`: a researcher, an accessibility auditor, a copy checker and a design reviewer.
- **Hooks:** SessionStart, the changelog hook and secret scanning.
- **Connectors and MCP servers:** list the ones in use and the ones that need fixing (Unsplash's email, Mobbin's plan).

**10. The full project**
- Recheck doc 04's phases:
  - what Phase 1 (the design foundation) delivers, and how it's tested with 5 to 8 women;
  - what Phase 2's first slice is;
  - what stays late.
- One page that shows it all: the repo tree, the context system, the path from design to code, and the phases. GitHub renders Mermaid diagrams.

## What to deliver

1. **An audit, first.** Write section 1 of `docs/00-discovery/17-foundation.md`: what works and what hurts, with evidence.
2. **The blueprint.** The rest of doc 17 gets one section per area above. Each ends with a recommendation, the alternatives and "Ian decides". Include diagrams and sources.
3. **Draft ADRs** for the big technical choices, marked *Proposed*, in `docs/decisions/`. Nothing goes in the decision log until Ian decides.
4. **Proposals, not changes,** in an appendix of doc 17:
   - a new CLAUDE.md;
   - the doc templates;
   - the folder tree;
   - changes to `.claude/settings.json`;
   - the skill specs.
5. **Decisions and a setup plan.** Put the big forks to Ian with a recommendation first. Then write the setup plan for the next pass: small steps in order, each with its check.
6. **The ritual.** Update the CHANGELOG, TASKS (T-120), STATUS, `docs/README.md`, and open questions for anything new. Commit and push.

## How to work

- **Start from `main`, on a properly named branch.** Work on `docs/foundation-blueprint`, created from `main` (D-044). Cloud sessions are handed an automatic branch name (`claude/…`); don't use it.
- **Verify, don't recall.** Check versions, licences, prices and data locations on the web or with context7, and write down the date you checked. Claude Code's own features change fast, so read its current docs. Browse with `scripts/screenshot.mjs` or the Playwright server when a site blocks plain requests.
- **To look at the Round 7 board,** render it as in doc 06. `scripts/export-page.mjs` and `export-page.py` give you the whole page as a PDF, with a contact sheet per section.
- **Delegate wide research to subagents** and keep their conclusions, not their dumps.
- **The CHANGELOG hook** blocks any command that both edits files and commits. Edit in one call and commit in another.

## The kickoff prompt (paste into a new session)

```text
You're working on AWO (African Wealth Oasis), still in Phase 0. Nine rounds of design exploration are done. The Round 7 board on the design canvas (https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9, page r7) is the reference for UI and UX, and it now holds Rounds 8 and 9 too, grouped by topic. Before any product code, Ian wants to agree the foundation. This pass researches and lays out the whole project. It writes no product code, scaffolds nothing, and changes no harness settings until Ian approves.

Read first:
- CLAUDE.md, docs/STATUS.md, and docs/handover/2026-10-13-foundation-kickoff.md (the brief, the questions for each area, the deliverables).
- Docs 04 (technical leanings), 06 (tooling and harness), 07 (brand and motion), 13 (Round 7), 15 (Round 9) and 16 (the suggested brand system), all in docs/00-discovery/.
- The decision log, D-001 to D-044.
- The open questions, especially Q-09, Q-10, Q-13 to Q-15, Q-17, Q-25 to Q-27, Q-30, Q-34, Q-47, Q-49 and Q-50.

Then look at the repo itself: its branches, .claude/settings.json and the Round 7 board. Render the board as in doc 06 if you need to see it.

Branch: start from main and work on a branch called docs/foundation-blueprint (D-044: branches are named by type and topic). Don't use the automatic claude/… branch the session was given.

Ian's brief is to lay out how we build AWO's foundation:
1. The repo: one repository or several, protecting main and how work branches merge into it, and binary assets.
2. The folder structure, end to end: docs, design, apps, packages, content, infra and .claude.
3. Our practices:
   - a definition of done, reviews and CI;
   - testing, including golden tests for scoring;
   - accessibility and performance on mid-range Android;
   - versioning, data-location notes and secrets.
4. Our docs: each one's job; what to keep, merge or retire; size budgets; a CLAUDE.md per app or package; templates for the coming product, design, engineering, governance and operations docs.
5. Context and handovers: how a cold session gets up to speed, parallel sessions, when and how to hand over, and what to automate.
6. Our design, from the Round 7 board:
   - the inventory and Design Standard v1's outline;
   - a token architecture (primitives, semantic roles and components; a night mode; a brand layer that can take Q-49's answer);
   - the path from canvas to Figma to code.
7. The tools, each with a data-location note.
8. The assets we need, where they live, their formats and licences.
9. Skills, plugins, subagents, hooks and MCP servers: what to keep, add and write.
10. The full project: the phases, what Phase 1 delivers and how it's tested with 5 to 8 women, and Phase 2's first slice.

Work in this order:
1. Audit what works and what hurts today, with evidence. This starts docs/00-discovery/17-foundation.md.
2. Research current practice and tools. Verify versions, licences, prices and data locations on the web or with context7, and date them. Read Claude Code's current docs on skills, plugins, subagents, hooks and memory. Compare with strong open-source monorepos and design systems. Send wide research to subagents.
3. Write the blueprint: the rest of doc 17, one section per area, each ending with a recommendation, the alternatives and what Ian decides. Add Mermaid diagrams for the repo tree, the context system, the path from design to code and the phases. Draft ADRs, marked Proposed, for the big technical choices.
4. Put the big forks to Ian, with a recommendation first. Then write the setup plan for the next pass: small steps in order, each with its check.

After each step: update the CHANGELOG, TASKS (T-120) and STATUS, then commit and push to docs/foundation-blueprint.

Keep every rule in CLAUDE.md. Don't decide what's Ian's call: the stack, which brand leads (Q-49), web or native first (Q-10), the task tracker, and paid tools. Never commit secrets. Use UK spelling.
```
