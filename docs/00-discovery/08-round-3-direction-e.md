# 08 · Round 3: Direction E, Ola v2 and the assets

> **Status:** Draft v0 for discussion (25 Sep 2026). Round 3 brief: D-024 and the [handover](../handover/2026-09-24-round-3.md) §5.
> **Canvas:** [AWO Direction Explorations](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9), page **Round 3**.

## Taste board (what we take)

Twelve real references, picked before designing. The board credits and links each one.

| Reference | Take |
|---|---|
| Wise (Play Store) | Captions set as headlines, one feature per frame. **Watch-out:** lime on dark green is Wise's signature, so blush and photography keep E distinct. |
| Kuda (Play Store) | Real people in real, modern moments, with the product floating over the photo. |
| Cash App (Play Store) | One oversized thing per frame. |
| Monzo (Play Store) | The product in someone's hand, a bold colour field, proof points as pills. |
| Headspace (Play Store) | A plain orb with closed eyes carries a whole brand: the north star for Ola. |
| Duolingo (Play Store) | Lesson feedback in one glance: coloured banner, one big button. |
| Unglue mascots (Manu, Dribbble) | Every mood from the eyes alone. |
| Mental health mascot (The Ash Branding, Dribbble) | One soft shape, capsule eyes, squash and stretch. |
| AI assistant (Budiarti R., Dribbble) | A mint orb glowing on a dark ground: closest to Round 1 Night Oasis. |
| iOS widgets (Mari Chubina, Dribbble) | One big numeral per widget, three sizes. |
| Nestable (sleek.design, Dribbble) | Goals as vessels that fill, which becomes AWO's **pools**. |
| AuraFit (Rasel Mahmud Shakil, Dribbble) | Bento with one hero tile and quiet satellites. |

## Direction E tokens

**E = A's calm + D's people. Day for doing, night for learning.**

| Role | Day (Home, DIVA, Community, Buddy, Me) | Night (Learn and Ask only) |
|---|---|---|
| Ground | Mist #EEF3F0 | Night #0B0F0E |
| Surface | White #FFFFFF | Deep #151B19, raised #1C2421, lines #232C29 / #2E3A36 |
| Brand | Evergreen #0F4A36 (deep #0A3326) | Mint #86E3C4 |
| Accents | Lime #D8F36A (wins, progress), Blush #FFC7D6 (people, warmth) | Iris #A99BFF (focus); lime still marks wins |
| Support | Pool #D3E8E4 (water, calm surfaces) | Glow: mint → iris with a blush rim, on Ola and AI moments only |
| Text | Ink #101814, muted #56625C | #F2F1EC, muted #9AA39F |

- **Type:** Bricolage Grotesque 700–800, width 84–90%, tight tracking, for headlines and big numbers. Geist for everything else, with tabular figures for money. One type system for day and night (Round 1 B used Sora; E unifies).
- **Radius follows rank:** 32 hero, 24 card, 16 tile, pill for actions.
- **Motifs:** ripple (progress, loading, the DIVA rings), **pools** (goals fill like water), stepping stones (the path). People in arches and circles, with blush behind them.
- **Motion:** 90 ms tap, 180 ms toggles and chips, 280 ms cards and sheets, 600 ms wins. Ease-out `cubic-bezier(.2,.8,.2,1)`; spring `cubic-bezier(.34,1.56,.64,1)` only for wins. Reduce motion stops every loop.

## Ola v2

- **A glowing orb with only eyes:** a mint-to-iris glass body (Round 1 B's presence orb) with a thin blush rim and a bounce light, a soft highlight and a halo.
- **Capsule eyes carry every emotion:** open, blink, look, wonder (up), listen (wide), proud (^ ^), asleep (closed arcs). No mouth, no limbs.
- **The body squashes and stretches;** the eyes stay put.
- **Six states:** idle (breathes, blinks), looking (glances and leans), listening (wide eyes, rings pulse), thinking (looks up, a dot orbits; never a spinner), celebrating (^ ^, jump, sparkles in lime, blush and iris), resting (closed eyes, dimmed, z).
- **Rules:** Learn and Ask only; never on a DIVA result; celebrates effort, never scores. Built as one Rive file with one state machine. At 24px the highlight drops and the eyes thicken.

## Learn and Ask (Night Oasis, interactive)

- **Learn flow (one board, real state):** the path is **stepping stones across water** (done = mint with a check, current = iris with ripples and a Start callout, locked = raised with a lock). Tapping Start opens **story cards** with progress bars (four cards, each one visual and one idea), then a **quiz** (pick, check, feedback banner; a wrong answer shakes and explains), then a **celebration** (Ola jumps, confetti, effort stats in a bento), then **back to the path**, which updates (lesson done, today's learning dot filled, Ola proud).
- **Vault flip cards:** 3D flip to a plain definition on the term's accent colour, filter chips, save toggle with a count. Sample definitions include stokvel, chama, debit order and an advance-fee scam.
- **Ask Ola:** keeps Round 1 B's liked layout (presence, question, 2×2 suggestions, composer). A suggestion opens a chat: Ola thinks (eyes up, dots), then answers with a Vault source chip, *Reviewed by AWO* and "Reworded by AI from AWO-reviewed text". Ask no longer offers "Explain my DIVA result", to keep Ola away from results.

## Direction E screens (day)

- **Three Home variants:** *bento* (hero step tile, safety-net pool, 30-day ring, word of the week, community tile with a photo arch, a night "keep learning" tile, profile rings), *timeline* (the 30-day loop as a rail with stones: done, now, today, buddy, check-in), *stories* (wins rail with real photos, a full-bleed member story, step and buddy rows).
- **DIVA profile:** four concentric **ripple rings**, one per dimension in weight order, drawn in one hue and labelled directly; tapping a dimension dims the other rings and swaps in its sample interpretation. The overall number counts up once. **Evidence confidence** sits in its own box, outside the score. There is no mascot and no confetti, and the result shows its version ("Version 3, 13 Sep").
- **Progress:** hero number with a plain-words delta, a single-line chart with time-true spacing and a tap tooltip, and small multiples by area (each with its own range, said in words). Effort stats (lessons, actions, check-ins) and a separate evidence track.
- **Charts follow the dataviz skill:** single hue, 2px lines, 1px solid gridlines, one axis, direct labels, emphasis by dimming. The brand colours fail as a categorical palette (validator), so no chart relies on two brand hues for identity.
- **Short dimension labels used (proposed, Q-05):** Health, Resilience, Capital, Goals.

## Components, widgets and marketing

- **Controls board:** buttons (day and night), switches with a check knob, segmented controls, sliders (day and night), chips, provenance labels, inputs, glass navigation. All live.
- **Data and feedback board:** stat tiles (value, delta, sparkline), a **what-if calculator** (monthly amount → 12 months, plain arithmetic with no interest, labelled "not a forecast"), five progress forms (bar, ring, pool, stones, story bars), notifications (toast, banner, scam warning with icon and label, push), skeletons (day and night).
- **Widgets:** a home screen (safety-net pool, 30-day ring, this week's step, a Learn widget with Ola) and a lock screen (inline, circular and rectangular widgets over a real photo). Amounts appear only on widgets the member adds, never on the lock screen by default.
- **Marketing:** six Play Store screenshots, a feature graphic, an app icon candidate, a device hero (a real phone photo with a real AWO screen composited in), three square ads, a story ad and a simplified listing preview with character counts. PNG exports and sources are in [`design/marketing/`](../../design/marketing/README.md). Play specs were checked on 25 Sep 2026.
- **Watch-outs for Ian:** Ola appears outside the app in the Learn widget, store screenshot 2 and the story ad (Q-30). Store name and copy are drafts (Q-29).

## Canvas map (page Round 3)

| Row | Boards |
|---|---|
| Top | Taste board · E foundations · Ola v2 · Learn flow, Vault, Ask (under Ola) |
| E screens | Bento, timeline and story Homes · DIVA · Progress · Check-in · Community · Buddy · Settings · three onboarding screens |
| Components | Controls · Data and feedback · Widgets |
| Marketing | Six store screenshots · listing, feature graphic, icon, device hero · four ads |

Boards marked "press Play" or "tap" in their titles are interactive.

## People imagery (working assumption for Q-27)

Real photography from **[nappy.co](https://nappy.co/license)** (CC0: free for commercial use, credit optional) stands in until AWO photographs real members. Photos show contemporary women (founders, friends, mothers) in real settings, cropped into arches and circles.

## Sources and tools that worked (25 Sep)

| Source | Status |
|---|---|
| Dribbble search (headless Chromium, scraping `li.shot-thumbnail`) | Works |
| Google Play listings (store screenshots via `img[alt*=Screenshot]`) | Works |
| nappy.co | Works (CC0 photos of Black and Brown people) |
| Unsplash connector | Blocked until Ian confirms his Unsplash account email |
| Mobbin connector | Needs a paid Mobbin plan |
| Figma connector | Connected (Ian's account has a View seat on the Starter plan) |

- **Self-checks:** Ian asked Claude to check every board before publishing (D-026). `scripts/canvas-preview.mjs` renders boards locally with the canvas runtime and screenshots them, including interactive states.
