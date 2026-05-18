# 🔗 D-POAF® Jira — GitHub Integration Setup

> Connect your Jira project to GitHub so that each PA issue auto-displays linked commits, branches, and PRs. ~10 minutes.

---

## What this gives you

After integration, each Prompt Action issue shows:
- ✅ **Commits** that mention the issue key in their message
- ✅ **Branches** named after the issue key (e.g., `feature/DPOAF-7`)
- ✅ **Pull Requests** that reference the issue
- ✅ **Status of PRs** (open / merged / closed)

This is the **forward direction** of the traceability chain:
```
Wave Epic → Prompt Action → Branch → Commit → PR → Merged code
```

---

## Step 1 — Install the GitHub for Jira app

1. In Jira, top right gear icon → **Apps** (or **Atlassian Marketplace**)
2. Search for **GitHub for Jira**
3. Click **Try it free** (the app is free for Jira Cloud)
4. Confirm installation

The app needs:
- Permission to read your Jira issues
- A GitHub account with admin access to your repository

---

## Step 2 — Authorize GitHub

1. After installation, you're redirected to a setup wizard
2. Click **Connect GitHub account**
3. Sign in to GitHub
4. Choose: **Install GitHub for Jira for** → select your organization (`INOVIONIX`) or personal account
5. Choose repos:
   - **All repositories** (if you want all Inovionix repos linked)
   - **Only select repositories** → pick your D-POAF repo (e.g., `INOVIONIX/D-POAF`)
6. Click **Install** in GitHub

---

## Step 3 — Wait for backfill

GitHub for Jira will index your repos and find existing references. This takes 5-15 minutes for large repos.

You can check status: Jira → Apps → GitHub → Configuration → status should say "Connected, indexing complete".

---

## Step 4 — Test the integration

### Test A — Create a branch named after a Jira issue

In your terminal:
```bash
git checkout -b feature/DPOAF-7-add-classifier
```

Then in Jira, open issue DPOAF-7 (your PA-001 Task). After 1-2 minutes, you should see a **Development panel** on the right side showing:
- 1 branch: `feature/DPOAF-7-add-classifier`

### Test B — Commit referencing the issue

```bash
git commit -m "DPOAF-7: Implement sentiment classifier [AI:claude-sonnet-4-5:PA-001]"
git push origin feature/DPOAF-7-add-classifier
```

In Jira, DPOAF-7 should now show:
- 1 commit
- The commit message (with the D-POAF tag visible)

### Test C — Open a Pull Request

Open a PR on GitHub. Title: `DPOAF-7: Add sentiment classifier function`

In Jira, DPOAF-7 should show:
- 1 PR (open)
- Author, target branch, status

When you merge the PR, Jira auto-updates the status to "merged" and (optionally) transitions the issue to Done.

---

## Step 5 — Recommended commit message convention for D-POAF

Standardize your commit messages to maximize traceability:

```
DPOAF-7: <imperative description of what changed> [AI:<model>:<PA-ID>]

<longer optional description>

Closes: DPOAF-1 (Wave)
```

Example:
```
DPOAF-7: Implement 6-category sentiment classifier [AI:claude-sonnet-4-5:PA-001]

Implements the classify_feedback function using prompt PA-001 with Claude 
Sonnet 4.5. Coverage report attached. Test suite passes 100%.

Closes: DPOAF-1
```

This commit:
- ✅ Links to PA issue (DPOAF-7) via `DPOAF-7:` prefix
- ✅ Tags AI authorship per DL-005 with `[AI:claude-sonnet-4-5:PA-001]`
- ✅ Closes the parent Wave Epic via `Closes: DPOAF-1`

---

## Step 6 — Set up auto-transitions (optional)

You can configure GitHub for Jira to auto-transition issues based on PR events:

1. Jira → Apps → GitHub for Jira → Configuration → **Workflow automation**
2. Configure rules:
   - When PR opened → move issue to **3. Execute & Evolve**
   - When PR merged → move issue to **4. Learn & Adapt** or **Done**
   - When PR closed without merge → add label `pr-rejected`

This automates the macro-phase progression based on Git activity.

---

## Step 7 — Add Development data to your Jira board

Make commits/branches visible on the board:

1. Open your D-POAF® Governance project board
2. **Board settings** → **Card layout**
3. Add field: **Development**
4. Save

Now each card shows a small icon with branch/commit/PR counts. Click for details.

---

## Optional — GitLab / Bitbucket / Azure DevOps

Same principle, different apps:
- **GitLab for Jira** — official app, free
- **Bitbucket** — natively integrated if you're on Atlassian
- **Azure DevOps for Jira** — Microsoft official integration

All work with the same `ISSUE-KEY: message` convention.

---

## ✅ Verification checklist

After setup, you should see on each PA issue:

- [ ] Development panel on the right side
- [ ] Linked branches (if any)
- [ ] Linked commits (with the AI tag visible)
- [ ] Linked PRs (with status)
- [ ] Auto-transitions if configured

If yes — the **forward direction** of the traceability chain is working. Combined with the **reverse direction** (git blame → AI tag → PA → Wave), you now have full bidirectional traceability.

---

## 🔗 Related

- `manual_setup_guide.md` — How to set up the D-POAF Jira project structure
- `jql_cookbook.md` — JQL queries that leverage the Development data
- `workflow_setup_guide.md` — Configure board columns for macro-phases

---

D-POAF® Framework v1.1 — d-poaf.org — Licensed under CC BY 4.0
