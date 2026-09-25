# Round 8 generator

Round 8 is written natively in the Round 7 language (Geist, Kalam for rare moments, corners 6/10/14 and a circle) and passed through Round 7's `transform(native=True)`, which adds the shared CSS, the handwriting link and the `hand` Tweak. The design is explained in [doc 14](../../docs/00-discovery/14-round-8.md).

| File | Writes |
|---|---|
| `lib8.py` | Shared pieces: imports from Rounds 6 and 7, the three Hub icon directions (`hub_icon()`; `HUB_KIND` is the keystone), their moves (`HUB_CSS`), extra line icons (`ic8()`), the Round 8 tab bar (`tabbar8()`: Home, Learn, Hub, Community, Me) and `nb_text()`, which keeps amounts on one line |
| `icons8.py` | Batch 1: `R8-Hub-Icons`, the Hub's icon three ways, each in a working tab bar, on night, at five sizes and blurred. The keystone was picked (D-039) |
| `ia8.py` | Batch 2: `R8-IA`, the five tabs, what moved where, and a live tab bar |
| `learn8.py` | Batch 2: `R8-Learn` (Paths, Words, Stories and the switch), `R8-Topic-Shares` (the bakery explainer) and `R8-Words-Decoder` (the buzzword decoder; `WORDS` holds its sample entries) |
| `hub8.py` | Batch 3: `R8-Hub` (Naledi, opens on Me), `R8-Hub-Biz` (Wanjiru, opens on My business) and `R8-Tool-Skeleton` |
| `tools8.py` | Batch 3, the Me tools, with the shared tool frame (`tool_page()`, `beat()`, `means()`, `learn_this()`, `make_goal()`, `milestone()`): `R8-Tool-Payslip`, `-Payday`, `-Debt`, `-Fees`, `-Statement` |
| `biz8.py` | Batch 3, the business tools for Wanjiru: `R8-Tool-Price`, `R8-Tool-Invoice`, `R8-Shop-Edit`, `R8-Shop-Public`. `crop()` cuts products out of her stall photo |
| `goals8.py` | Batch 3: `R8-Goals` and `R8-Home` (Round 7's Home, patched: several goals, a Hub card, the Round 8 tab bar) |
| `round8.py` | Builds every board: `python3 round8.py <project dir> [Board ...]`. Boards that already carry Round 7's transform (Home) aren't transformed twice |
| `layout8.py` | Lays out canvas page `r8` row by row, from a fresh read of the live `canvas.json`: `python3 layout8.py <live canvas.json> <out canvas.json> <project dir>` |

Render and check as in [doc 06](../../docs/00-discovery/06-tooling-and-harness.md#reviewing-canvas-boards-locally-render-recipe): serve with `scripts/serve-boards.py`, then run `scripts/board-check.mjs` with a plan.
