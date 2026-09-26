# Round 7 generator

Round 7 is Round 6 with three changes, applied as a transform so the two rounds stay comparable. The design is explained in [doc 13](../../docs/00-discovery/13-round-7.md).

| File | Writes |
|---|---|
| `round7.py` | `R7-Welcome`, `R7-Starter`, `R7-Home`, `R7-Learn`, `R7-Ask`, `R7-Vault`, `R7-Community`, `R7-Me`, `R7-Components`. It builds each Round 6 board, then: adds the handwritten moments (`moments()`), swaps the display type to Geist, maps every corner to 6, 10, 14 or a circle, relinks tabs to Round 7, and adds a `hand` Tweak |
| `areas7.py` | `vault()`, `me()` and `community()`: the three screens redesigned natively in Round 7 style (new layouts, not a transform). `round7.py` still adds the `hand` Tweak and Round 7 links, but skips the moments, corner and type steps for them |
| `screens7.py` | Screens Round 6 never had, from Round 3's set: `R7-Entry` (photo-led welcome), `R7-Goals`, `R7-Progress`, `R7-Checkin`, `R7-Buddy`, `R7-Settings` |
| `kit7.py` | `R7-Components` (controls) and `R7-Data` (data and feedback). `R7-Widgets` is Round 6's widgets board through the transform |
| `brand7.py` | `R7-Brand` (app icon A, the wordmark in Geist), `R7-Icons`, `R7-Motion` (M1 to M6, live), `R7-Foundations` |
| `marketing7.py` | `R7-Store-1…8`, `R7-Listing`, `R7-Feature-Graphic`, `R7-App-Icon`, `R7-Hero-Device`, `R7-Ad-Photo`, `R7-Ad-Pool`, `R7-Ad-Word`, `R7-Ad-Story`, from 2x captures of the Round 7 screens (`CAPS`). Exports live in `design/marketing/round-7/` |
| `auth7.py` | Batch 1: `R7-Auth-Signin`, `R7-Auth-Code`, `R7-Auth-Profile`, `R7-Auth-Consent`, `R7-Reveal`, `R7-FirstStep`, `R7-Auth-Notify`, `R7-Auth-Lock`, `R7-Auth-Back` |
| `loop7.py` | Batch 2: `R7-Lesson`, `R7-Compare`, `R7-Simulator`, `R7-Offer`, `R7-Report` (A4), `R7-Hard` |
| `biz7.py` | Batch 3: `R7-Biz-Profile`, `R7-Biz-Check`, `R7-Biz-Home` |
| `admin7.py` | Batch 5, AWO Admin at 1440 wide: `R7-Admin-Overview`, `-Approvals`, `-Scoring`, `-Members`, `-Moderation`, `-Content`, `-Audit` |
| `pull8.py` | Copies every Round 8 board onto page `r7` as `R7-R8-*` (linked to each other, below Round 7's rows), so Round 7 is one full board. Round 7 and page `r8` stay unchanged |
| `typeboard.py` | `R7-Type`: Geist's scale, the handwriting candidates with a live switcher, and the corners, each with a Round 6 comparison |

```sh
cd design/round-7
python3 round7.py /path/to/project
python3 typeboard.py /path/to/project
```

Change a Round 6 screen, rerun both rounds, and the comparison stays fair. `moments()` asserts each anchor exists, so a Round 6 wording change fails loudly instead of silently losing a moment.

**Capturing screens for marketing:** render each screen at 390 by 844 with a device scale of 2. For a taller screen, first set `flex-shrink: 0` on every child of `.scr`, then set the board to 844px tall. Without the first step its sections squash to fit. Save the captures as JPEG, upload them to the canvas's image store, and update `CAPS`.
