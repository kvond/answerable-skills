#!/usr/bin/env bash
# Push answerable-skills to GitHub, and say what happened.
#
# Run it from anywhere:   ~/code/answerable-skills/push.sh
#
# It exists because the repository is canonical and a local repository is not a
# backup. Until this runs, the only copy of everything in it is this machine.
#
# It never takes a token, a password, or any credential. Git uses whatever is
# already in your macOS keychain, which is why this has to run in your Terminal
# rather than anywhere else.

set -u
REPO="$HOME/code/answerable-skills"
cd "$REPO" || { echo "Cannot find $REPO"; exit 1; }

echo
echo "  answerable-skills — $(date '+%A %-d %B %Y, %-I:%M %p')"
echo "  ────────────────────────────────────────────────────────"

# 1. Anything uncommitted?
if [ -n "$(git status --porcelain)" ]; then
  echo
  echo "  Uncommitted changes are present. They will NOT be pushed:"
  git status --short | sed 's/^/      /'
  echo
  echo "  To include them, commit first:"
  echo "      cd ~/code/answerable-skills"
  echo "      git add -A"
  echo "      git commit -m \"what changed\""
  echo
fi

# 2. What is about to go
AHEAD=$(git rev-list --count @{u}..HEAD 2>/dev/null || echo "?")
if [ "$AHEAD" = "0" ]; then
  echo
  echo "  Nothing to push — GitHub already has every commit."
  echo
  exit 0
fi

echo
echo "  $AHEAD commit(s) to push:"
git log --pretty='      %h  %ad  %s' --date=format:'%b %d' @{u}..HEAD
echo

# 3. Push
if git push; then
  echo
  echo "  Pushed. GitHub now has all $AHEAD."
  echo "  https://github.com/kvond/answerable-skills"
  echo
else
  echo
  echo "  Push failed. The two usual reasons:"
  echo
  echo "  1. Git asked for a username and password. GitHub stopped accepting"
  echo "     passwords — it wants a personal access token as the password."
  echo "     Make one at github.com/settings/tokens (scope: repo), and the"
  echo "     keychain will remember it after the first successful push."
  echo
  echo "  2. Someone pushed to GitHub since you last pulled. Then:"
  echo "         cd ~/code/answerable-skills && git pull --rebase && ./push.sh"
  echo
  exit 1
fi
