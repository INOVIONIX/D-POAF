#!/usr/bin/env python3
"""
D-POAF (R) Confluence Patch v1.1 -> v1.2
Adds the 3 missing reference pages to the Space:
- Wave Lifecycle (if missing)
- Workflow (NEW - day-by-day operations)
- Traceability (NEW - how to trace back from artifact to business intent)

USAGE (PowerShell):
    $env:CONFLUENCE_URL = "https://dpoaf.atlassian.net"
    $env:CONFLUENCE_EMAIL = "dpoaf.inovionix@gmail.com"
    $env:CONFLUENCE_TOKEN = "ATATT3xFfGF0..."
    $env:CONFLUENCE_SPACE_KEY = "DPOAFGOV"
    python patch_dpoaf_confluence.py

Licensed under CC BY 4.0 - Azzeddine IHSINE & Sara IHSINE - d-poaf.org
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error
import urllib.parse

URL = os.environ.get("CONFLUENCE_URL")
EMAIL = os.environ.get("CONFLUENCE_EMAIL")
TOKEN = os.environ.get("CONFLUENCE_TOKEN")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY")

if not all([URL, EMAIL, TOKEN, SPACE_KEY]):
    print("ERROR: Set CONFLUENCE_URL, CONFLUENCE_EMAIL, CONFLUENCE_TOKEN, CONFLUENCE_SPACE_KEY.")
    sys.exit(1)

URL = URL.rstrip("/")
BASE_API = f"{URL}/wiki/rest/api"
auth_b64 = base64.b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()
AUTH_HEADER = f"Basic {auth_b64}"

class APIError(Exception):
    pass

def api_call(method, path, body=None, query=None):
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

def log(msg):
    print(f"  -> {msg}", flush=True)

def page_url(page):
    webui = page.get("_links", {}).get("webui", "")
    return f"{URL}/wiki{webui}" if webui else "(no URL)"

def find_page_by_title(title):
    """Return existing page object or None."""
    result = api_call("GET", "content", query={
        "spaceKey": SPACE_KEY,
        "title": title,
        "expand": "version",
    })
    results = result.get("results", [])
    return results[0] if results else None

def create_page(title, xml_content):
    body = {
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "body": {"storage": {"value": xml_content, "representation": "storage"}},
    }
    return api_call("POST", "content", body=body)

# ============================================================
# Page content
# ============================================================

WAVE_LIFECYCLE_XML = """
<h1>📊 Wave Lifecycle — The 4 Macro-Phases</h1>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>Every D-POAF Wave traverses 4 macro-phases. This page is the visual control room: each Wave's current phase is tracked in its Wave Scope page, and the parent <ac:link><ri:page ri:content-title="🌊 Waves" /></ac:link> page lists every active Wave by phase.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>The 4 macro-phases (Canonical Specification v1.1)</h2>

<table>
  <thead>
    <tr><th>#</th><th>Macro-Phase</th><th>Sub-phases</th><th>What happens</th><th>Sprint &amp; Repo activity</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Blue</ac:parameter><ac:parameter ac:name="title">1</ac:parameter></ac:structured-macro></td>
      <td><strong>Instruct &amp; Scope</strong></td>
      <td>1 — Intent &amp; Scope</td>
      <td>Translate intent into a scoped instruction. Wave Scope opens.</td>
      <td><em>None yet.</em></td>
    </tr>
    <tr>
      <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Yellow</ac:parameter><ac:parameter ac:name="title">2</ac:parameter></ac:structured-macro></td>
      <td><strong>Shape &amp; Align</strong></td>
      <td>2 — Contextualize &amp; Extract<br/>3 — Design Prompt Actions</td>
      <td>RAGer prepares context. Wave Surfer designs Prompt Actions.</td>
      <td><strong>Allocate to a sprint here.</strong> Create the working branch in the repo. Link the Jira Epic.</td>
    </tr>
    <tr>
      <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Purple</ac:parameter><ac:parameter ac:name="title">3</ac:parameter></ac:structured-macro></td>
      <td><strong>Execute &amp; Evolve</strong></td>
      <td>4 — Build &amp; Generate<br/>5 — Coordinate &amp; Validate<br/>6 — Deliver &amp; Monitor</td>
      <td>AI invoked; outputs validated; reliability monitored.</td>
      <td><strong>Sprint runs.</strong> Commits with [AI:&lt;model&gt;:PA-ID] tag. PRs reviewed. Release tag at the end.</td>
    </tr>
    <tr>
      <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">4</ac:parameter></ac:structured-macro></td>
      <td><strong>Learn &amp; Adapt</strong></td>
      <td>7 — Feedback &amp; Evolve</td>
      <td>Outcomes synthesized. Intent, governance, standards adapted for the next Wave.</td>
      <td><em>Sprint retrospective. PromptRegister updates. Dynamic Laws amendments if needed.</em></td>
    </tr>
  </tbody>
</table>

<ac:structured-macro ac:name="note">
  <ac:rich-text-body>
    <p><strong>Sprint &amp; Repository association.</strong> Each Wave Scope page has fields for Sprint ID · Sprint URL · Linked Jira Epic · Repository · Branch · Release Tag. These are filled during <strong>Shape &amp; Align</strong> and updated through <strong>Execute &amp; Evolve</strong>.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>Visual loop</h2>

<ac:structured-macro ac:name="code">
  <ac:parameter ac:name="language">text</ac:parameter>
  <ac:plain-text-body><![CDATA[
   ┌─── 1. Instruct & Scope ────┐
   │                             │
   │   ▼                         │
   │  2. Shape & Align ──┐       │
   │   │                  │      │
   │   ▼                  │      │
   │  3. Execute & Evolve │      │
   │   │                  │      │
   │   ▼                  │      │
   │  4. Learn & Adapt ───┘      │
   │   │                         │
   └───┘  back to next Wave
]]></ac:plain-text-body>
</ac:structured-macro>

<h2>Why the 4 macro-phases matter</h2>

<ul>
  <li><strong>For the Wave Captain</strong> — "We're in Execute &amp; Evolve" is enough context to communicate status. No need to dive into the sub-phase.</li>
  <li><strong>For sponsors and stakeholders</strong> — The 4 phases mirror common product lifecycle vocabulary (discover → design → build → learn).</li>
  <li><strong>For governance reviews</strong> — Auditors can see at a glance whether a Wave is in flight (phases 1-3) or in adaptation (phase 4).</li>
  <li><strong>For continuous improvement</strong> — Phase 4 (Learn &amp; Adapt) is what makes D-POAF a <em>living</em> framework rather than a one-shot pipeline.</li>
</ul>

<h2>Source</h2>
<p>The 4 macro-phases are normatively defined in the <a href="https://d-poaf.org/wp-content/uploads/2026/01/Canonical_D_POAF.pdf">D-POAF® Canonical Specification v1.1</a>, §4.1 (Lifecycle Macro-Phases — Wave Lifecycle Core).</p>

<hr/>
<p><em>D-POAF® Framework — Wave Lifecycle v1.1 — d-poaf.org — Licensed under CC BY 4.0</em></p>
"""

WORKFLOW_XML = """
<h1>📋 Workflow — Day-by-Day D-POAF Operations</h1>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>How a Wave Captain, a Wave Surfer, and a RAGer actually <em>use</em> this Space, day by day. Concrete steps, in order.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>The 6 daily operations</h2>

<ac:structured-macro ac:name="table-of-contents" />

<h3>1. Open a new Wave (every new project or feature)</h3>

<p><strong>Who does it:</strong> Wave Captain</p>
<p><strong>When:</strong> Macro-phase 1 (Instruct &amp; Scope)</p>
<p><strong>How:</strong></p>
<ol>
  <li>Click <strong>+ Create</strong> in the top bar</li>
  <li>Choose <strong>🌊 D-POAF Wave Scope</strong> from the Templates list</li>
  <li>Fill the Identification section: Wave ID, Name, Profile, Captain, Sponsor</li>
  <li>Fill the Business Objective + Scope (in/out)</li>
  <li>Fill PoD / PoV / PoR criteria (the exit conditions of the Wave)</li>
  <li>Save the page under <ac:link><ri:page ri:content-title="🌊 Waves" /></ac:link></li>
</ol>

<ac:structured-macro ac:name="tip">
  <ac:rich-text-body>
    <p>Use a stable Wave ID format: <code>WAVE-YYYY-NNN</code> (e.g., WAVE-2026-001). Sortable and clear.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h3>2. Log every Prompt Action BEFORE invoking the AI</h3>

<p><strong>Who does it:</strong> Wave Surfer (the person prompting)</p>
<p><strong>When:</strong> Before sending any prompt to the AI</p>
<p><strong>Why it's mandatory:</strong> <ac:link><ri:page ri:content-title="Dynamic Laws" /></ac:link> DL-006 — PromptRegister is Mandatory. Retroactive logging defeats traceability.</p>
<p><strong>How:</strong></p>
<ol>
  <li>Click <strong>+ Create</strong> → <strong>🤖 D-POAF Prompt Action</strong></li>
  <li>Fill the Identification: PA-ID, Wave (link to parent Wave page), Sub-Phase, Role, Date</li>
  <li>Fill the <strong>★ Traceability Thread</strong> (mandatory):
    <ul>
      <li>★ Model identity — provider/model/exact version</li>
      <li>★ Model configuration — temperature, top_p, max_tokens, system prompt, tools, etc.</li>
      <li>★ Context source — what documents/data fed the prompt</li>
    </ul>
  </li>
  <li>Paste the full Prompt text (or its sha256 hash if sensitive)</li>
  <li>Save the page under <ac:link><ri:page ri:content-title="🤖 Prompt Actions" /></ac:link></li>
  <li><strong>Now</strong> invoke the AI</li>
  <li>After generation, come back to the PA page and fill: Output summary, Quality (1-5), Reusable? (Yes/No), Status</li>
</ol>

<h3>3. Commit AI-generated code with proper tagging</h3>

<p><strong>Who does it:</strong> Wave Surfer (after AI generation is validated)</p>
<p><strong>How:</strong></p>
<ol>
  <li>Code is reviewed by a second human (DL-002 — No Blind Acceptance)</li>
  <li>Commit message uses the D-POAF tag format:
    <ac:structured-macro ac:name="code">
      <ac:parameter ac:name="language">text</ac:parameter>
      <ac:plain-text-body><![CDATA[
feat(WAVE-2026-001): add sentiment classifier function [AI:claude-sonnet-4-5:PA-001]

Closes WAVE-2026-001 PA-001.
]]></ac:plain-text-body>
    </ac:structured-macro>
  </li>
  <li>Open a PR, link it back to the PA page (field "Pull Request URL")</li>
</ol>

<ac:structured-macro ac:name="warning">
  <ac:rich-text-body>
    <p>The <code>[AI:model:PA-ID]</code> tag is required by DL-005 — AI Output Attribution. This is what enables backward traceability from any line of code.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h3>4. Move the Wave through the macro-phases</h3>

<p><strong>Who does it:</strong> Wave Captain</p>
<p><strong>When:</strong> Each time the Wave changes Sub-Phase</p>
<p><strong>How:</strong></p>
<ol>
  <li>Open the Wave Scope page</li>
  <li>Update <strong>Current Sub-Phase</strong> (1-7)</li>
  <li>The Macro-Phase derivation is conceptually:
    <ul>
      <li>Sub-Phase 1 → Macro-Phase 1 (Instruct &amp; Scope)</li>
      <li>Sub-Phase 2-3 → Macro-Phase 2 (Shape &amp; Align)</li>
      <li>Sub-Phase 4-6 → Macro-Phase 3 (Execute &amp; Evolve)</li>
      <li>Sub-Phase 7 → Macro-Phase 4 (Learn &amp; Adapt)</li>
    </ul>
  </li>
  <li>Update Sprint ID / Repository / Branch fields when entering Shape &amp; Align</li>
</ol>

<h3>5. Close the Wave with a Proof Record</h3>

<p><strong>Who does it:</strong> Wave Captain</p>
<p><strong>When:</strong> At Wave completion, before marking Status = Closed</p>
<p><strong>Why mandatory:</strong> DL-012 — Proof Record Mandatory for Wave Close.</p>
<p><strong>How:</strong></p>
<ol>
  <li>Click <strong>+ Create</strong> → <strong>✅ D-POAF Proof Record</strong></li>
  <li>Link to the Wave (relation)</li>
  <li>Fill PoD section: Deliverables + Validation + Status (✓ Approved / ⚠ Partial / ✗ Not Met / N/A)</li>
  <li>Fill PoV section: Expected + Achieved + Status</li>
  <li>Fill PoR section: Compliance + Status</li>
  <li>Lessons learned (mandatory free text, feeds Macro-Phase 4)</li>
  <li>Sign-offs (multi-select: Wave Captain + Sponsor minimum)</li>
  <li>Save under <ac:link><ri:page ri:content-title="✅ Proof Records" /></ac:link></li>
  <li>Return to the Wave Scope page → Status → <strong>Closed</strong></li>
</ol>

<h3>6. Run a retrospective (Macro-Phase 4 — Learn &amp; Adapt)</h3>

<p><strong>Who does it:</strong> Wave Captain + team</p>
<p><strong>When:</strong> Sprint retrospective at end of Wave</p>
<p><strong>What to review:</strong></p>
<ul>
  <li>Quality ratings of Prompt Actions used (any rated 1-2 to refine?)</li>
  <li>Reusable prompts identified (add to Reusable Library)</li>
  <li>Lessons learned from the Proof Record</li>
  <li>Do any Dynamic Laws need an amendment proposal? (DL-014 — Amendment by Proposal)</li>
  <li>What feeds the next Wave's intent?</li>
</ul>

<h2>Quick-reference table</h2>

<table>
  <thead>
    <tr><th>Operation</th><th>Who</th><th>When</th><th>Page template used</th></tr>
  </thead>
  <tbody>
    <tr><td>Open Wave</td><td>Wave Captain</td><td>Macro-phase 1</td><td>🌊 D-POAF Wave Scope</td></tr>
    <tr><td>Log Prompt Action</td><td>Wave Surfer</td><td>Before EVERY AI invocation</td><td>🤖 D-POAF Prompt Action</td></tr>
    <tr><td>Commit code</td><td>Wave Surfer</td><td>After AI validated</td><td>(no page, Git commit)</td></tr>
    <tr><td>Advance phase</td><td>Wave Captain</td><td>On Sub-Phase change</td><td>(edit Wave Scope)</td></tr>
    <tr><td>Close Wave</td><td>Wave Captain</td><td>At Wave end</td><td>✅ D-POAF Proof Record</td></tr>
    <tr><td>Retrospective</td><td>Captain + team</td><td>End of sprint</td><td>(edit Wave Scope + Proof Record)</td></tr>
  </tbody>
</table>

<hr/>
<p><em>D-POAF® Framework — Workflow v1.1 — d-poaf.org — Licensed under CC BY 4.0</em></p>
"""

TRACEABILITY_XML = """
<h1>🔗 Traceability — How to Trace Back from Any Artifact to Business Intent</h1>

<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>This page answers the auditor question: <em>"Why does this line of code exist? Who decided it? Which prompt produced it? Was it aligned with the original business requirement?"</em> In D-POAF, the answer is always reachable in under 5 minutes.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>The traceability chain</h2>

<ac:structured-macro ac:name="code">
  <ac:parameter ac:name="language">text</ac:parameter>
  <ac:plain-text-body><![CDATA[
   Production artifact (code, document, decision)
                  ↑
                  │ [AI:model:PA-ID] tag in commit message
                  │
   Pull Request / Commit (Git history)
                  ↑
                  │ Linked PR URL in PA page
                  │
   Prompt Action (PA-NNN)
                  ↑
                  │ Model + Config + Context (Traceability Thread)
                  │ Wave relation (link to parent Wave Scope)
                  │
   Wave Scope (WAVE-YYYY-NNN)
                  ↑
                  │ Business Objective + PoD/PoV/PoR criteria
                  │ Linked Jira Epic
                  │
   Business Intent (Sponsor's request)
]]></ac:plain-text-body>
</ac:structured-macro>

<h2>Forward direction — Following the chain top-down</h2>

<p><strong>Use case:</strong> "Where did the AI generate code for our sentiment classifier?"</p>

<ol>
  <li>Open the Wave Scope page: <ac:link><ri:page ri:content-title="🌊 WAVE-EXAMPLE-001 — Customer Feedback Categorization (Pilot)" /></ac:link></li>
  <li>Read the Business Objective and PoD/PoV/PoR criteria</li>
  <li>Navigate to <ac:link><ri:page ri:content-title="🤖 Prompt Actions" /></ac:link> and filter by Wave = WAVE-EXAMPLE-001</li>
  <li>For each PA, read the Model + Config + Context</li>
  <li>Follow the PR URL field to the actual code in GitHub</li>
</ol>

<p><strong>Time to answer: 2-3 minutes.</strong></p>

<h2>Reverse direction — From artifact to business intent</h2>

<p><strong>Use case:</strong> "Why is this line of code in the codebase? Who wrote it?"</p>

<ol>
  <li>Run <code>git blame</code> on the suspicious line</li>
  <li>The commit message contains the tag: <code>[AI:claude-sonnet-4-5:PA-001]</code></li>
  <li>Search this Confluence space for <strong>PA-001</strong> → opens the Prompt Action page</li>
  <li>On the PA page, read:
    <ul>
      <li><strong>Wave</strong> field → click the link to the parent Wave Scope</li>
      <li><strong>Model identity</strong> → claude-sonnet-4-5-20250929</li>
      <li><strong>Model config</strong> → temperature 0.2, system prompt sha256...</li>
      <li><strong>Context source</strong> → which documents fed the prompt</li>
      <li><strong>Prompt text</strong> → the exact instruction given to the AI</li>
      <li><strong>Output summary</strong> + Quality rating</li>
    </ul>
  </li>
  <li>On the Wave Scope page (now opened):
    <ul>
      <li><strong>Business Objective</strong> → the original sponsor request</li>
      <li><strong>Wave Captain</strong> → who owned this</li>
      <li><strong>Linked Jira Epic</strong> → the formal requirement</li>
      <li><strong>PoD/PoV/PoR criteria</strong> → what success looks like</li>
    </ul>
  </li>
</ol>

<p><strong>Time to answer: 5 minutes.</strong></p>

<h2>What makes this work — The 3 mandatory links</h2>

<table>
  <thead><tr><th>Link</th><th>Mechanism</th><th>Mandated by</th></tr></thead>
  <tbody>
    <tr><td>Code → PA</td><td><code>[AI:model:PA-ID]</code> tag in commit message</td><td>DL-005 — AI Output Attribution</td></tr>
    <tr><td>PA → Wave</td><td>"Wave" relation field on PA page</td><td>DL-006 — PromptRegister is Mandatory</td></tr>
    <tr><td>Wave → Intent</td><td>"Linked Jira Epic" + "Business Objective" on Wave Scope</td><td>DL-004 — Context Integrity</td></tr>
  </tbody>
</table>

<ac:structured-macro ac:name="warning">
  <ac:rich-text-body>
    <p>If <strong>any one</strong> of these 3 links is broken (missing tag, empty Wave field, no Jira Epic), the traceability chain breaks. Per DL-002 (No Blind Acceptance), the PR should be rejected.</p>
  </ac:rich-text-body>
</ac:structured-macro>

<h2>The audit scenario — Replay an AI generation</h2>

<p>An external auditor asks: "Show me you can reproduce the exact generation that created line 42 of <code>classify_feedback.py</code>."</p>

<p>Steps:</p>
<ol>
  <li><code>git blame src/classify_feedback.py</code> → commit <code>abc123de</code> with tag <code>[AI:claude-sonnet-4-5:PA-001]</code></li>
  <li>Open <ac:link><ri:page ri:content-title="🤖 PA-001 — Build sentiment classifier function" /></ac:link></li>
  <li>Copy the <strong>Model configuration</strong> block (temperature, top_p, etc.)</li>
  <li>Copy the <strong>Prompt text</strong></li>
  <li>Reload the <strong>Context source</strong> documents (with the recorded sha256 hashes for integrity)</li>
  <li>Invoke <code>claude-sonnet-4-5-20250929</code> with the exact same config + context + prompt</li>
  <li>Compare the output — should be ≈identical (within model stochasticity)</li>
</ol>

<p><strong>This is the D-POAF® proof of reproducibility.</strong> No other framework gives you this.</p>

<h2>Why it matters for compliance</h2>

<p>Major regulations require this kind of traceability for AI-generated content:</p>
<ul>
  <li><strong>EU AI Act (2024)</strong> — Article 14 (Human Oversight) + Article 13 (Transparency)</li>
  <li><strong>NIST AI RMF (2023)</strong> — Govern/Map functions require model + data provenance</li>
  <li><strong>ISO/IEC 42001 (2023)</strong> — AI Management System Standard, clause 8.3 (Operation)</li>
  <li><strong>SOC 2 Type II</strong> — Common Criteria CC8.1 (Change management) for AI-assisted code</li>
</ul>

<p>D-POAF® provides the audit trail these frameworks demand, without imposing custom tools.</p>

<hr/>
<p><em>D-POAF® Framework — Traceability Guide v1.1 — d-poaf.org — Licensed under CC BY 4.0</em></p>
"""

# ============================================================
# Run
# ============================================================
print()
print("=" * 60)
print("D-POAF (R) Confluence Patch v1.2 - Adding missing pages")
print("=" * 60)
print()

# Verify space access
log("Verifying space access...")
try:
    space_result = api_call("GET", "space", query={"spaceKey": SPACE_KEY})
    if not space_result.get("results"):
        raise APIError(f"Space '{SPACE_KEY}' not found")
    log(f"  OK - {space_result['results'][0]['name']}")
except APIError as e:
    print(f"ERROR: {e}")
    sys.exit(1)

pages_to_create = [
    ("Wave Lifecycle", WAVE_LIFECYCLE_XML),
    ("Workflow", WORKFLOW_XML),
    ("Traceability", TRACEABILITY_XML),
]

print()
for title, xml in pages_to_create:
    log(f"Checking '{title}'...")
    existing = find_page_by_title(title)
    if existing:
        log(f"  Already exists: {page_url(existing)}")
        continue
    log(f"  Creating...")
    try:
        result = create_page(title, xml)
        log(f"  OK - {page_url(result)}")
    except APIError as e:
        log(f"  FAILED: {e}")

print()
print("=" * 60)
print("✓ Patch applied successfully")
print("=" * 60)
print()
print(f"Open your space: {URL}/wiki/spaces/{SPACE_KEY}/overview")
print()
print("You should now see 5 reference pages in the sidebar:")
print("  📖 Practical Guide")
print("  📋 Workflow              <- NEW")
print("  📊 Wave Lifecycle        <- added if missing")
print("  🔗 Traceability          <- NEW")
print("  ⚖ Dynamic Laws")
print()
print("Plus 3 parent index pages:")
print("  🌊 Waves")
print("  🤖 Prompt Actions")
print("  ✅ Proof Records")
print()
print("Done.")
