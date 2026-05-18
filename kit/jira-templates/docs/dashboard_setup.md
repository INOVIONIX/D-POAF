# 📊 D-POAF® Jira — Dashboard Setup

> Configure a D-POAF® Control Room dashboard in 10 minutes.

---

## Why a dashboard?

A D-POAF® dashboard gives Wave Captains, Sponsors, and Auditors a one-glance view of:
- Where each active Wave is in its lifecycle (macro-phase)
- Which Prompt Actions need attention (low quality, missing traceability)
- Recent closures (Proof Records)
- Compliance status (DL-006 / DL-012 violations)

Open it each morning to know what to focus on.

---

## Create the dashboard

1. In Jira, top menu → **Dashboards** → **Create dashboard**
2. Name: `D-POAF® Control Room`
3. Description: `Operational view of all D-POAF Waves, Prompt Actions, and Proof Records.`
4. Layout: **2 columns** (or 3 if you have a wide screen)
5. Permissions: choose who can view (your team / public)
6. **Add**

---

## Recommended gadgets — 6 essential

Add these gadgets in order. Each takes ~1 minute to configure.

### Gadget 1 — Pie Chart: Active Waves by Macro-Phase

**Type**: Pie Chart
**Filter or JQL**: 
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" AND status != Done
```
**Statistic Type**: Labels (or Macro-Phase custom field if you upgraded)

**Why**: At-a-glance balance of your portfolio across the 4 macro-phases. Too many Waves stuck in Shape & Align? Time to push them forward.

---

### Gadget 2 — Filter Results: Stale Waves (alert)

**Type**: Filter Results
**JQL**:
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" AND status != Done AND updated <= -14d
```
**Columns**: Key, Summary, Assignee, Updated

**Why**: Waves not touched in 14 days. Likely stuck or abandoned. Wave Captain action needed.

---

### Gadget 3 — Issue Statistics: PAs by Quality Rating

**Type**: Issue Statistics (Two Dimensional Filter Statistics works too)
**JQL**:
```jql
project = DPOAF AND labels = "prompt-action"
```
**Statistic Type**: Labels (filter for `quality-X` labels)

**Why**: Distribution of prompt quality. Lots of 1-2? Refinement needed. Lots of 4-5? Add to Reusable Library.

---

### Gadget 4 — Recently Created: Last 10 D-POAF issues

**Type**: Activity Stream
**Filter**: Project = DPOAF
**Max items**: 10

**Why**: What's new in the project. Useful for daily standup or async team awareness.

---

### Gadget 5 — Two-Dimensional Filter Statistics: PAs by Wave × Macro-Phase

**Type**: Two Dimensional Filter Statistics
**JQL**:
```jql
project = DPOAF AND labels = "prompt-action"
```
**X-Axis**: Epic Link (which Wave)
**Y-Axis**: Labels containing "macro-"

**Why**: Heatmap of AI work per Wave per macro-phase. Identifies which Waves are AI-heavy and where in their lifecycle.

---

### Gadget 6 — Filter Results: DL-006 Compliance Violations

**Type**: Filter Results
**JQL**:
```jql
project = DPOAF AND labels = "prompt-action" AND labels != "traceability-thread-complete"
```
**Columns**: Key, Summary, Assignee, Created

**Why**: Prompt Actions missing the mandatory Traceability Thread (Model + Config + Context). Each row is a governance violation.

---

## Optional bonus gadgets

### Gadget 7 — Pie: Wave Profile distribution

```jql
project = DPOAF AND labels = "wave"
```
Statistic: Labels containing "deliver-wave", "decide-wave", etc.

### Gadget 8 — Resolution Time chart

Time to close Waves (from creation to Done). Look for outliers.

### Gadget 9 — Heatmap: Active Waves per Captain

Who's overloaded? Who's free for new work?

### Gadget 10 — Sprint Report

For each sprint, see what D-POAF work was completed.

---

## Tips

- **Refresh interval**: set to 15 minutes for live data without overloading Jira
- **Share dashboard URL** with the team in Slack/email — instant control room access
- **Add screenshots to the Wave Captain handbook** to onboard new Captains
- **Iterate**: after 2-3 sprints, you'll know which gadgets are useful. Drop the rest.

---

## ✅ Done

You now have a D-POAF® Control Room dashboard. Open it daily.

---

D-POAF® Framework v1.1 — d-poaf.org — Licensed under CC BY 4.0
