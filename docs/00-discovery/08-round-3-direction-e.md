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
