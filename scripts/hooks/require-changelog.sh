#!/usr/bin/env bash
# Claude Code PreToolUse hook (Bash): block `git commit` unless docs/CHANGELOG.md
# has been updated, so the project diary never falls behind.
# Bypass for trivial commits by putting SKIP_CHANGELOG=1 in the command.
set -uo pipefail

cmd="$(jq -r '.tool_input.command // empty')"

case "$cmd" in
  *"git commit"*) ;;
  *) exit 0 ;;
esac

case "$cmd" in
  *SKIP_CHANGELOG=1*) exit 0 ;;
esac

root="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
[ -f "$root/docs/CHANGELOG.md" ] || exit 0

if [ -n "$(git -C "$root" status --porcelain -- docs/CHANGELOG.md)" ]; then
  exit 0
fi

echo "Commit blocked: add an entry to docs/CHANGELOG.md first (and update docs/TASKS.md, plus docs/STATUS.md if the focus changed). For a trivial commit, prefix the command with SKIP_CHANGELOG=1." >&2
exit 2
