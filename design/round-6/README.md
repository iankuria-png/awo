# Round 6 board generator

Writes the Round 6 boards on the [design canvas](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9) (page Round 6). The design is explained in [doc 12](../../docs/00-discovery/12-round-6.md). It builds on Round 5's shared pieces in [`../round-5/lib.py`](../round-5/lib.py) at Volume 1 (Clean).

| File | Writes |
|---|---|
| `lib6.py` | Round 6 pieces: linked tab bars, the phone artboard wrapper, the readiness arc, extra photos. Holes are written `[[ name ]]` and become `{{ name }}` |
| `onboarding.py` | `R6-Welcome`, `R6-Starter` |
| `home.py` | `R6-Home` (Ian's order: greeting, stories, bento, carousel, step, keep learning, profile) |
| `areas.py` | `R6-Learn`, `R6-Ask`, `R6-Vault`, `R6-Community`, `R6-Me` |
| `kit.py` | `R6-Components`, `R6-Widgets` |
| `marketing.py` | `R6-Store-1…6`, `R6-Listing`, `R6-Feature-Graphic`, `R6-App-Icon`, `R6-Hero-Device`, `R6-Ad-Word`, `R6-Ad-Pool`, `R6-Ad-Story` |
| `foundations.py` | `R6-Foundations` |

## Use

```sh
cd design/round-6
python3 areas.py /path/to/project        # writes the five area boards into that folder
python3 home.py /path/to/project/R6-Home.dc.html
```

Then render and click through the boards (D-026) and publish them with the Artifact tool.

**The marketing boards use captures of the screens**, uploaded to the canvas (`CAPS` in `marketing.py`). When a screen changes:
1. Recapture it at 2x with the render script: set each board to 844px tall and take a screenshot of the viewport.
2. Upload the capture and update its id in `CAPS`.
3. Regenerate and re-export `design/marketing/round-6/`.

All content is sample content.
