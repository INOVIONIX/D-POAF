#!/usr/bin/env python3
"""
D-POAF (R) Jira Install Kit - All-in-One Installer v2.0

This single script does EVERYTHING that 5 separate scripts did before:
  Phase 1 - Sample lifecycle (1 Wave + 1 PA + 1 Proof)
  Phase 2 - Enrichment (15 Dynamic Laws + 4 more PAs + 1 Partial Proof)
  Phase 3 - Sprint creation + start with sprint-relevant tickets
  Phase 4 - 8 saved JQL filters (D-POAF views + Universal Outcome Search)
  Phase 5 - Dashboard + 4 gadgets (colored layout)
  Phase 6 - Manual-steps report

Run once. Re-run safely - all operations are idempotent.

PREREQUISITES:
  1. Jira Cloud project already created (key = DPOAF or similar)
  2. Atlassian API token from id.atlassian.com
  3. Python 3.7+ - no external dependencies

USAGE (PowerShell):
  $env:JIRA_URL = "https://yoursite.atlassian.net"
  $env:JIRA_EMAIL = "your.email@example.com"
  $env:JIRA_TOKEN = "ATATT3xFfGF0..."
  $env:JIRA_PROJECT_KEY = "DPOAF"
  python install_dpoaf_jira.py

Licensed under CC BY 4.0 - Azzeddine IHSINE & Sara IHSINE - d-poaf.org
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
import urllib.parse
import datetime

# ============================================================
# Configuration
# ============================================================
URL = os.environ.get("JIRA_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL")
TOKEN = os.environ.get("JIRA_TOKEN")
PROJECT_KEY = os.environ.get("JIRA_PROJECT_KEY")

if not all([URL, EMAIL, TOKEN, PROJECT_KEY]):
    print("ERROR: Set all 4 environment variables before running:")
    print('  $env:JIRA_URL = "https://yoursite.atlassian.net"')
    print('  $env:JIRA_EMAIL = "your.email@example.com"')
    print('  $env:JIRA_TOKEN = "ATATT3xFfGF0..."')
    print('  $env:JIRA_PROJECT_KEY = "DPOAF"')
    print("  python install_dpoaf_jira.py")
    sys.exit(1)

BASE_API_V3 = f"{URL}/rest/api/3"
BASE_AGILE = f"{URL}/rest/agile/1.0"
AUTH = f"Basic {base64.b64encode(f'{EMAIL}:{TOKEN}'.encode()).decode()}"

# ============================================================
# HTTP helpers
# ============================================================
class APIError(Exception):
    def __init__(self, code, body, url):
        self.code = code
        self.body = body
        self.url = url
        super().__init__(f"HTTP {code} on {url}")

def call(method, full_url, body=None, query=None):
    url = full_url
    if query:
        url += "?" + urllib.parse.urlencode(query)
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", AUTH)
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            text = resp.read().decode("utf-8")
            return json.loads(text) if text else {}
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        raise APIError(e.code, err, url)

def log(msg, prefix="  -> "):
    print(f"{prefix}{msg}", flush=True)

def section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)

# ============================================================
# ADF helpers
# ============================================================
def adf(blocks):
    return {"type": "doc", "version": 1, "content": blocks}

def p(text, bold=False):
    c = [{"type": "text", "text": text}]
    if bold:
        c[0]["marks"] = [{"type": "strong"}]
    return {"type": "paragraph", "content": c}

def h(text, lvl=2):
    return {"type": "heading", "attrs": {"level": lvl},
            "content": [{"type": "text", "text": text}]}

def ul(items):
    return {"type": "bulletList",
            "content": [{"type": "listItem", "content": [p(i)]} for i in items]}

def panel(text, ptype="info"):
    return {"type": "panel", "attrs": {"panelType": ptype},
            "content": [p(text)]}

# ============================================================
# Jira operations
# ============================================================
def find_issue_by_summary(summary_substr):
    """Search for issue by partial summary match."""
    try:
        result = call("POST", f"{BASE_API_V3}/search/jql", body={
            "jql": f'project = {PROJECT_KEY} AND summary ~ "{summary_substr}"',
            "fields": ["summary", "labels", "issuetype"],
            "maxResults": 5,
        })
        return result.get("issues", [])
    except APIError:
        return []

def create_issue(summary, desc_adf, issuetype, labels, parent_key=None):
    fields = {
        "project": {"key": PROJECT_KEY},
        "summary": summary,
        "issuetype": {"name": issuetype},
        "description": desc_adf,
        "labels": labels,
    }
    if parent_key:
        fields["parent"] = {"key": parent_key}
    return call("POST", f"{BASE_API_V3}/issue", body={"fields": fields})

def issue_url(issue):
    return f"{URL}/browse/{issue.get('key', '?')}"

# ============================================================
# Banner
# ============================================================
print()
print("=" * 60)
print("D-POAF (R) Jira Install Kit - All-in-One v2.0")
print("=" * 60)
print(f"Jira URL:      {URL}")
print(f"Project key:   {PROJECT_KEY}")
print(f"User:          {EMAIL}")
print("-" * 60)

# Verify project access
log("Verifying project access...")
try:
    project = call("GET", f"{BASE_API_V3}/project/{PROJECT_KEY}")
    log(f"  OK - '{project['name']}' (type: {project.get('projectTypeKey', '?')})")
except APIError as e:
    print(f"FATAL: Cannot access project '{PROJECT_KEY}'.")
    print(f"  {e}")
    print()
    print("Common causes:")
    print("  - Project doesn't exist (create it manually first via Jira UI)")
    print("  - Wrong project key (case-sensitive)")
    print("  - Wrong API token or email")
    sys.exit(1)

# Get current user accountId
log("Fetching current user accountId (for dashboard ownership)...")
try:
    me = call("GET", f"{BASE_API_V3}/myself")
    my_account_id = me["accountId"]
    log(f"  OK - {me.get('displayName', '?')} (id: {my_account_id[:20]}...)")
except APIError as e:
    print(f"WARNING: Cannot get user info: {e}")
    my_account_id = None

# ============================================================
# PHASE 1: Sample lifecycle (Wave + PA + Proof)
# ============================================================
section("PHASE 1 - Sample lifecycle (Wave + PA + Proof)")

# Check if WAVE-EXAMPLE-001 already exists
existing = find_issue_by_summary("WAVE-EXAMPLE-001")
if existing:
    wave_key = existing[0]["key"]
    log(f"WAVE-EXAMPLE-001 already exists as {wave_key} - skipping creation")
else:
    log("Creating Wave Epic (WAVE-EXAMPLE-001)...")
    wave_desc = adf([
        panel("Sample Wave demonstrating the complete D-POAF lifecycle.", "info"),
        h("Identification"),
        ul([
            "Wave ID: WAVE-EXAMPLE-001",
            "Wave Profile: Deliver Wave",
            "Wave Captain: Sara IHSINE",
            "Business Sponsor: Inovionix CEO",
            "Date Opened: 2026-05-01",
            "Status: Active",
        ]),
        h("Wave Lifecycle Position"),
        ul([
            "Macro-Phase: 3. Execute & Evolve",
            "Current Sub-Phase: 4 - Build & Generate",
        ]),
        h("Sprint & Repository Association"),
        ul([
            "Sprint ID: SPRINT-2026-W12",
            "Repository: github.com/myorg/sentiment-classifier",
            "Working Branch: feature/WAVE-EXAMPLE-001",
        ]),
        h("Business Objective"),
        p("Build a sentiment classifier for customer reviews. Target: 95% accuracy across 6 categories. Reduce manual triage time on customer feedback."),
        h("Scope"),
        p("In Scope:", bold=True),
        ul([
            "Classification function (Python)",
            "REST API endpoint",
            "Test suite covering all 6 categories",
            "API integration documentation",
        ]),
        p("Out of Scope:", bold=True),
        ul([
            "Multilingual support (English only)",
            "Real-time streaming",
            "CRM integration (next Wave)",
        ]),
        h("Proof Model (PoD / PoV / PoR)"),
        ul([
            "PoD: 95%+ accuracy on test dataset, all 6 categories functional",
            "PoV: Client deploys API independently within 2 weeks of handover",
            "PoR: N/A - decision-support tool, no autonomous action",
        ]),
        p("D-POAF (R) Framework v1.1 - d-poaf.org - Licensed CC BY 4.0"),
    ])
    try:
        wave = create_issue(
            "WAVE-EXAMPLE-001 - Customer Feedback Categorization (Pilot)",
            wave_desc,
            "Epic",
            ["d-poaf", "wave", "macro-3", "phase-4", "deliver-wave", "active"],
        )
        wave_key = wave["key"]
        log(f"  OK - {issue_url(wave)}")
    except APIError as e:
        print(f"FATAL: Cannot create Wave: {e}")
        sys.exit(1)

# PA-001
existing_pa = find_issue_by_summary("PA-001 - Build sentiment classifier")
if existing_pa:
    log(f"PA-001 already exists as {existing_pa[0]['key']} - skipping")
else:
    log("Creating PA-001 (Build sentiment classifier function)...")
    pa_desc = adf([
        panel("Sample Prompt Action linked to WAVE-EXAMPLE-001. Demonstrates the Traceability Thread.", "info"),
        h("Identification"),
        ul([
            "PA-ID: PA-001",
            "Linked Wave: WAVE-EXAMPLE-001",
            "Sub-Phase: 3 - Design Prompt Actions",
            "Macro-Phase: 2. Shape & Align",
            "Role: Wave Surfer",
            "Date: 2026-05-08",
        ]),
        panel("The 3 Traceability Thread sections below are MANDATORY per DL-006.", "warning"),
        h("Model identity", 3),
        p("Anthropic / Claude / claude-sonnet-4-5-20250929"),
        h("Model configuration", 3),
        ul([
            "temperature: 0.2",
            "top_p: 1.0",
            "max_tokens: 4000",
            "system_prompt: sp-team-v1 (sha256: 8a2c...d3b1)",
        ]),
        h("Context source", 3),
        ul([
            "client_spec_v1.2.pdf (sha256: a3f9...e7c4) section 2.1",
            "test_v2.csv referenced as file path",
        ]),
        h("Output"),
        ul([
            "Quality (1-5): 5 - Excellent",
            "Reusable? Yes (Wave Captain approved)",
            "Status: Active",
        ]),
        h("Linked Repository & PR"),
        ul([
            "Repository: github.com/myorg/sentiment-classifier",
            "Branch: feature/WAVE-EXAMPLE-001",
            "Commit: abc123de [AI:claude-sonnet-4-5:PA-001]",
            "PR: github.com/myorg/sentiment-classifier/pull/12",
        ]),
    ])
    try:
        pa = create_issue(
            "PA-001 - Build sentiment classifier function",
            pa_desc,
            "Task",
            ["d-poaf", "prompt-action", "macro-2", "phase-3", "wave-surfer",
             "quality-5", "reusable-prompt", "traceability-thread-complete"],
            parent_key=wave_key,
        )
        log(f"  OK - {issue_url(pa)}")
    except APIError as e:
        log(f"  FAILED: {e.body[:200]}")

# PROOF-001
existing_proof = find_issue_by_summary("PROOF-EXAMPLE-001")
if existing_proof:
    log(f"PROOF-001 already exists as {existing_proof[0]['key']} - skipping")
else:
    log("Creating PROOF-EXAMPLE-001 (full approval)...")
    proof_desc = adf([
        panel("Sample Proof Record closing WAVE-EXAMPLE-001. PoD Approved, PoV Approved, PoR N/A.", "info"),
        h("Identification"),
        ul([
            "Proof ID: PROOF-EXAMPLE-001",
            "Linked Wave: WAVE-EXAMPLE-001",
            "Date Closed: 2026-05-17",
        ]),
        h("PoD - Proof of Delivery"),
        ul([
            "Status: APPROVED",
            "Deliverables: classify_feedback.py (90 lines, commit abc123de)",
            "Validation: Test suite passes 100%, accuracy 96.3% (>95% target)",
        ]),
        h("PoV - Proof of Value"),
        ul([
            "Status: APPROVED",
            "Expected: Client deploys API within 2 weeks",
            "Achieved: Client integrated within 8 days (target <=14 days)",
            "Impact: Manual triage time reduced by 73%",
        ]),
        h("PoR - Proof of Reliability"),
        ul([
            "Status: N/A",
            "Compliance: N/A - decision-support tool, no autonomous action",
        ]),
        h("Sign-offs"),
        ul([
            "Wave Captain - Sara IHSINE",
            "Sponsor - Inovionix CEO",
        ]),
    ])
    try:
        create_issue(
            "PROOF-EXAMPLE-001 - Closure of WAVE-EXAMPLE-001",
            proof_desc,
            "Task",
            ["d-poaf", "proof-record", "macro-4", "phase-7",
             "pod-approved", "pov-approved", "por-na",
             "wave-captain-signed", "sponsor-signed"],
            parent_key=wave_key,
        )
        log(f"  OK")
    except APIError as e:
        log(f"  FAILED: {e.body[:200]}")

# ============================================================
# PHASE 2: Enrichment - 15 Dynamic Laws + 4 PAs + Partial Proof
# ============================================================
section("PHASE 2 - Enrichment (15 Dynamic Laws + 4 PAs + Partial Proof)")

DYNAMIC_LAWS = [
    ("DL-001", "AI Tool Usage", "Approved AI Tools", "Only AI tools on the team's approved list may be used within a Wave."),
    ("DL-002", "AI Tool Usage", "No Blind Acceptance", "No AI-generated output may be committed to a deliverable without review by a human role."),
    ("DL-003", "AI Tool Usage", "Model Version Logging", "The AI model version used in each Prompt Action must be recorded."),
    ("DL-004", "AI Tool Usage", "Context Integrity", "AI tools must be prompted using only the context prepared by the RAGer."),
    ("DL-005", "AI Tool Usage", "AI Output Attribution", "All code, documents, and artifacts generated by AI must be tagged as AI-generated."),
    ("DL-006", "Prompt Management", "PromptRegister is Mandatory", "Every Prompt Action must be logged BEFORE the AI is invoked."),
    ("DL-007", "Prompt Management", "Prompt Quality Rating", "Each AI generation cycle must have a quality rating (1-5). Prompts rated 1-2 must be refined."),
    ("DL-008", "Prompt Management", "Reusable Prompt Approval", "A prompt may only be marked Reusable if quality >=4 AND Wave Captain approved."),
    ("DL-009", "Roles & Accountability", "Role Assignment Before Wave Start", "A Wave may not begin Sub-Phase 2 without a Wave Captain and a RAGer."),
    ("DL-010", "Roles & Accountability", "Single Wave Captain", "Each Wave has exactly one Wave Captain. Co-captains are not permitted."),
    ("DL-011", "Roles & Accountability", "No Self-Validation", "A role may not validate their own work."),
    ("DL-012", "Proof & Validation", "Proof Record Mandatory for Wave Close", "No Wave closed without a signed Proof Record."),
    ("DL-013", "Proof & Validation", "Evidence Must Be Accessible", "All evidence referenced in a Proof Record must be accessible at Wave close."),
    ("DL-014", "Governance Process", "Amendment by Proposal", "Any team member may propose an amendment to the Dynamic Laws."),
    ("DL-015", "Governance Process", "Majority Vote Required", "Amendments require simple majority (>50%) vote of active team members."),
]

CATEGORY_LABELS = {
    "AI Tool Usage": "dl-ai-tool-usage",
    "Prompt Management": "dl-prompt-management",
    "Roles & Accountability": "dl-roles-accountability",
    "Proof & Validation": "dl-proof-validation",
    "Governance Process": "dl-governance-process",
}

dls_created = 0
for dl_id, cat, title, desc in DYNAMIC_LAWS:
    existing_dl = find_issue_by_summary(f"{dl_id} - {title}")
    if existing_dl:
        continue
    summary = f"{dl_id} - {title}"
    desc_adf = adf([
        panel(f"Dynamic Law {dl_id} - Category: {cat}", "info"),
        p("Statement:", bold=True),
        p(desc),
        h("Status", 3),
        p("Adopted (default)"),
    ])
    labels = [
        "d-poaf", "dynamic-law",
        f"dl-{dl_id.split('-')[1].lstrip('0') or '0'}",
        CATEGORY_LABELS.get(cat, "dl-custom"),
        "adopted",
    ]
    try:
        create_issue(summary, desc_adf, "Task", labels)
        dls_created += 1
        log(f"  {dl_id} - {title[:35]}")
    except APIError as e:
        log(f"  {dl_id} FAILED: {e.body[:100]}")
log(f"Dynamic Laws created: {dls_created} / 15 (skipped if already existed)")

# Additional PAs
print()
ADDITIONAL_PAS = [
    ("PA-002", "Generate test data for sentiment classifier", "4 - Build & Generate", "macro-3", "phase-4", 4, True, True),
    ("PA-003", "Draft API documentation for handover", "6 - Deliver & Monitor", "macro-3", "phase-6", 3, False, True),
    ("PA-004", "Quick refactor of edge-case handling", "5 - Coordinate & Validate", "macro-3", "phase-5", 2, False, False),
    ("PA-005", "Synthesize lessons learned for retrospective", "7 - Feedback & Evolve", "macro-4", "phase-7", 5, True, True),
]
for pa_id, title, sub_phase, macro, phase, quality, reusable, trace_complete in ADDITIONAL_PAS:
    if find_issue_by_summary(f"{pa_id} - {title[:30]}"):
        continue
    desc_adf = adf([
        panel(f"PA {pa_id} linked to {wave_key}. Quality {quality}/5.", "info" if trace_complete else "warning"),
        h("Identification"),
        ul([
            f"PA-ID: {pa_id}",
            f"Sub-Phase: {sub_phase}",
            f"Quality: {quality}/5",
            f"Reusable: {'Yes' if reusable else 'No'}",
        ]),
        h("Traceability Thread"),
        p("Model: Anthropic / Claude / claude-sonnet-4-5-20250929"),
        p("Config: temperature=0.2, top_p=1.0"),
    ])
    labels = ["d-poaf", "prompt-action", macro, phase, "wave-surfer", f"quality-{quality}"]
    if reusable:
        labels.append("reusable-prompt")
    if trace_complete:
        labels.append("traceability-thread-complete")
    try:
        create_issue(f"{pa_id} - {title}", desc_adf, "Task", labels, parent_key=wave_key)
        log(f"  {pa_id} - Q={quality}, reusable={reusable}, trace={trace_complete}")
    except APIError as e:
        log(f"  {pa_id} FAILED: {e.body[:100]}")

# Partial Proof
print()
if not find_issue_by_summary("PROOF-EXAMPLE-002"):
    partial_desc = adf([
        panel("Sample Proof Record with PARTIAL status. PoV not fully met.", "warning"),
        h("PoD - Proof of Delivery"),
        ul(["Status: APPROVED", "Deliverables: Feature delivered", "Validation: 95% accuracy met"]),
        h("PoV - Proof of Value"),
        ul(["Status: PARTIAL", "Expected: Reduce manual triage by 70% in 2 weeks", "Achieved: 45% reduction in 3 weeks"]),
        h("PoR - Proof of Reliability"),
        ul(["Status: APPROVED", "Compliance: Audit logs in place, MTTR within SLA"]),
        h("Lessons Learned"),
        p("Value criterion too aggressive for pilot scope. Next Wave should re-scope PoV criterion."),
    ])
    try:
        create_issue(
            "PROOF-EXAMPLE-002 - Partial closure example (PoV not fully met)",
            partial_desc, "Task",
            ["d-poaf", "proof-record", "macro-4", "phase-7",
             "pod-approved", "pov-partial", "por-approved", "wave-captain-signed"],
            parent_key=wave_key,
        )
        log("  PROOF-EXAMPLE-002 (PARTIAL) created")
    except APIError as e:
        log(f"  PROOF-EXAMPLE-002 FAILED: {e.body[:100]}")

# ============================================================
# PHASE 3: Sprint
# ============================================================
section("PHASE 3 - Sprint creation + ticket assignment")

# Discover all D-POAF tickets
log("Searching all D-POAF tickets to categorize...")
try:
    search = call("POST", f"{BASE_API_V3}/search/jql", body={
        "jql": f'project = {PROJECT_KEY} ORDER BY created ASC',
        "fields": ["summary", "labels", "issuetype"],
        "maxResults": 100,
    })
    issues = search.get("issues", [])
    log(f"  Found {len(issues)} tickets total")
except APIError as e:
    log(f"  Search failed: {e}")
    issues = []

waves, pas, proofs, dls = [], [], [], []
for issue in issues:
    labels = issue.get("fields", {}).get("labels", [])
    summary = issue.get("fields", {}).get("summary", "")
    key = issue["key"]
    if "wave" in labels:
        waves.append(key)
    elif "prompt-action" in labels:
        pas.append(key)
    elif "proof-record" in labels:
        proofs.append(key)
    elif "dynamic-law" in labels:
        dls.append(key)
log(f"  Waves: {len(waves)} | PAs: {len(pas)} | Proofs: {len(proofs)} | DLs: {len(dls)}")

# Find board
print()
log("Locating board...")
board_id = None
try:
    boards = call("GET", f"{BASE_AGILE}/board", query={"projectKeyOrId": PROJECT_KEY})
    if boards.get("values"):
        board_id = boards["values"][0]["id"]
        log(f"  Board ID: {board_id}")
except APIError as e:
    log(f"  No board found: {e}")

# Create + start sprint
if board_id:
    sprint_name = f"D-POAF Sprint 1 - {datetime.date.today().isoformat()}"
    log(f"Creating sprint: {sprint_name}...")
    try:
        sprint = call("POST", f"{BASE_AGILE}/sprint", body={
            "name": sprint_name,
            "originBoardId": board_id,
            "goal": "Pilot D-POAF Wave through full lifecycle",
        })
        sprint_id = sprint["id"]
        log(f"  Sprint created: id={sprint_id}")

        # Add Wave + PAs + Proofs (NOT DLs)
        sprint_tickets = waves + pas + proofs
        if sprint_tickets:
            log(f"Adding {len(sprint_tickets)} tickets to sprint...")
            try:
                call("POST", f"{BASE_AGILE}/sprint/{sprint_id}/issue", body={"issues": sprint_tickets})
                log(f"  OK - {len(sprint_tickets)} tickets in sprint")
            except APIError as e:
                log(f"  Batch add failed: {e.body[:150]}. Adding individually...")
                for k in sprint_tickets:
                    try:
                        call("POST", f"{BASE_AGILE}/sprint/{sprint_id}/issue", body={"issues": [k]})
                    except APIError:
                        pass

        # Try to start the sprint
        log("Starting sprint...")
        now = datetime.datetime.now(datetime.timezone.utc)
        end = now + datetime.timedelta(days=14)
        try:
            call("PUT", f"{BASE_AGILE}/sprint/{sprint_id}", body={
                "state": "active",
                "startDate": now.isoformat(),
                "endDate": end.isoformat(),
            })
            log(f"  OK - Sprint active until {end.date()}")
        except APIError as e:
            log(f"  Auto-start failed - YOU MUST START IT MANUALLY in Backlog UI")
            log(f"  Error: {e.body[:150]}")
    except APIError as e:
        log(f"  Sprint creation failed: {e.body[:200]}")
else:
    log("  No board, skipping sprint creation")

# ============================================================
# PHASE 4: Saved JQL Filters
# ============================================================
section("PHASE 4 - 8 saved JQL filters")

FILTERS = [
    ("D-POAF - Active Waves",
     "All D-POAF Waves currently in flight (Epic + label=wave, not Closed).",
     f'project = {PROJECT_KEY} AND issuetype = Epic AND labels = "wave" AND status != Done'),
    ("D-POAF - PromptRegister (all PAs)",
     "All Prompt Actions logged. The D-POAF PromptRegister, per DL-006.",
     f'project = {PROJECT_KEY} AND labels = "prompt-action" ORDER BY created DESC'),
    ("D-POAF - Reusable Prompt Library",
     "Prompts approved as reusable (Quality >=4, per DL-008).",
     f'project = {PROJECT_KEY} AND labels = "prompt-action" AND labels = "reusable-prompt"'),
    ("D-POAF - DL-006 Compliance Violations",
     "Prompt Actions missing the mandatory Traceability Thread.",
     f'project = {PROJECT_KEY} AND labels = "prompt-action" AND labels != "traceability-thread-complete"'),
    ("D-POAF - Dynamic Laws (governance baseline)",
     "The 15 Dynamic Laws governing AI-enabled software delivery.",
     f'project = {PROJECT_KEY} AND labels = "dynamic-law" ORDER BY summary ASC'),
    ("D-POAF - Proof Records",
     "All Wave closures (PoD/PoV/PoR records).",
     f'project = {PROJECT_KEY} AND labels = "proof-record" ORDER BY created DESC'),
    ("D-POAF - Stale Waves",
     "Waves not updated in 14 days. Likely stuck or abandoned.",
     f'project = {PROJECT_KEY} AND issuetype = Epic AND labels = "wave" AND status != Done AND updated <= -14d'),
    ("D-POAF - Universal Outcome Search",
     "Find any issue by outcome (PA-ID, commit, keyword). EDIT the JQL to replace REPLACE_WITH_OUTCOME with your search term.",
     f'project = {PROJECT_KEY} AND text ~ "REPLACE_WITH_OUTCOME" ORDER BY issuetype, key'),
    ("D-POAF - Full chain for [Wave]",
     "Show the complete chain for a Wave: Wave Epic + all PAs + all Proofs. EDIT the JQL to replace the Wave key.",
     f'project = {PROJECT_KEY} AND (key = "{waves[0] if waves else "DPOAF-1"}" OR parent = "{waves[0] if waves else "DPOAF-1"}") ORDER BY issuetype DESC, created ASC'),
]

filters_created = 0
for name, desc, jql in FILTERS:
    log(f"Creating filter: {name}...")
    try:
        result = call("POST", f"{BASE_API_V3}/filter", body={
            "name": name,
            "description": desc,
            "jql": jql,
        })
        filters_created += 1
        log(f"  OK - id={result.get('id')}")
    except APIError as e:
        if "name" in e.body.lower() and "exist" in e.body.lower():
            log(f"  Already exists - skip")
        else:
            log(f"  FAILED: {e.body[:150]}")
log(f"Filters created: {filters_created} / {len(FILTERS)}")

# ============================================================
# PHASE 5: Dashboard + gadgets
# ============================================================
section("PHASE 5 - Dashboard 'D-POAF Control Room' + 4 gadgets")

# Check if dashboard exists
dashboard_id = None
try:
    search = call("GET", f"{BASE_API_V3}/dashboard/search", query={"dashboardName": "D-POAF Control Room"})
    found = [d for d in search.get("values", []) if d.get("name") == "D-POAF Control Room"]
    if found:
        dashboard_id = found[0]["id"]
        log(f"Dashboard already exists: id={dashboard_id}")
except APIError:
    pass

# Create dashboard if needed
if not dashboard_id:
    log("Creating dashboard...")
    body = {
        "name": "D-POAF Control Room",
        "description": "Operational view of D-POAF Waves, Prompt Actions, Proof Records, and compliance.",
        "sharePermissions": [{"type": "loggedin"}],
    }
    if my_account_id:
        body["editPermissions"] = [{"type": "user", "user": {"accountId": my_account_id}}]
    else:
        body["editPermissions"] = [{"type": "loggedin"}]
    try:
        dashboard = call("POST", f"{BASE_API_V3}/dashboard", body=body)
        dashboard_id = dashboard.get("id")
        log(f"  OK - id={dashboard_id}")
    except APIError as e:
        log(f"  FAILED: {e.body[:200]}")
        # Try minimal payload
        try:
            dashboard = call("POST", f"{BASE_API_V3}/dashboard", body={
                "name": "D-POAF Control Room",
                "description": "D-POAF operational dashboard",
            })
            dashboard_id = dashboard.get("id")
            log(f"  Fallback OK - id={dashboard_id}")
        except APIError as e2:
            log(f"  Even minimal failed: {e2.body[:200]}")

# Discover gadgets (bilingual EN + FR)
filter_results_gadget = None
if dashboard_id:
    log("Discovering available gadgets (bilingual)...")
    try:
        gadgets_resp = call("GET", f"{BASE_API_V3}/dashboard/gadgets")
        gadgets = gadgets_resp.get("gadgets", [])
        for g in gadgets:
            title = g.get("title", "").lower()
            if ("filter" in title and "result" in title) or ("résultat" in title and "filtre" in title) or ("resultat" in title and "filtre" in title):
                filter_results_gadget = g
                log(f"  Found 'Filter Results' gadget: {g.get('title')}")
                break
        if not filter_results_gadget:
            log(f"  WARNING: 'Filter Results' gadget not found among {len(gadgets)} gadgets")
    except APIError as e:
        log(f"  Discovery failed: {e}")

# Add 4 gadgets
gadgets_added = 0
if dashboard_id and filter_results_gadget:
    uri = filter_results_gadget.get("uri")
    log(f"Adding 4 gadgets to dashboard...")
    GADGET_LAYOUT = [
        ("Active Waves", "blue", {"column": 0, "row": 0}),
        ("DL-006 Compliance Violations", "red", {"column": 1, "row": 0}),
        ("PromptRegister", "purple", {"column": 0, "row": 1}),
        ("Reusable Prompt Library", "green", {"column": 1, "row": 1}),
    ]
    for title, color, position in GADGET_LAYOUT:
        try:
            payload = {"color": color, "uri": uri, "position": position, "title": title,
                       "ignoreUriAndModuleKeyValidation": False}
            call("POST", f"{BASE_API_V3}/dashboard/{dashboard_id}/gadget", body=payload)
            gadgets_added += 1
            log(f"  [{title}] added (color: {color})")
        except APIError as e:
            log(f"  [{title}] FAILED: {e.body[:150]}")
log(f"Gadgets added: {gadgets_added} / 4")

# ============================================================
# PHASE 6: Final report with manual steps
# ============================================================
section("PHASE 6 - Installation summary + MANUAL STEPS")

print()
print(f"  Project URL: {URL}/jira/software/projects/{PROJECT_KEY}/board")
print(f"  Dashboard:   {URL}/jira/dashboards/{dashboard_id if dashboard_id else 'N/A'}")
print(f"  Filters:     {URL}/jira/filters")
print()
print("  Created:")
print(f"    - 1 Wave Epic ({wave_key})")
print(f"    - 5 Prompt Actions (PA-001 to PA-005)")
print(f"    - 2 Proof Records (1 approved + 1 partial)")
print(f"    - {dls_created} Dynamic Laws (newly created in this run)")
print(f"    - {filters_created} JQL filters")
print(f"    - 1 Dashboard with {gadgets_added} gadgets")
print()

section("MANUAL STEPS REMAINING (5-10 minutes total)")

print()
print("These steps cannot be automated due to Atlassian API limitations.")
print()

print("STEP A - Board: rename columns to macro-phases (5 min)")
print("---------------------------------------------------------")
print(f"  1. Open the board: {URL}/jira/software/projects/{PROJECT_KEY}/board")
print(f"  2. Project settings (gear) -> Tableau (Board) -> Colonnes (Columns)")
print(f"  3. Rename and add columns to match macro-phases:")
print(f"     - '1. Instruct & Scope'")
print(f"     - '2. Shape & Align'")
print(f"     - '3. Execute & Evolve'  <- {wave_key} lives here (Sub-Phase=4)")
print(f"     - '4. Learn & Adapt'")
print(f"     - 'Done' (keep as final)")
print(f"  4. Drag tickets into the correct column based on their macro-X label")
print()

print("STEP B - Filters: star them in favorites (1 min)")
print("---------------------------------------------------------")
print(f"  1. Open the filters list: {URL}/jira/filters")
print(f"  2. Search 'D-POAF' in the search box")
print(f"  3. Click the star (⭐) next to each D-POAF filter")
print(f"  4. Now they appear in the sidebar under Favoris > Filtres")
print()

print("STEP C - Sprint: start it manually if auto-start failed (30 sec)")
print("---------------------------------------------------------")
print(f"  1. Open the Backlog: {URL}/jira/software/projects/{PROJECT_KEY}/backlog")
print(f"  2. Find 'D-POAF Sprint 1 - {datetime.date.today().isoformat()}'")
print(f"  3. Click 'Démarrer un sprint' (Start sprint)")
print(f"  4. Confirm duration (2 weeks) and goal")
print()

print("STEP D - Dashboard: configure 4 gadgets (1 min total)")
print("---------------------------------------------------------")
print(f"  Open: {URL}/jira/dashboards/{dashboard_id if dashboard_id else ''}")
print(f"  For each gadget, click the gear (⚙) icon and select the matching filter:")
print(f"    - 'Active Waves' (blue, top-left)        -> D-POAF - Active Waves")
print(f"    - 'DL-006 Violations' (red, top-right)   -> D-POAF - DL-006 Compliance Violations")
print(f"    - 'PromptRegister' (purple, bottom-left) -> D-POAF - PromptRegister (all PAs)")
print(f"    - 'Reusable' (green, bottom-right)       -> D-POAF - Reusable Prompt Library")
print(f"  Set 'Number of results' to 10 for each. Save.")
print(f"  Then click the star (⭐) on the dashboard to favorite it.")
print()

print("STEP E - Traceability: how to walk Outcome -> Intent (read only)")
print("---------------------------------------------------------")
print(f"  Scenario: You found a commit '[AI:claude-sonnet-4-5:PA-001]' and want to know why.")
print()
print(f"  Method 1 (3 clicks, NATIVE Jira navigation):")
print(f"    1. Search bar (top) -> type 'PA-001' -> click the matching PA")
print(f"    2. On the PA page, look at the right panel -> click 'Epic Link' value")
print(f"    3. You arrive at the Wave Epic -> 'Tickets enfants' shows all PAs + Proofs")
print(f"       -> 'Description' shows Business Objective = the intent")
print(f"    Total time: ~15 seconds")
print()
print(f"  Method 2 (JQL filter, parameterized):")
print(f"    1. Open filter 'D-POAF - Universal Outcome Search'")
print(f"    2. Click 'Modifier le JQL' (Edit JQL)")
print(f"    3. Replace 'REPLACE_WITH_OUTCOME' with your outcome (e.g., 'PA-001')")
print(f"    4. Exécuter (Run)")
print(f"    5. Click on the matching issue to navigate further")
print()
print(f"  Method 3 (Full Wave chain in one view):")
print(f"    1. Open filter 'D-POAF - Full chain for [Wave]'")
print(f"    2. Click 'Modifier le JQL'")
print(f"    3. Replace '{waves[0] if waves else 'DPOAF-1'}' (twice) with target Wave key")
print(f"    4. Exécuter -> see Wave + all PAs + all Proofs in one list")
print()

section("INSTALLATION COMPLETE")
print()
print(f"  Total D-POAF tickets: 1 Wave + 5 PAs + 2 Proofs + 15 DLs = 23 issues")
print(f"  JQL filters: {filters_created}")
print(f"  Dashboard with {gadgets_added} gadgets")
print()
print(f"  After completing the 5 manual steps above, your D-POAF Jira is fully operational.")
print()
print("Done.")
