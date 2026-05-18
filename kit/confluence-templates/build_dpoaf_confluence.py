#!/usr/bin/env python3
"""
D-POAF (R) Confluence Space Builder - v1.1
Automatically installs the D-POAF (R) Governance Space in Confluence Cloud.

INCLUDES:
- 3 page templates (Wave Scope, Prompt Action, Proof Record) with Storage Format
- 3 one-shot pages (Practical Guide, Wave Lifecycle, Dynamic Laws)
- 3 parent index pages (Waves, Prompt Actions, Proof Records) with Children macros
- 1 sample lifecycle (WAVE-EXAMPLE-001 -> PA-001 -> PROOF-EXAMPLE-001)

PREREQUISITES:
1. A Confluence Cloud Space (already created)
2. An API token from https://id.atlassian.com/manage-profile/security/api-tokens
3. The XML templates in the folder dpoaf_confluence_xml/

USAGE (PowerShell):
    $env:CONFLUENCE_URL = "https://dpoaf.atlassian.net"
    $env:CONFLUENCE_EMAIL = "dpoaf.inovionix@gmail.com"
    $env:CONFLUENCE_TOKEN = "ATATT3xFfGF0..."
    $env:CONFLUENCE_SPACE_KEY = "DPOAFGOV"
    python build_dpoaf_confluence.py

The script will print URLs of the created pages and templates.

Licensed under CC BY 4.0 - Azzeddine IHSINE & Sara IHSINE - d-poaf.org
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
import urllib.parse
import re

# ============================================================
# Configuration
# ============================================================
URL = os.environ.get("CONFLUENCE_URL")
EMAIL = os.environ.get("CONFLUENCE_EMAIL")
TOKEN = os.environ.get("CONFLUENCE_TOKEN")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY")

if not all([URL, EMAIL, TOKEN, SPACE_KEY]):
    print("ERROR: Set all 4 environment variables before running:")
    print("  CONFLUENCE_URL = https://yoursite.atlassian.net")
    print("  CONFLUENCE_EMAIL = your.email@example.com")
    print("  CONFLUENCE_TOKEN = ATATT3xFfGF0...")
    print("  CONFLUENCE_SPACE_KEY = DPOAFGOV")
    print()
    print("Example (PowerShell):")
    print('  $env:CONFLUENCE_URL="https://dpoaf.atlassian.net"')
    print('  $env:CONFLUENCE_EMAIL="dpoaf.inovionix@gmail.com"')
    print('  $env:CONFLUENCE_TOKEN="ATATT3xFfGF0..."')
    print('  $env:CONFLUENCE_SPACE_KEY="DPOAFGOV"')
    print("  python build_dpoaf_confluence.py")
    sys.exit(1)

URL = URL.rstrip("/")
BASE_API = f"{URL}/wiki/rest/api"

# Basic Auth header
auth_str = f"{EMAIL}:{TOKEN}"
auth_b64 = base64.b64encode(auth_str.encode()).decode()
AUTH_HEADER = f"Basic {auth_b64}"

# Path to XML templates folder (same dir as the script, or override via env)
XML_DIR = os.environ.get(
    "XML_DIR",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "dpoaf_confluence_xml"),
)

# ============================================================
# HTTP helpers
# ============================================================
class APIError(Exception):
    pass

def api_call(method, path, body=None, query=None):
    """Raw HTTP call to the Confluence API."""
    url = f"{BASE_API}/{path}"
    if query:
        url += "?" + urllib.parse.urlencode(query)
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", AUTH_HEADER)
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            text = resp.read().decode("utf-8")
            return json.loads(text) if text else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise APIError(f"HTTP {e.code} on {method} {path}\n{err_body}")
    except urllib.error.URLError as e:
        raise APIError(f"Network error on {method} {path}: {e.reason}")

def log(msg):
    print(f"  -> {msg}", flush=True)

# ============================================================
# Storage Format helpers
# ============================================================
def strip_xml_comments(xml_str):
    """Remove HTML/XML comments from the file (the header documentation)."""
    return re.sub(r"<!--.*?-->", "", xml_str, flags=re.DOTALL).strip()

def load_xml(filename):
    """Load and clean an XML template file."""
    path = os.path.join(XML_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"XML file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return strip_xml_comments(f.read())

def storage_payload(xml_content):
    """Wrap XML content in the Confluence storage format payload."""
    return {
        "storage": {
            "value": xml_content,
            "representation": "storage",
        }
    }

# ============================================================
# Confluence operations
# ============================================================
def get_space_id():
    """Resolve the numeric Space ID from the Space Key."""
    log(f"Resolving space ID for key '{SPACE_KEY}'...")
    result = api_call("GET", "space", query={"spaceKey": SPACE_KEY})
    if not result.get("results"):
        raise APIError(f"Space '{SPACE_KEY}' not found or not accessible")
    space = result["results"][0]
    log(f"  Space ID: {space['id']} - {space['name']}")
    return space["id"]

def create_template(name, description, xml_content, labels=None):
    """Create a page template in the space."""
    body = {
        "name": name,
        "templateType": "page",
        "space": {"key": SPACE_KEY},
        "description": description,
        "body": storage_payload(xml_content),
        "labels": [{"prefix": "global", "name": l} for l in (labels or [])],
    }
    return api_call("POST", "template", body=body)

def create_page(title, xml_content, parent_id=None):
    """Create a regular page in the space."""
    body = {
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "body": storage_payload(xml_content),
    }
    if parent_id:
        body["ancestors"] = [{"id": parent_id}]
    return api_call("POST", "content", body=body)

def page_url(page_obj):
    """Build a clickable URL for a created page."""
    webui = page_obj.get("_links", {}).get("webui", "")
    return f"{URL}/wiki{webui}" if webui else "(no URL)"

# ============================================================
# Build script
# ============================================================
print()
print("=" * 60)
print("D-POAF (R) Confluence Space Builder - v1.1")
print("=" * 60)
print(f"Confluence URL: {URL}")
print(f"Space key:      {SPACE_KEY}")
print(f"User:           {EMAIL}")
print(f"XML dir:        {XML_DIR}")
print("-" * 60)
print()

# Sanity check: XML dir exists
if not os.path.isdir(XML_DIR):
    print(f"ERROR: XML directory not found: {XML_DIR}")
    print("Make sure the 'dpoaf_confluence_xml' folder is next to this script,")
    print("or set the XML_DIR environment variable.")
    sys.exit(1)

# Test auth + resolve space
try:
    space_id = get_space_id()
except APIError as e:
    print(f"ERROR: {e}")
    print()
    print("Common causes:")
    print("  - Wrong email or API token (re-generate from id.atlassian.com)")
    print("  - Wrong Space key (check from your Confluence URL)")
    print("  - Wrong CONFLUENCE_URL (must be https://yoursite.atlassian.net)")
    sys.exit(1)

# ============================================================
# Phase 1: Page Templates
# ============================================================
print()
print("Phase 1: Creating 3 page templates")
print("-" * 60)

templates_info = [
    {
        "file":  "01_wave_scope_template.xml",
        "name":  "D-POAF Wave Scope",
        "desc":  "Open a new D-POAF Wave. Use at the START of every project or feature.",
        "labels": ["d-poaf", "wave", "governance"],
    },
    {
        "file":  "02_prompt_action_template.xml",
        "name":  "D-POAF Prompt Action",
        "desc":  "Log a single AI generation event. ONE template per AI invocation (DL-006).",
        "labels": ["d-poaf", "prompt-action", "traceability"],
    },
    {
        "file":  "03_proof_record_template.xml",
        "name":  "D-POAF Proof Record",
        "desc":  "Close a Wave with a signed Proof Record. PoD, PoV, PoR with evidence.",
        "labels": ["d-poaf", "proof-record", "closure"],
    },
]

template_ids = {}
for t in templates_info:
    log(f"Creating template: {t['name']}...")
    try:
        xml = load_xml(t["file"])
        result = create_template(t["name"], t["desc"], xml, labels=t["labels"])
        template_ids[t["name"]] = result.get("templateId", "?")
        log(f"  OK - templateId: {template_ids[t['name']]}")
    except APIError as e:
        log(f"  FAILED: {e}")
        # Continue with other templates rather than aborting
        continue

print()
print(f"Templates created: {len(template_ids)} / 3")

# ============================================================
# Phase 2: One-shot reference pages
# ============================================================
print()
print("Phase 2: Creating 3 one-shot reference pages")
print("-" * 60)

oneshot_info = [
    {
        "file":  "05_practical_guide_page.xml",
        "title": "Practical Guide",
    },
    {
        "file":  "06_wave_lifecycle_page.xml",
        "title": "Wave Lifecycle",
    },
    {
        "file":  "04_dynamic_laws_page.xml",
        "title": "Dynamic Laws",
    },
]

oneshot_pages = {}
for p in oneshot_info:
    log(f"Creating page: {p['title']}...")
    try:
        xml = load_xml(p["file"])
        result = create_page(p["title"], xml)
        oneshot_pages[p["title"]] = result
        log(f"  OK - {page_url(result)}")
    except APIError as e:
        log(f"  FAILED: {e}")
        continue

print()
print(f"Reference pages created: {len(oneshot_pages)} / 3")

# ============================================================
# Phase 3: Parent index pages
# ============================================================
print()
print("Phase 3: Creating 3 parent index pages")
print("-" * 60)

CHILDREN_MACRO = """
<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>All children pages are auto-listed below. Create a new entry from the
    <strong>+ Create</strong> button using the matching D-POAF template.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<ac:structured-macro ac:name="children">
  <ac:parameter ac:name="sort">creation</ac:parameter>
  <ac:parameter ac:name="reverse">true</ac:parameter>
  <ac:parameter ac:name="excerpt">true</ac:parameter>
</ac:structured-macro>
"""

parent_info = [
    {"emoji": "🌊", "title": "Waves",          "intro": "Every D-POAF Wave Scope created in this space is listed below."},
    {"emoji": "🤖", "title": "Prompt Actions", "intro": "Every AI invocation logged in this space is listed below (DL-006)."},
    {"emoji": "✅", "title": "Proof Records",  "intro": "Every signed Proof Record (PoD/PoV/PoR with sign-offs) closing a Wave."},
]

parent_pages = {}
for p in parent_info:
    full_title = f"{p['emoji']} {p['title']}"
    log(f"Creating parent page: {full_title}...")
    intro_xml = f"<p>{p['intro']}</p>"
    page_xml = intro_xml + CHILDREN_MACRO
    try:
        result = create_page(full_title, page_xml)
        parent_pages[p["title"]] = result
        log(f"  OK - {page_url(result)}")
    except APIError as e:
        log(f"  FAILED: {e}")
        continue

print()
print(f"Parent pages created: {len(parent_pages)} / 3")

# ============================================================
# Phase 4: Sample lifecycle (1 Wave + 1 PA + 1 Proof linked)
# ============================================================
print()
print("Phase 4: Creating sample lifecycle (1 Wave + 1 PA + 1 Proof)")
print("-" * 60)

# 4.1 Sample Wave
SAMPLE_WAVE_XML = """
<h1>🌊 WAVE-EXAMPLE-001 — Customer Feedback Categorization (Pilot)</h1>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>This is a sample Wave demonstrating the complete D-POAF lifecycle. Replace it with your own Wave when ready, or delete it.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>Identification</h2>
<table><tbody>
<tr><th>Wave ID</th><td><strong>WAVE-EXAMPLE-001</strong></td></tr>
<tr><th>Wave Name</th><td>Customer Feedback Categorization — Pilot</td></tr>
<tr><th>Wave Profile</th><td>Deliver Wave</td></tr>
<tr><th>Wave Captain</th><td>Sara IHSINE</td></tr>
<tr><th>Business Sponsor</th><td>Inovionix CEO</td></tr>
<tr><th>Date Opened</th><td><time datetime="2026-05-01" /></td></tr>
<tr><th>Status</th><td>
  <ac:structured-macro ac:name="status">
    <ac:parameter ac:name="colour">Blue</ac:parameter>
    <ac:parameter ac:name="title">Active</ac:parameter>
  </ac:structured-macro>
</td></tr>
</tbody></table>

<h2>★ Wave Lifecycle Position</h2>
<table><tbody>
<tr><th>Macro-Phase</th><td>
  <ac:structured-macro ac:name="status">
    <ac:parameter ac:name="colour">Purple</ac:parameter>
    <ac:parameter ac:name="title">3. Execute &amp; Evolve</ac:parameter>
  </ac:structured-macro>
</td></tr>
<tr><th>Current Sub-Phase</th><td>4 - Build &amp; Generate</td></tr>
</tbody></table>

<h2>★ Sprint &amp; Repository Association</h2>
<table><tbody>
<tr><th>Sprint ID</th><td>SPRINT-2026-W12</td></tr>
<tr><th>Sprint URL</th><td><a href="https://example.atlassian.net/jira/.../sprints/Wsprint">example.atlassian.net/sprints/Wsprint</a></td></tr>
<tr><th>Linked Jira Epic</th><td><a href="https://example.atlassian.net/browse/OJ-123">example.atlassian.net/browse/OJ-123</a></td></tr>
<tr><th>Repository</th><td><a href="https://github.com/myorg/sentiment-classifier">github.com/myorg/sentiment-classifier</a></td></tr>
<tr><th>Working Branch</th><td><code>feature/WAVE-EXAMPLE-001</code></td></tr>
<tr><th>Release Tag</th><td><em>(set at Wave close)</em></td></tr>
</tbody></table>

<h2>Business Objective</h2>
<p>Build a sentiment classifier for customer reviews. Target: 95% accuracy across 6 categories (positive, negative, neutral, mixed, off-topic, spam). Reduce manual triage time on customer feedback.</p>

<h2>Scope</h2>
<h3>In Scope</h3>
<ul>
<li>Classification function (Python)</li>
<li>REST API endpoint</li>
<li>Batch processing for backlog</li>
<li>Test suite covering all 6 categories</li>
<li>API integration documentation</li>
</ul>
<h3>Out of Scope</h3>
<ul>
<li>Multilingual support (English only)</li>
<li>Real-time streaming</li>
<li>CRM integration (next Wave)</li>
</ul>

<h2>AI Tools Authorized</h2>
<p>Claude (claude-sonnet-4-5)</p>

<h2>Proof Model (PoD / PoV / PoR)</h2>
<table><tbody>
<tr><th>PoD Criterion</th><td>≥95% accuracy on test dataset. All 6 categories functional.</td></tr>
<tr><th>PoV Criterion</th><td>Client deploys API independently within 2 weeks of handover.</td></tr>
<tr><th>PoR Criterion</th><td>N/A — decision-support tool, no autonomous action.</td></tr>
</tbody></table>

<hr/>
<p><em>D-POAF® Framework — Wave Scope v1.1 — d-poaf.org — Licensed CC BY 4.0</em></p>
"""

# 4.2 Sample Prompt Action
SAMPLE_PA_XML = """
<h1>🤖 PA-001 — Build sentiment classifier function</h1>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>This is a sample Prompt Action linked to WAVE-EXAMPLE-001. It demonstrates the Traceability Thread (Model + Configuration + Context) required by Dynamic Law DL-006.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>Identification</h2>
<table><tbody>
<tr><th>PA-ID</th><td><strong>PA-001</strong></td></tr>
<tr><th>Wave</th><td><ac:link><ri:page ri:content-title="🌊 WAVE-EXAMPLE-001 — Customer Feedback Categorization (Pilot)" /></ac:link></td></tr>
<tr><th>Requirement reference</th><td>REQ-CFC-001</td></tr>
<tr><th>Sub-Phase</th><td>3 - Design Prompt Actions</td></tr>
<tr><th>Macro-Phase (derived)</th><td>
  <ac:structured-macro ac:name="status">
    <ac:parameter ac:name="colour">Yellow</ac:parameter>
    <ac:parameter ac:name="title">2. Shape &amp; Align</ac:parameter>
  </ac:structured-macro>
</td></tr>
<tr><th>Role</th><td>Wave Surfer</td></tr>
<tr><th>Date</th><td><time datetime="2026-05-08" /></td></tr>
</tbody></table>

<h2>★ Traceability Thread — Model + Config + Context</h2>

<ac:structured-macro ac:name="warning">
  <ac:rich-text-body>
    <p>These three sections are <strong>mandatory</strong> per Dynamic Law DL-006. Together they let any future auditor reproduce the exact AI generation.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h3>★ Model identity</h3>
<p><code>Anthropic / Claude / claude-sonnet-4-5-20250929</code></p>

<h3>★ Model configuration</h3>
<ac:structured-macro ac:name="code">
  <ac:parameter ac:name="language">yaml</ac:parameter>
  <ac:plain-text-body><![CDATA[
temperature: 0.2
top_p: 1.0
max_tokens: 4000
system_prompt: "sp-team-v1"  (sha256: 8a2c...d3b1)
tools: none
response_format: text
]]></ac:plain-text-body>
</ac:structured-macro>

<h3>★ Context source</h3>
<ul>
<li><code>client_spec_v1.2.pdf</code> (sha256: a3f9...e7c4) section 2.1 — pasted into user message</li>
<li><code>test_v2.csv</code> — referenced as file path</li>
</ul>

<h2>Output</h2>
<table><tbody>
<tr><th>Quality (1-5)</th><td>
  <ac:structured-macro ac:name="status">
    <ac:parameter ac:name="colour">Green</ac:parameter>
    <ac:parameter ac:name="title">5 - Excellent</ac:parameter>
  </ac:structured-macro>
</td></tr>
<tr><th>Reusable?</th><td>Yes (Wave Captain approved)</td></tr>
<tr><th>Status</th><td>
  <ac:structured-macro ac:name="status">
    <ac:parameter ac:name="colour">Blue</ac:parameter>
    <ac:parameter ac:name="title">Active</ac:parameter>
  </ac:structured-macro>
</td></tr>
</tbody></table>

<h2>Linked Repository &amp; PR</h2>
<table><tbody>
<tr><th>Repository</th><td><a href="https://github.com/myorg/sentiment-classifier">github.com/myorg/sentiment-classifier</a></td></tr>
<tr><th>Branch</th><td><code>feature/WAVE-EXAMPLE-001</code></td></tr>
<tr><th>Commit hash</th><td><code>abc123de</code> — tagged [AI:claude-sonnet-4-5:PA-001]</td></tr>
<tr><th>Pull Request URL</th><td><a href="https://github.com/myorg/sentiment-classifier/pull/12">github.com/myorg/.../pull/12</a></td></tr>
<tr><th>Files touched</th><td><code>src/classify_feedback.py</code> / <code>tests/test_classify.py</code></td></tr>
</tbody></table>

<hr/>
<p><em>D-POAF® Framework — Prompt Action v1.1 — d-poaf.org — Licensed CC BY 4.0</em></p>
"""

# 4.3 Sample Proof Record
SAMPLE_PROOF_XML = """
<h1>✅ PROOF-EXAMPLE-001 — Closure of WAVE-EXAMPLE-001</h1>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>This is a sample Proof Record closing WAVE-EXAMPLE-001. PoD ✓ Approved, PoV ✓ Approved, PoR N/A. Required per DL-012.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>Identification</h2>
<table><tbody>
<tr><th>Proof ID</th><td><strong>PROOF-EXAMPLE-001</strong></td></tr>
<tr><th>Wave</th><td><ac:link><ri:page ri:content-title="🌊 WAVE-EXAMPLE-001 — Customer Feedback Categorization (Pilot)" /></ac:link></td></tr>
<tr><th>Date Closed</th><td><time datetime="2026-05-17" /></td></tr>
</tbody></table>

<h2>PoD — Proof of Delivery</h2>
<table><tbody>
<tr><th>Status</th><td>
  <ac:structured-macro ac:name="status">
    <ac:parameter ac:name="colour">Green</ac:parameter>
    <ac:parameter ac:name="title">✓ Approved</ac:parameter>
  </ac:structured-macro>
</td></tr>
<tr><th>Deliverables</th><td>classify_feedback.py (90 lines, commit abc123de), tests/test_classify.py, 6-category coverage report</td></tr>
<tr><th>Validation</th><td>Test suite passes 100% on validation dataset. Accuracy 96.3% (&gt;95% target).</td></tr>
</tbody></table>

<h2>PoV — Proof of Value</h2>
<table><tbody>
<tr><th>Status</th><td>
  <ac:structured-macro ac:name="status">
    <ac:parameter ac:name="colour">Green</ac:parameter>
    <ac:parameter ac:name="title">✓ Approved</ac:parameter>
  </ac:structured-macro>
</td></tr>
<tr><th>Expected</th><td>Client deploys API independently within 2 weeks of handover. Reduce manual triage time on customer feedback.</td></tr>
<tr><th>Achieved</th><td>Client integrated and tested API within 8 days (target ≤14 days). Sentiment classifier reduces manual triage time by 73%. Production deployment scheduled W22.</td></tr>
</tbody></table>

<h2>PoR — Proof of Reliability</h2>
<table><tbody>
<tr><th>Status</th><td>
  <ac:structured-macro ac:name="status">
    <ac:parameter ac:name="colour">Grey</ac:parameter>
    <ac:parameter ac:name="title">N/A</ac:parameter>
  </ac:structured-macro>
</td></tr>
<tr><th>Compliance</th><td>N/A — decision-support tool, no autonomous action. Reliability governance not applicable per DL-012.</td></tr>
</tbody></table>

<h2>Lessons Learned</h2>
<p>Edge cases in mixed-language reviews required prompt refinement (3 iterations). RAGer context preparation took 4 cycles vs estimated 2 — under-scoped. Reusable prompt for sentiment classification approved (Quality=5) — added to Reusable Library. Recommendation: include "language detection step" as a sub-prompt for future Waves on multilingual feedback.</p>

<h2>Sign-offs</h2>
<ul>
<li>Wave Captain — Sara IHSINE</li>
<li>Sponsor — Inovionix CEO</li>
</ul>

<hr/>
<p><em>D-POAF® Framework — Proof Record v1.1 — d-poaf.org — Licensed CC BY 4.0</em></p>
"""

waves_parent_id = parent_pages.get("Waves", {}).get("id")
pas_parent_id = parent_pages.get("Prompt Actions", {}).get("id")
proofs_parent_id = parent_pages.get("Proof Records", {}).get("id")

if waves_parent_id:
    log("Creating sample WAVE-EXAMPLE-001 under 🌊 Waves...")
    try:
        result = create_page(
            "🌊 WAVE-EXAMPLE-001 — Customer Feedback Categorization (Pilot)",
            SAMPLE_WAVE_XML,
            parent_id=waves_parent_id,
        )
        log(f"  OK - {page_url(result)}")
    except APIError as e:
        log(f"  FAILED: {e}")

if pas_parent_id:
    log("Creating sample PA-001 under 🤖 Prompt Actions...")
    try:
        result = create_page(
            "🤖 PA-001 — Build sentiment classifier function",
            SAMPLE_PA_XML,
            parent_id=pas_parent_id,
        )
        log(f"  OK - {page_url(result)}")
    except APIError as e:
        log(f"  FAILED: {e}")

if proofs_parent_id:
    log("Creating sample PROOF-EXAMPLE-001 under ✅ Proof Records...")
    try:
        result = create_page(
            "✅ PROOF-EXAMPLE-001 — Closure of WAVE-EXAMPLE-001",
            SAMPLE_PROOF_XML,
            parent_id=proofs_parent_id,
        )
        log(f"  OK - {page_url(result)}")
    except APIError as e:
        log(f"  FAILED: {e}")

# ============================================================
# Done
# ============================================================
print()
print("=" * 60)
print("✓ D-POAF (R) Confluence Space built successfully")
print("=" * 60)
print()
print(f"Open your space here: {URL}/wiki/spaces/{SPACE_KEY}/overview")
print()
print("Next steps:")
print("  1. Review the Practical Guide and Wave Lifecycle pages")
print("  2. Adopt the 15 Dynamic Laws with your team")
print("  3. Test: click + Create -> Templates -> D-POAF Wave Scope to open a new Wave")
print("  4. Optional: pin the 3 reference pages at the top of the space sidebar")
print()
print("Confluence-side TODOs (1-2 min each):")
print("  - Pin Practical Guide / Wave Lifecycle / Dynamic Laws in the sidebar")
print("  - Disable the default Atlassian blueprints (Space settings -> Templates)")
print("  - Set space permissions when ready to publish (Anonymous Access)")
print()
print("Documentation:")
print("  - Framework reference: https://d-poaf.org")
print("  - GitHub starter repo: https://github.com/INOVIONIX/D-POAF")
print()
print("Done.")
