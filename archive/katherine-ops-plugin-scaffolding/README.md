# katherine-ops

A plugin marketplace holding one plugin. Cowork installs from this repository and updates by pulling it, so the skills are drawn from GitHub rather than re-uploaded by hand.

## What a marketplace is

Cowork installs plugins from a git repository that carries `.claude-plugin/marketplace.json` at its root. That file is a catalogue: it names the plugins in the repository and where each one sits. Adding this repository as a marketplace makes its plugins installable; running an update pulls the repository and picks up whatever changed. One repository can hold many plugins — this one holds `katherine-ops`.

This is the reason to use a plugin rather than a folder of `SKILL.md` files. Account skills are not read from git. A repository of loose skill files is a backup you re-upload by hand; a marketplace is a source the tool reads on its own.

## Layout

```
.claude-plugin/marketplace.json     the catalogue
plugins/katherine-ops/              the plugin
  .claude-plugin/plugin.json          manifest
  .mcp.json                           Roam MCP server
  skills/                             16 skills
    manuscript-ops/scripts/             the two Python scripts
  CONNECTORS.md                       what is wired where
  README.md                           skill-by-skill
reference/                          documents with no other home
```

## Installing

Add the marketplace, then install:

```
/plugin marketplace add kvond12/katherine-ops
/plugin install katherine-ops@katherine-ops
```

Before the Roam skills will run, set the two environment variables the MCP server reads:

```bash
export ROAM_API_TOKEN='...'      # from Roam → Settings → Graph → API tokens
export ROAM_GRAPH_NAME='kvond'
```

Put them in `~/.zshrc` or a `.env` file. `.env` is gitignored; never commit the token.

## Publishing this repository

From the directory this repository was unpacked into:

```bash
git init
git add -A
git commit -m "katherine-ops: 16 skills, Roam MCP, manuscript-ops scripts"
gh repo create katherine-ops --private --source=. --push
```

`gh` is the GitHub CLI. If it is not installed: `brew install gh`, then `gh auth login` once.

Use `--private` unless you intend the skills to be readable by anyone. They carry your calendar identifiers, Drive file IDs, and email routing.

## Updating

The skills in this repository are now the source. Edit here, commit, push, and run the plugin update in Cowork. Editing a synced skill file on disk does not change anything — that copy is a cache.

## `reference/`

Two documents that exist nowhere else. Verified against the Roam graph before being placed here:

- **`Decisions & Citations.md`** — eleven sections: the core argument, the naming, the agency taxonomy, load-bearing conceptual decisions, the five apprenticeship movements, scoping rules, the AI framing, voice conventions, working conventions, citation ballast, current structure. `Answerable Teaching/Editorial Notes` in Roam overlaps it but does not contain it; a search for "five apprenticeship movements" returns no blocks.
- **`Finishing Map.md`** — the June 7, 2026 item-by-item build-out status, marked `[PLACED]` / `[DRAFTED]` / `[CONFIRM]` / `[OPEN]`. Not a Roam page. Its instructions were distributed into the chapters as 【NOTE】 markers that then cite it by name — `Chapter 4 — Dialogic Teaching` reads "the Finishing Map expected his introduction in Ch3." Seven blocks in the graph point at a document the graph cannot open.

Both are reference material rather than plugin content, which is why they sit outside `plugins/`.

## Not carried here

- **The manuscript.** Roam is canonical; `Sync Book.command` pushes it to its own repository.
- **`check_citations.py`.** Marked planned in `manuscript-ops`, never written. It has no `sources.json` to run against either; `Answerable Teaching/References` in Roam is the material one would be built from.
- **Google connectors.** Account-level OAuth, not plugin-declarable. See `plugins/katherine-ops/CONNECTORS.md`.
