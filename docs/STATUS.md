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

## Environment (blocking Round 3 inspiration)

The cloud environment's network policy blocks design sites (Behance, Dribbble, Pinterest, Mobbin, Awwwards, Medium, Unsplash, Pexels, LottieFiles, Rive, Google Play and the App Store) and Figma's MCP server (`mcp.figma.com`). Ian is widening **Network access** in the environment settings. In the next session, first check access with `curl -s -o /dev/null -w '%{http_code}' https://dribbble.com`, then continue with Round 3.

## Round 3 brief (from Ian, D-024): start here next session

Ian will answer Q-02/04/05/25/26/27 later. Don't block on them.

1. **Combine A + D** into one direction (new letter **E**), with many more screen variants and non-generic layouts: bento home, timeline home, story-led home, DIVA result reveal, progress over time with graphs, an interactive check-in, community, buddy, and settings with switches.
2. **Fix the weakest parts:** Ola (redesign; Round 1 B's glowing orb look was better), colours (return to Round 1 Night Oasis for the dark AI and Learn surfaces), and **Learn interactivity** (a real tappable lesson flow: path → story cards → quiz → celebration; flip cards).
3. **Design elements for everything:** widgets (including home-screen and lock-screen widgets), stats bars, micro-animations, switches, sliders, graphs, notifications, skeleton loaders, bento grids, layout variations.
4. **Mock-ups and marketing:** device mock-up hero shots, campaign ads (square post and story), Play Store feature graphic (1024×500), store screenshots with captions, and a store listing preview (simplified, not Google's UI).
5. **Inspiration first:** once the network is open, gather real references (Dribbble, Behance, Mobbin, Pinterest and similar) into a taste board with what to take from each, before designing.
6. Charts: follow the `dataviz` skill (run its palette validator).

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
