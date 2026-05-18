# 🔗 D-POAF® Jira — JQL Filters for Outcome → Intent Traceability

> Use these **5 JQL filters** to walk the D-POAF traceability chain entirely from Jira UI, without scripts.

JQL doesn't support runtime variables, but the patterns below let you trace any outcome back to business intent in **3 clicks** or by editing a single value in the filter.

---

## Filter 1 — Universal Outcome Search (the swiss army knife)

**Use when:** You have a commit hash, file name, keyword, or PA-ID and want to find the matching Jira issue.

**JQL:**
```jql
project = DPOAF AND text ~ "REPLACE_WITH_OUTCOME"
ORDER BY issuetype, key
```

**Procedure (5 seconds):**
1. Open the filter
2. Click **Modifier le JQL**
3. Replace `REPLACE_WITH_OUTCOME` with your search term (e.g., `PA-001`, `abc123de`, `sentiment classifier`)
4. **Exécuter**
5. Jira returns all matching issues — typically the PA or Wave you're looking for

**How `text ~` works:** Jira's `text` operator searches across summary, description, comments, and environment fields all at once. It's the universal full-text search.

---

## Filter 2 — Full Chain for [Wave]

**Use when:** You know the Wave-ID and want the complete chain (Wave + all PAs + all Proofs).

**JQL:**
```jql
project = DPOAF AND (key = "DPOAF-1" OR parent = "DPOAF-1")
ORDER BY issuetype DESC, created ASC
```

**Procedure:**
1. Open the filter
2. To trace a different Wave: click **Modifier le JQL**, replace `DPOAF-1` with the target Wave-ID
3. **Exécuter**
4. You see: 1 Wave Epic + all linked PAs + all linked Proofs in one list

---

## Filter 3 — Latest Active Wave (and its chain)

**Use when:** You want to instantly see what the team is currently working on.

**JQL:**
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" 
AND status != Done 
ORDER BY updated DESC
```

Combined with Filter 2 (after you copy the latest Wave key), you get the current activity.

---

## Filter 4 — Reverse Trace from PA to Wave

**Use when:** You found the PA from Filter 1, and now want to "walk up" to the Wave.

**JQL:**
```jql
key in (parentEpic("DPOAF-2"))
```

Where `DPOAF-2` is the PA-ID. The `parentEpic()` JQL function returns the Epic of any issue.

⚠️ **Note:** `parentEpic()` works on Company-managed projects. On Team-managed Scrum, use:
```jql
key = parent("DPOAF-2")
```

---

## Filter 5 — Audit Trail (everything for compliance review)

**Use when:** External auditor or quarterly review.

**JQL:**
```jql
project = DPOAF AND labels in ("wave", "prompt-action", "proof-record")
ORDER BY labels ASC, created DESC
```

Returns every D-POAF object in the project, grouped by category. Use this for audit reports.

---

## 🎯 The 3-click navigation pattern (no filter needed)

Jira has a built-in "issue hierarchy" view. The most natural way to walk the chain:

1. **Click 1** — Type the outcome in the Jira top search bar → click the matching PA
2. **Click 2** — On the PA page, find the **Epic Link** field → click the Wave key
3. **Click 3** — On the Wave Epic page, see all child issues (PAs + Proofs) in the **Child Issues** panel

Time: ~15 seconds.

This is **faster than any filter** because Jira does the hierarchy walk natively.

---

## 💡 Tips for filter usage

**Save your edited filter as a new one** — If you customize Filter 1 or Filter 2 for a specific outcome/Wave, save it as a new filter:
1. After editing the JQL → click **Enregistrer sous** (Save as)
2. Name: `D-POAF - Chain for WAVE-2026-007` (or similar)
3. Now you have a permanent filter for that specific Wave

**Star your favorites** — In the Filters page, star each new filter so it appears in the sidebar quick access.

**Share filters with the team** — Edit filter → Settings → Permissions → choose "Project: D-POAF" or "Any logged-in user"

---

D-POAF® Framework v1.1 — d-poaf.org — Licensed under CC BY 4.0
