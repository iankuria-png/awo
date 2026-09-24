# 03 · Design direction: global craft, local truth

> **Status:** Draft v0. The rules below become the core of the Design Standard once we agree on them.
> **Round 2 update:** C is retired and replaced by D · Human. Brand, icon and motion work, plus rule D13 (avoid AI-made tells), are in [07-brand-and-motion](07-brand-and-motion.md).
> **Explorations canvas:** [AWO Direction Explorations](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9) (private to the owner until shared).

## The problem we're solving

When "designing for Africa", AI tools and many agencies reach for decoration: kente and ankara patterns, map-of-Africa logos, sunset-and-savannah palettes, earthy browns and oranges, flag colours, "tribal" display fonts, baobabs and drums.

This is wrong for AWO for three reasons:

1. **It is decoration standing in for understanding.** It signals "about Africa" without being *for* anyone in particular.
2. **It reads as charity or tourism, not premium product.** Our members use Discovery, TymeBank, Apple Pay, Monzo and Revolut. They deserve the same craft.
3. **It flattens 54 countries and a global diaspora into one aesthetic.**

## The principle

> **Global craft, local truth.** AWO should stand next to the best products in the world on craft alone. Africa shows up in the **substance**: her names, her currency, her savings group, her family obligations, her irregular income, her remittances. It never shows up as **decoration**.

## Rules (checkable)

| # | Rule | Check |
|---|---|---|
| D1 | **Benchmark globally.** | Would this screen hold up next to Monzo, Headspace or Linear? |
| D2 | **No stereotype motifs.** No ethnic textile patterns, continent outlines, safari or sunset palettes, "tribal" or hand-drawn "African" fonts, baobabs or drums as decoration. | Remove the motif. Does the design lose meaning? If not, it was decoration. |
| D3 | **Restrained colour.** One confident brand hue, calm neutrals and at most two accents. No flag palettes (red/yellow/green/black) and no default earth tones. | Count the hues. |
| D4 | **Dignified, specific imagery.** Contemporary women (professionals, founders, students, mothers, retirees) in real modern settings, across a range of skin tones, ages, bodies and hair. No poverty imagery. The village market is not the default. No generic "smiling woman with laptop" stock photos. | Would she recognise herself, and feel respected? |
| D5 | **Local truth in content.** Names, examples and currencies rotate across regions (Naledi, Wanjiru, Adaeze, Chipo, Amara…). Stokvels, chamas and susus appear as real financial instruments, not local colour. | Is the example true to a real life? |
| D6 | **Locale-aware formatting.** Currency, dates and numbers are formatted by locale, e.g. `R 12 500,00` for en-ZA and `£1,250.00` for en-GB. | No hand-formatted numbers. |
| D7 | **Plain words first, numbers second.** Every number comes with a sentence that explains it. | Could someone who hates numbers still understand the screen? |
| D8 | **Never a credit-score aesthetic.** No red-to-green "credit meter" and no "approved / declined" language for DIVA. Readiness is a stage in a journey. | Could this be mistaken for a credit check? |
| D9 | **Provenance is visible.** Governed text is marked "Reviewed by AWO". AI output is marked "AI-assisted". Sample data is marked "Sample". | Can she tell who said this? |
| D10 | **Accessible by default.** WCAG 2.2 AA, body text 16px or larger, touch targets 44px or larger, never colour alone, readable with the system font size increased. | Automated plus manual audit. |
| D11 | **Performance is design.** Budget for mid-range Android on expensive, patchy data. Subset fonts, compress images, design offline states. | Test on a throttled mid-range phone. |
| D12 | **Warm, never patronising.** Plain language without dumbing down. Celebrate progress without infantilising. | Read it aloud to a smart friend who isn't in finance. |
| D13 | **No AI-made tells.** No default cream grounds, all-caps eyebrows, "A · B · C" meta strings or fake 01/02/03 numbering. Spend boldness in one place per screen. | Would a design lead mistake this for a template? |
| D14 | **Motion with meaning.** Motion answers a touch, shows progress or marks a win (M1–M6). Nothing important depends on it. | Turn on reduce motion. Does the screen still work? |

## What we take from your references

| Reference | Take | Leave |
|---|---|---|
| **Finora (green, sky)** | Restraint, with one dominant hue on warm off-white. The **narrator card**: a sentence that tells you what's going on ("You're 12% under budget…"), which maps to our governed interpretation. Big, confident numerals. Pill badges. | "Spent today" and balances, since we don't have live financial data. |
| **Finora (screens)** | Modular card grid. Health-score ring. **What-if simulator**, which maps to educational calculators. Goals with progress. | Transaction timeline (for now). |
| **AI assistant (dark)** | Chat-first entry. Suggestion chips. Voice. A "presence" for the assistant. | "17 AI agents running" hype, glossy 3D orbs and a personal "your score" gauge without explanation. |
| **Pock-style wallet (violet)** | Soft, friendly surfaces. Generous rounding. Clear sectioning ("Upcoming", "Quick menu"). | Heavy gradients. Transaction-centric home. |

> **The Behance link is blocked from my environment.** If Pock matters beyond the violet wallet screens you attached, please drop a few screenshots and tell me what specifically you like about it.

## Three directions on the canvas (Round 1)

The same member (Naledi), the same sample numbers and the same two screens (**Home** and **DIVA profile**), so you compare the feel, not the content.

| | A · Oasis | B · Night Oasis | C · Editorial Violet |
|---|---|---|---|
| **Axis** | Calm and guided | Conversation-first | Learning-first |
| **From** | Finora | AI assistant | Pock + editorial |
| **Palette** | Evergreen, pistachio, paper | Night, mint, iris | Violet, lilac, paper |
| **Type** | Geist | Sora + Hanken Grotesk | Instrument Serif + Sans |
| **Home is…** | A dashboard of where you are in the loop | An "Ask AWO" conversation | A daily edition: one step, one word, one question |
| **Strength** | Most credible and trustworthy. Closest to a premium financial product. | Most distinctive. AI is the hero. Great for low-literacy users via voice. | Warmest and most human. Education feels inviting. Strong for content and SEO. |
| **Risk** | Could feel like "yet another green fintech". | Dark-first is harder on cheap screens in sunlight. AI-first raises governance stakes and cost. | Serif display needs care at small sizes. Violet is common in fintech (Kuda, Nubank). |

**Round 1 outcome (D-019):** A was liked, B's Ask was strong but needs micro-interactions (now the Learn and Ask area), and C was rejected as text-heavy. See [07-brand-and-motion](07-brand-and-motion.md) for Round 2.

## Brand motif idea: ripples

"Oasis" gives us a meaningful, non-stereotyped metaphor: **water, calm, shade, abundance in a dry place.** A ripple spreading from a single point expresses the product's core idea: *one step, spreading outward*. It works as:

- a card texture,
- the AI "thinking" animation,
- a progress metaphor (rings filling), and
- a report cover pattern.

It is ownable and universal, and it says something true about the product.
