# Round 8 generator

Round 8 is written natively in the Round 7 language (Geist, Kalam for rare moments, corners 6/10/14 and a circle) and passed through Round 7's `transform(native=True)`, which adds the shared CSS, the handwriting link and the `hand` Tweak. The design is explained in [doc 14](../../docs/00-discovery/14-round-8.md).

| File | Writes |
|---|---|
| `lib8.py` | Shared pieces: imports from Rounds 6 and 7, the three Hub icon directions (`hub_icon()`; `HUB_KIND` is the keystone), their moves (`HUB_CSS`), extra line icons (`ic8()`), the Round 8 tab bar (`tabbar8()`: Home, Learn, Hub, Community, Me) and `nb_text()`, which keeps amounts on one line |
| `icons8.py` | Batch 1: `R8-Hub-Icons`, the Hub's icon three ways, each in a working tab bar, on night, at five sizes and blurred. The keystone was picked (D-039) |
| `ia8.py` | Batch 2: `R8-IA`, the five tabs, what moved where, and a live tab bar |
| `learn8.py` | Batch 2: `R8-Learn` (Paths, Words, Stories and the switch), `R8-Topic-Shares` (the bakery explainer) and `R8-Words-Decoder` (the buzzword decoder; `WORDS` holds its sample entries) |
| `round8.py` | Builds every board: `python3 round8.py <project dir> [Board ...]` |
| `layout8.py` | Lays out canvas page `r8` row by row, from a fresh read of the live `canvas.json`: `python3 layout8.py <live canvas.json> <out canvas.json> <project dir>` |

Render and check as in [doc 06](../../docs/00-discovery/06-tooling-and-harness.md#reviewing-canvas-boards-locally-render-recipe): serve with `scripts/serve-boards.py`, then run `scripts/board-check.mjs` with a plan.
