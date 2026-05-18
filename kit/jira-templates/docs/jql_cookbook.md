# 📋 D-POAF® JQL Cookbook — 15 ready-to-use queries

> Paste any of these JQL (Jira Query Language) queries into Jira's search bar to filter your D-POAF® work.

All queries assume:
- Your project key is **DPOAF** (replace if different)
- The label taxonomy from this kit is in use

---

## 🌊 Wave queries

### 1. All active Waves
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" AND status != Done
```
**Use case**: Daily Wave Captain check-in. Shows every Wave still in flight.

### 2. Waves in Execute & Evolve (macro-phase 3)
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" AND labels = "macro-3" AND status != Done
```
**Use case**: "What are we actively building right now?"

### 3. Stale Waves (not updated in 14 days)
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" AND status != Done AND updated <= -14d
```
**Use case**: Identify Waves that may be stuck or abandoned.

### 4. Closed Waves this quarter
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" AND status = Done AND updated >= startOfQuarter()
```
**Use case**: Quarterly retrospective: which Waves shipped?

### 5. Waves by Profile (e.g., Deliver Wave)
```jql
project = DPOAF AND labels = "wave" AND labels = "deliver-wave"
```
**Use case**: Filter by Wave Profile (Deliver / Decide / Control / Delegate / Operate Wave).

---

## 🤖 Prompt Action queries

### 6. All Prompt Actions for a specific Wave
```jql
project = DPOAF AND labels = "prompt-action" AND "Epic Link" = WAVE-EXAMPLE-001
```
**Use case**: Audit every AI invocation that contributed to a specific Wave.

### 7. Reusable prompts (high-quality, approved)
```jql
project = DPOAF AND labels = "prompt-action" AND labels = "reusable-prompt"
```
**Use case**: Browse the team's Reusable Prompt Library.

### 8. Prompt Actions missing Traceability Thread (DL-006 violation!)
```jql
project = DPOAF AND labels = "prompt-action" AND labels != "traceability-thread-complete"
```
**Use case**: Compliance audit. Per Dynamic Law DL-006, every PA MUST have Model + Config + Context filled.

### 9. Low-quality prompts to refine
```jql
project = DPOAF AND labels = "prompt-action" AND (labels = "quality-1" OR labels = "quality-2")
```
**Use case**: Prompts rated 1-2 must be refined before reuse (per DL-007).

### 10. Prompt Actions in design phase
```jql
project = DPOAF AND labels = "prompt-action" AND labels = "phase-3"
```
**Use case**: PAs currently being designed (Sub-Phase 3 - Design Prompt Actions).

---

## ✅ Proof Record queries

### 11. Recent Proof Records (last 30 days)
```jql
project = DPOAF AND labels = "proof-record" AND created >= -30d
```
**Use case**: Activity dashboard — what closures happened recently.

### 12. Approved Proofs (PoD + PoV)
```jql
project = DPOAF AND labels = "proof-record" AND labels = "pod-approved" AND labels = "pov-approved"
```
**Use case**: Browse successful Wave closures.

### 13. Proofs with partial or failed validations
```jql
project = DPOAF AND labels = "proof-record" AND (labels = "pod-partial" OR labels = "pod-not-met" OR labels = "pov-partial" OR labels = "pov-not-met")
```
**Use case**: Lessons-learned source — Proofs that didn't fully meet criteria.

---

## 🔍 Compliance & governance queries

### 14. Anti-pattern: Tasks without D-POAF labels (untracked AI work?)
```jql
project = DPOAF AND issuetype = Task AND (labels is EMPTY OR labels != "d-poaf")
```
**Use case**: Detect issues created without D-POAF labeling — possible governance leak.

### 15. Wave Captain dashboard — my Waves
```jql
project = DPOAF AND labels = "wave" AND assignee = currentUser() AND status != Done
```
**Use case**: Each Wave Captain's personal control room.

---

## 🎨 Bonus — Custom field queries (admin upgrade)

Once you create the custom fields (see `custom_fields_setup.md`), you can run more precise queries:

### Bonus 1. Prompt Actions for a specific model
```jql
project = DPOAF AND "Model Identity" ~ "claude-sonnet"
```

### Bonus 2. High-quality reusable prompts
```jql
project = DPOAF AND "Quality Rating" >= 4 AND labels = "reusable-prompt"
```

### Bonus 3. Waves in a specific macro-phase
```jql
project = DPOAF AND "Macro-Phase" = "3. Execute & Evolve" AND status != Done
```

---

## 💡 Tips for using JQL

- **Save your queries as filters** for one-click reuse: Search → Save as → name it (e.g., "Active Waves")
- **Subscribe to filters** to get email alerts: Filters → Subscribe → frequency
- **Share filters** with your team via the filter's permission settings
- **Use saved filters in dashboards** (see `dashboard_setup.md`)

---

## 🔗 Related

- `manual_setup_guide.md` — How to set up your D-POAF Jira project
- `custom_fields_setup.md` — Admin upgrade path with custom fields
- `dashboard_setup.md` — Configure a D-POAF control room dashboard

---

D-POAF® Framework v1.1 — d-poaf.org — Licensed under CC BY 4.0
