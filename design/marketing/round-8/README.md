# Round 8 marketing exports

These are exported from the Round 8 marketing boards on the canvas (page Round 8, the last three rows). They're built from 2x captures of the Round 8 screens taken on 26 Sep 2026, so they show the new tab bar: Home, Learn, Hub, Community, Me. The type, lockup and app icon are the same as Round 7: Geist throughout, the stepping-stones lockup and app icon A (D-031, D-033). They're drafts. The wordmark (Q-25), the app name and the store copy (Q-31) are still open, and every number is a sample.

| File | Size | Use |
|---|---|---|
| `store-1-me.png` … `store-8-shop.png` | 1080 × 1920 | Google Play phone screenshots (the store allows eight): Me, Home with goals, the Hub, the payslip decoder, Words, Community, Stories and a member's shop |
| `feature-graphic-1024x500.png` | 1024 × 500 | Google Play feature graphic |
| `device-hero.png` | 1600 × 900 | Website or press hero |
| `ad-square-diva.png`, `ad-square-payslip.png`, `ad-square-goals.png`, `ad-square-words.png`, `ad-square-shop.png`, `ad-square-explained.png` | 1080 × 1080 | Social posts |
| `ad-story-podcast-1080x1920.png` | 1080 × 1920 | Story ad for the podcast. The quote is in the hand because it's the guest's own words |

The store icon hasn't changed, so use `../round-7/app-icon-512.png`.

What the set holds to:

- **Education only.** No ad names a company. The investing ad says what AWO won't do: "Shares, explained. Never sold."
- **The DIVA score says what it is:** readiness to learn, never a credit score. The app calls it the DIVA score too (D-040).
- **Samples are labelled.** Wanjiru's shop carries a Sample chip, the podcast guest is called a sample guest, and the amounts on screens are samples.
- **No ranking or promo words** (best, top, new) and no install prompts on store graphics.

To regenerate, run `design/round-8/marketing8.py` (through `round8.py`), then export each board at its exact pixel size as a 24-bit PNG. When a screen changes, recapture it with `design/round-8/capture8.mjs` (the steps are at the top of that file), upload the JPEG and update `CAPS8` in `marketing8.py`.
