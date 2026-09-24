# 02 · Product shape: IA, starter check, AI and ideas

> **Status:** Draft v0 for discussion. These are proposals to react to, not decisions.

## Information architecture (first sketch)

### Member app: five destinations

| Tab | Purpose | Holds |
|---|---|---|
| **Today** | Where am I in the loop? | This week's step · check-in countdown · profile summary · community prompt · nudges |
| **Learn** | AWO Academy | Paths · modules · lessons · milestone quizzes · weekly actions · simulators |
| **Vault** | Knowledge library | Terms · collections · search · saved · word of the week |
| **Community** | Belonging | Feed · weekly prompt · questions · wins · accountability buddy |
| **Me** | Her record and controls | DIVA profile and history · reports · business profile and venture assessment · settings · consent and data |

**Ask AWO** (the AI surface) is a global entry point rather than a tab: a button on Today and contextual buttons on results, lessons and terms. Direction B on the canvas explores making it *the* home instead. **Opportunities** arrives later, probably under Learn.

### Public website

Home · How it works (DIVA explained) · For individuals · For entrepreneurs · Diaspora · Academy preview · **Public Vault** · Community · About · Contact · Privacy · Terms.

> **Idea: the public Vault as the search-engine engine.** Every glossary term becomes a fast, well-structured public page ("What is a tax-free savings account?"). That is genuinely useful, ranks well, and leads naturally into "see where you stand".

### Admin (later phase, small non-technical team)

Members · Invitations and beta · Assessments (definitions, versions, publish) · Scoring methods · Interpretation library (versions and approvals) · Next steps and check-in schedules · Academy and Vault content · Moderation · Opportunities · Translations · Communications · Analytics · Audit log · Legal documents and settings.

## Rethinking the starter check

The brief says questionnaires are "boring and overused". Agreed. But we still need structured, scoreable inputs. The trick is to change the *experience* without changing the *data contract*.

**Principles**

- **Behaviour over self-rating.** "It's payday. What happens first?" gets a more honest answer than "Rate your discipline from 1 to 5".
- **One thing per screen.** Show progress and time left ("about 3 minutes").
- **Every question earns its place.** It maps to a dimension, or it isn't asked.
- **Always allow "prefer not to say".** Missing data lowers evidence confidence; it does not break the result.
- **No invented social proof.** Never say "6 in 10 women say…" unless we have the data.

**Formats to prototype**

| Format | Example | Good for |
|---|---|---|
| Scenario cards | "An unexpected R3 000 bill arrives. What do you do?" (4 illustrated choices) | Risk and resilience, behaviour |
| This-or-that | "Save first, spend the rest" vs "Spend first, save what's left" | Habits, mindset |
| Anchored slider | "How many months could you cover if income stopped?" (0, <1, 1–3, 3–6, 6+) | Financial health |
| Card sort | Rank four goals by priority | Goal clarity |
| Reflection | "What would feeling in control of money look like for you?" (optional, free text, not scored) | Personalising the next step and her own words |

**Progressive profiling.** The starter check (about 8 items) gives an *early* profile. Micro-questions woven into lessons and check-ins add evidence over time, so confidence grows and the profile sharpens. No one ever sits a 40-question exam.

**One question graph, many renderers.** Each question is defined once, with short labels, 5 or fewer options and plain text. It can then render as app cards, a scripted chat, a WhatsApp message and later a USSD menu (screens hold about 160–182 characters). Designing for USSD constraints now makes every channel better.

## AI opportunity map

**The rule:** AI can **explain, find, reword, capture and flag**. It never **scores, classifies, interprets beyond the approved library, or recommends financial products**. Every AI surface is labelled, logged and has a non-AI fallback.

| # | Use case | Why it matters here | Guardrail pattern | Risk |
|---|---|---|---|---|
| 1 | **Explain my result more simply** | Literacy varies widely | Rewords *only* the governed interpretation at a chosen reading level. Labelled "AI-assisted · based on AWO-reviewed text". Original always one tap away. | Low–Med |
| 2 | **Ask the Vault** | Instant, plain-language answers | Answers only from Vault and Academy content, with citations. Politely declines personal advice and redirects to learning. | Med |
| 3 | **Check an offer** | Investment scams and pyramid schemes spread fast on WhatsApp | Compares a pasted offer against a *governed red-flag checklist* (guaranteed returns, urgency, recruitment rewards, unregistered provider). Never says "this is safe". Points to the regulator's public register. | Med–High |
| 4 | **Conversational check-in** | Talking is easier than forms | AI proposes answers to the structured check-in questions from her own words. She confirms each one, then the deterministic scorer runs. Provenance: *self-reported, AI-captured, member-confirmed*. | Med |
| 5 | **Voice in and out** | Literacy, accessibility, busy lives | Speech-to-text for input and read-aloud for lessons and results. | Low |
| 6 | **Content co-pilot (admin)** | A tiny team must produce a lot of content | Drafts translations, glossary entries and lesson variants for **human review**. Never auto-publishes. | Low |
| 7 | **Moderation assist** | Scams, unlicensed "advice", oversharing | Flags content for a human decision, with reasons. | Low–Med |

**Never AI:** computing or adjusting DIVA scores, choosing categories, writing interpretations outside the library, recommending products or providers, or stating eligibility.

## Features worth adding (suggestions)

### Vault

- Three depths per term: *New to this* / *I know the basics* / *Go deeper*.
- **Country variants:** the same concept, local reality (for example a tax-free savings account in South Africa vs an ISA in the UK).
- **Read aloud** and pronunciation.
- **See also / often confused with** links between terms.
- **Red-flag entries:** Ponzi scheme, pyramid scheme, "guaranteed returns", advance-fee fraud.
- **Collections:** "Your first payslip", "Starting a business: 20 words", "Sending money home".
- Saved terms **available offline**.
- **Terms for your focus area:** Vault suggestions linked to her lowest DIVA dimension.

### Across the product

- **What-if simulators:** deterministic, educational and labelled illustrative. Emergency-fund runway, savings goal, debt payoff and the real cost of a loan, in her currency. The "what if" reference screen is a great pattern for this.
- **Progress against herself:** "since your last check-in" deltas, never rankings against other women.
- **Printable one-page report**, for members who prefer paper or share with a mentor.
- **Stokvel / savings-group literacy module.** A real, widely used financial instrument that global apps ignore.
