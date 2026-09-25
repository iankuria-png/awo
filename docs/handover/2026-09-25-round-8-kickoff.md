# Round 8 kickoff: Learn with the Vault, the Hub, goals of every kind, real stories, a real feed

> **What this is:** the handover and kickoff prompt for the next design pass. Round 8 builds on Round 7 (the full reference board, [doc 13](../00-discovery/13-round-7.md)) with Ian's new direction (D-037, D-038). Paste the prompt at the end into a new session.

## Where we are

- **Round 7** on the [canvas](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9) (page `r7`) is the reference: Geist for all type, Kalam for rare handwritten moments, corners 6, 10 and 14 plus a circle, and the five area shapes. It holds:
  - foundations and brand;
  - accounts and the first loop;
  - the five areas, plus progress, the check-in, the buddy and settings;
  - the deeper loop (lesson, compare, what-if, check an offer, report, hard moments);
  - entrepreneurs, components and widgets;
  - AWO Admin;
  - marketing.
- **Generators** are in `design/round-7/*.py` (`round7.py` builds them all). Render with `scripts/serve-boards.py` and `scripts/board-check.mjs`; lay out with `design/round-7/layout7.py` (see [06](../00-discovery/06-tooling-and-harness.md#reviewing-canvas-boards-locally-render-recipe)).
- **Phase 0:** design exploration only. No product code.

## Ian's brief for the next pass (his words, tidied)

1. **Learn and Vault merge.** Inside Learn, a tab design makes room for the Vault, with a clean, animated switch.
2. **A new centre tab: AWO Hub, or simply Hub.** This is where entrepreneurs and employed people get real value, through tools that serve both. It sits where the Vault was, and needs its own icon, hierarchy and page structure.
   - Ian's starting list: a payslip or salary analyser, a loan's real cost, invoices, a DIVA score calculator, an ROI calculator, quotes, statement analysis, goals, and e-commerce stores inside AWO for business people, with world-class UI and UX.
   - "I don't want this to be just generic tools. You should identify more, and how each is woven into the Hub."
3. **Goals of every kind,** not just a safety net: a car, moving out, starting to invest.
4. **Learning beyond chama lessons:** the buzzwords (forex, crypto), dividends, shares, and featured startups and companies. "People need real value."
5. **Content people respond to:** real human stories, failure and rising, painful money lessons and mistakes, and key lessons from top moguls (an AWO podcast).
6. **Community as a place to consume content:** a feed where members post ("started my new business"), X-style or Substack-style, with visuals, but unique to AWO.

## Proposed information architecture

| Tab | Shape | Holds |
|---|---|---|
| Home | pool | Today: goals (several pools, not one), this week's step, stories and the community pulse |
| Learn | moon | Tabs: **Paths** (courses and topics), **Words** (the Vault: the arch lives on here), **Stories** (human stories and the podcast) |
| **Hub** (centre) | new shape | Tools that do things, in two modes: **My job** and **My business** |
| Community | ripple | A feed of notes, letters, milestones and questions; circles; member shops |
| Me | stones | DIVA profile, progress, report, settings, data |

**Hub icon: explore three and animate each.**
- **A keystone:** the stone that holds an arch together. The Vault's arch moves into Learn, and its keystone becomes the Hub.
- **A dial:** tools that adjust.
- **A market awning:** "things you do".

It must read at 24px, match the 2px line family, and move in one meaningful way.

## Hub: a proposed tool catalogue (research, trim and rank it)

Every tool follows one skeleton:
- **input** (typed, or read from a photo or PDF that she confirms);
- **one big, plain result**;
- **what it means**, from governed text;
- **learn this** (a lesson and the Vault words);
- **make it a goal or a step**;
- **share a milestone** (without numbers).

Calculations are deterministic and versioned. AI may only read documents or explain; it is labelled and logged.

**My job (employed)**

| Tool | What it does | Woven in | Guard rail |
|---|---|---|---|
| Payslip decoder | Photo or PDF of a payslip: each line explained (SA: PAYE, UIF, pension, medical aid; KE: PAYE, NSSF, SHIF, Housing Levy), what's missing, and what a raise really adds after tax | Words (PAYE, UIF); the lesson "Your first payslip"; goal "Start retirement saving" | Tax tables versioned per country and year; she confirms what AI read (Q-37) |
| Offer comparer | Two job offers side by side, benefits included (pension match, medical aid, allowances, leave): the total package and the take-home | Lesson on reading an offer | Illustration only |
| Pay-day plan | Splits net pay into needs, **family support**, goals and spending money | Goals; the Family support planner | No judgement copy |
| Family support planner | Plans "black tax" as a budget line, with scripts for the hard conversations | Stories; circles | Culturally real, never preachy |
| True cost of sending money home | From quotes she enters: the fee plus the exchange-rate margin, the real cost | Words (exchange rate, remittance fee) | Never ranks or recommends providers |
| Debt payoff planner | Snowball or avalanche across store cards and loans: a debt-free date and interest saved | Lesson; a goal | Educational |
| Loan and contract decoder | The real cost (from the Round 7 simulator) plus "explain my agreement": balloon payments, credit life add-ons, fees, from a governed red-flag list | Check an offer; Words | Never says "sign" or "don't sign" (Q-37) |
| Fee eater | How 1 to 3% in yearly fees shrinks an investment over 20 years | The Investing path | Illustration |
| Before you invest | A readiness checklist: cushion, debt, time horizon | Investing path; goals | Not advice; no products |
| Retirement pulse | "At this rate, what might my pension pay?" | Me; goals | Illustration |
| Statement insights | A bank statement PDF becomes spending by category, recurring debit orders and fees found | Goals; the pay-day plan | Consent per upload, processing in SA, deleted after extraction by default (Q-37) |
| Credit report reader | Explains the sections of her free credit report, and how to dispute errors | Words | AWO never computes a credit score |

**My business (entrepreneurs)**

| Tool | What it does | Woven in | Guard rail |
|---|---|---|---|
| Invoice maker | Invoices with her logo, currency, a VAT line only if she's registered, bank or mobile-money details; sent as a PDF by WhatsApp or email; tracks paid and unpaid | Business Home; "Who owes me" | Templates reviewed per country |
| Quote builder | A quote that becomes an invoice in one tap | Invoice maker | |
| Who owes me | Debtors, with polite reminder messages | Business Home | |
| Price it right | Costs, time and margin; markup against margin (a common mistake); break-even units | The pricing lesson; Words | Illustration |
| Is it worth it? | Payback and ROI on a purchase (a fridge, a sewing machine, a delivery bike) | Goals | Illustration |
| Pay yourself | Separates business and home money; plans an owner's salary | Business check | |
| Notebook and profit snapshot | Daily takings (Round 7) become a monthly profit one-pager for her records | Business Home | Her own records, not bank data |
| Stock counter | What to reorder, and what's slow | Business Home | |
| Shop | A mobile storefront: products, prices and a WhatsApp order button, shared as a link, and shown in Community as "shop local" cards | Community feed; Me | No payments through AWO at first; seller terms and moderation (Q-35) |
| Business setup checklist | Registration (CIPC, BRS), tax registration thresholds and a business account, per country | Business check | Every fact verified and dated |
| Funding explorer | Kinds of funding (grants, supplier credit, stokvel, microloans) with honest pros and cons | Learn | Never names or ranks providers (D-003) |

**Everyone**

| Tool | What it does | Guard rail |
|---|---|---|
| Goals studio | Any goal from a template (a car, moving out, starting to invest, school fees, travel home, a home deposit, business stock, a safety net), each its own pool with a timeline | AWO never picks a product for the goal |
| Car cost reality | The total cost of owning a car: deposit, balloon payment, insurance, fuel, depreciation | Illustration |
| Moving-out planner | First-month and monthly costs of moving out | Illustration |
| Check an offer | Round 7's scam check, moved to the Hub under "Stay safe" | As in Round 7 |
| Explain a document | A contract, policy or loan in plain words, with red flags | AI-assisted, logged (Q-37) |
| What I own and owe | A private net-worth snapshot | Private by default |
| DIVA check-in | The way into the governed check. **Not a separate calculator** (Q-38) | D-004 |
| Buzzword decoder | Type "ETF" or "crypto" to get the Vault word, or a request to add it | AI finds; it doesn't invent definitions |

**Hub page structure (proposal):**
- A mode switch: My job or My business, or both.
- "Pick up where you left off": drafts and goals in progress.
- Your goals, as small pools.
- Tools grouped by job to be done: **Understand**, **Plan**, **Grow**, **Run my business** and **Stay safe**.
- Each group shows its best three tools, then "all tools".

## Learning, stories and community

- **Paths beyond savings groups:**
  - money basics, pay and tax, debt and credit, goals;
  - investing: shares, dividends, ETFs, unit trusts, bonds, compound growth, fees;
  - crypto: what it is, volatility, scams, regulation;
  - forex: why most retail traders lose, and the signal-seller scams;
  - property and business;
  - **Companies explained:** how a company makes money, what an IPO is, featured African startups. This is editorial, never an invitation to invest (Q-36).
- **Stories** (Learn tab, and in the feed):
  - "Rise" stories (failure, then rising);
  - "My worst money mistake" (member submissions, edited, with consent);
  - painful lessons;
  - the **AWO Podcast**: lessons from business leaders, with chapters, a transcript, key-lesson cards to save, and low-data audio or offline (Q-39).
- **Community feed:**
  - **Notes:** short posts, with an optional image.
  - **Letters:** long form, like Substack.
  - **Milestones:** structured posts where a stone lands; amounts are hidden by default.
  - **Questions** to her circle.
  - **Shop cards** for member businesses.
  - Reactions beyond likes: Cheer, Same here, Taught me.
  - Two views: "For you" and "Circles".
  - Rules as in Round 7: no advice to buy or switch, no recruiting, first names; AI flags, people decide.
  - The hand stays rare: keep it to her own words, and at most one line on a screen.

## Where the new ideas meet the rules (don't resolve these silently)

| Idea | Tension | Design the safe version, and log |
|---|---|---|
| E-commerce stores | Payments, seller liability, moderation, scope | A catalogue with WhatsApp orders first (Q-35) |
| Featured startups and companies | Promotion, investor matching (excluded, D-003) | Editorial "companies explained", disclosures, no paid placement unless labelled (Q-36) |
| Statement, payslip and document analysis | Very personal data, POPIA, data in SA | Consent per upload, SA processing, deletion after extraction, she confirms what AI read (Q-37) |
| A DIVA score calculator | Scoring is server-side, governed and versioned (D-004) | A DIVA check-in in the Hub, not a free calculator (Q-38) |
| AWO Podcast with business leaders | Real people's names, consent and rights | Use sample people in designs (Q-39) |
| Crypto and forex learning | Scams, regulation (FSCA, CMA, FCA) | Education and scam awareness only; never signals or platforms (Q-40) |
| AI in Hub tools | Ola lives only in Learn and Ask (D-021) | Hub AI is labelled "AI-assisted" without Ola, unless Ian decides otherwise (Q-32) |

## What to deliver in Round 8 (canvas page `r8`, "Round 8")

1. **A brief first** (`docs/00-discovery/14-round-8.md`):
   - research notes: benchmarks such as Cleo, Monzo, Revolut, Wealthsimple, Emma, Copilot, YNAB, Robinhood Learn, Finimize, Blinkist, Spotify's podcast player, Substack, Threads and X, Lemon8, Shopify, Take App, Yoco, Paystack Storefront, Zoho Invoice, Invoice Simple, 22seven, TymeBank, EasyEquities, Duolingo;
   - the ranked Hub shortlist;
   - the new IA.
2. **The new IA and tab bar**, with three Hub icon directions, animated. Show Ian early.
3. **Learn with tabs** (Paths, Words, Stories) and the switch animation, a topic page (for example "Shares and dividends"), and the buzzword decoder in Words.
4. **The Hub:**
   - the landing page in both modes, and a board showing the shared tool skeleton;
   - about eight priority tools: payslip decoder, invoice maker with quote to invoice, price it right, goals studio (car, moving out, investing), debt payoff, fee eater, statement insights, and Shop (the editor and the public page).
5. **Home** with several goals (pools) and Hub shortcuts.
6. **Stories:** a story reader, the podcast player (chapters, transcript, key lessons), and a "my worst money mistake" submission.
7. **The Community feed:** "For you" and "Circles"; the composer (Note, Letter, Milestone, Question); a post with replies; a shop card; reporting a post.
8. **Later:** admin for stories, companies and shops, and a marketing refresh.

## How to work (gotchas that cost time before)

- **Generators:** in `design/round-8/`, importing Round 7's helpers (`lib6`, `screens7`, `kit7.board7`, `auth7.primary`). Run boards through `round7.transform(name, html, native=True)` for the Round 7 type, corners and the `hand` Tweak.
- **Canvas publishing:**
  - Publish with the Artifact tool (`url`, `root`, `file_path` for `project/canvas.json`, and `files`).
  - **Always re-read the live `canvas.json` right before publishing.** Ian's editor saves it, so merge onto the live copy.
  - If a file changed, read it, compare, and never resend an old copy.
  - Upload images as assets and reference their `/_blob/<id>` URLs.
- **Canvas runtime gotchas:**
  - Holes in SVG text don't render.
  - `img` is void (never write `</img>`).
  - Give flex children `flex-shrink: 0`.
  - Before a tall-screen capture, switch off shrinking in `.scr`.
  - The logic class needs `renderVals()`.
- **Python 3.11:**
  - No backslashes inside f-string expressions.
  - Don't reuse the outer quote type in a nested f-string.
  - Precompute strings, and use `json.dumps` for data passed to JavaScript.
- **Commits:** the CHANGELOG hook blocks a command that both edits and commits, so edit in one call and commit in another. Every commit updates CHANGELOG and TASKS.
- **Self-check every board** before publishing (D-026): no `{{holes}}`, no text under 12px, targets of 44px or more, no overflow.
- **Samples:** keep sample content labelled. Log anything that would invent a business rule as an open question.

## The kickoff prompt (paste into a new session)

```text
You're continuing AWO's design exploration, Phase 0 (design only, no product code). Round 7 on the design canvas (https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9, page r7) is the reference board: Geist for all type, Kalam for rare handwritten moments, corners 6/10/14 and a circle, the five area shapes, and motion that means something. Build Round 8 on a new canvas page "r8" (Round 8) in that same language.

Read first: CLAUDE.md; docs/STATUS.md; docs/handover/2026-09-25-round-8-kickoff.md (the brief, the proposed Hub tool catalogue, the guard rails and the deliverables); docs/00-discovery/13-round-7.md; docs/00-discovery/02-product-shape.md; the decision log (especially D-003 to D-006, D-021, D-029, D-033 to D-038); and the open questions Q-32 and Q-34 to Q-40.

Ian's direction for Round 8:
1. Learn and Vault merge: the Vault becomes a tab inside Learn (Paths, Words, Stories), with a clean, animated switch.
2. A new centre tab, the Hub: tools that give real value to employed women and to entrepreneurs, from a payslip decoder and invoices to a storefront. It needs its own icon, hierarchy and page structure. Go beyond generic calculators: research, then trim and rank the catalogue in the handover, and show how each tool is woven into Learn, Words, goals, Community and Me.
3. Goals of every kind (a car, moving out, starting to invest), not only a safety net.
4. Learning with real value: buzzwords, shares and dividends, ETFs, crypto, forex, and companies and startups explained.
5. Real human stories: failure and rising, painful money lessons, and an AWO podcast with lessons from business leaders.
6. Community as a feed to read and post in (notes, long letters, milestones, questions, member shops), unique to AWO.

Work in batches. After each one: render and click through every board (scripts/serve-boards.py and scripts/board-check.mjs); fix what you find; publish to the canvas (re-read the live canvas.json first and merge; lay out with design/round-7/layout7.py adapted for r8); update the docs (CHANGELOG, TASKS, STATUS, and doc 14); commit and push to this session's branch.
1. Brief and research: write docs/00-discovery/14-round-8.md, with benchmarks, the ranked Hub shortlist and the new IA. Draw three Hub icon directions, animated, and show them to Ian before going further.
2. The IA and tab bar; Learn with tabs and the switch animation; a topic page; the buzzword decoder.
3. The Hub landing in both modes; the tool skeleton; about eight priority tools; Home with several goals.
4. Stories and the podcast player; the Community feed, composer, post and shop card.

Keep every product rule in CLAUDE.md:
- Education only: never recommend products, providers or trades.
- DIVA stays server-side, governed and versioned, so there is no free DIVA calculator.
- AI is labelled and logged. Ola appears only in Learn and Ask.
- Samples are visibly labelled. Data stays in South Africa.
- WCAG 2.2 AA, with touch targets of 44px or more. Motion always respects reduce-motion.
- No AI tells (rule D13). Africa appears in substance, never as decoration. UK spelling.

Where an idea collides with a rule (stores, featured companies, statement analysis, a DIVA calculator, the podcast, crypto and forex), design the safe version, label it, and log or update the open question. Don't decide it silently. Ask Ian when it's his call.
```
