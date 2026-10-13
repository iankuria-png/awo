# 17 · The foundation: how we build AWO

> **Status:** Draft v0 for Ian, written in the foundation pass (T-120, 13 October 2026) on the branch `docs/foundation-blueprint`. It researches and proposes; it builds nothing. Nothing here is decided until Ian says so and it lands in the [decision log](../decisions/log.md).
> **The brief:** [handover/2026-10-13-foundation-kickoff.md](../handover/2026-10-13-foundation-kickoff.md).
> **How to read it:** section 1 is the audit (what works and what hurts today, with evidence). Sections 2 to 11 are the blueprint, one area each, and each ends with a recommendation, the alternatives and what Ian decides. Section 12 puts the big forks to Ian; section 13 is the setup plan for the next pass. The appendices hold the proposals (a new CLAUDE.md, templates, settings, skill specs).

## Contents

1. [The audit: what works and what hurts](#1-the-audit-what-works-and-what-hurts)
2. The repository *(step 3)*
3. The folder structure *(step 3)*
4. Our practices *(step 3)*
5. Our docs *(step 3)*
6. Context and handovers *(step 3)*
7. Our design, from the Round 7 board *(step 3)*
8. Tools *(step 3)*
9. Assets *(step 3)*
10. Skills, plugins, subagents, hooks and MCP servers *(step 3)*
11. The full project *(step 3)*
12. Decisions for Ian *(step 4)*
13. The setup plan *(step 4)*

## 1. The audit: what works and what hurts

Checked on 13 October 2026 against the repository (49 commits, 24 September to 13 October), its five remote branches, `.claude/settings.json` and the published canvas (`canvas.json`, version 1790881571).

### 1.1 The repository at a glance

| Measure | Today |
|---|---|
| Commits | 49 in 20 days, all by Claude sessions; no pull requests |
| Branches on GitHub | `main` (= `claude/nifty-gauss-7odogg`, the old default), `docs/foundation-kickoff` (two commits ahead of `main`, not merged), `claude/intelligent-hypatia-ja9g5n` (one commit, already inside `docs/foundation-kickoff`), `claude/exciting-cray-7z7fke` (stale at Round 5, already inside `main`) |
| Working tree | `docs/` 331 KB of Markdown; `design/` 21 MB, of which `design/marketing/` is 19 MB (57 PNGs); 53 Python generators (14 552 lines); 7 scripts |
| Git history | 25.5 MB packed; 81 image blobs, 26.5 MB across history |
| Harness | 8 plugins at project scope (D-023), one hook (the changelog), one MCP server (Playwright); no project skills, no subagents, no SessionStart hook |
| Design canvas | 9 pages and 391 boards; the Round 7 board alone has **161 boards in 20 sections** |

### 1.2 What works (keep it)

| What | Evidence |
|---|---|
| **The repo is the memory.** A cold session starts from CLAUDE.md, STATUS and a kickoff prompt, and is working within minutes | This session started from the [kickoff prompt](../handover/2026-10-13-foundation-kickoff.md) with no other context. Three handovers so far, each with a prompt to paste |
| **CLAUDE.md is short** | 77 lines, under doc 06's budget of about 120 |
| **Decisions carry their source** | 44 decisions, each with the owner's words or "Joint", so nobody re-argues a settled point (D-031 even records that it came from a draft typed in a screenshot) |
| **The open-questions register stops invention** | 50 questions. Round 9 raised Q-45 to Q-48 instead of inventing rules for savings-group books, sharing, email and ambassadors, and designed "safe versions" meanwhile |
| **The changelog hook keeps the diary current** | Every commit since the hook arrived (44) touched the CHANGELOG, which holds 47 entries; the five without one came before the hook |
| **Claude self-checks every board** (D-026) | The renders caught real defects: SVG text that doesn't render, a squashed card, overflow under the tab bar, a tooltip over a stone, banding in exports ([10](10-round-4.md), [13](13-round-7.md#round-7-as-the-full-board)) |
| **Generators make the design reproducible** | Every board since Round 5 is regenerated from Python in `design/`. Corners are named constants (`R_S, R_M, R_L = 6, 10, 14`) and are used consistently |
| **Two easings already dominate** | In rounds 7 to 9, `cubic-bezier(.2,.8,.2,1)` (ease-out) appears 163 times and `cubic-bezier(.34,1.56,.64,1)` (the spring) 24 times: motion tokens in all but name |
| **Plugins load everywhere** | D-023: every session of this repo, local or cloud, gets the same eight plugins |
| **The browser works in the cloud** | `scripts/playwright-mcp.sh` and `screenshot.mjs` run the pre-installed Chromium with the proxy pinned, which made research, self-checks and the 18 MB board export possible |

### 1.3 What hurts (fix it in the foundation)

| # | What hurts | Evidence | Where the blueprint answers it |
|---|---|---|---|
| H1 | **Branches drift, and nothing merges them** | GitHub's default was a session branch. Session 3 branched before session 2's commits landed, so both reused IDs; the merge renumbered two docs (09, 10), two questions (Q-31, Q-32) and a task (T-028) ([CHANGELOG, 25 Sep](../CHANGELOG.md)). Today the kickoff itself sat on an unmerged branch, and this session had to bring it in. No branch is protected and no change has gone through a pull request | §2 |
| H2 | **IDs are handed out by whoever writes first** | T-, Q- and D- numbers are taken from the files on the session's branch, so two parallel sessions collide (H1) | §6 |
| H3 | **STATUS isn't a snapshot any more** | 4.7 KB; its "current focus" is one 600-character sentence; "Start here" lists five items, and item 2 still says Ian reacts to Round 8 (T-093), which Round 9 has overtaken | §5 |
| H4 | **TASKS is half history** | 17.8 KB and 92 rows: 62 are Done, 17 wait on Ian (the oldest, T-075 and T-085, since 25 September). The "Now" heading is a paragraph | §5 |
| H5 | **The CHANGELOG grows by about 2.3 KB a day** | 46.6 KB and 313 lines after 20 days. A session reads only the top, but the file costs more each week to open and to edit | §5 |
| H6 | **A cold start costs a lot of context** | The kickoff's reading list is 128 KB (about 32 000 tokens) before any work; all of `docs/` is 331 KB (about 83 000). Round docs are long: doc 14 is 44 KB | §5, §6 |
| H7 | **Binary files live in git** | 57 PNGs (19 MB) in four generations of marketing sets (Rounds 3, 6, 7 and 8), of which only Round 8 is current. Every regenerated PNG adds a new blob for good (81 image blobs, 26.5 MB in history) | §2, §9 |
| H8 | **The photos have one home** | The nappy.co stand-in photos exist only in the canvas's asset store (`/_blob/<id>` in `design/round-5/lib.py`), with no copy in the repository or elsewhere | §9 |
| H9 | **The design isn't a system yet** | The palette is Python constants in `design/round-5/lib.py`, inherited through a chain (round-5 → 6 → 7 → 8 → 9; `sys.path` inserts in 22 files), so archiving Round 5 would break Round 9. Rounds 7 to 9 use **86 distinct raw hex colours**, **36 font sizes** and about **20 gap values** (2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 36, 40): no spacing scale. There is no component inventory, and nothing is in Figma | §7 |
| H10 | **The reference board doesn't say what's current** | The Round 7 board keeps superseded boards beside their replacements: Round 7's Home beside Round 8's, "Store 4: Vault" and a Vault screen although the Vault became Words inside Learn (D-037), and Ask beside Learn's new tabs. Nothing marks which is canonical | §7 |
| H11 | **Two brand systems are open** (Q-49) | The app (evergreen, lime, Geist, corners 6/10/14) and AWO's suggested social brand (plum, terracotta, warm stone, a serif with Montserrat, 4 px corners) differ in every token layer but motion | §7 |
| H12 | **Ian's reactions are the bottleneck** | 17 tasks wait on Ian. Design Standard v1 (T-048) waits on T-075 (Round 7) and Q-49, Q-25, Q-26 and Q-30 | §11, §12 |
| H13 | **The harness has gaps** | No SessionStart hook (T-050), no project skills (T-036), no subagents, no secret scanning, no `permissions` (nothing stops a session reading a future `.env`). The changelog hook only checks that the CHANGELOG changed (not TASKS), and it blocks any command that contains `git commit`, so editing and committing in one call fails | §10 |
| H14 | **The canvas is a single, heavy home** | 161 boards on one page: the canvas's own export gives up, so two scripts were written to download it (an 18 MB PDF). Board layout and notes live only in the artifact's `canvas.json`, not in git | §7, §9 |
| H15 | **No repository basics** | No licence, security policy, pull-request template, `.editorconfig` or Node version file. Fine for Phase 0, needed before code | §2 |
| H16 | **The platform question is open** (Q-10) | Web first or native first decides the first app, the token outputs and the motion runtime | §11, §12 |

### 1.4 What the audit means for the blueprint

- **Most of the memory system is right; it needs budgets, not a rewrite.** The jobs in CLAUDE.md's table are sound. What's missing is a size limit per file, a place for finished things to go (archives), and IDs that can't collide.
- **The branch problem is a process problem.** One branch per pass, a pull request into `main`, and a rule that `main` is the truth would have prevented every collision above.
- **The design language is consistent where it was named** (corners, easings, the area colours) **and drifts where it wasn't** (spacing, greys, type sizes). That is the case for tokens: name the rest.
- **Binaries and the canvas need a home outside git's history**, with the repository keeping only sources and small, final assets.
- **Three things are Ian's before Design Standard v1 can be written:** which brand leads (Q-49), web or native first (Q-10), and the Round 7 reaction (T-075).
