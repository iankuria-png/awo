# Round 9 generator

Round 9 connects what Rounds 7 and 8 built, and designs the material around the app. The brief and batches are in [doc 15](../../docs/00-discovery/15-round-9.md).

| File | Writes |
|---|---|
| `lib9.py` | Shared pieces: the sample member's versions, `page9()` for phone boards, area badges, stepping stones at any size |
| `loop9.py` | Batch 1: the loop flow board, the reminder, notifications, what changed, this month's step, a milestone and sharing, three WhatsApp status cards, search, help, reporting a problem |
| `tools9.py` | Batch 2: All tools, seven Hub tools (sending money home, a loan's real cost, two job offers, retirement pulse, what I own and owe, is it worth it, business setup) and the savings-group book |
| `channels9.py` | Batch 3: Home and the DIVA profile on a computer, Learn on a tablet, the WhatsApp and USSD check-ins, one question in every channel; `screen_board()` (in `lib9.py`) draws boards at any size |
| `round9.py` | Builds the boards: `python3 round9.py <project dir> [Board ...]` |
| `layout9.py` | Lays out page `r9` and opens the canvas on it |
| `pull9.py` | Copies every Round 9 board onto page `r7` as `R7-R9-*`, with links rewritten; then run `../round-7/group7.py` |

To publish a batch: read the live `canvas.json`, build, run `layout9.py`, `pull9.py` (naming any Round 8 board that now links to Round 9, such as `R8-Home`) and `group7.py`, then publish `canvas.json` with the boards and copies.

The flow board uses 2x captures of the loop's screens (`design/round-8/capture8.mjs`); when a screen changes, recapture it, upload it and update `FLOW_CAPS` in `loop9.py`.
