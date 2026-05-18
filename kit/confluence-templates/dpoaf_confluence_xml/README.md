# 🐘 D-POAF® — Confluence Storage Format Templates

Drop-in **Confluence Storage Format XML** templates that bring the D-POAF® Framework Starter Kit into Confluence Cloud in ~30 minutes.

**Bundle v1.1** — adds the 4 macro-phases (Canonical Spec v1.1), Sprint + Repository association on the Wave Scope, and a dedicated Wave Lifecycle page.

Six templates. Three are page templates (instantiated many times). Three are one-shot pages.

---

## 📦 What's in this bundle

| File | Type | Purpose |
|---|---|---|
| `01_wave_scope_template.xml` | **Page template** | 🌊 Open a new Wave. Now includes **Macro-Phase + Sub-Phase + Sprint + Repository + Branch + Linked Jira Epic + Release Tag**. Instantiated 1 per Wave. |
| `02_prompt_action_template.xml` | **Page template** | 🤖 Log every AI invocation. The Traceability Thread fields (★ Model + Config + Context) are mandatory. Now includes **Macro-Phase (derived from Sub-Phase) + Repository + Branch + Commit hash + PR URL + Files touched**. Instantiated 1 per AI generation. |
| `03_proof_record_template.xml` | **Page template** | ✅ Close a Wave with PoD/PoV/PoR evidence and sign-offs. Instantiated 1 per closed Wave. |
| `04_dynamic_laws_page.xml` | **One-shot page** | ⚖ 15 governance rules + amendment log + adoption sign-off. Lives at the root of the Space. |
| `05_practical_guide_page.xml` | **One-shot page** | 📖 Onboarding page explaining D-POAF® concepts. ~15-minute read. |
| `06_wave_lifecycle_page.xml` | **One-shot page** | 📊 NEW — The 4 macro-phases (Instruct &amp; Scope · Shape &amp; Align · Execute &amp; Evolve · Learn &amp; Adapt). With Sprint &amp; Repo activity per phase. Embedded live view of active Waves. |

---

## 🚀 Installation (30 minutes total)

### Step 1 — Create the Confluence Space

1. In Confluence Cloud, click **Spaces → Create Space → Blank space**
2. Space name: **D-POAF® Governance**
3. Space key: `DPOAF`
4. Description: *"Governed AI-enabled software delivery. Wave Scope · Prompt Actions · Proof Records · Dynamic Laws."*

### Step 2 — Register the 3 page templates

For each of the **page template** XML files (01, 02, 03):

1. Open **Space settings → Templates** (gear icon in the Space sidebar)
2. Click **Create new template**
3. Name and description per the table below:

   | XML file | Template Name | Description |
   |---|---|---|
   | `01_wave_scope_template.xml` | 🌊 D-POAF Wave Scope | Open a new D-POAF® Wave. Use at the START of every project or feature. |
   | `02_prompt_action_template.xml` | 🤖 D-POAF Prompt Action | Log a single AI generation event. ONE template per AI invocation. |
   | `03_proof_record_template.xml` | ✅ D-POAF Proof Record | Close a Wave with a signed Proof Record. PoD, PoV, PoR with evidence. |

4. In the template editor, click the **`...`** menu in the top right → **View Source** (or **Storage Format Editor**)
5. **Paste the contents of the XML file** (skip the HTML comment header)
6. **Save**

### Step 3 — Create the 3 one-shot pages

For each of the **one-shot page** XML files (04, 05, 06):

1. In the Space, click **+ Create → Blank page**
2. Title per the table below:

   | XML file | Page title |
   |---|---|
   | `04_dynamic_laws_page.xml` | Dynamic Laws |
   | `05_practical_guide_page.xml` | Practical Guide |
   | `06_wave_lifecycle_page.xml` | Wave Lifecycle |

3. In the page editor, click `...` → **View Source** (or **Storage Format Editor**)
4. **Paste the contents of the XML file** (skip the HTML comment header)
5. **Save**

### Step 4 — Create the parent index pages

Create 3 Blank pages — these will host child pages (one per Wave / PA / Proof Record):

| Page title | Purpose |
|---|---|
| 🌊 Waves | Parent for all Wave Scope pages |
| 🤖 Prompt Actions | Parent for all Prompt Action pages |
| ✅ Proof Records | Parent for all Proof Record pages |

In each parent page, add this macro so the page lists its children automatically:

```xml
<ac:structured-macro ac:name="children">
  <ac:parameter ac:name="sort">creation</ac:parameter>
  <ac:parameter ac:name="reverse">true</ac:parameter>
  <ac:parameter ac:name="excerpt">true</ac:parameter>
</ac:structured-macro>
```

---

## ✅ Test the install

1. In the Space, click **+ Create → ⚓ Template**
2. You should see your 3 templates: **🌊 D-POAF Wave Scope · 🤖 D-POAF Prompt Action · ✅ D-POAF Proof Record**
3. Click **🌊 D-POAF Wave Scope** → fill in a test Wave → save under the **🌊 Waves** parent
4. The new page should appear with all D-POAF® sections, dropdowns for status, and properly formatted tables

If you see this, **you have D-POAF® governance live in your Confluence Space**.

---

## 🧰 Distribute to other teams

Once your Space is built, you have 2 distribution paths:

### Path A — Export Space as XML
1. **Space settings → Content tools → Export space → XML**
2. Download the `.zip`
3. Share with other teams; they import via **Space settings → Content tools → Import XML**

### Path B — Atlassian Marketplace App (Sprint 3 of Distribution Roadmap)
A future Marketplace App will publish D-POAF® as a 1-click installable Atlassian app. Until then, Path A is the way.

---

## 📚 Further reading

- 🌐 **D-POAF® Framework** — [d-poaf.org](https://d-poaf.org)
- 📦 *