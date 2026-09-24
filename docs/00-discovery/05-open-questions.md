# 05 · Open questions register

> **How this works:** every product, design or technical question that we must *not* silently invent an answer to lives here. When a question is answered, move the answer to [`../decisions/log.md`](../decisions/log.md) and mark the question **Answered → D-0xx**.
>
> **Priority:** **Now** = shapes the next set of docs and designs · **Before build** = needed before the related code · **Later** = parked until its phase.

## Now

| ID | Question | Why it matters | My recommendation | Status |
|---|---|---|---|---|
| Q-01 | Does AWO have an existing **logo, wordmark, colours, fonts or brand guidelines** we must keep? Or is brand identity part of this work? | Decides whether the canvas directions are *brand* or *product-UI* explorations. | If nothing is locked, treat brand identity as in scope, done alongside the design standard. | Open |
| Q-02 | **Reactions to directions A / B / C** on the canvas. What do you love, hate or want to mix? And what specifically drew you to Pock? (Behance is blocked for me, so screenshots help.) | Sets the design-standard foundation. | A as foundation, C's editorial voice for learning, B's Ask AWO as an entry point. | Open |
| Q-03 | **Who are the first 100–500 members?** Where are they (SA city, other countries, diaspora)? Individuals or entrepreneurs? Age range? How will they hear about AWO? | Personas, copy tone, device and connectivity assumptions, launch order of features. | Pick one primary persona for v1 and design the others as secondary. | Open |
| Q-04 | **Keep Bronze / Silver / Gold / Platinum?** These read like credit-card and loyalty tiers, the connotation the brief warns against. | Affects every result screen, report and communication. | Keep the names only if the brand depends on them, and lead with stage language ("Stage 2 of 4"). Otherwise explore growth-stage names. | Open |
| Q-05 | **What does DIVA stand for** (if it's an acronym)? Can we agree **short labels** for the four dimensions (e.g. *Financial Health · Risk & Resilience · Capital Positioning · Goal Clarity*)? | Mobile rows, reports, WhatsApp and USSD all need short labels. | Approve short and long forms as a pair. | Open |
| Q-06 | **Who builds and operates this with me?** In-house developers? Which languages and tools do they know? Who runs the VPS day to day? | The single biggest input to the stack decision. | — | Open |
| Q-07 | **What content exists** from the previous AWO (question bank, interpretations, glossary, lessons)? Can I see it (content only, not code)? **Who approves** interpretations and lessons? | Governed content needs an owner and a workflow, and existing material saves months. | Name one content owner and one reviewer. | Open |
| Q-08 | Do you have a **compliance or legal adviser** for FAIS (advice boundary) and POPIA (privacy)? Is an Information Officer registered? | Copy, AI guardrails, consent flows and data handling depend on their review. | Get a one-hour review of the scope boundary and AI plan early. It's cheap insurance. | Open |
| Q-09 | **AI and data residency.** Most strong AI models process data outside South Africa. Which posture? (a) explicit consent + data minimisation / pseudonymisation; (b) in-region only (limits model choice); (c) AI only on non-personal content (e.g. Vault Q&A) until decided. | Determines which AI features are possible and when. | (c) for the first release, moving to (a) with your adviser's sign-off. | Open |
| Q-10 | **Platform priority:** web/PWA first and native apps later, or native first? | Build order, budget, app-store timelines. | PWA first (reach, speed, one codebase), native in phase 8. | Open |
| Q-11 | **Design tool:** do you work in **Figma**? | If yes, I can build the design system and wireframes directly in a Figma file via the Figma plugin. If not, we stay on Claude design canvases plus code. | — | Open |

## Before build

| ID | Question | Status |
|---|---|---|
| Q-12 | Starter check: is "**eight questions**" a hard product promise, or is "**about 3 minutes**" the real promise? Open to scenario-based formats and progressive profiling? | Open |
| Q-13 | Approved starter questions and **scoring mappings and thresholds** (configurable later in admin). Until then we use clearly labelled sample rules. | Open |
| Q-14 | Approved **interpretation and next-step library**, and its review workflow. | Open |
| Q-15 | **Evidence-confidence rules.** What counts as behavioural or derived evidence, and how does confidence level up? | Open |
| Q-16 | **Target dates:** beta cohort date, launch event, fundraising or partner milestones? | Open |
| Q-17 | **Hosting provider** in South Africa, domain names, email-sending provider. | Open |
| Q-18 | **Account identity:** email only, or phone number too (important later for WhatsApp and USSD)? | Open |
| Q-19 | Community **naming and tone** (e.g. "Community" vs "Circle"). Is the community open or cohort-based at launch? | Open |

## Later

| ID | Question | Status |
|---|---|---|
| Q-20 | Opportunity Discovery: categories, content sources, eligibility information and discovery rules. | Open |
| Q-21 | WhatsApp and USSD: supported journeys, providers, identity and consent handling. | Open |
| Q-22 | Languages after English, and translation approval workflow. | Open |
| Q-23 | Financial-data integrations: which countries and providers, what consent model. | Open |
| Q-24 | Any future paid tier (the product is free for now). | Open |
