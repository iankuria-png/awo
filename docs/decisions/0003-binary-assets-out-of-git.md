# ADR 0003: Generated binaries stay out of git; masters stay in

- **Status:** Proposed (foundation pass, T-120, 13 October 2026). Not in the decision log until Ian decides.
- **Relates to:** doc 17 §1 (H7, H8), §2 and §9.

## Context

`design/marketing/` holds 57 PNGs (19 MB) in four generations (Rounds 3, 6, 7 and 8); only Round 8's is current. Each regeneration adds new blobs for good: 81 image blobs (26.5 MB before packing; PNGs barely compress) make up almost all of the 25.5 MB packed history. Meanwhile the stand-in photos exist only in the canvas's asset store.

Facts (GitHub docs, checked 13 October 2026): GitHub warns on files over 50 MiB and blocks files over 100 MiB, and recommends repositories under 1 GB. Git LFS on Free and Pro includes 10 GiB of storage and 10 GiB of bandwidth a month, then $0.07 per GiB-month and $0.0875 per GiB; CI checkouts count against bandwidth. Release assets may be up to 2 GiB each, with no limit on the total or on bandwidth. None of the nine reference monorepos checked uses LFS.

## Options

| Option | For | Against |
|---|---|---|
| **A. Sources and masters in git; generated exports out** (published as release assets) | The repo stays small and fast to clone; exports can always be rebuilt from their generators; release assets are free and versioned by tag | Exports aren't browsable in the repo tree; regenerating needs the canvas and the scripts |
| **B. Git LFS for images** | Images stay in the tree, versioned | Metered bandwidth (every CI checkout), more setup in cloud sessions, and moving existing files needs a history rewrite anyway |
| **C. Keep everything in git** | Simple | The repo grows with every export round; already most of its size |

## Proposed decision

**Option A.**

- **In git:** generators and scripts; small, final masters (SVG wordmark, mark, app icon source, the five shapes and the keystone; fonts come from npm packages, not files); fixtures; and a few small PNGs a doc needs to show.
- **Out of git:** generated exports (store screenshots, ads, renders, PDFs). `design/marketing/**/*.png` is ignored from the setup pass on; finished sets are published as **GitHub release assets** under a tag (`design-exports/round-8`), and `design/marketing/README.md` links to them.
- **The existing PNGs** move out of the working tree in one commit after they're attached to a release; they stay in history (26 MB is small). **No history rewrite:** it would change every commit hash, and the docs cite some (D-044 cites `e84d2dc`).
- **Photos and other licensed media** get a home that isn't only the canvas: an `assets` release with a manifest (source, licence, consent) committed to `design/assets.md` (doc 17 §9). Member photography, once it exists, is personal data and lives in South Africa, not on GitHub.
- `.gitattributes` marks images as binary (`*.png binary`, `*.jpg binary`), lines end in LF, and `docs/CHANGELOG.md merge=union`.

## Consequences

- Cloning stays quick for cloud sessions, which clone on every start.
- The setup pass needs one script (`scripts/publish-exports.sh` or a workflow) that zips a set and attaches it to a release.

## Data-location note

Release assets live on GitHub (United States). Only AWO's own marketing drafts and CC0 stand-in photos go there; never member photos or member data.

## Ian decides

Release assets (recommended), LFS, or keeping everything in git; whether old exports leave the working tree.
