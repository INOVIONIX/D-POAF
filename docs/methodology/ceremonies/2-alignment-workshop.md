# 🔄 Alignment Workshop

**Structuring, Clarifying, and Measuring Feature Intentions**

## 📌 Overview

**Purpose:** Convert feature drafts into structured, measurable definitions with BVS/ERS/PVS  
**Duration:** 2-4 hours  
**Frequency:** After Instruct Session, start of each Wave  
**Participants:** RAGer, Wave Surfer, Wave Captain, Peacekeeper, Community

---

## 🎯 Objectives

- [ ] Clarify and enrich feature definitions
- [ ] Assign BVS (Business Value Score 1-10)
- [ ] Assign ERS (Effort & Risk Score 1-10)
- [ ] Compute PVS (Priority Value Score = BVS² / ERS)
- [ ] Identify dependencies and risks
- [ ] Define shortest development paths (ODP)
- [ ] Create Adaptive Roadmap
- [ ] Generate 3D Vision (Value × Effort × Module) Matrix

---

## 📥 Inputs

- Draft features from Instruct Session
- Stakeholder clarifications
- Contextual knowledge
- Team capacity
- Previous Wave velocity

---

## 📤 Outputs

- **Structured Feature Blocks** with clear definitions
- **BVS & ERS** assigned to each feature
- **PVS** calculated (BVS² / ERS)
- **Dependencies map**
- **Optimal Development path** (ODP MVP algorithm)
- **Adaptive Roadmap** (vX.Y releases)
- **3D Vision Matrix** (visualizations)
- **Supporting artifacts** (schemas, templates, Dyanamic laws)

---

## 📋 Process

### **1. Feature Clarification (45 min)**

**For each feature candidate:**

**Clarify:**
- What exactly does this do?
- Who benefits?
- What's the success criteria?
- What are the edge cases?

**Enrich:**
- What & Why 
- BVS & ERS & PVS
- Acceptance criteria
- Dependencies
- Risks

**Output:** Feature Block specification

**Template:**
```markdown
## Feature Block: [Name]

**Description:** [What it does]

**What & Why:**
- Problem: [What business problem are we solving? Keep it simple - 1-2 sentences.]
- Solution: [What will this feature do? Describe the outcome in business terms.]
- Success Looks Like: [How will we know this worked? What will users be able to do?]

**PVS:**
- BVS
- ERS
- BVS^2/ERS

**Dependencies:**
- Feature X must be completed first

**Risks:**
- Risk 1 (technical)
- Risk 2 (business)

**Module:** [Core/UI/Backend/etc.]
```

---

### **2. BVS Scoring (30 min)**

**Business Value Score (1-10)**

Rate each feature from 1-10 based on business value.

**BVS Scoring Criteria:**

| Score | Category | Examples |
|-------|----------|----------|
| **9-10** | **Critical** | Core product, blocks everything else, massive revenue |
| **7-8** | **High** | Important functionality, significant impact |
| **5-6** | **Medium** | Valuable but not critical |
| **3-4** | **Low** | Nice to have, minor impact |
| **1-2** | **Negligible** | Why are we doing this? |

---

**Questions to Ask:**

**User Impact**
- How many users benefit?
- Is it essential for the user journey?

**Revenue Impact**
- Does it directly generate revenue?
- Does it reduce costs?

**Strategic Value**
- Does it align with company vision?
- Is it a differentiator?

**Dependencies**
- Do other features depend on this?
- Is it a blocker?

**Risk Mitigation**
- Does it reduce business risk?
- Does it ensure compliance?

---

**Process:**
```
1. RAGer presente BVS (1-10)
2. Team discusses using questions above
4. Document rationale
```

**Example:**
```
Feature: User Authentication

User Impact:      10/10 (Every user needs it)
Revenue:          8/10 (Enables paid features)
Strategic:        9/10 (Core to product)
Dependencies:     10/10 (Blocks everything)
Risk Mitigation:  9/10 (Security critical)

Team Discussion:
- RAGer: "This is foundational, I'd say 9"
- Wave Cpatain : "Ask for more infomations"
- Peacekeeper: "Ask about security"

Rationale: "Critical for all users, blocks other features, security foundation. Essential for MVP."
```

---

### **3. ERS Scoring (30 min)**

**Effort & Risk Score (1-10)**

Rate each feature from 1-10 based on effort and risk.

**ERS Scoring Criteria:**

| Score | Category | Examples |
|-------|----------|----------|
| **8-10** | **Very High** | Complex, novel tech, many unknowns |
| **6-7** | **High** | Significant effort, some risk |
| **4-5** | **Medium** | Moderate complexity |
| **2-3** | **Low** | Well-known patterns, low risk |
| **1** | **Trivial** | Minimal effort |

---

**Questions to Ask:**

**Technical Complexity**
- Is this a well-known pattern?
- Do we have experience with this?
- Are there third-party libraries?

**Unknowns & Risks**
- How many unknowns?
- What could go wrong?
- Any external dependencies?

**Estimation**
- Best case scenario 
- Worst case scenario
- Hidden complexity?

**Testing & QA**
- How hard to test?
- Security implications?
- Edge cases?

**Maintenance**
- Long-term cost?
- Need ongoing work?

---

**Process:**
```
1. Team identify technical complexity
2. Team identify Unkowns 
3. Team identify maturity 
4. Team identify risks
5. Team identify maintenance cost
6. Team identify testing cost
7. Compute ERS
8. Document risks
```

**Example:**
```
Feature: AI Recommendation Engine

Technical Complexity: 9/10 (ML model, new to team)
Unknowns:            8/10 (Data quality, accuracy)
Testing:             8/10 (Hard to validate accuracy)
Risk:                8/10 (Model retraining needed)
Maintenance:         8/10 (Model retraining needed)

Team Discussion:
- Team: "This is complex, 8-9"
- Team: "Never done ML, 9"
- Team: "Data is messy, high risk, 9"

Compute: ERS = 9 high

Rationale: "Complex ML implementation, data quality unknowns, requires model training and validation. High technical risk."
```

**Another Example:**
```
Feature: Email Notifications

Technical Complexity: 2/10 (SendGrid SDK)
Unknowns:            1/10 (Standard integration)
Time:                2/10 (1-2 days)
Testing:             2/10 (Easy to test)
Maintenance:         2/10 (Low)

Compute: ERS = 2 easy 

Rationale: "Simple third-party integration, well-documented, low risk. Standard pattern."
```

---

### **4. PVS Calculation & Prioritization (30 min)**

**Run D-POAF Script:**
```bash
python dpoaf-prioritization.py --features matrix.json
```

**Script outputs:**
- **PVS** for each feature (BVS² / ERS)
- **Prioritization Matrix:**
  - 🟢 Quick Wins (high BVS, low ERS)
  - 🔵 Strategic (high BVS, high ERS)
  - 🟡 Nice-to-have (low BVS, low ERS)
  - 🔴 To Avoid (low BVS, high ERS)

**Example Output:**
```
PRIORITIZATION MATRIX
─────────────────────────────────────
🟢 QUICK WINS
FB-A1  User Auth        9.0  2.0  40.5
FB-B2  Shopping Cart    8.0  3.0  21.3

🔵 STRATEGIC
FB-B3  Payment          9.5  5.0  18.1

🔴 TO AVOID
FB-I1  AI Recommender   7.0  8.5  5.8
```

---

### **5. Optimal Development path for MVP Optimization (20 min)**

**Script calculates optimal implementation order:**
- Respects dependencies
- Minimizes total effort/value ratio (w = ERS/BVS)
- Finds optimal path: Start → MVP

**Example:**
```
OPTIMAL PATH (ODP)
─────────────────────────────────────
1. FB-A1  User Auth       w=0.22
2. FB-B1  Product Catalog w=0.44
3. FB-B2  Shopping Cart   w=0.38
4. FB-B3  Payment         w=0.53
5. FB-C2  Notifications   w=0.36
```

**Validation:**
- Does path make sense?
- Dependencies respected?
- Fits team capacity?

---

### **6. Roadmap Creation (30 min)**

**Optimal Development path Releases Define Releases:**

**Release 1 (MVP):** Features needed for launch
**Release 2:** Quick Wins + Strategic  
**Release 3:** Nice-to-have  
**Release N:** Deferred features

**Example:**
```
v1.0 MVP (Release 1):
- User Auth
- Product Catalog
- Shopping Cart
- Payment
Total: 14.0 ERS

v1.1 (Release 2):
- Email Notifications
- User Dashboard
- Product Reviews
Total: 10.5 ERS
```

---

### **7. 3D Vision (15 min)**

**Generate visualizations:**

**Matrix 2D:**
- X-axis: ERS
- Y-axis: BVS
- Color: Category

**Matrix 3D:**
- X-axis: ERS
- Y-axis: BVS
- Z-axis: Module

**Dependency Graph:**
- Nodes: Features
- Edges: Dependencies
- Highlighted: Optimal path

---

## 💡 Best Practices

### **✅ DO:**
- Use consensus vote no authority
- Document all rationale
- Challenge assumptions
- Visualize the matrix
- Follow Optimal Development path (ODP) for MVP and Release's path
- Keep it data-driven

### **❌ DON'T:**
- Score alone
- Ignore To Avoid quadrant
- Skip dependency analysis
- Overload the Wave
- Trust gut feeling only

---

## 📊 JSON Template

```json
{
  "features": [
    {
      "id": "FB-A1",
      "name": "User Authentication",
      "description": "Login, register, OAuth",
      "module": "Core",
      "bvs": 9.0,
      "ers": 2.0,
      "dependencies": [],
      "rationale": {
        "bvs": "Critical for all users, blocks other features",
        "ers": "Well-known pattern, low risk"
      }
    }
  ],
  "mvp": ["FB-B2"]
}
```

---

## 🔗 Next Steps

After Alignment Workshop:
1. Start Wave development
2. Daily check-ins
3. When feature complete → **[PoD Review](2-pod-review.md)**

---

**Why It Exists:** This workshop creates structural alignment and replaces subjective prioritization with measurable, data-informed planning.