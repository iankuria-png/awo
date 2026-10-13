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

Appendix F: [facts checked on 13 October 2026](#appendix-f-facts-checked-on-13-october-2026) (versions, licences, prices, data locations, sources)

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
| H17 | **The project's plugins don't load in cloud sessions** | D-023 assumed every session, local or cloud, gets the eight plugins. Claude Code's docs (checked 13 Oct 2026) say a cloud session "doesn't install the plugins a repository turns on under `enabledPlugins`". This session bears it out: `context7` and `frontend-design` are absent, and the design and engineering skills present come from Ian's claude.ai account, not the repo. What a cloud session must have has to be committed as `.claude/skills/` and `.claude/agents/`, or enabled on claude.ai ([cloud environments](https://code.claude.com/docs/en/cloud-environments)) | §10 |

### 1.4 What the audit means for the blueprint

- **Most of the memory system is right; it needs budgets, not a rewrite.** The jobs in CLAUDE.md's table are sound. What's missing is a size limit per file, a place for finished things to go (archives), and IDs that can't collide.
- **The branch problem is a process problem.** One branch per pass, a pull request into `main`, and a rule that `main` is the truth would have prevented every collision above.
- **The design language is consistent where it was named** (corners, easings, the area colours) **and drifts where it wasn't** (spacing, greys, type sizes). That is the case for tokens: name the rest.
- **Binaries and the canvas need a home outside git's history**, with the repository keeping only sources and small, final assets.
- **Three things are Ian's before Design Standard v1 can be written:** which brand leads (Q-49), web or native first (Q-10), and the Round 7 reaction (T-075).

## Appendix F. Facts checked on 13 October 2026

Research for this pass, checked on the day: versions from the npm registry (`registry.npmjs.org/<name>/latest`), everything else from the vendor's own docs, pricing pages or release notes. Prices are in US dollars unless stated, and change: recheck before paying for anything. Items a source couldn't confirm are marked *unverified*.

### F.1 Versions and licences

| Package | Latest | Licence | Note |
|---|---|---|---|
| Node.js | 24 LTS; 26 becomes LTS on 28 Oct 2026 | MIT | Corepack no longer ships from Node 25 ([schedule](https://github.com/nodejs/Release)) |
| pnpm | 12.11.2 | MIT | Catalogs since 9.5 |
| turbo | 2.11.8 | MIT | |
| typescript | 7.0.2 | Apache-2.0 | Native compiler, stable since 8 Jul 2026; no programmatic API yet, so some tools alias TypeScript 6 ([Microsoft](https://devblogs.microsoft.com/typescript/)) |
| @biomejs/biome | 2.5.15 | MIT or Apache-2.0 | |
| eslint | 10.12.0 | MIT | Flat config only; v9 reached end of life on 6 Aug 2026 |
| next | 16.4.0 | MIT | [Self-hosting guide](https://nextjs.org/docs/app/guides/self-hosting) |
| react | 19.3.0 | MIT | |
| expo | 57.0.28 (SDK 57) | MIT | React Native 0.86; the New Architecture only; pnpm isolated installs supported since SDK 54 ([monorepos](https://docs.expo.dev/guides/monorepos/)) |
| hono / fastify | 4.13.13 / 5.12.7 | MIT | Hono 5 in release candidate; Fastify 6 in alpha |
| zod | 4.6.7 | MIT | |
| drizzle-orm | 0.45.4 | Apache-2.0 | 1.0 in release candidates since Apr 2026 |
| pg-boss | 12.38.0 | MIT | Needs Postgres 13+ |
| better-auth | 1.7.7 | MIT | Joined Vercel, Jul 2026; about 40 advisories to date, one critical in Sep 2026 ([advisories](https://github.com/better-auth/better-auth/security/advisories)) |
| tailwindcss | 4.3.3 | MIT | |
| vitest / @playwright/test / storybook | 5.0.4 / 1.64.0 / 10.6.2 | MIT / Apache-2.0 / MIT | |
| @axe-core/playwright / @lhci/cli / size-limit | 4.13.0 / 0.15.1 / 14.2.0 | MPL-2.0 / Apache-2.0 / MIT | axe's WCAG 2.2 `target-size` rule is off by default |
| @terrazzo/cli / style-dictionary | 2.8.0 / 5.6.1 | MIT / Apache-2.0 | Terrazzo supports the DTCG 2025.10 resolver; Style Dictionary's support is "a work in progress" ([SD](https://styledictionary.com/info/dtcg/)) |
| serwist | 9.5.13 | MIT | |
| geist / @fontsource/kalam | 1.7.2 / 5.3.0 | SIL OFL 1.1 | Geist's latin subset about 29 KB; Kalam is static only, about 22 KB per weight (latin) |
| @rive-app/react-canvas / motion | 4.36.0 / 14.2.0 | MIT | Rive's canvas runtime is about 0.97 MB gzipped (lite 0.42 MB) |
| nativewind / react-native-unistyles | 4.2.7 / 3.5.3 | MIT | NativeWind 5 (Tailwind 4) is a release candidate |
| lefthook / knip / gitleaks | 2.2.2 / 6.41.0 / 8.30.1 | MIT / ISC / MIT | gitleaks is "feature complete"; its author now works on Betterleaks |
| PostgreSQL | 18.6 | PostgreSQL | |
| pgBackRest / restic | 2.59.3 / 0.19.1 | MIT / BSD-2 | |
| Caddy | 2.11.7 | Apache-2.0 | |
| GlitchTip / Umami | 6.2.6 / 3.4.0 | MIT | Umami runs on Postgres alone |

**Avoid:** MinIO (repository archived 25 Apr 2026), Lost Pixel (joining Figma, product ending), Lucia (deprecated Mar 2025), Highlight (hosted service ended Feb 2026).

### F.2 GitHub

| Fact | Source |
|---|---|
| Protected branches and rulesets on **private** repositories need Pro, Team or Enterprise | [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) |
| An author can't approve their own pull request | [Required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews) |
| No secret scanning for personal private repositories short of Enterprise; user push protection covers public repositories only | [Secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning) |
| Actions: 2 000 minutes a month on Free, 3 000 on Pro; Linux $0.006 a minute after | [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) |
| LFS: 10 GiB storage and 10 GiB bandwidth on Free and Pro; release assets up to 2 GiB each, no total or bandwidth limit | [LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs), [releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) |
| Data residency only on Enterprise Cloud (EU, Australia, Japan); no South Africa | [Data residency](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/about-github-enterprise-cloud-with-data-residency) |
| Pro's price isn't on GitHub's pricing page; about $4 a month per a third-party source (*unverified*) | [Pricing](https://github.com/pricing) |

### F.3 Claude Code

| Fact | Source |
|---|---|
| `@path` imports in CLAUDE.md (up to four hops); nested CLAUDE.md files load on demand; `.claude/rules/*.md` with `paths:` globs | [Memory](https://code.claude.com/docs/en/memory) |
| After compaction the root CLAUDE.md is re-read; a SessionStart hook with the `compact` source can re-inject context | [Context window](https://code.claude.com/docs/en/context-window) |
| Skills in `.claude/skills/<name>/SKILL.md`, with `disable-model-invocation`, `allowed-tools`, `paths`, `context: fork` and `` !`command` `` injection; keep under 500 lines | [Skills](https://code.claude.com/docs/en/skills) |
| Subagents in `.claude/agents/`, with `tools`, `model`, `skills`, `isolation: worktree` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| Hooks: SessionStart sources `startup`, `resume`, `clear`, `compact`; an `if` field scopes a tool hook (`"Bash(git *)"`); `CLAUDE_CODE_REMOTE` is `true` in cloud sessions | [Hooks](https://code.claude.com/docs/en/hooks) |
| **A cloud session doesn't install the plugins a repository enables**; committed skills, agents, hooks and `.mcp.json` servers do carry over; skills enabled on claude.ai load in cloud sessions | [Cloud environments](https://code.claude.com/docs/en/cloud-environments) |
| Network secrets (Pro and Max): the proxy attaches a key to requests for listed hosts and the session never sees it; environment variables are readable by anyone using the environment | [Cloud environments](https://code.claude.com/docs/en/cloud-environments) |
| `.env` files aren't blocked by default; use `permissions.deny` | [Permissions](https://code.claude.com/docs/en/permissions) |
| Managed Code Review is Team and Enterprise only, about $15 to $25 a review; `/code-review` works locally | [Code Review](https://code.claude.com/docs/en/code-review) |

### F.4 Services and data location

| Service | Where data is stored or processed | Price | Source |
|---|---|---|---|
| AWS S3, af-south-1 | **Cape Town** (an opt-in region) | Standard $0.0274, Standard-IA $0.0149 per GB-month | AWS Price List API |
| Azure Blob, South Africa West | Cape Town, access by request (for disaster recovery) | Hot $0.0274 | [Azure regions](https://learn.microsoft.com/azure/reliability/regions-paired) |
| Google Cloud Storage, africa-south1 | **Johannesburg** (the same city as Vultr) | about $0.020 (*unverified*) | [GCS pricing](https://cloud.google.com/storage/pricing) |
| Cloudflare R2, Backblaze B2, Hetzner | No South African option | — | vendor docs |
| Amazon SES, af-south-1 | **Cape Town**, API only (no SMTP there) | $0.10 per 1 000 emails | [SES endpoints](https://docs.aws.amazon.com/general/latest/gr/ses.html) |
| Postmark / Resend / Mailgun / Brevo | US / US (account data) / US or EU / EU | from $15 / $20 / $15 / about $9 a month | vendor pages |
| Twilio Verify (SMS to South Africa) | Not stated | $0.1355 an SMS plus $0.05 a verification | [Twilio pricing](https://www.twilio.com/en-us/sms/pricing/za) |
| Clickatell | Personal data in AWS Ireland | — | Clickatell privacy notice |
| WhatsApp authentication messages | Meta | $0.0095 to South Africa, $0.004 to Kenya, $0.022 to the UK, from 1 Oct 2026 | Meta's rate card |
| Firebase Cloud Messaging | Anywhere Google has facilities | Free | [Firebase privacy](https://firebase.google.com/support/privacy) |
| Web Push with VAPID | Browser vendors' push services see only encrypted payloads (RFC 8291) | Free | RFC 8291, 8292 |
| Anthropic API | `inference_geo` is `global` or `us`; data at rest in the US | +10% for `us` | [Data residency](https://platform.claude.com/docs/en/manage-claude/data-residency) |
| Amazon Bedrock, af-south-1 | Claude models listed with global cross-region inference only | — | Bedrock model cards |
| Azure OpenAI, South Africa North | In-country processing for embeddings only | — | Azure docs |
| Figma | US; other regions Enterprise only | Professional: Full seat $16, Dev $12, Collab $3 a month; View free; Code Connect needs Organization ($55 Full, $25 Dev) | [Figma pricing](https://www.figma.com/pricing/) |
| Figma MCP server | Remote server on every plan; View, Collab and Starter seats limited to a few calls a month; Professional Dev and Full seats 200 a day | — | [Figma MCP plans](https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/) |
| Figma variables | Modes per collection: Starter 1, Professional 10, Organization 20; native import and export of DTCG JSON | — | [Figma help](https://help.figma.com/hc/en-us/articles/15343816063383) |
| Rive | The free plan adds a Rive splash screen to exports; Cadet $9 a seat a month removes it | — | [Rive pricing](https://rive.app/pricing) |
| Tokens Studio | Git sync and themes on Team, €39 an editor a month | — | [Pricing](https://tokens.studio/pricing) |
| Expo EAS | Android builds on Google Cloud, iOS on Expo's Macs, no region stated; free tier 15 + 15 builds a month | Starter $19 a month | [EAS pricing](https://expo.dev/pricing) |
| GitHub Container Registry | US; images hold code only | Free | GitHub Packages billing |
| Trello / Linear / GitHub Issues | US / US or EU / US | Free tiers; Issues free on private repositories | vendor pages |

### F.5 South Africa and Kenya: networks, data cost and phones

| Fact | Source |
|---|---|
| Mobile median in South Africa: 69.6 Mbps down, 10 up, 22 ms (Aug 2026); medians hide coverage gaps, and capped bundles throttle to 2 Mbps | [Ookla](https://www.speedtest.net/global-index/south-africa) |
| A 1 to 1.5 GB, 30-day bundle averages about R63; operators charge 6c to 8c a MB in bundle: **1 MB costs about 7c** | [ICASA tariff report, Jul to Dec 2025](https://www.icasa.org.za/) |
| Phones on the web, Jul 2026: South Africa Samsung 46%, Apple 24%, Huawei 10%; Kenya Samsung 26%, Tecno 14%, Oppo 9%, Infinix 7% | StatCounter |
| Galaxy A-series (A06, A16) are 60% of Samsung's African shipments; Transsion (Tecno, Infinix, Itel) leads the continent | [Canalys](https://canalys.com/newsroom/africa-smartphone-market-q1-2025) |
| Lighthouse's mobile profile: 150 ms round trip, 1.6 Mbps down, 4× CPU slowdown, a Moto G Power | [Lighthouse throttling](https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md) |
| Good Core Web Vitals at the 75th percentile: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 | [web.dev](https://web.dev/articles/vitals) |

### F.6 Reference monorepos

| Repo | Tools | Layout | Merge |
|---|---|---|---|
| [cal.com](https://github.com/calcom/cal.com) | yarn, Turborepo, Biome, Changesets | apps, packages | squash |
| [documenso](https://github.com/documenso/documenso) | npm, Turborepo, Biome, commitlint | apps, packages | squash |
| [formbricks](https://github.com/formbricks/formbricks) | pnpm (catalogs), Turborepo, ESLint | apps, packages, docs | squash |
| [Bluesky social-app](https://github.com/bluesky-social/social-app) | pnpm, oxlint; one Expo app at the root | app at root; assets listed with owners in `ASSETS.md` | squash |
| [Expo](https://github.com/expo/expo) | pnpm, Turborepo, oxlint, Changesets | apps, packages, tools | squash |
| [shadcn/ui](https://github.com/shadcn-ui/ui) | pnpm, Turborepo, Changesets | apps, packages | squash |
| [create-t3-turbo](https://github.com/t3-oss/create-t3-turbo) | pnpm (named catalogs), Turborepo, Renovate | apps, packages, `tooling/` for shared configs | squash |

None uses Git LFS; many now carry a `CLAUDE.md` or `AGENTS.md`. Design systems compared for tokens: [GitHub Primer](https://primer.style/foundations/primitives/token-names) (base, functional and component tokens; nine themes; code to Figma), [Adobe Spectrum](https://spectrum.adobe.com/page/design-tokens), [Atlassian](https://atlassian.design/foundations/tokens/design-tokens), [Shopify Polaris](https://polaris-react.shopify.com/design/colors/color-tokens), [Salesforce SLDS 2](https://lightningdesignsystem.com/), [Radix Colors](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale) and Material 3. The DTCG format reached its first stable version, [2025.10](https://www.designtokens.org/tr/2025.10/format/), with a [resolver module](https://www.designtokens.org/tr/2025.10/resolver/) for brands and modes.
