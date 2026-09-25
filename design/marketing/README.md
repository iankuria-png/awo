# Marketing assets (Round 3 drafts)

Exploration drafts for Direction E. They are not final brand assets: the wordmark (Q-25), app name and store copy (Q-31) are still open. Every number on a screen is a sample.

| File | Size | Use |
|---|---|---|
| `store/store-01…06-*.png` | 1080 × 1920, 24-bit PNG | Google Play phone screenshots (9:16) |
| `feature-graphic-1024x500.png` | 1024 × 500, 24-bit PNG | Google Play feature graphic |
| `app-icon-512.png` | 512 × 512, 32-bit PNG | App icon candidate (stepping stones) |
| `hero-device-1600x900.png` | 1600 × 900 | Website or press hero: a real photo with a real AWO screen |
| `ads/ad-square-*-1080.png` | 1080 × 1080 | Social posts: photo-led, safety-net pool, word of the week |
| `ads/ad-story-1080x1920.png` | 1080 × 1920 | Story ad |

## Rules they follow

- Google Play specs checked on 25 Sep 2026: icon 512 × 512 PNG with alpha; feature graphic 1024 × 500 with no alpha; screenshots 9:16 at 1080 × 1920, no alpha.
- Store graphics carry no ranking or promo words ("best", "top", "new") and no install prompts. Social ads may use "Join free".
- Educational wording only (see `CLAUDE.md`). People are real photographs from [nappy.co](https://nappy.co/license) (CC0), standing in until AWO photographs members.

## How they were made

- Each asset is a board on the [design canvas](https://claude.ai/artifact/KxjTM3X7VQiEButw4QNiV9) (page Round 3). The sources are in `src/`; images inside them point at the canvas's uploaded assets (`/_blob/<id>`).
- `scripts/canvas-preview.mjs` renders a board at its exact pixel size; the exports were then flattened to RGB (the icon keeps alpha).
- `src/composite-phone-photo.py` puts an app screenshot into a phone photo using the measured screen corners, keeping the thumbs on top.
