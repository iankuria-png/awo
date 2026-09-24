# Status

**Phase:** 0 · Discovery
**Last updated:** 2026-09-24 (session 1, second pass)

## Where we are

Round 2 of the design exploration is on the canvas, and Ian's first answers are recorded as decisions D-014 to D-023. Plugins are installed at project scope. Still no product code, by design.

## Done so far

- **Round 1** ([canvas](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9), page Round 1): three directions, each with a system sheet, Home and DIVA profile. Feedback: A liked, B's Ask strong (needs motion), C rejected.
- **Round 2** (page Round 2):
  - Brand foundations: three wordmark directions with motion ideas, a 16-icon hand-drawn set, and a live motion-principles board.
  - **A · Oasis v2:** welcome, a tappable starter-check question, a new Home (30-day loop tracker, money-feeling check, floating glass nav).
  - **B · Night Oasis as Learn and Ask:** Ola the mascot in five animated states, an Ask conversation with voice and typing states, and a Learn path.
  - **D · Human:** welcome with illustrated people, a tappable "what brings you here" picker, and a Home with member wins, a buddy card and a community question.
- **Docs:** discovery 01–07, a decision log (D-001 to D-023), an open-questions register, a glossary and `CLAUDE.md`.
- **Tooling:** 9 plugins enabled in `.claude/settings.json` (design, figma, engineering, security-guidance, modern-web-guidance, frontend-design, playwright, context7, skill-creator). Video frames were reviewed using a pip-installed ffmpeg.

## Waiting on (Ian)

- **Q-02:** Round 2 reactions (comment on the canvas or reply in chat)
- **Q-25:** wordmark pick; AWO vs awo
- **Q-26:** keep Ola? Name?
- **Q-04:** tier names direction
- **Q-27:** illustrator vs photography for people
- **Q-05, Q-07:** DIVA short labels; existing content and who approves it
- **Connect the Figma connector** at claude.ai/customize/connectors, then start a new session

## Next (once answers are in)

1. Converge on one direction (likely A as the base, B for Learn and Ask, D's warmth for Community). Then write **Design Standard v1**: tokens, type, colour, icon rules, motion tokens, components, states, content style.
2. **Brand identity v1:** refine the chosen wordmark, app icon, icon set and Ola; build it as a Figma library once connected.
3. **PRD v1** + **feature map** + **IA** (member, public, admin).
4. **Wireframes**, then a clickable prototype of the priority journey. Plan 5–8 member test sessions.
5. **Tech stack ADR** now that the builder is known (D-015), plus architecture and domain docs.
6. **Implementation plan**; project skills (`awo-copy-check`, `awo-design-review`, `awo-decision`, `awo-handoff`).
