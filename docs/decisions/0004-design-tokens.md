# ADR 0004: Design tokens in the DTCG format, in three layers, with brand and mode as resolver inputs

- **Status:** Proposed (foundation pass, T-120, 13 October 2026). Not in the decision log until Ian decides.
- **Relates to:** D-017 (Figma), D-028, D-032, D-033, D-037, D-039; Q-10, Q-30, Q-49; T-030, T-048; doc 17 §7.

## Context

AWO's design language exists as Python constants and inline values in the canvas generators: 86 raw hex colours, 36 font sizes and about 20 spacing values in rounds 7 to 9 (doc 17, H9). It must reach the web (CSS, Tailwind), later React Native, Figma and the canvas, and it must survive Q-49: AWO's suggested social brand (plum, terracotta, warm stone, a serif and Montserrat, 4 px corners) differs from the app's in every visual layer. Learn and Ask are always night (Q-30's proposal), so night has to apply to a part of a screen, not only to the whole app.

The DTCG format reached its first stable version, 2025.10, with a resolver module that expresses brands and modes as inputs (Appendix F of doc 17).

## Options

| Option | For | Against |
|---|---|---|
| **A. DTCG 2025.10 JSON in git, three layers, brand and mode as resolver inputs, built with Terrazzo** | A standard format; one source for every platform; brand and mode switch without touching components; Figma imports DTCG natively; Terrazzo supports the resolver fully | Terrazzo is younger than Style Dictionary; React Native gets typed objects rather than a dedicated plugin |
| **B. The same, built with Style Dictionary 5** | The widest set of outputs and the largest community | Its DTCG 2025.10 and resolver support is "a work in progress"; themes need one build per permutation |
| **C. Figma variables as the source, synced by Tokens Studio** | Designers edit in place | €39 an editor a month for Git sync; Figma's mode limits depend on the plan; harder to review and test |
| **D. A TypeScript theme object only** | Simple for one platform | No standard; Figma and the canvas need their own copies |

## Proposed decision

**Option A.**

- **Three layers:** primitives (one file per brand, all with the same keys: `palette.primary|accent|highlight|neutral|night`, `font.family.sans|display|hand`, `radius.sm|md|lg`; plus shared space, size, motion, opacity and z-order), semantic roles (`color.bg.surface`, `color.fg.secondary`, `color.action.primary.bg`, `color.area.learn.bg`, `color.status.decrease`, `color.provenance.sample`, `type.title`, `radius.card`, `motion.duration.sheet`), and component tokens (`button.primary.bg`, `tabbar.item.active.fg`).
- **Semantic tokens point at roles, never hues,** so the brand is one resolver input. The five areas are semantic tokens too, so the Stone brand's "two grounds and one accent" is just another mapping.
- **Resolver inputs:** `brand` (oasis | stone), `mode` (light | night), `motion` (full | reduced), later `contrast`.
- **Night applies to a subtree:** `data-mode="night"` on the web, a scoped theme in React Native.
- **Outputs:** CSS variables (`--awo-…`), a Tailwind 4 theme (`@theme inline`), typed TypeScript themes, Figma variables JSON, and flat JSON for the canvas kit.
- **Checks in CI:** the build, a contrast test of every semantic text and UI pair in every brand and mode, and a lint rule against raw values in components and apps.
- **Versioned** with semantic versions; renaming or removing a token is a major version.

## Consequences

- The canvas generators can read real tokens through `design/canvas-kit`, ending the drift.
- Q-49 stops being a redesign risk: whichever brand leads, the change is in one primitives file and a short overrides file.
- One more tool (Terrazzo) to keep current; if Style Dictionary catches up, switching is a build-config change, since the source format is the standard.

## Data-location note

Tokens are AWO's own design data, with no member data. They live on GitHub (United States) and, once imported, in Figma (United States).

## Ian decides

Whether the brand layer is worth building before Q-49 is answered (recommended: yes, it costs a naming discipline, not extra screens); Terrazzo (recommended) or Style Dictionary; and tokens in code as the source of truth with Figma fed from them (recommended) or the reverse.
