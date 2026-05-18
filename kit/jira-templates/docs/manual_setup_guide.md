# 🛠 D-POAF® Jira — Manual Setup Guide

> Step-by-step setup if you prefer not to run the Python script. ~30 minutes.

---

## Step 1 — Create the Jira project

1. In Jira Cloud, click **+ Create** → **Project**
2. Template: **Scrum**
3. Type: **Team-managed** (recommended) or **Company-managed** (for custom fields)
4. Project name: `D-POAF® Governance`
5. Project key: `DPOAF`
6. Lead: yourself
7. Click **Create**

---

## Step 2 — Create the sample Wave Epic

1. Click **+ Create** (top bar)
2. Project: `D-POAF® Governance`
3. Issue Type: **Epic**
4. Summary: `WAVE-EXAMPLE-001 - Customer Feedback Categorization (Pilot)`
5. Description: paste the Wave template (see `wave_description_template.md` below)
6. Labels: add all of these (comma-separated):
   - `d-poaf`
   - `wave`
   - `macro-3`
   - `phase-4`
   - `deliver-wave`
   - `active`
7. Click **Create**

---

## Step 3 — Create the sample Prompt Action

1. **+ Create**
2. Issue Type: **Task** (or Story)
3. Summary: `PA-001 - Build sentiment classifier function`
4. Epic Link: select `WAVE-EXAMPLE-001` (the Epic from step 2)
5. Description: paste the PA template
6. Labels:
   - `d-poaf`
   - `prompt-action`
   - `macro-2`
   - `phase-3`
   - `wave-surfer`
   - `reusable-prompt`
   - `traceability-thread-complete`
   - `quality-5`
7. Click **Create**

---

## Step 4 — Create the sample Proof Record

1. Open the Wave Epic (WAVE-EXAMPLE-001)
2. Click **+ Add a child issue** (or **Create sub-task**)
3. Issue Type: **Sub-task**
4. Summary: `PROOF-EXAMPLE-001 - Closure of WAVE-EXAMPLE-001`
5. Description: paste the Proof Record template
6. Labels:
   - `d-poaf`
   - `proof-record`
   - `macro-4`
   - `phase-7`
   - `pod-approved`
   - `pov-approved`
   - `por-na`
   - `wave-captain-signed`
   - `sponsor-signed`
7. Click **Create**

---

## Step 5 — Save your first JQL filter

1. In the Jira search bar, click **JQL**
2. Paste:
   ```
   project = DPOAF AND issuetype = Epic AND labels = "wave" AND status != Done
   ```
3. Click **Save as** → Filter name: `Active D-POAF Waves`
4. Save → mark as Favorite for quick access

Repeat with other queries from `jql_cookbook.md`.

---

## Step 6 — Create a dashboard

See `dashboard_setup.md` for the full dashboard configuration.

---

## ✅ Done

You now have:
- 1 Wave Epic with full D-POAF structure
- 1 Prompt Action Task linked to the Wave
- 1 Proof Record Sub-task closing the Wave
- 1 saved filter

Total time: ~30 min manually, or ~5 min via the Python script (recommended).

---

D-POAF® Framework v1.1 — d-poaf.org — Licensed under CC BY 4.0
