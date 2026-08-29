# Connectors

Two different mechanisms reach outside tools. They are configured in different places.

## Declared by this plugin

| Service | Server | Credentials |
|---|---|---|
| Roam Research | `roam-research-mcp`, run via `npx` | `ROAM_API_TOKEN`, `ROAM_GRAPH_NAME` from the environment |

Installing the plugin brings this server with it. Nothing to authorize in a browser; it needs the two environment variables and a working `npx`.

## Authorized in your Cowork account

| Service | Used by |
|---|---|
| Gmail | `daily-brief` (the email pass), the student-feedback drafts |
| Google Calendar | `daily-brief`, `activity-scout` |
| Google Drive | `daily-brief` (Tiller, Master Agenda), `formative-pipeline-v2` |

These are OAuth connectors held against your account, not this repository. A plugin cannot carry them, and should not — the alternative would be committing tokens. Authorize them once in Cowork's connector settings; every session and every install of this plugin then sees them.

## Reference values the skills expect

Carried here so they survive outside the skill bodies:

| Value | Identifier |
|---|---|
| Roam graph | `kvond` |
| Appts calendar | `1afa0atpk8s5e0c1hu9950ekd4@group.calendar.google.com` |
| Master Agenda (Drive) | `1Tqh7eB_I3z-eP9FYMCPvNVclmR9VGXVaae0ZdRICy1g` |
| Tiller (Drive) | `1i725p49qPBpNYRXWWMKJkAE1GSTM4unKOrcIV1INCQU` |

Gmail receives four accounts by forwarding into `kvond12@gmail.com`. Filter by original recipient:

| Account | Filter |
|---|---|
| Personal | `kvond12@gmail.com` |
| UD | `to:kvond@udel.edu` |
| WilmU | `to:katherine.s.vonduyke@wilmu.edu` |
| Red Clay | `to:katherine.vonduyke@redclay.k12.de.us` |
