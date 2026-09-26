# 05 · Open questions register

> **How this works:** every product, design or technical question that we must *not* silently invent an answer to lives here. When a question is answered, move the answer to [`../decisions/log.md`](../decisions/log.md) and mark the question **Answered → D-0xx**.
>
> **Priority:** **Now** = shapes the next set of docs and designs · **Before build** = needed before the related code · **Later** = parked until its phase.

## Now

| ID | Question | Why it matters | My recommendation | Status |
|---|---|---|---|---|
| Q-02 | **Round 2 reactions.** A v2, B as Learn and Ask with Ola, D · Human, the wordmarks, the icons and the motion board. | Sets the design-standard foundation. | A as the base and B for Learn and Ask. D's warmth for Community and Buddy. | Open (Round 1 → D-019) |
| Q-04 | **Tier names.** Keep Bronze/Silver/Gold/Platinum, or use growth-stage names? | Affects every result, report and message. | Explore stage names tied to the oasis story; keep "Stage 2 of 4" as the lead either way. | Open (exploring, D-022) |
| Q-05 | **What does DIVA stand for** (if it's an acronym)? Can we agree **short labels** for the four dimensions? | Mobile rows, reports, WhatsApp and USSD all need short labels. | Approve short and long forms as a pair. | Open |
| Q-07 | **What content exists** from the previous AWO (question bank, interpretations, glossary, lessons)? Who **approves** interpretations and lessons? | Governed content needs an owner, and existing material saves months. | Name one content owner and one reviewer. | Open |
| Q-09 | **AI providers and data location.** Compliance is AWO's (D-016). What does AWO's compliance position allow: a non-SA AI provider with consent and minimisation, in-region only, or AI on non-personal content only at first? | Determines which AI features are possible and when. | Start with non-personal content (Vault Q&A, rewording approved text), then widen. | Open |
| Q-10 | **Platform priority:** web/PWA first and native later, or native first? | Build order and app-store timelines. | PWA first, native in phase 8. Revisit given motion-first ambitions: native runs Rive and Reanimated best. | Open |
| Q-25 | **Wordmark:** Ripple, Wave or Stepping stones (or a mix)? Uppercase **AWO** or lowercase **awo**? | Everything downstream uses it. | Wave wordmark with the Stones or Ripple app icon. | Open |
| Q-26 | **Mascot:** keep Ola? Name? Only in Learn and Ask? | Character work takes time to commission and animate. | Yes, Learn and Ask only. "Ola" is a working name to test with members. | Open |
| Q-27 | **People imagery:** commission an illustrator, run a photo shoot with real members, or both? | D depends on it, and it matters for dignity (D4). | Photography for product and marketing (Rounds 3 to 5 use nappy.co CC0 photos as stand-ins); commission a member shoot. | Open |
| Q-29 | **Who is AWO to her?** Mentor (quiet companion), Journal (her story) or Circle (women who get it)? See [09 § Directions](09-round-3-review.md#directions-to-explore-three-human-axes). | Sets Home, tone and what the product celebrates. | Mentor as the spine, Circle as the heart, her own words from Journal. Test all three on the first result reveal before converging. | Open. Ian leans Mentor + Circle (D-027). Round 5 settles the design language first (D-028). |
| Q-30 | **Theme logic:** is Learn (and Ask) *always* dark, or does the app follow the phone's dark mode? | Supporting both doubles design and QA work. | Learn and Ask always dark ("night for learning"); the rest follows the system later, if at all. | Open |
| Q-31 | **Store name and copy:** is "AWO: money in plain words" right, and who approves store copy? | Needed before any store listing or ad goes out. | Keep AWO as the lead; test two short descriptions with first members. | Open. Round 8's refreshed store set and ads use sample copy (`design/marketing/round-8/`, [14](14-round-8.md#batch-5-companies-explained-and-the-marketing-refresh)) |
| Q-35 | **Shops inside AWO:** may members sell through AWO? Who handles payments, seller terms and moderation? | Ian wants e-commerce stores in the Hub; payments add licensing and liability. | A catalogue with WhatsApp orders first. No payments through AWO until decided. | Open. Safe version designed: `R8-Shop-Edit` and `R8-Shop-Public` (seller rules, report a shop) |
| Q-36 | **Featured companies and startups:** what are the editorial rules, the disclosures, and is any placement paid? | Featuring can read as promotion; investor matching is out of scope (D-003). | Editorial "companies explained". Never a call to invest. No paid placement unless clearly labelled. | Open. Safe version designed: `R8-Companies` (with six proposed editorial rules), `R8-Company-Brief` (a real listed company from its own dated results, labelled "Sample editorial") and `R8-Startup` (a sample startup). Still to decide: real companies or made-up ones, and whether the rules stand |
| Q-37 | **Reading members' documents** (payslips, statements, contracts): consent, where it's processed, how long it's kept? | Very personal data under POPIA. | Consent per upload, processed in South Africa, originals deleted after extraction by default. AI reads; she confirms. | Open. Safe version designed: `R8-Tool-Payslip`, `R8-Tool-Statement` and the document path on `R8-Tool-Skeleton` |
| Q-38 | **A "DIVA score calculator" in the Hub:** Ian listed one, but DIVA scoring is governed (D-004). | A free calculator would bypass versioning and audit. | The Hub offers the DIVA check-in, not a separate calculator. | Open. `R8-Hub` shows a doorway to Me, not a calculator |
| Q-39 | **The AWO podcast:** who hosts, guests' consent and rights, languages? | Real people's stories need consent; designs need sample people. | Sample people in designs until guests are confirmed. | Open. `R8-Podcast` uses a sample guest and an AI-assisted transcript checked by a person |
| Q-40 | **Crypto and forex learning:** what's the stance, and which regulators do we cite per country? | Scams are common; crypto is regulated in South Africa. | Education and scam awareness only: no signals, platforms or trades. Cite the FSCA, CMA and FCA as relevant. | Open. Built as Words entries (Pips, Crypto, Crypto scam) with a regulator line per country, and "Scam checks" on the paths |
| Q-34 | **Admin approvals:** who may approve a new interpretation, scoring version or lesson, and does it take one person or two? | Results must stay auditable; a small team can't block itself either. | Two people for scoring and interpretations (the author can't approve their own change); one reviewer for lessons and Vault words. Shown as a proposal on the Round 7 admin boards. | Open |
| Q-41 | **Facts behind Hub tools:** who keeps tax tables, statutory deductions (PAYE, UIF; SHIF, NSSF, Housing Levy), VAT thresholds and registration steps current for each country, and how often are they checked? | The payslip decoder and the business setup checklist are only as good as their figures, and these change every year (South Africa's VAT threshold moved to R 2,3 million on 1 April 2026). | One named owner. Figures versioned by country and tax year, each with a source and a "checked on" date that every tool shows. Until then, designs use labelled samples. | Open (Round 8, [14](14-round-8.md)) |
| Q-42 | **Members' stories** (Rise stories, "My worst money mistake"): who may edit them, how are members credited, are contributors paid, and how is a story taken down? | Real lives and real embarrassment; an edit can change what she meant. | An editor may shorten and correct; she approves the final text; first name and city by default, first name only or anonymous if she prefers; amounts optional; taken down on request. No payment at first. | Open (Round 8, `R8-Mistake`) |
| Q-43 | **Reaction counts in the Community feed:** show public totals, or let only the author see hers? | Counts invite comparison and chasing, which fights the tone of the Circle (Q-29). | Hide public totals and follower counts; three reactions (Cheer, Same here, Taught me); the author sees her own numbers. | Open (Round 8, `R8-Feed-Parts`) |
| Q-44 | **The DIVA score's name:** the marketing says "DIVA score" (Ian's words), while the app shows "Your DIVA profile" with "Readiness 63". One name for the number, everywhere? | Two names for one number confuse members, and the store screenshots show the app. | "DIVA score" for the 0 to 100 number in the app and the marketing; "DIVA profile" for the whole picture (score, stage, areas, evidence). Always paired with "not a credit score". | Open (the marketing uses "DIVA score"; the app still says "Readiness") |
| Q-32 | **Ola beyond Learn and Ask:** may Ola appear in the Learn widget, store screenshots and ads? | D-021 limits the mascot to one area; marketing and widgets are edge cases. | Yes when the surface is about Learning; never next to results or money amounts. | Open |

## Answered

| ID | Question | Answer |
|---|---|---|
| Q-01 | Existing brand assets? | None to keep. Brand designed from scratch. → D-014 |
| Q-03 | First members? | Women and business people wanting to understand their finances. → D-018 |
| Q-06 | Who builds and operates? | Ian Kuria, product developer and software engineer, with Claude. → D-015 |
| Q-33 | Handwriting face, and marketing type? | Kalam in the app; marketing moves to Geist. → D-033 |
| Q-18 | Account identity: email, or phone too? | Phone number first, plus Google and Apple. → D-035 |
| Q-08 | Compliance adviser? | Covered by AWO; Claude doesn't spend time on it. → D-016 |
| Q-11 | Figma? | Yes. → D-017 |

## Before build

| ID | Question | Status |
|---|---|---|
| Q-12 | Starter check: is "**eight questions**" a hard promise, or is "**about 3 minutes**" the real promise? Open to scenario-based formats and progressive profiling? | Open |
| Q-13 | Approved starter questions and **scoring mappings and thresholds** (configurable later in admin). Until then we use clearly labelled sample rules. | Open |
| Q-14 | Approved **interpretation and next-step library**, and its review workflow. | Open |
| Q-15 | **Evidence-confidence rules.** What counts as behavioural or derived evidence, and how does confidence level up? | Open |
| Q-16 | **Target dates:** beta cohort, launch event, partner milestones? | Open |
| Q-17 | **Hosting provider** in South Africa, domain names, email-sending provider. | Open |
| Q-19 | Community **naming and tone**. Open community or cohort-based at launch? | Open |
| Q-28 | **Motion craft:** freelance motion designer and illustrator, or Claude-built Rive and Lottie assets reviewed by Ian? | Open |

## Later

| ID | Question | Status |
|---|---|---|
| Q-20 | Opportunity Discovery: categories, content sources, eligibility information and discovery rules. | Open |
| Q-21 | WhatsApp and USSD: supported journeys, providers, identity and consent handling. | Open |
| Q-22 | Languages after English, and translation approval workflow. | Open |
| Q-23 | Financial-data integrations: which countries and providers, what consent model. | Open |
| Q-24 | Any future paid tier (the product is free for now). | Open |
