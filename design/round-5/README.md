# Round 5 board generator

Writes the four Round 5 boards on the [design canvas](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9) (page Round 5). The design is explained in [doc 11](../../docs/00-discovery/11-round-5-volume-test.md).

| File | Writes |
|---|---|
| `lib.py` | Shared pieces: colour tokens, photos, base CSS and motion, the five shape icons, tab bars, Ola, moon, pool, stones, the board wrapper and the tap logic |
| `lang.py` | `R5-Language.dc.html`: one language, five areas |
| `v1.py`, `v2.py`, `v3.py` | `R5-Volume-1/2/3.dc.html`: the five areas at each volume |

## Use

```sh
cd design/round-5
python3 v2.py /path/to/project/R5-Volume-2.dc.html
```

Then render and check the board with `scripts/canvas-preview.mjs` (D-026) and publish it to the canvas with the Artifact tool. Change a shared piece in `lib.py` once and regenerate every board.

- Photos are `/_blob/<id>` uploads already in the canvas's asset store (nappy.co stand-ins, Q-27). To render them locally, map the ids to downloaded files in the preview's blob map.
- All content is sample content. The boards carry a "Sample content" label.
