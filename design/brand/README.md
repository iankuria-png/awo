# Brand system page

Draws AWO's suggested Visual Brand System Brief (Instagram and LinkedIn) as the canvas page **Brand system (suggested)**: thirteen boards, one per section, in the brief's own system (deep plum, terracotta and warm stone; Playfair Display and Montserrat). Summary, contrast findings and how it differs from the app: [doc 16](../../docs/00-discovery/16-brand-system-brief.md).

| Command | Does |
|---|---|
| `python3 brand.py build <project dir> [Board ...]` | Writes the `BS-*.dc.html` boards |
| `python3 brand.py layout <live canvas.json> <out canvas.json> <project dir>` | Adds the page, lays out its three rows and opens the canvas on it |

To publish: read the live `canvas.json`, build, lay out, then publish `canvas.json` with the boards. Check them first with `scripts/board-check.mjs`.
