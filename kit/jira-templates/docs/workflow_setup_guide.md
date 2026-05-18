# 📊 D-POAF® Jira — Board Workflow Setup (Macro-Phase Columns)

> Configure your Jira board so columns = D-POAF macro-phases. ~5 minutes, no admin needed for team-managed projects.

---

## The goal

Instead of generic columns **"À faire / En cours / Terminé"**, your board should look like this:

```
┌──────────────────┬──────────────────┬──────────────────┬──────────────────┬───────────┐
│ 1. Instruct      │ 2. Shape         │ 3. Execute       │ 4. Learn         │ ✅ Closed │
│    & Scope       │    & Align       │    & Evolve      │    & Adapt       │           │
├──────────────────┼──────────────────┼──────────────────┼──────────────────┼───────────┤
│                  │                  │                  │                  │           │
│  [new Wave]      │  [Wave in        │  [WAVE-EX-001]   │  [Wave in        │ [closed]  │
│                  │   scoping]       │                  │   retro]         │           │
│                  │                  │  [Wave shipping] │                  │           │
└──────────────────┴──────────────────┴──────────────────┴──────────────────┴───────────┘
```

Drag-and-drop a Wave to advance it through the macro-phases. Instant visual control.

---

## Method A — Team-managed Scrum project (easy, no admin)

1. Open your **D-POAF® Governance** project
2. Click the **Board** view (left sidebar, or the icon ⊞)
3. Click **Project settings** (bottom of left sidebar)
4. Choose **Board** (or **Columns**)
5. **Add column** → name it `1. Instruct & Scope`
6. Repeat for the 3 other macro-phases:
   - `2. Shape & Align`
   - `3. Execute & Evolve`
   - `4. Learn & Adapt`
7. Keep `Done` as the final column (auto-created)
8. **Reorder** the columns so they appear in macro-phase order
9. **Delete the default** `À faire / En cours` columns (or rename them if you prefer to keep their status IDs)
10. Save

⚠️ Note: in team-managed Scrum, each column = a status. When you create the column, Jira creates the matching status. Your Wave issues need to be moved to this status to appear in the column.

To move them in bulk:
1. Open the **Liste** view
2. Filter by `labels = "wave"` (your existing Waves)
3. Select all → **Edit status** → choose `3. Execute & Evolve` for WAVE-EXAMPLE-001

The Wave now appears in the corresponding column.

---

## Method B — Company-managed Scrum project (advanced)

For company-managed projects, you customize the workflow:

1. **Project settings** → **Workflows**
2. **Edit** the default workflow
3. **Add status** → name it after each macro-phase (4 statuses)
4. **Configure transitions** between statuses (typically: linear forward, plus "rollback" transition from any to phase 1)
5. **Add resolution screen** for the transition to Done
6. Save and publish the workflow
7. **Board settings** → **Columns** → map each status to a column

This is more powerful (custom transition logic, validators, post-functions) but requires Jira admin permission.

---

## Optional — Sub-phase as Components or Labels

If you want even finer granularity (the 7 sub-phases), use Jira **Components** or keep labels:

**Option 1 — Components**
- Project settings → Components → Create 7 components matching the 7 Sub-Phases
- Assign each issue to the relevant Component
- Filter by Component on the board

**Option 2 — Labels (no admin)** — this is what the build script does
- Each issue has `phase-1` to `phase-7` label
- Filter the board view: JQL `labels = "phase-4"`

---

## Optional — Color-code your columns

Make the macro-phase columns visually distinct:

| Column | Suggested color | Match canonical |
|---|---|---|
| 1. Instruct & Scope | **Blue** | ✅ |
| 2. Shape & Align | **Yellow** | ✅ |
| 3. Execute & Evolve | **Purple** | ✅ |
| 4. Learn & Adapt | **Green** | ✅ |
| Done | Grey | (closed) |

Some Jira versions allow column color via Board settings → Columns. If not available, the label colors propagate visually.

---

## Bonus — Group your board by Epic

When you want to see all the Prompt Actions (Tasks) under a Wave (Epic):

1. On the board, click the dropdown **Group by** (or the gear icon → Group)
2. Choose **Epic**
3. The board now groups Tasks under their parent Wave

This gives you a **Wave-centric Kanban** where each row is a Wave and each card is a PA.

---

## ✅ Validation

After setting up the workflow:

1. Open the board
2. You should see 4 macro-phase columns + Done
3. WAVE-EXAMPLE-001 appears in **3. Execute & Evolve** (its current macro-phase)
4. New Waves can be created starting in **1. Instruct & Scope**
5. Drag-and-drop a Wave to advance it through phases

---

## 🆘 Troubleshooting

**Issue: Column doesn't appear after creation**
- Make sure you saved Board settings
- Refresh the page

**Issue: Can't drag issues between columns**
- Check the workflow transitions are configured to allow the move
- In team-managed projects, transitions are usually auto-permitted

**Issue: Wave appears in wrong column**
- Open the Wave issue
- Check its current status
- Update status to the matching macro-phase

---

D-POAF® Framework v1.1 — d-poaf.org — Licensed under CC BY 4.0
