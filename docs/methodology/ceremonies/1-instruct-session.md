# 🎯 Instruct Session

**Initial Contextualization and AI Mandate Definition**

## 📌 Overview

**Purpose:** Establish cognitive, functional, and strategic boundaries for the cycle  
**Duration:** 1-2 hours  
**Frequency:** Start of each Version
**Participants:** Stakeholders,RAGer, Wave Surfer, Wave Captain, Peacekeeper, Community

---

## 🎯 Objectives

- [ ] Define AI Mandate (constraints, objectives, boundaries)
- [ ] Frame business context and functional scope
- [ ] Initialize core registers (trace, glossary, patterns)
- [ ] Draft initial feature candidates with BVS
---

## 📥 Inputs

- Business context and vision
- Functional scope (what we're building)
- Constraints (technical, regulatory, security)
- Reference documents and existing architectures
- Domain knowledge

---

## 📤 Outputs

- **AI Mandate:** Clear constraints, objectives, boundaries
- **Feature Draft:** Bullet-point list of feature candidates
- **Core Registers:**
  - Trace Register (decision log)
  - Glossary (domain terms)
  - Patterns (reusable solutions)
  - Domain Model (entities, relationships)

---

## 📋 Process

### **1. Context Framing (20 min)**

**Questions to answer:**
- What problem are we solving?
- Who are the users?
- What's the business model?
- What are the success criteria?

**Output:** Written context document

### **2. Constraints Definition (15 min)**

**Technical Constraints:**
- Stack limitations
- Performance requirements
- Security requirements
- Compliance needs

**Business Constraints:**
- Budget
- Timeline
- Resource availability

**Output:** Constraint list in AI Mandate

### **3. AI Mandate Creation (20 min)**

**Define AI boundaries:**
```
AI can:
- Propose architectures
- Generate code patterns
- Suggest optimizations

AI cannot:
- Make final architecture decisions
- Deploy to production
- Access sensitive data
```

**Output:** AI Mandate document

### **4. Feature Drafting (30 min)**

**Brainstorm feature candidates:**
- List all potential features
- Group by theme/module
- No scoring yet (that's for Alignment Workshop)

**Output:** Feature list (bullet points)

**Example:**
```
Authentication Module:
- User registration
- Login/logout
- Password reset
- OAuth integration

E-commerce Module:
- Product catalog
- Shopping cart
- Checkout
- Payment processing
```

### **5. Register Initialization (15 min)**

**Create core registers:**

**Trace Register:**
```
Date       | Decision                | Rationale
-----------|-------------------------|---------------------------
2025-01-15 | Chose PostgreSQL        | Better JSON support
2025-01-15 | Google Sheets           | Storing Prompts, Feedback...
```

**Glossary:**
```
Term          | Definition
--------------|--------------------------------------
Wave          | 8 hours max development cycle
Feature Block | Cohesive unit of functionality
PoD           | Proof of Delivery (technical validation)
PoV           | Proof of Value (business validation)
```

---

## 💡 Best Practices

### **✅ DO:**
- Be explicit about constraints
- Write down all assumptions
- Involve domain experts
- Keep AI boundaries clear
- Document everything

### **❌ DON'T:**
- Skip constraint definition
- Assume AI understands context
- Mix this with feature prioritization
- Rush through framing

---

## 📊 Template - AI Mandate

```markdown
# AI Mandate - [Project Name]

## Context
[Brief description of the project]

## Objectives
- Objective 1
- Objective 2

## Constraints
**Technical:**
- Constraint 1
- Constraint 2

**Business:**
- Constraint 1
- Constraint 2

## AI Boundaries

**AI Can:**
- Action 1
- Action 2

**AI Cannot:**
- Action 1
- Action 2

**AI Must Ask Before:**
- Action 1
- Action 2

## Reference Documents
- Document 1
- Document 2

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

---

## 🔗 Next Step

After Instruct Session → **[Alignment Workshop](2-alignment-workshop.md)**

---

**Why It Exists:** Without explicit cognitive framing, AI tends to drift. The Instruct Session ensures precision, alignment, and controlled autonomy.