# These are COPIES. Do not edit them here.

Canonical source: `~/code/answerable-skills/skills/`
`~/.claude/skills` is a symlink to that directory, so edits there are the ones
that take effect and the ones git tracks.

Refreshed from canonical 2026-08-29. Anything edited in this folder is invisible
to Claude and will be overwritten by the next refresh.

To re-refresh:

    for f in vt-deck-authoring vt-fusion-retrofit vt-bio-skill; do
      cp ~/code/answerable-skills/skills/$f/SKILL.md \
         ~/Desktop/AT_docs/3_SKILLS_desktop/$f/SKILL.md
    done
