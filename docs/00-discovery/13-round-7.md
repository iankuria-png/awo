# 13 · Round 7: Geist, a hand, and tighter corners

> **Status:** Published on canvas page `r7` (Round 7), 25 Sep 2026. Every board was rendered and clicked through locally before publishing (D-026). Generator: [`design/round-7/`](../../design/round-7/README.md).
> **Ian's brief (D-032):** "Experiment with this typeface (Round 1's Oasis board, Geist), only a few handwritten fonts for those special moments, and a more restricted border radius."
> **Carried in from Round 6 (D-031):** app icon A (stepping stones); Home stays as it is.

## How it was built

Round 7 is the Round 6 screens with three changes applied as a transform. The content, flows and interactions are identical, so the two pages compare fairly.

| Change | Round 6 | Round 7 |
|---|---|---|
| Display type | Bricolage Grotesque 800, condensed to 82% | **Geist 600**, tracking −0.045em, at 86% of the old sizes. Geist already carried the body text |
| Handwriting | none | **Kalam** by default. Nanum Pen Script and Delicious Handrawn are a Tweak on every board |
| Corners | seven radii (16 to 44) plus pills | **6, 10, 14 and a circle**. Bars and tracks get 2px ends |

## The special moments (the only handwriting in the app)

| Screen | Moment | Whose voice |
|---|---|---|
| Welcome | "start here", with an arrow to the first stepping stone | AWO |
| Starter check | "Here's where you start." above the first stage | AWO, at a milestone |
| Home | Each win's story text | The member's own words |
| Home | "Done for this week. Nicely done!" when the step is finished | AWO, at a milestone |
| Learn | "You showed up three evenings this week." | AWO |
| Community | Her answer to the week's question, once shared | Her own words |

**These stay typeset on purpose:**
- **Me:** results, scores and stages.
- **Ask:** anything Ola or AI writes. Handwriting would pass machine text off as a person's.
- **Vault:** definitions.

**The rules:**
- Handwriting is only for someone's own words or AWO's short note at a real milestone.
- Never for numbers, buttons or instructions.
- Never under 20px.
- At most one line on a screen.
- Always real text, so it can be read aloud and translated.
- `font-size-adjust` keeps the three candidate faces at the same apparent size, so switching faces doesn't reflow layouts.

## The corners

| Radius | Used for |
|---|---|
| 6 | Chips, tags, small controls, the tail corner of a speech bubble |
| 10 | Buttons (no more pills), inputs, list rows, tab pills |
| 14 | Cards, bento tiles, hero blocks, sheets |
| Circle | Faces, dots, story rings and the five shapes. The pool stays a capsule |

## Choices for Ian to check

- **Which hand** (Q-33)?
  - **Kalam:** the most legible at 20 to 30px; warm, grown-up.
  - **Nanum Pen Script:** most like a real note, but loose.
  - **Delicious Handrawn:** a bold marker, better for ads than the app.
- **Geist in marketing:** the store screenshots and ads are still Round 6 (Bricolage). Moving them is a regenerate once the type is settled.
- **Buttons are no longer pills.** With 10px corners they read more "tool", less "toy". Round 1's Oasis board used pills, so that's worth a look.
- **Candidates rejected:** Caveat (seen everywhere) and Playpen Sans (reads as a font, not a hand). The Fonts connector only suggests commercial faces, and the canvas loads Google Fonts only.

## Self-check notes

All ten boards rendered without broken bindings, text under 12px or touch targets under 44px. The transform keeps circles and rings round: an element stays a circle when it is square or sized to fill its parent. One label wrapped on the type board and was shortened.
