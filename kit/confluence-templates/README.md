# 🐘 D-POAF® Confluence Install Kit — v1.2

> **Open-source governance for AI-enabled software delivery** — your Confluence Cloud Space, production-ready in 5 to 30 minutes.

D-POAF® (Decentralized Proof-Oriented AI Framework) is a free, open-source framework that brings traceable governance to AI-enabled software delivery. This kit installs the complete D-POAF® Governance Space in your Confluence Cloud, with all templates, reference pages, and sample lifecycle pre-configured.

---

## 🚀 Get the Overview

👉 **[Open the D-POAF® Confluence Template →](https://dpoaf.atlassian.net/wiki/spaces/DPOAFGOV/overview)**

---

## 🎯 What this kit installs in your Confluence

After installation, your `D-POAF® Governance` Space will contain:

**5 reference pages** (ready to read, ~15 min onboarding)
- 📖 **Practical Guide** — Understand D-POAF® in 15 minutes
- 📋 **Workflow** — Day-by-day operations (6 daily ops detailed)
- 📊 **Wave Lifecycle** — The 4 macro-phases (Instruct & Scope → Shape & Align → Execute & Evolve → Learn & Adapt)
- 🔗 **Traceability** — How to trace back from any artifact to business intent (audit-ready)
- ⚖ **Dynamic Laws** — 15 pre-built governance rules (amendable by team vote)

**3 page templates** (accessible via + Create)
- 🌊 **D-POAF Wave Scope** — Open a new Wave at the start of every project
- 🤖 **D-POAF Prompt Action** — Log every AI invocation with full Traceability Thread
- ✅ **D-POAF Proof Record** — Close a Wave with PoD/PoV/PoR evidence

**3 parent index pages** with auto-listing
- 🌊 Waves — auto-lists every Wave Scope created
- 🤖 Prompt Actions — auto-lists every PA logged
- ✅ Proof Records — auto-lists every closure record

**1 complete sample lifecycle** (cohesive demo)
- WAVE-EXAMPLE-001 → PA-001 → PROOF-EXAMPLE-001, linked end-to-end

---

## 🚀 3 installation methods — Pick your favorite

| Method | Duration | Skill required | Best for |
|---|---|---|---|
| **A. Automated (recommended)** | 5 minutes | Run a Python script | Most teams |
| **B. Manual via Build Guide** | 30 minutes | Confluence admin UI | Non-technical leads |
| **C. XML import** | 15 minutes | Storage Format editing | Confluence Data Center / Server |

---

## 🅰️ Method A — Automated (5 min) — RECOMMENDED

### Prerequisites

1. A Confluence Cloud account with admin permission on a Space (or create a new one first)
2. **Python 3.7+** installed on your computer ([download](https://www.python.org/downloads/))
3. An **Atlassian API token** (free to generate — see step 2)

### Step 1 — Create your Confluence Space

If you don't already have a dedicated Space:

1. In Confluence Cloud, click **Spaces** → **Create Space** → **Blank space** (or "Knowledge base" template)
2. Space name: `D-POAF® Governance`
3. Space key: `DPOAFGOV` (or any other key you prefer)
4. Description: `Governed AI-enabled software delivery. Wave Scope · Prompt Actions · Proof Records · Dynamic Laws.`
5. Create the Space

### Step 2 — Generate your API token

1. Open https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **Create API token**
3. Label: `D-POAF Builder`
4. Expiry: 1 year (recommended)
5. **Copy the token** — save it locally, Atlassian will not show it again

### Step 3 — Run the auto-install script

Open a terminal (PowerShell on Windows, Terminal on macOS/Linux), navigate to this kit's folder, and:

**PowerShell (Windows):**

```powershell
$env:CONFLUENCE_URL = "https://YOURSITE.atlassian.net"
$env:CONFLUENCE_EMAIL = "your.email@example.com"
$env:CONFLUENCE_TOKEN = "ATATT3xFfGF0..."
$env:CONFLUENCE_SPACE_KEY = "DPOAFGOV"
python build_dpoaf_confluence.py
```

**Bash (macOS/Linux):**

```bash
export CONFLUENCE_URL="https://YOURSITE.atlassian.net"
export CONFLUENCE_EMAIL="your.email@example.com"
export CONFLUENCE_TOKEN="ATATT3xFfGF0..."
export CONFLUENCE_SPACE_KEY="DPOAFGOV"
python3 build_dpoaf_confluence.py
```

The script will create the 3 templates, 5 reference pages, 3 parent pages, and sample lifecycle.

### Step 4 — Apply the v1.2 patch (adds Workflow + Traceability pages)

In the same terminal (variables still set):

```bash
python3 patch_dpoaf_confluence.py
```

This adds the Workflow and Traceability pages that complete the v1.2 set.

### Step 5 — Verify

Open your Space at `https://YOURSITE.atlassian.net/wiki/spaces/DPOAFGOV/overview`. You should see all 8 pages in the sidebar + 3 templates available via + Create.

**Total time: ~5 minutes.** ✅

---

## 🅱️ Method B — Manual via Build Guide (30 min)

If you don't want to run scripts, follow the step-by-step Build Guide. It covers:

1. Creating the Space
2. Registering each of the 3 page templates (via Space settings → Templates)
3. Creating each of the 5 reference pages
4. Setting up the 3 parent index pages with the Children macro
5. Testing the install

See **`DPOAF_Confluence_Build_Guide_v1.2.pdf`** (or download from d-poaf.org) for the full 12-step walkthrough with screenshots.

---

## 🅲 Method C — XML import (15 min) — for Data Center / Server

If you're on Confluence Data Center or Server (not Cloud), or you prefer to manually paste Storage Format:

1. Open each `.xml` file in the `dpoaf_confluence_xml/` folder
2. In Confluence, create a new page (or template) and click the **••• → View source** option
3. Paste the XML content
4. Save

For the 3 templates (`01`, `02`, `03`), go to **Space settings → Templates** and create new templates using the Storage Format source editor.

For the 3 one-shot pages (`04`, `05`, `06`), create them as regular pages in the Space.

---

## 🧪 Test your install

Once installed, validate end-to-end:

1. In your Space, click **+ Create** → **From a template**
2. You should see 3 D-POAF templates: 🌊 Wave Scope, 🤖 Prompt Action, ✅ Proof Record
3. Click **🌊 D-POAF Wave Scope** → a new page opens with the complete Wave Scope structure pre-filled
4. Save it under the 🌊 Waves parent page

If you see this, **your D-POAF® install is production-ready.** ✅

---

## 🧹 Recommended post-install cleanup

After install, optionally:

1. **Delete the default Atlassian templates** (e.g., "How-to guide", "Troubleshooting article") from the sidebar — clean appearance
2. **Disable blueprint templates** not needed (Space settings → Templates → toggle off)
3. **Pin the 5 reference pages** at the top of the sidebar for quick access
4. **Set Space permissions** when ready to publish (private → restricted → public)

---

## 📚 Adopt with your team

1. **Hold a 30-min kickoff** — walk the team through Practical Guide + Wave Lifecycle
2. **Sign-off Dynamic Laws** — review the 15 rules, propose amendments if needed (DL-014 / DL-015)
3. **Open your first real Wave** — pick a small project to pilot the framework
4. **Iterate** — feedback loop in Macro-Phase 4 (Learn & Adapt) — refine your practice each Wave

---

## 🗂️ Kit contents

```
DPOAF_Confluence_Install_Kit_v1.2/
├── README.md                          (this file)
├── LICENSE.txt                         (CC BY 4.0)
├── dpoaf_confluence_xml/               (Storage Format XML templates)
│   ├── 01_wave_scope_template.xml
│   ├── 02_prompt_action_template.xml
│   ├── 03_proof_record_template.xml
│   ├── 04_dynamic_laws_page.xml
│   ├── 05_practical_guide_page.xml
│   ├── 06_wave_lifecycle_page.xml
│   └── README.md                       (bundle-specific notes)
├── build_dpoaf_confluence.py           (Method A — auto install)
└── patch_dpoaf_confluence.py           (v1.2 patch — adds Workflow + Traceability)
```

---

## 🆘 Troubleshooting

| Error | Likely cause | Fix |
|---|---|---|
| `HTTP 401 Unauthorized` | Wrong email or API token | Regenerate token from id.atlassian.com |
| `HTTP 404 Not Found` | Wrong Space key | Check the key in your Confluence URL |
| `Space 'XXX' not found` | No permission on Space | You must be Space admin |
| `HTTP 400 Bad Request` | XML file corrupted | Re-extract the ZIP cleanly |
| `XML file not found` | `dpoaf_confluence_xml/` not at script's folder | Check folder structure |
| Templates don't show in + Create | Templates created but not promoted | Space settings → Templates → toggle "Promote" |

If you hit a blocker not in this list, open an issue on GitHub: https://github.com/INOVIONIX/D-POAF/issues

---

## 🔗 Resources

- 🌐 **Framework reference**: https://d-poaf.org
- 🐙 **GitHub starter repo**: https://github.com/INOVIONIX/D-POAF
- 📋 **Notion template** (alternative platform): see d-poaf.org/notion-template
- 📖 **Full Canonical Specification v1.1** (PDF): https://d-poaf.org/wp-content/uploads/2026/01/Canonical_D_POAF.pdf
- 💬 **Community Discord**: https://discord.gg/DMZMeHxzNd

---

## 📜 License

Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use, modify, and distribute with attribution.

D-POAF® is a registered trademark of Inovionix.

© 2025–2026 Azzeddine IHSINE & Sara IHSINE — d-poaf.org

---

## 📊 Version

**v1.2 — May 2026**
- Added Workflow page (day-by-day operations)
- Added Traceability page (artifact → business intent chain)
- API-based installer (build_dpoaf_confluence.py)
- Patch script (patch_dpoaf_confluence.py)
- Sample lifecycle pre-filled (WAVE-EXAMPLE-001 / PA-001 / PROOF-EXAMPLE-001)

Previous: v1.1 (XML bundle + Build Guide, Sprint/Repo + macro-phases integration)
