# 11 · Round 5: one language, five areas, three volumes

> **Status:** Published on canvas page `r5` (Round 5), 25 Sep 2026. Every board was rendered and clicked through locally before publishing (D-026).
> **Ian's brief:** Round 4 "lost a lot of character". Bring back Round 3's bold condensed type, colour as big blocks, signature shapes and visual-first layouts, as a "meaningful design language: fun, modern, clean" (D-028). Build around **Home, Learn, Vault, Community, Me** (D-029). Start with a volume test.

## Why Round 4 felt flat

Round 4 improved the content and removed the look. Each rule in the [Round 3 review](09-round-3-review.md) was reasonable on its own, but they were all applied at once, and each one took something away:

- **Type lost its voice.** Heavy condensed Bricolage was retired from the app, so every title became medium weight at about 26px.
- **Colour shrank to accents.** With lime only on dark and blush only on people, most screens were grey-green, white and one green card.
- **The shapes went.** Rings, ripples, stones and arches were cut; only the pool survived.
- **Words replaced pictures.** The Home step grew from 5 words to 15; the Mentor reveal was three screens of sentences before anything visual.
- **One template everywhere:** a caption, a title, stacked white cards and a full-width green button.

What Round 4 got right stays: fewer, deeper flows with real states; hard moments without shame; three members with their own currencies; privacy lines; a warmer voice.

## The language

Each area has a colour and a shape. A shape means one thing and moves one way. A tile wears the colour of the area it opens, so Home becomes a map of the app.

| Area | Colour | Shape | Means | Moves |
|---|---|---|---|---|
| **Home** | Evergreen `#0F4A36` | **Pool** (a capsule filling with water) | Money she's building: the safety net and goals | Fills and ripples when money goes in |
| **Learn** | Night `#0B0F0E` | **Moon** (phases) | Learning in progress; Ola lives here and in Ask | Waxes as a lesson goes on; Ola looks, blinks, cheers |
| **Vault** | Lime `#D8F36A` | **Arch** (a doorway) | Money words she has kept | Flips over to show an example |
| **Community** | Blush `#FFC7D6` | **Ripple** (rings around faces) | Other women and their words | Spreads out when someone cheers |
| **Me** | Pool `#D3E8E4` | **Stones** (stepping stones across water) | Where she stands: her stage and versions | Steps forward when a new profile version lands |

- The **tab bar icons are the five shapes**, and the active tab takes its area's colour, so the navigation teaches the language.
- **Type:** Bricolage Grotesque 800, condensed (`font-stretch` 82%), for numbers, the names of things and big moments; never paragraphs. Geist for everything read: 15–17px, 13px small print, 12px floor.
- **Rules:** a shape means one thing (the pool is never used for learning, the moon never for money); one main button per screen; Ola only in Learn and Ask, never beside results or amounts; no chips over faces, no streak counts, no red for a month that went down; cover the logo and the screen should still look like AWO.

## The volume test

The same five screens with identical sample content, at three volumes. Ian points at one, or mixes ("Volume 2, with Vault from 3").

| Volume | What changes |
|---|---|
| **1: Clean** | Mist screens with one block in the area colour. Shapes small (icons, a small pool, a row of moons). Condensed type for titles and the key number only. Home is a colour-coded list that links to every area. |
| **2: Bold** | Bento tiles in each area's colour, big condensed type, the shapes as heroes (a tall pool, a big moon with Ola, a lime arch card, a ring of eight faces, stones with her photo), bigger photos, a small single-hue chart on Me. One ambient motion per screen. |
| **3: Playful** | Each area's colour edge to edge. Type as image ("R 1 800" at 104px over the pool, "Vault" cropped by the screen edge, a giant stage numeral), shapes breaking the frame, tilted stickers, a floating tab bar, a few things moving on their own. Still one main button. |

**Sample content (same in every volume):** Naledi on Friday 25 September, payday; safety net R 1 800 of R 5 000; this week's step "pay yourself first: move R 100 in"; lesson 3 of 6, "Where to keep it"; word of the week "Stokvel"; Wanjiru's cheer and her stall post; this week's question "What did you say no to this week?"; Stage 2 of 4 with four sample dimensions and readiness 55, 59, 63 across three versions.

**Try tapping (every volume):** "I moved R 100" fills the pool (R 1 900, droplets, a splash); Ola jumps with happy eyes; the Stokvel card flips to an example; Cheer sends a ripple and counts up. Reduce motion turns the loops and splashes off.

## Watch-outs for Ian

- **Volume 3's Me screen** shows the stage as a giant "2". It is bold, but it may read like a level; check it against D8 (no gamified results) before choosing it.
- **Learn** stays night with a lime button (D-024). That pairing is common in generated designs; the moon, the craters and Ola are what make it AWO's.
- **Lime on evergreen is Wise's pairing** (noted in [08](08-round-3-direction-e.md)); blush, the shapes and photography keep AWO distinct.
- **If Volume 1 wins,** the colour map survives mainly in the icons and tab pills; Home's colour-coded rows keep it visible.
- **Not in this test:** Round 4's hard moments (day one, a missed week, a month that went down, offline) and the three-member range. They return when the five areas become full flows (T-064).
- Stage names, dimension names, numbers and the stokvel example are **samples** (Q-04, Q-05, Q-13, Q-14). Photos are the nappy.co stand-ins from Round 4 (Q-27).

## How it was made

- A small generator in [`design/round-5/`](../../design/round-5/) writes the four boards from shared pieces (the five shape icons, pool, moon, stones, Ola, tab bars). Change a piece once and every volume follows; see its README.
- Rendered with `scripts/canvas-preview.mjs` and clicked through. The self-check caught: Home content running under the tab bar, an arch outline crossing a label, a wrapped tag on Me, the big amount crossing the pool's rim (now outlined so it sits in front), "12 words kept" colliding with the title, the moon hiding its lit side, a cramped tab label and splash droplets left frozen under reduce motion.
