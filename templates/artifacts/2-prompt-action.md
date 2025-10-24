# Prompt Action Template

## 📋 Overview

This template provides a standardized format for creating **Prompt Action** documents in the D-POAF® Framework. Each Prompt Action represents an AI instruction designed to generate specific deliverables within a Wave delivery cycle.

---

# Prompt Action - [TITLE]

**ID:** `PA-[MODULE]-[NUMBER]-[TYPE]-[description]`  
**Feature:** `FB-[MODULE]-[NUMBER]`  
**Wave:** `W-[NUMBER]`  
**Type:** `[ ] Code` `[ ] Tests` `[ ] Docs` `[ ] UI`  
**Created:** [YYYY-MM-DD]  
**Author:** [Name]  
**AI Model:** [e.g., GPT-5, Claude 3.5, Mistral-Large]  
**Status:** `[ ] Draft` `[ ] Ready` `[ ] Done` `[ ] Validated (PoV)` 

---

## What Do You Want AI To Create?

### Goal
[What should the AI build? Be specific about the outcome.]

*Example: Create a login form that validates email/password and shows error messages.*

### Success Means
- [ ] [It does this specific thing]
- [ ] [It handles this case correctly]  
- [ ] [It meets this quality standard]

---

## AI Instructions

### Tell the AI:
```
You are a [role - developer/designer/etc.] building [what type of thing].

Create [specific deliverable] that:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

Make sure it:
- Works on [platform/environment]
- Handles [error cases or edge cases]
- Follows [coding standards if relevant]

Generate:
1. [Main file] - [what it does]
2. [Test file] - [what it tests]
3. [Doc file] - [what it explains]
```

### Technical Context (If Needed)
- **Language/Framework:** [Python, React, etc.]
- **Style:** [Naming conventions, patterns to follow]
- **Integration:** [APIs, databases, other services to use]

---

## Expected Output

**Files to Generate:**
- [ ] `[path/filename]` - [Main functionality]
- [ ] `[path/test-filename]` - [Tests for the functionality]
- [ ] `[path/readme]` - [Documentation/usage instructions]

**Quality Checks:**
- [ ] Code runs without errors
- [ ] Tests pass
- [ ] Handles expected user inputs
- [ ] Secure (validates inputs, no hardcoded secrets)

---

## Notes & Refinements

**First Try Results:**
[How did it go? What worked? What needs adjustment?]

**Prompt Improvements:**
[How to make the instructions clearer for next time?]

**Lessons Learned:**
[What did you discover about working with AI on this?]

---

**Quick Start Guide:**
1. **Be specific** - Vague prompts get vague results
2. **Include examples** - Show the AI what "good" looks like  
3. **Test and iterate** - First result might not be perfect
4. **Save what works** - Reuse good prompts for similar tasks

**Tips for Better AI Results:**
- Give context about your project and users
- Specify the exact format/structure you want
- Include error handling requirements
- Ask for tests and documentation together
- Be clear about integrations and dependencies

**When to Use This:**
- You want AI to help build something specific
- You have a clear idea of the desired outcome
- You want to iterate and improve the AI instructions
- You're building as part of a larger Feature Block
---

**Template Version:** 1.0  
**Last Updated:** October 2025  
**License:** Apache 2.0  
**Copyright:** © 2025 INOVIONIX - D-POAF® Framework