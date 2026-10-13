# ADR 0002: Branches, pull requests and merging into `main`

- **Status:** Proposed (foundation pass, T-120, 13 October 2026). Not in the decision log until Ian decides.
- **Relates to:** D-044 (`main` is the default; branches named by type and topic); T-121; doc 17 §1 (H1, H2), §2 and §6.2.

## Context

Until now, sessions committed straight to their own branches and the branches were merged by hand. Two sessions reused IDs and a merge renumbered docs, questions and a task. This session found its brief on a branch that hadn't reached `main`. Nothing is protected.

GitHub facts that shape the options (checked 13 October 2026, GitHub docs):

- **Protected branches and rulesets on a private repository need GitHub Pro, Team or Enterprise.** On the Free plan they apply to public repositories only.
- A pull request's author **can't approve their own pull request**, so a solo owner can't require an approval; required status checks still work.
- The merge queue is for organisations only (public, or Enterprise Cloud for private).
- Secret scanning on a personal private repository isn't available on any plan short of Enterprise; push protection for users only blocks pushes to public repositories.

## Proposed decision

1. **`main` is the truth.** Every branch starts from the latest `main`, named by type and topic (D-044): `docs/…`, `design/…`, `feat/…`, `fix/…`, `chore/…`, `content/…`.
2. **One pull request per pass**, or per batch when a pass is long. Claude opens it at the end of the pass (or when Ian asks), with the template's checklist (CHANGELOG, TASKS, STATUS, decisions, open questions, data-location note).
3. **Squash merge** by default, as nearly every reference monorepo does, so `main` reads as one commit per change; the pull request keeps the working commits. The pull-request title becomes the commit's subject, so it's written to stand alone (from Phase 2, in Conventional Commits form, `feat(api): …`, checked by CI).
4. **Protect `main`** with a ruleset: no force-push, no deletion, changes only through a pull request, and CI must pass. Required approvals: none (a solo owner can't approve their own). **This needs GitHub Pro** (a paid plan, Ian's call). Until then, a Claude Code hook refuses `git push` to `main` from a session, which covers Claude though not people.
5. **Tags:** `content/<kind>/<id>@<semver>` for published governed content (ADR 0005); `design-exports/<set>` for exported design sets (ADR 0003); app releases from Phase 2 with calendar versions (`web@2027.03.1`).
6. **Old session branches:** after GitHub's default switches to `main` (T-121), delete `claude/nifty-gauss-7odogg` (identical to `main`), `claude/intelligent-hypatia-ja9g5n` and `claude/exciting-cray-7z7fke` (both already contained in `main` or in this branch). `docs/foundation-kickoff` is contained in `docs/foundation-blueprint`, so merging this pass's pull request brings it in. Deletion is Ian's call.

## Alternatives

- **Merge commits** instead of squash: keeps every working commit on `main`, which suits long design passes, but makes `main`'s history noisy and harder for a session to scan.
- **Trunk-based, committing straight to `main`:** fastest for one person, but parallel sessions collide (as they did), and there's no point at which CI checks a change before it lands.
- **A GitHub organisation on the Team plan:** adds organisation features (and Secret Protection at an extra cost per committer), which one person doesn't need yet.

## Consequences

- Every pass ends with a pull request; Ian merges it (or tells Claude to). The pull request is also where Claude Code reviews and Ian comments.
- The CHANGELOG cites pull requests rather than commit hashes.

## Data-location note

GitHub (United States). Code, docs and synthetic data only.

## Ian decides

Squash (recommended) or merge commits; whether to pay for GitHub Pro to protect `main`; when to delete the old session branches.
