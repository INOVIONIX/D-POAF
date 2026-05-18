# 🛠 D-POAF® Jira Install Kit — v2.0 FINAL

> **Bring D-POAF® governance to your Jira project in 15 minutes.** A single Python script + ~10 minutes of UI configuration.

D-POAF® (Decentralized Proof-Oriented AI Framework) is a free, open-source framework for traceable governance of AI-enabled software delivery. This kit configures a Jira Software project to track Waves, Prompt Actions, Proof Records, and Dynamic Laws — with full outcome-to-intent traceability.

---

## 📦 What's in this kit

```
DPOAF_Jira_Install_Kit_v1.0/
├── README.md                              (this file — read first)
├── LICENSE.txt                             (CC BY 4.0)
├── install_dpoaf_jira.py                   (THE all-in-one installer)
├── config/
│   └── labels_taxonomy.json                (D-POAF label taxonomy)
└── docs/
    ├── manual_setup_guide.md              (alternative if you don't run scripts)
    ├── custom_fields_setup.md             (admin upgrade path)
    ├── jql_cookbook.md                    (15 JQL queries)
    ├── dashboard_setup.md                 (dashboard config)
    ├── workflow_setup_guide.md            (board columns macro-phases)
    ├── github_integration_setup.md        (GitHub for Jira)
    └── traceability_jql_filters.md        (outcome -> intent chain)
```

A single Python script (`install_dpoaf_jira.py`) does 90% of the setup. The remaining 10% requires UI configuration (Atlassian API limitations).

---

## 🚀 Quick start (15 minutes total)

### Prerequisites

1. **Jira Cloud account** with project admin permission
2. **Atlassian API token** — generate at https://id.atlassian.com/manage-profile/security/api-tokens
3. **Python 3.7+** installed
4. **Empty Jira project** with key `DPOAF` (or any other) — create manually first (see Step 1)

### Step 1 — Create the Jira project manually (1 min)

The Jira REST API requires the project to exist first.

1. In Jira Cloud, click **+ Create** → **Project**
2. Template: **Scrum**
3. Type: **Team-managed** (recommended) or **Company-managed**
4. Project name: `D-POAF® Governance`
5. Project key: `DPOAF`
6. Lead: yourself
7. **Create**

### Step 2 — Run the installer (3 min)

In a terminal (PowerShell on Windows, Terminal on macOS/Linux):

```powershell
# Set credentials
$env:JIRA_URL = "https://yoursite.atlassian.net"
$env:JIRA_EMAIL = "your.email@example.com"
$env:JIRA_TOKEN = "ATATT3xFfGF0..."
$env:JIRA_PROJECT_KEY = "DPOAF"

# Run the installer
python install_dpoaf_jira.py
```

The script will:
- ✅ Create 1 Wave Epic + 5 Prompt Actions + 2 Proof Records
- ✅ Create 15 Dynamic Laws as tracked issues
- ✅ Create a sprint and add Wave/PAs/Proofs to it
- ✅ Try to start the sprint
- ✅ Create 9 saved JQL filters
- ✅ Create the "D-POAF Control Room" dashboard
- ✅ Add 4 colored gadgets to the dashboard

Output at the end will list any remaining manual steps.

### Step 3 — Complete the 5 manual steps below (~10 min)

These cannot be automated — Atlassian API doesn't expose them.

---

## 🔧 Manual steps after script (mandatory)

### Manual Step A — Board: rename columns to macro-phases (5 min)

The default Jira board has 3 columns (À faire / En cours / Terminé). Replace them with the 4 D-POAF macro-phases.

1. Open the board: `https://yoursite.atlassian.net/jira/software/projects/DPOAF/board`
2. Click the gear icon → **Paramètres du projet** → **Tableau** → **Colonnes**
3. Configure the columns:
   - `1. Instruct & Scope` (rename "À faire" or add)
   - `2. Shape & Align` (add)
   - `3. Execute & Evolve` (rename "En cours" or add)
   - `4. Learn & Adapt` (add)
   - `Done` (keep as final)
4. Save

**Move tickets to their correct column:**
- WAVE-EXAMPLE-001 → `3. Execute & Evolve` (Sub-Phase = 4)
- PA-001 → `2. Shape & Align` (Sub-Phase = 3)
- PA-002, PA-003, PA-004 → `3. Execute & Evolve`
- PA-005 → `4. Learn & Adapt`
- PROOF-001, PROOF-002 → `4. Learn & Adapt`

Drag-and-drop in the board view, or click each ticket and change its status.

### Manual Step B — Star the filters to add them to favorites (1 min)

Filters created by the API are not automatically starred. Star them to make them appear in the sidebar.

1. Open the filters list: `https://yoursite.atlassian.net/jira/filters`
2. Search `D-POAF` in the search box at the top
3. You'll see 9 D-POAF filters in the results
4. Click the **star (⭐)** next to each one
5. Refresh the page — the filters now appear in the sidebar under **Filtres → Favoris**

The 9 D-POAF filters:
- ⭐ D-POAF - Active Waves
- ⭐ D-POAF - PromptRegister (all PAs)
- ⭐ D-POAF - Reusable Prompt Library
- ⭐ D-POAF - DL-006 Compliance Violations
- ⭐ D-POAF - Dynamic Laws (governance baseline)
- ⭐ D-POAF - Proof Records
- ⭐ D-POAF - Stale Waves
- ⭐ D-POAF - Universal Outcome Search ← THE traceability filter
- ⭐ D-POAF - Full chain for [Wave]

### Manual Step C — Start the sprint manually if auto-start failed (30 sec)

The script tries to start the sprint, but the API can be capricious. If the script reports `auto-start failed`:

1. Open the Backlog: `https://yoursite.atlassian.net/jira/software/projects/DPOAF/backlog`
2. Find `D-POAF Sprint 1 - YYYY-MM-DD`
3. Click **Démarrer un sprint** (Start sprint)
4. Confirm duration (default 2 weeks) and goal
5. **Démarrer**

Once started, the board shows the sprint tickets in their correct columns.

### Manual Step D — Configure the 4 dashboard gadgets (2 min)

The dashboard exists and has 4 colored gadgets, but each needs a filter selection.

1. Open the dashboard: `https://yoursite.atlassian.net/jira/dashboards/<id>`
2. For each gadget, click the **gear icon (⚙)** in the gadget
3. Select the matching **Saved Filter**:

| Gadget position | Color | Filter to select |
|---|---|---|
| Top-left | 🔵 Blue | `D-POAF - Active Waves` |
| Top-right | 🔴 Red | `D-POAF - DL-006 Compliance Violations` |
| Bottom-left | 🟣 Purple | `D-POAF - PromptRegister (all PAs)` |
| Bottom-right | 🟢 Green | `D-POAF - Reusable Prompt Library` |

For each gadget:
- **Saved Filter** → pick from dropdown
- **Number of results** → 10
- **Columns to display** → Key, Summary, Status, Updated
- **Refresh interval** → 15 minutes
- **Save**

Then click the **star (⭐)** at the top of the dashboard to add it to your favorites.

### Manual Step E — How to use the traceability chain (read once, use forever)

This is **the** killer feature of D-POAF. Here's how to walk from any outcome back to business intent.

**Scenario:** You found a commit `[AI:claude-sonnet-4-5:PA-001]` and want to know why this code exists.

**Method 1 — Native Jira navigation (3 clicks, 15 seconds)**

1. **Click 1**: In the Jira search bar (top), type `PA-001` → click the matching PA result
2. **Click 2**: On the PA page (DPOAF-2), look at the right panel → click **Epic Link** value
3. **Click 3**: You're on the Wave Epic page → see all child PAs + Proofs + Business Objective

That's it. The chain is walked.

**Method 2 — Universal Outcome Search filter (5 seconds to edit JQL)**

Use this when you have a less specific outcome (commit hash, keyword, etc.).

1. Open the filter **D-POAF - Universal Outcome Search**
2. Click **Modifier le JQL** (Edit JQL)
3. Replace `REPLACE_WITH_OUTCOME` with your outcome:
   - `PA-001` (PA-ID)
   - `abc123de` (commit hash)
   - `sentiment classifier` (keyword)
   - `claude-sonnet-4-5` (model name)
   - `WAVE-EXAMPLE-001` (Wave-ID)
4. **Exécuter** (Run)
5. Click the matching issue → navigate from there

The `text ~` JQL operator searches across summary, description, comments — everything text-based — at once.

**Method 3 — Full chain for one Wave (edit Wave key in JQL)**

When you know which Wave you want, this filter shows the **complete chain in one view**: Wave Epic + all PAs + all Proofs.

1. Open the filter **D-POAF - Full chain for [Wave]**
2. Click **Modifier le JQL**
3. Replace the Wave key (e.g., `DPOAF-1`) with your target Wave key (e.g., `DPOAF-25`)
4. **Exécuter**
5. See the complete chain in one list, ready for audit/review

---

## 🗺️ D-POAF → Jira mapping

| D-POAF concept | Jira mapping | Detail |
|---|---|---|
| **Wave** | Epic | Container, lives across sprints |
| **Prompt Action** | Task | Linked to a Wave Epic via "Epic Link" |
| **Proof Record** | Task (child of Epic) | Wave closure with PoD/PoV/PoR |
| **Dynamic Law** | Task with label "dynamic-law" | Reference, not active work |
| **Sub-Phase 1-7** | Label `phase-X` | Granular phase tracking |
| **Macro-Phase 1-4** | Label `macro-X` + Board column | Visual via board columns |
| **Traceability Thread** | Description (rich text) + labels | Model + Config + Context |
| **Quality Rating 1-5** | Label `quality-X` | DL-007 compliance |

---

## 📋 The label taxonomy

The kit uses ~40 labels organized in 9 categories. See `config/labels_taxonomy.json` for the full list.

**Key compliance labels** (filterable via JQL):

- `d-poaf` — global filter (every D-POAF issue)
- `wave` / `prompt-action` / `proof-record` / `dynamic-law` — issue category
- `macro-1` / `macro-2` / `macro-3` / `macro-4` — lifecycle macro-phase
- `phase-1` to `phase-7` — granular sub-phase
- `quality-1` to `quality-5` — PA quality rating
- `reusable-prompt` — added to Reusable Library
- `traceability-thread-complete` — DL-006 compliant
- `pod-approved` / `pod-partial` / `pod-not-met` — PoD status
- `pov-approved` / `pov-partial` / `pov-not-met` — PoV status
- `por-approved` / `por-na` — PoR status

---

## 📊 The JQL Cookbook (top 15 queries)

See `docs/jql_cookbook.md` for the full cookbook. Top 5:

**Active Waves in Execute & Evolve**:
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" AND labels = "macro-3" AND status != Done
```

**DL-006 Compliance Violations**:
```jql
project = DPOAF AND labels = "prompt-action" AND labels != "traceability-thread-complete"
```

**Reusable Prompt Library**:
```jql
project = DPOAF AND labels = "prompt-action" AND labels = "reusable-prompt"
```

**Stale Waves (14+ days inactive)**:
```jql
project = DPOAF AND issuetype = Epic AND labels = "wave" AND status != Done AND updated <= -14d
```

**Full chain for a specific Wave**:
```jql
project = DPOAF AND (key = "DPOAF-1" OR parent = "DPOAF-1") ORDER BY issuetype DESC
```

---

## 🔧 Optional: Upgrade to custom fields (Jira admin)

The default install uses labels (no admin needed). For richer typed data, upgrade to custom fields:

- PA-ID (text)
- Macro-Phase (Select list, 4 values)
- Sub-Phase (Select list, 7 values)
- Model Identity (text)
- Model Configuration (paragraph)
- Context Source (paragraph)
- Quality Rating (number 1-5)

See `docs/custom_fields_setup.md` for the full procedure (requires Jira admin permission).

---

## 🔗 Optional: GitHub integration (10 min)

Connect Jira to your GitHub repo so each PA shows its linked commits/branches/PRs:

1. Install the **GitHub for Jira** app (Marketplace, free)
2. Authorize your GitHub org/repo
3. Adopt the commit convention: `DPOAF-7: <message> [AI:claude:PA-001]`
4. Jira auto-displays linked commits on each PA

See `docs/github_integration_setup.md` for the full setup.

---

## 🆘 Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `HTTP 401 Unauthorized` | Wrong email or API token | Regenerate token at id.atlassian.com |
| `HTTP 403 Forbidden` | Not project admin | Ask Jira admin to grant permission |
| `HTTP 404 Project not found` | Wrong project key | Verify project key (case-sensitive) |
| `HTTP 410 Gone on /search` | API deprecated | Update to script v2.0 (uses /search/jql) |
| Dashboard gadget filter not bound | API limitation | Configure manually (see Step D) |
| Sprint not started | API edge case | Start manually (see Step C) |
| Filters not in sidebar | Not starred | Star them (see Step B) |

---

## 🌐 D-POAF® ecosystem

D-POAF® is available across multiple platforms:

- 🐘 **Confluence** — Documentation governance (`DPOAF_Confluence_Install_Kit`)
- 📋 **Notion** — All-in-one workspace (https://www.notion.so/@dpoaf)
- 🛠 **Jira** — Issue tracking (this kit)
- 🐙 **GitHub** — Issue forms + PR templates + starter repo
- 📊 **Excel** — PromptRegister.xlsx for prompt management

**Recommended combo**: Confluence (docs) + Jira (execution) + GitHub (code) — full traceability stack.

---

## 🔗 Resources

- 🌐 **Framework reference**: https://d-poaf.org
- 🐙 **GitHub starter repo**: https://github.com/INOVIONIX/D-POAF
- 📦 **All install kits**: https://d-poaf.org/kits
- 📖 **Canonical Specification v1.1**: https://d-poaf.org
- 💬 **Community Discord**: https://discord.gg/DMZMeHxzNd

---

## 📜 License

Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use, modify, and distribute with attribution.

D-POAF® is a registered trademark of Inovionix.

© 2025–2026 Azzeddine IHSINE & Sara IHSINE — d-poaf.org

---

## 📊 Version

**v2.0 — May 2026 (FINAL)**
- Single all-in-one installer (`install_dpoaf_jira.py`) replaces the 5 previous scripts
- 9 JQL filters (added Universal Outcome Search + Full chain for [Wave])
- Improved error handling (full error body on failure)
- Idempotent (safe to re-run)
- Bilingual gadget discovery (FR + EN)
- Comprehensive manual-steps documentation

**Previous versions:**
- v1.3 / v1.4 / v1.5 — Iterative fixes (deprecated)
- v1.2 — Sprint + filters + dashboard
- v1.1 — XML bundle + Build Guide
- v1.0 — MVP

---

**Made by Sara IHSINE & Azzeddine IHSINE / Inovionix.**
