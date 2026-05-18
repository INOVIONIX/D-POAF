# 🔧 D-POAF® Jira — Custom Fields Setup (Admin)

> Upgrade your D-POAF® Jira install from label-based MVP to fully custom fields. **Requires Jira admin permission at the site level.**

---

## Why upgrade to custom fields?

The MVP install uses labels (no admin needed). Labels work, but have limitations:
- Free-form strings (typos creep in)
- No data validation
- Limited reporting (JQL only)
- Cannot be required on issue creation

Custom fields solve all of this:
- Typed (text, number, select, date)
- Required on creation
- Reportable via dashboards
- Searchable via custom JQL

---

## 7 Custom fields to create

### 1. PA-ID (Text, single-line)
- **Type**: Text (single line)
- **Description**: Unique identifier for the Prompt Action. Format: PA-NNN (e.g., PA-001).
- **Required on**: Prompt Action issues only
- **Searchable**: Yes

### 2. Macro-Phase (Select list)
- **Type**: Select List (single choice)
- **Options**:
  - `1. Instruct & Scope`
  - `2. Shape & Align`
  - `3. Execute & Evolve`
  - `4. Learn & Adapt`
- **Required on**: Wave, Prompt Action issues
- **Default**: (none — must be set explicitly)

### 3. Sub-Phase (Select list)
- **Type**: Select List (single choice)
- **Options**:
  - `1 - Intent & Scope`
  - `2 - Contextualize & Extract`
  - `3 - Design Prompt Actions`
  - `4 - Build & Generate`
  - `5 - Coordinate & Validate`
  - `6 - Deliver & Monitor`
  - `7 - Feedback & Evolve`
- **Required on**: Wave, Prompt Action issues

### 4. Model Identity (Text, single-line)
- **Type**: Text (single line)
- **Description**: Provider / model / exact version. E.g., "Anthropic / Claude / claude-sonnet-4-5-20250929"
- **Required on**: Prompt Action issues
- **Validation hint**: should contain at least one slash

### 5. Model Configuration (Text, multi-line / paragraph)
- **Type**: Text (multi-line) or "Paragraph"
- **Description**: All parameters needed to reproduce the generation (YAML/JSON). Include temperature, top_p, max_tokens, system_prompt hash, tools.
- **Required on**: Prompt Action issues

### 6. Context Source (Text, multi-line / paragraph)
- **Type**: Text (multi-line)
- **Description**: Documents and data fed to the prompt. Include sha256 hashes for integrity.
- **Required on**: Prompt Action issues

### 7. Quality Rating (Number)
- **Type**: Number (integer 1-5)
- **Description**: Quality of the AI generation. 1=poor, 5=excellent. Prompts <=2 must be refined before reuse (DL-007).
- **Required on**: Prompt Action issues
- **Validation**: integer between 1 and 5

---

## How to create these fields

### Path A — Team-managed project (limited)

Team-managed projects support per-project custom fields:

1. Go to **Project settings** → **Issue types**
2. Select an issue type (e.g., Task for Prompt Action)
3. Click **+ Add field**
4. Choose the field type, name it, configure
5. Save

⚠️ Limitation: Team-managed custom fields are scoped to the project only. They don't appear in other projects.

### Path B — Company-managed project (recommended for serious use)

1. Site admin: **Settings (gear icon)** → **Issues** → **Custom fields**
2. Click **Create custom field**
3. Choose type → name → configure
4. **Add field to screens**: associate with the screens used by your project's issue types
5. Save

Company-managed fields are reusable across all projects on your site.

---

## Recommended screen configuration

After creating the 7 custom fields, add them to the appropriate screens:

| Field | Wave Epic screen | PA Task screen | Proof Sub-task screen |
|---|---|---|---|
| PA-ID | — | ✅ | ✅ |
| Macro-Phase | ✅ | ✅ | — |
| Sub-Phase | ✅ | ✅ | — |
| Model Identity | — | ✅ | — |
| Model Configuration | — | ✅ | — |
| Context Source | — | ✅ | — |
| Quality Rating | — | ✅ | — |

---

## Update the build script for custom fields

Once your custom fields are configured, you can use them programmatically. Edit `build_dpoaf_jira.py` and replace label-based labeling with custom field values:

```python
# Get custom field IDs (Jira generates them - typically customfield_10XYZ)
# To find them: GET /rest/api/3/field

# In the issue creation:
fields = {
    "project": {"key": PROJECT_KEY},
    "summary": "PA-001 - Build sentiment classifier",
    "issuetype": {"name": "Task"},
    "description": PA_DESCRIPTION,
    "labels": ["d-poaf", "prompt-action"],  # keep some labels
    
    # NEW: custom field values
    "customfield_10100": "PA-001",  # PA-ID
    "customfield_10101": {"value": "2. Shape & Align"},  # Macro-Phase
    "customfield_10102": {"value": "3 - Design Prompt Actions"},  # Sub-Phase
    "customfield_10103": "Anthropic / Claude / claude-sonnet-4-5-20250929",  # Model Identity
    "customfield_10104": "temperature: 0.2\ntop_p: 1.0\n...",  # Model Configuration
    "customfield_10105": "client_spec_v1.2.pdf (sha256: ...)",  # Context Source
    "customfield_10106": 5,  # Quality Rating
}
```

To discover your custom field IDs:
```bash
curl -u email:token https://yoursite.atlassian.net/rest/api/3/field | python3 -m json.tool | grep -A1 "name.*Macro-Phase"
```

---

## Optional — Custom workflow

If you want Sub-Phase to be a workflow status (not a select field):

1. Site admin → **Settings** → **Issues** → **Workflows**
2. Copy the default workflow
3. Add 7 states matching the 7 Sub-Phases
4. Define transitions:
   - 1 → 2 → 3 (sequential)
   - 3 → 4 → 5 → 6 (sequential)
   - 6 → 7 (sequential)
   - 7 → Closed (final)
   - Any → 7 (rollback for re-work)
5. Assign the workflow to your Wave Epic issue type only

This gives you Wave lifecycle tracking via status (visible on the board as columns).

---

## ✅ When you're done

After custom fields setup:
- Existing label-based issues continue to work
- New issues can use custom fields for richer data
- Dashboards become more powerful (pie charts by Macro-Phase select, etc.)
- JQL queries become more precise (`"Macro-Phase" = "3. Execute & Evolve"`)

You're now in production-grade D-POAF® Jira.

---

D-POAF® Framework v1.1 — d-poaf.org — Licensed under CC BY 4.0
