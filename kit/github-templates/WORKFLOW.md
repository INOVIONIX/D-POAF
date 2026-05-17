# 📖 D-POAF® - Workflow Guide

A practical walkthrough of how a real engineering team uses the D-POAF® Starter Kit on GitHub — from `git clone` to a closed Wave with full Traceability Thread.

> 🎯 Read this once. Pin it. Refer back to it during your first 2-3 Waves until it becomes muscle memory.

---

## 📑 Quick navigation

- [TL;DR — the loop in 60 seconds](#tldr--the-loop-in-60-seconds)
- [Day 0 — Install](#day-0--install)
- [Day 1 — Open a Wave](#day-1--open-a-wave)
- [Days 2-N — Log every Prompt Action](#days-2-n--log-every-prompt-action)
- [Day N — Close the Wave](#day-n--close-the-wave)
- [6 months later — Trace back an artifact](#6-months-later--trace-back-an-artifact)
- [Pro tips](#pro-tips)
- [FAQ](#faq)
- [Glossary](#glossary)

---

## TL;DR — the loop in 60 seconds

```
  Open Wave Scope (issue)
            │
            ▼
  ┌──────────────────────────────┐
  │ For each AI generation:      │
  │  1. Open Prompt Action issue │
  │  2. Log model + config + ctx │
  │  3. Invoke AI                │
  │  4. Update PA with output    │
  │  5. Commit with [AI:m:PA-ID] │
  │  6. Open PR — checklist auto │
  └──────────────────────────────┘
            │
            ▼
  Close with Proof Record (issue)
            │
            ▼
  Wave Scope issue closed
  Audit chain preserved forever
```

That's the entire D-POAF® loop. Everything below is detail.

---

## Day 0 — Install

You have two ways to bring D-POAF® into your repo. Pick one.

### Path A — Brand new project (recommended)

1. Go to [github.com/INOVIONIX/dpoaf-starter-repo](https://github.com/INOVIONIX/dpoaf-starter-repo)
2. Click the green **"Use this template" → "Create a new repository"**
3. Name it, set visibility, click **"Create repository from template"**

Done. Your new repo has D-POAF® governance active.

### Path B — Existing project

```bash
cd your-existing-project
npx degit INOVIONIX/dpoaf-starter-repo/.github .github
git add .github
git commit -m "feat: install D-POAF® governance templates"
git push
```

### What just got installed

```
your-repo/
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── config.yml                 # Disable blank issues + link to docs
    │   ├── wave-scope.yml             # 🌊 Open a Wave
    │   ├── prompt-action.yml          # 🤖 Log an AI invocation
    │   └── proof-record.yml           # ✅ Close a Wave
    └── PULL_REQUEST_TEMPLATE.md       # PR checklist enforcing Dynamic Laws
```

### Recommended labels (1 minute)

Go to **Issues → Labels** on your repo and create these:

| Label | Color | Description |
|---|---|---|
| `dpoaf:wave` | `#0E2148` | Wave Scope issues |
| `dpoaf:prompt-action` | `#13B5D8` | Prompt Action issues |
| `dpoaf:proof-record` | `#16A34A` | Proof Record issues |
| `ai-generated` | `#7C7DFF` | Any AI-touched PR or issue |

You'll use these to filter your board: `is:issue label:dpoaf:wave is:open` → all active Waves.

### Recommended GitHub Project board (5 minutes)

Create a Project on your repo with these columns:

```
[ Backlog Waves ] → [ Active ] → [ Validating ] → [ Closed ]
```

Filter by label `dpoaf:wave`. You now have a visual board of every Wave in your org — perfect for daily stand-ups.

---

## Day 1 — Open a Wave

A **Wave** is a governed unit of AI-enabled work. Think of it as a smart sprint: it tracks what was done, why, how the AI contributed, and what proof exists that it worked.

### Steps

1. Click **Issues → New issue → 🌊 D-POAF Wave Scope**
2. Fill the form (10 minutes — be specific):

   | Field | What to write | Example |
   |---|---|---|
   | Wave ID | Unique identifier | `WAVE-2026-001` |
   | Wave Name | Short descriptive title | `AI Recommender — Phase 1` |
   | Wave Profile | Pick the appropriate profile | `Deliver Wave` |
   | Wave Captain | Single accountable person + email | `Sven A. (sven@team.io)` |
   | Business Objective | The problem + why now | *"Reduce browse-to-purchase friction by 15%"* |
   | AI Tools Authorized | Exact model + version | `Claude claude-sonnet-4-5-20250929` |
   | In Scope | Explicit list | `Ranking algorithm, API, 3 test scenarios` |
   | Out of Scope | Explicit list | `Mobile app, real-time analytics` |
   | PoD criterion | What "done" looks like | `All 3 scenarios validated by pilot client` |
   | PoV criterion | Measurable business outcome | `15% reduction at 30-day review` |
   | PoR criterion | Compliance / security | `GDPR data handling reviewed` |

3. Add the label `dpoaf:wave`
4. Click **Submit new issue**

You get an issue like `#42 — [WAVE] AI Recommender — Phase 1`. **This issue IS your Wave Scope Document.** No PDF, no separate file. Every Prompt Action and the closing Proof Record will reference `#42`.

---

## Days 2-N — Log every Prompt Action

> ⚖ Dynamic Law DL-006 — **PromptRegister is Mandatory.** Every Prompt Action must be logged BEFORE the AI is invoked.

### For every AI generation event

#### Step 1 — Before invoking the AI

1. Click **Issues → New issue → 🤖 D-POAF Prompt Action (PA)**
2. Fill the form:

   | Field | Example value |
   |---|---|
   | PA-ID | `PA-001` |
   | Wave reference | `#42` |
   | Requirement reference | `REQ-02` |
   | Wave Sub-Phase | `3 - Design Prompt Actions` |
   | Role | `Wave Surfer` |
   | **Model identity** | `Anthropic / Claude / claude-sonnet-4-5-20250929` |
   | **Model configuration** | `temperature: 0.2 · max_tokens: 4500 · system: "sp-team-v1" (sha256 4b8f…) · tools: none · format: text` |
   | **Context source** | `spec_v1.2.md §3.1 (sha256 c4e8…), task_schema.json` |
   | Prompt title | `Generate recommender scoring function` |
   | Prompt text (full) | (paste the actual user prompt) |

3. Submit → you get issue `#43`

#### Step 2 — Invoke the AI

Use the **exact** parameters you logged. Anything else breaks reproducibility.

#### Step 3 — After generation

Go back to issue `#43` and add a comment with:

- **Output summary** — `recommender.py — 95 lines, handles null inputs`
- **Quality (1-5)** — `5`
- **Reusable?** — `Yes`
- **Status** — `Active`
- **Issues / notes** — anything that affects reuse or debugging

#### Step 4 — Commit with the tag

```bash
git commit -m "feat(rec): add recommender scoring [AI:claude-sonnet-4-5:PA-001]"
```

> ⚖ Dynamic Law DL-005 — **AI Output Attribution.** All AI-touched commits MUST carry the `[AI:<model>:<PA-ID>]` tag.

#### Step 5 — Open a Pull Request

The PR template auto-loads with the D-POAF® checklist:

```markdown
☐ AI was used — commit messages carry [AI:<model>:<PA-ID>] tag (DL-005)
☐ All AI Prompt Actions logged in PromptRegister BEFORE invocation (DL-006)
☐ All AI-generated outputs reviewed by second human role (DL-002 + DL-011)
☐ Model + config + context recorded for every PA
☐ Every AI-touched file has a corresponding PA-ID in commit history
```

Fill in the PA references:

```
Prompt Actions in this PR:
- PA-001 — Recommender scoring — #43
- PA-007 — API endpoint — #51
```

The reviewer goes through the checklist before merge. **No merge without compliance.**

> ⚖ Dynamic Law DL-011 — **No Self-Validation.** A role may not validate their own work. The PR reviewer must be different from the PR author.

---

## Day N — Close the Wave

When the Wave is delivered and value has been measured (typically 30 days after delivery for PoV):

1. Click **Issues → New issue → ✅ D-POAF Proof Record (Wave Close)**
2. Fill the form:

   #### PoD — Proof of Delivery
   - **Deliverables** — list commits + file paths
   - **Validation method** — `Automated tests + UAT signed by client`
   - **Validated by** — Name + role
   - **Status** — `✓ Approved`

   #### PoV — Proof of Value
   - **Expected value (from Wave Scope)** — `15% reduction in planning time at 30 days`
   - **Achieved value** — `17.2% measured over 4 weeks`
   - **Measurement method** — `Pilot client's time-tracking tool`
   - **Status** — `✓ Approved`

   #### PoR — Proof of Reliability
   - **Security checks** — `OWASP review, dependency scan`
   - **Compliance** — `GDPR passed`
   - **Anomalies detected** — `None`
   - **Status** — `✓ Approved` or `N/A — Justified`

   #### Lessons Learned
   - What worked well
   - What should be improved
   - PromptRegister updates needed (reusable / archived)

3. Add label `dpoaf:proof-record`
4. Submit → issue `#67`

5. **Cross-link** — in the original Wave Scope issue `#42`, add a comment:

   > Wave closed. Proof Record: #67

6. **Close both issues** — `#67` (Proof Record) and `#42` (Wave Scope)

> ⚖ Dynamic Law DL-012 — **Proof Record is Mandatory for Wave Close.** No Wave may be marked as closed without a completed and signed Proof Record.

---

## 6 months later — Trace back an artifact

A new developer joins the team. They look at `recommender.py` and ask: *"Why this scoring logic? Who built it? What model? Can we reproduce it?"*

Here's the chain they walk:

### Step 1 — Read the commit message

```bash
git log --follow recommender.py
```

Returns:
```
feat(rec): add recommender scoring [AI:claude-sonnet-4-5:PA-001]
```

### Step 2 — Search for the PA-ID

In GitHub, search issues for `PA-001` → finds issue `#43`.

`#43` contains:
- The full prompt
- Model identity (claude-sonnet-4-5-20250929)
- Model config (temperature, system prompt hash)
- Context sources (spec docs with hashes)
- Author + reviewer
- Output summary + quality score

### Step 3 — Walk back to the Wave

Issue `#43` references `#42` (the Wave Scope).

`#42` reveals:
- Business objective (the "why")
- In/out scope (what was promised vs not)
- Authorized AI tools (which models were OK)
- PoD/PoV/PoR success criteria

### Step 4 — Confirm validation

`#42` references `#67` (the Proof Record).

`#67` reveals:
- What was delivered (PoD evidence)
- What value was achieved (PoV measurement)
- Compliance status (PoR)
- Who signed off

### Result

**Total time to trace back: 5-10 minutes.** No PDFs opened. No old developer contacted. No assumption made. The Traceability Thread is fully restored from GitHub alone.

This is what **proof-oriented governance** means in practice.

---

## Pro tips

### 1. Use issue templates for everything else too

Create issues for bugs, features, etc. using **Blank issue** (maintainers only) so the D-POAF® templates remain the dominant flow.

### 2. Naming convention for PA-IDs

Keep PA-IDs unique **within the Wave**:
- Wave WAVE-2026-001 → PA-001, PA-002, PA-003…
- Wave WAVE-2026-002 → PA-001, PA-002…

If your org runs many parallel Waves, prefix: `W001-PA-001`, `W002-PA-001`.

### 3. Multi-team coordination

For organizations with multiple teams, prefix Wave IDs with team:
- `RECEN-WAVE-2026-001` (Recommendation Engine team)
- `INFRA-WAVE-2026-001` (Infrastructure team)

### 4. Sensitive prompts

If a prompt contains secrets or proprietary content, paste a **SHA-256 hash + secure-storage link** in the issue body instead of the raw text. The hash proves integrity without leaking the content.

### 5. Reusable prompts library

When a PA scores 4 or 5, mark it `Reusable: Yes` and add to a shared **PromptRegister.xlsx** (in `kit/DPOAF_PromptRegister.xlsx` of the D-POAF main repo) under a `LIB-XXX` ID. Build your org's reusable prompt library over time.

### 6. Project board

Create a GitHub Project with views:
- **By Wave** — group issues by `Wave reference` label
- **By Status** — Backlog / Active / Validating / Closed
- **By Phase** — 1 (Intent) → 7 (Feedback)

### 7. Pin the WORKFLOW

Pin this `WORKFLOW.md` file in your repo so new team members find it immediately.

---

## FAQ

### Do I need to log a PA for every AI interaction?

**Yes — for every interaction that produces a deliverable** (code, doc, test, decision). Exploratory chats with the AI that don't end in a commit can be tracked separately in an "Exploration" tab of the spreadsheet. Per DL-006, **no commit without a logged PA**.

### Can I log a PA retroactively?

**No, except in exceptional cases.** Retroactive logging defeats the purpose of capturing the model state at generation time. Per DL-006: *"Retroactive logging is only permitted in exceptional cases and must be flagged."*

### What if my Wave Captain leaves?

A new Wave Captain must be formally designated **in writing** (comment on the Wave Scope issue with role transfer) before the Wave continues. Per DL-010: *"Each Wave has exactly one Wave Captain. Co-captains are not permitted."*

### My PR has 12 PAs in it. Is that OK?

It is technically OK, but practically a sign that your Waves are too large. Aim for **3-8 PAs per PR** for reviewable changes. Split larger PRs.

### Can I use multiple AI tools in one Wave?

Yes, **if all are listed in Wave Scope §B (AI Tools Authorized)**. Per DL-001: *"Only AI tools on the team's approved list may be used within a Wave."* Adding a new tool mid-Wave requires updating the Wave Scope and notifying stakeholders.

### What if the AI hallucinates and I commit the bug anyway?

The DL-002 (No Blind Acceptance) violation is the primary issue, not the bug itself. Document it in the PromptRegister `Issues / notes`, flag the PA as Quality 1, and update Dynamic Laws if needed.

### Do I need the GitHub Action / CI validation?

Not at first. Start with the templates + manual discipline. Add CI validation when your team has 3+ Waves and a stable rhythm. (See the Distribution Roadmap, Sprint 2.)

---

## Glossary

| Term | Definition |
|---|---|
| **Wave** | A governed unit of AI-enabled software delivery work. Contains scope, AI tools, PAs, PoD/PoV/PoR. |
| **Wave Captain** | Single accountable person for a Wave. Signs off on Proof Record. |
| **Wave Surfer** | Person drafting prompts and managing PAs during execution. |
| **RAGer** | Person preparing context (RAG snapshots, doc retrieval) for prompts. |
| **Peacekeepers** | Compliance + security guardrails monitoring delivery. |
| **PA (Prompt Action)** | A single AI invocation event. Logged in PromptRegister before generation. |
| **PoD (Proof of Delivery)** | Evidence that the deliverable exists and works as specified. |
| **PoV (Proof of Value)** | Evidence that the deliverable achieved the promised business outcome. |
| **PoR (Proof of Reliability)** | Evidence of compliance, security, and operational reliability. |
| **Dynamic Laws** | Team-adopted governance rules. The Starter Pack contains 15. |
| **Traceability Thread** | The audit chain from any artifact back to its originating prompt + model + context + Wave + business intent. |

---

## Need more?

- 📖 [Practical Guide (PDF)](https://d-poaf.org/resources/) — ~15 min read
- 🌐 [Framework Website](https://d-poaf.org)
- 💬 [Community Discord](https://discord.gg/DMZMeHxzNd)
- 🐙 [Full Starter Kit on GitHub](https://github.com/INOVIONIX/D-POAF/tree/main/kit)

---

© 2025–2026 Azzeddine IHSINE & Sara IHSINE — D-POAF® Framework — Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
