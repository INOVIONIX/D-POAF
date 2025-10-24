# Feature Block - [TITLE]

## 📋 Overview

This template provides a standardized format for creating **Feature Block** documents in the D-POAF Framework. Each Feature Block defines a single piece of functionality with clear business value, effort estimation, and completion criteria. It helps teams prioritize work and ensures everyone understands what needs to be built and why.

**Use this when:** You need to define a new feature, improvement, or piece of work for your product.

**Key Benefits:**
- **Clear prioritization** through simple value vs effort scoring
- **Shared understanding** of what success looks like  
- **Business focus** on solving real user problems
- **Team alignment** on scope and expectations
- **Ready for AI Model** with Prompt Action
---


**ID:** `FB-[MODULE]-[NUMBER]-[description]`  
**Created:** [YYYY-MM-DD]  
**Author:** [Name]  
**Status:** `[ ] Planned` `[ ] In Progress` `[ ] Done` `[ ] Validated (PoV)` 

---

## What & Why

### Problem 
[What business problem are we solving? Keep it simple - 1-2 sentences.]

### Solution
[What will this feature do? Describe the outcome in business terms.]

### Success Looks Like
[How will we know this worked? What will users be able to do?]

---

## Value & Effort

### Business Value Score (BVS)
Formula: `(0.5 × Impact) + (0.3 × Urgency) + (0.2 × Opportunity)`

| Factor | Score | Description |
|---------|-------|-------------|
| Impact | [1-10] | How much business value does this create? |
| Urgency | [1-10] | How soon is this needed? |
| Opportunity | [1-10] | What potential or competitive gain exists? |

**→ BVS Total:** _____

### Effort & Risk Score (ERS)
Formula: `1 + (Effort/10) + (Risk/10)`

| Factor | Score | Description |
|---------|-------|-------------|
| Effort | [1-10] | Complexity & time required |
| Risk | [1-10] | Technical or functional uncertainty |

**→ ERS Total:** _____

### Prioritization Value Score (PVS)
Formula: `BVS² / ERS`

**→ PVS:** _____  
**Priority:** 
- [ ] HIGH (>25)
- [ ] MEDIUM (15–25)
- [ ] LOW (<15)
---

## Definition of Done

**This feature is complete when:**
- [ ] [Specific, testable condition]
- [ ] [Specific, testable condition]  
- [ ] [Specific, testable condition]

**This feature must NOT:**
- [ ] [Important limitation or exclusion]

---

## Technical Notes

**Tech Stack:** [Language/Framework if relevant]

**Key Requirements:**
- [ ] Works on [platform/browser]
- [ ] Handles [expected load/usage]
- [ ] Secure (authentication, validation)
- [ ] Tested (unit + integration tests)

**Dependencies:**
- [ ] [What needs to be done first]
- [ ] [External service/API needed]

---

## AI Prompt (Optional)

If using AI to help build this:

> Create a [component/API/feature] that [does what] for [who], ensuring [key constraints].

*Example: Create a user login form that validates email/password and redirects to dashboard, ensuring form validation and error handling.*

---

**Quick Start Guide:**
1. Fill out "What & Why" - be specific about the problem
2. Score Value & Effort honestly - don't inflate scores  
3. Write clear "Done" criteria - make them testable
4. Add technical notes for your team
5. Use AI prompt action

---

**Template Version:** 1.0  
**Last Updated:** October 2025  
**License:** Apache 2.0  
**Copyright:** © 2025 INOVIONIX - D-POAF® Framework