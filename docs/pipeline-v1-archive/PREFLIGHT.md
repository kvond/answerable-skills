# PREFLIGHT — run before any pipeline session (paste to the model, wait for "go")

1. Composio `googlesheets` + `googledrive` both ACTIVE? If not, reconnect and WAIT_FOR_CONNECTIONS.
   Never fall back to the first-party Google connector (it blocks AI-restricted student files).
2. Read the **Config** tab of Dashboard `1W0s8YjcIt7h8ezICAF6SndTj97PiMcfjpXrmVmV8cBA`.
   Confirm `dashboard_sheet_id` == that same ID.
3. For each lesson about to run, confirm Config has its **notes/draft folder ID, template ID,
   and script ID**. If any is missing: resolve it, then WRITE IT BACK to Config before processing.
4. Running B1? Confirm `workflow_b1_script_id` is not `MISSING`.
   (Built 2026-05-29: extract_and_grade_rewrites.py.)
5. Glance at the Schoology submissions tab for late/orphaned work (sync-break check).
6. Restate scope: in-scope lessons only; EXCLUDE Sha'rod Watson and
   Pig Autopsy / Stages of Decomposition.
7. Use deployed scripts only — never reconstruct one from memory. If a download fails, retry or halt.

Then STOP and wait for "go."
