# 01 · Understanding AWO

> **Status:** Draft v0 for discussion (24 Sep 2026). Nothing here is decided unless it appears in [`../decisions/log.md`](../decisions/log.md).

## AWO in one paragraph

AWO (African Wealth Oasis) is a financial **education, intelligence and community** platform for African women in Southern Africa and the diaspora. It helps a member answer three questions, in order:

1. **Where am I?** A DIVA profile across four dimensions.
2. **What does this mean?** A clear, governed explanation in plain language.
3. **What can I learn or do next?** One practical educational step, then a 30-day check-in to see what changed.

Everything else (Academy, Vault, Community, Buddy, Opportunities, AI) exists to make that loop richer, stickier and more trustworthy.

## The priority journey is a loop, not a funnel

```
Discover ─▶ Join ─▶ Starter check ─▶ Profile ─▶ Meaning ─▶ One step
                                        ▲                      │
                                        └── 30-day check-in ◀──┘
                                                 │
                                        Progress + report
```

The check-in feeds back into the profile. Each pass adds evidence, updates the result as a new version (never overwriting the old one) and suggests the next step. This loop is the product, and the Home screen should be built around where the member is in it.

## Who she is (working assumptions, to validate)

| Context | What she might be carrying | Design implication |
|---|---|---|
| **Individual** | Salaried or irregular income. Family obligations ("black tax"), savings groups (stokvels, chamas, susus) and remittances. | Examples must reflect real money lives, not a US-centric "budget + 401k" model. |
| **Entrepreneur** | Informal or early-stage business, with personal and business money often mixed. | Business terms need plain-language bridges. The venture assessment stays separate from the personal one. |
| **Diaspora** | Earns in GBP/USD/EUR and supports or invests "back home". | Multi-currency awareness. She compares AWO to Monzo and Revolut, so our craft bar is global. |

Across all three we design for a range of financial literacy, digital confidence and connectivity. Android holds about 85% of mobile OS share across Africa, and data is expensive, so we design for **mid-range Android on patchy mobile data first**. The experience then scales up to iPhone and desktop.

## The boundary: education, not advice

AWO does not give personalised investment advice, credit decisions, investment execution, capital pooling or investor matching.

In South Africa the FAIS Act defines *advice* as a recommendation, guidance or proposal about buying, investing in, varying, replacing or terminating a **financial product**. Factual information, product descriptions and objective information are not advice.

AWO lives on the *education and factual information* side of that line. This shapes:

- **Copy:** "learn", "understand" and "explore" instead of "you should", "buy" or "switch".
- **Results:** categories describe *educational readiness*. They must never read as creditworthiness, suitability or eligibility.
- **AI:** it may explain and reword approved content. It may not recommend products, invent scores or improvise interpretations.
- **Community:** members will naturally give each other "advice" and share schemes. Moderation and design must handle that from day one.

> **Compliance is handled by AWO (D-016).** This is a design reading of the boundary, used to shape copy and features.

## Where I think the real value is

1. **A mirror, not a verdict.** A calm, honest picture of where she stands, with *evidence confidence* shown separately so we never overclaim.
2. **Momentum.** One step at a time, with a 30-day rhythm. Small wins compound.
3. **Belonging.** Community and an accountability buddy turn a private worry into a shared practice.
4. **Trust.** Governed interpretations, visible provenance ("Reviewed by AWO" vs "AI-assisted") and a clear scope boundary.

## Tensions I noticed (let's talk about these)

1. **Bronze / Silver / Gold / Platinum reads like credit-card and loyalty tiers.** Those are exactly the connotations the brief says to avoid (creditworthiness and status). Options: keep the names but lead with stage language ("Stage 2 of 4"), or rename them. → Q-04
2. **The inspiration is transaction-driven; AWO isn't (yet).** All four references show balances, "spent today" and bills. AWO has no live bank data, so we must not fake a banking dashboard. Our "data" is her profile, her steps, her learning and her check-ins. The references are useful for *craft* (restraint, narrator card, big numerals, simulators), not for *content*.
3. **Eight self-reported answers are a snapshot, not a diagnosis.** *Evidence confidence* is our honesty device: it starts "Early" and grows as check-ins, quizzes and (later) behavioural data add evidence. This also opens the door to a lighter, more engaging starter check (see [02-product-shape](02-product-shape.md)).
4. **Long dimension names.** "Risk Intelligence & Behavioural Resilience" doesn't fit a phone row, a WhatsApp message or a USSD screen. We need approved short labels. → Q-05
5. **AI appeal versus governance.** The dark "AI assistant" reference is compelling, but AI must never produce the score or unapproved advice. We need a clear pattern for what AI *can* do. → [02-product-shape § AI](02-product-shape.md#ai-opportunity-map)
6. **Data residency versus AI providers.** Most strong AI models are processed outside South Africa. POPIA section 72 allows cross-border transfer on specific grounds (for example consent or adequate protection agreements). This needs a deliberate choice. → Q-09
