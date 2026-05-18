# D-POAF® GitHub Templates

Drop-in **Issue forms** and **Pull Request template** that bring the [D-POAF® Framework](https://d-poaf.org) Starter Kit directly into GitHub.

Five minutes from `git clone` to a governed AI-enabled SDLC.

---

## What's inside

```
.github/
├── ISSUE_TEMPLATE/
│   ├── config.yml             # Disable blank issues + links to docs
│   ├── wave-scope.yml         # 🌊 Wave Scope — opens a new Wave
│   ├── prompt-action.yml      # 🤖 Prompt Action — logs an AI generation event
│   └── proof-record.yml       # ✅ Proof Record — closes a Wave with PoD/PoV/PoR
└── PULL_REQUEST_TEMPLATE.md   # PR checklist enforcing DL-001, DL-002, DL-005, DL-006, DL-011
```

### How they map to the Starter Kit

| GitHub artifact | Starter Kit document | Role |
|---|---|---|
| **Wave Scope issue** | `DPOAF_Wave_Scope_Template.pdf` | Opens a Wave with full identification, scope, AI tools, and success criteria. |
| **Prompt Action issue** | `DPOAF_PromptRegister.pdf` | One issue per AI invocation. Captures model + config + context for **Traceability Thread**. |
| **Proof Record issue** | `DPOAF_Proof_Record_Template.pdf` | Closes a Wave with PoD/PoV/PoR evidence and sign-offs. |
| **PR template** | `DPOAF_Dynamic_Laws_Starter.pdf` | Runtime enforcement of Dynamic Laws DL-001, DL-002, DL-005, DL-006, DL-011. |

---

## Installation (60 seconds)

```bash
# In your repo root
cp -R path/to/this/repo/.github .github
git add .github
git commit -m "feat: install D-POAF governance templates [dpoaf]"
git push
```

That's it. Next time someone opens a new issue on your repo, they'll see the 3 D-POAF templates as options. PR template applies automatically.

---

## The five Dynamic Laws this PR template enforces

| Law | What the template enforces |
|---|---|
| **DL-001** Approved AI Tools | AI tools listed in Wave Scope before use. |
| **DL-002** No Blind Acceptance | AI-generated code requires human review before merge. |
| **DL-005** AI Output Attribution | Commit messages carry `[AI:<model>:<PA-ID>]` tag. |
| **DL-006** PromptRegister Mandatory | Every Prompt Action is logged BEFORE the AI is invoked. |
| **DL-011** No Self-Validation | A role may not validate its own work. |

See [`DPOAF_Dynamic_Laws_Starter.pdf`](https://d-poaf.org/resources/) for the full 15-rule starter pack.

---

## Suggested labels

Add these labels to your repo to get the most out of the templates:

| Label | Color | When applied |
|---|---|---|
| `dpoaf:wave` | `#0E2148` (navy) | Wave Scope issues |
| `dpoaf:prompt-action` | `#13B5D8` (cyan) | Prompt Action issues |
| `dpoaf:proof-record` | `#16A34A` (green) | Proof Record issues |
| `ai-generated` | `#7C7DFF` (purple) | Any AI-touched PR or issue |
| `wave-closing` | `#F59E0B` (amber) | Wave near close |
| `needs-triage` | `#94A3B8` (gray) | Wave Scope just opened |

GitHub CLI quick-add:

```bash
gh label create "dpoaf:wave" --color 0E2148 --description "D-POAF Wave Scope"
gh label create "dpoaf:prompt-action" --color 13B5D8 --description "D-POAF Prompt Action"
gh label create "dpoaf:proof-record" --color 16A34A --description "D-POAF Proof Record"
gh label create "ai-generated" --color 7C7DFF --description "Contains AI-generated content"
gh label create "wave-closing" --color F59E0B --description "Wave preparing to close"
```

---

## GitHub Project board (optional)

Create a GitHub Project board with these columns to visualize your Waves:

```
[Backlog Waves] → [Active Waves] → [Validating] → [Closed Waves]
```

Filter by label `dpoaf:wave` to see only Wave Scope issues. Each Wave Scope issue acts as the **parent**; Prompt Actions and Proof Records reference it via `#<wave-issue-number>`.

---

## Workflow in practice

1. **Open a Wave** — Click `New Issue` → `🌊 D-POAF Wave Scope`. Fill in identification, scope, AI tools, success criteria. The issue number becomes your `Wave ID` if you don't use a custom one.
2. **Log every Prompt Action** — Before invoking the AI, click `New Issue` → `🤖 D-POAF Prompt Action (PA)`. Reference the Wave issue. After generation, update the body with output summary + commit hash.
3. **Commit with the tag** — `git commit -m "feat(rank): add scoring [AI:claude-sonnet-4-5:PA-001]"`
4. **PR review** — The PR template auto-loads its checklist. Reviewer confirms all D-POAF compliance boxes before merge.
5. **Close the Wave** — Click `New Issue` → `✅ D-POAF Proof Record`. Reference the Wave issue. Fill PoD/PoV/PoR with evidence. Get sign-offs. Close both this issue and the Wave Scope issue.

---

## License

The templates are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — same as the D-POAF Framework.

You may use, modify, and redistribute them in your own repos. Attribution to the D-POAF® Framework is appreciated.

---

© 2025–2026 Azzeddine IHSINE & Sara IHSINE — [d-poaf.org](https://d-poaf.org)
