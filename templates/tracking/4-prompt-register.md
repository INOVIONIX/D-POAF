# AI PromptRegister (Tracker) Template

## Overview

This template helps you track all the AI **Prompts Actions** you use during a Wave, what worked well, and what to improve next time. Use this to build a library of effective Prompts Actions and learn from your AI collaboration experience.

**Use this when:** You're using AI to help build features and want to track what prompts work well so you can reuse and improve them.

---

# AI Prompt Tracker - [PROJECT NAME]

**Project:** [Project Name]  
**Team:** [Team Name]  
**Period:** [Start Date] to [End Date]  
**Created by:** [Your Name]  

---

## AI Prompts Used This Wave

### Summary Table
| Prompt ID | What For | AI Model | Who Used | Result | Quality |
|-----------|----------|----------|----------|---------|---------|
| PA-001 | Login API code | ChatGPT-4 | [Name] | Good code, minor fixes needed | 8/10 |
| PA-002 | Login tests | Claude | [Name] | Excellent test coverage | 9/10 |
| PA-003 | Error handling | ChatGPT-4 | [Name] | Too generic, had to rewrite | 4/10 |
| PA-004 | Documentation | Claude | [Name] | Clear and helpful | 8/10 |

*Each Prompt ID links to detailed AI Prompt files (see prompts/PA-XXX.md)*

---

## What We Generated

### Files Created
| File/Component | From Prompt | Status | Notes |
|----------------|-------------|---------|-------|
| `src/auth/login.js` | PA-001 | ✅ Done | Small fixes for validation |
| `tests/auth/login.test.js` | PA-002 | ✅ Done | Great test coverage |
| `src/auth/errors.js` | PA-003 | 🔄 Redone | AI version too basic |
| `docs/login-api.md` | PA-004 | ✅ Done | Ready to use |

### Quality Check
- **Working as expected:** 3/4 outputs
- **Needed minor fixes:** 1/4 outputs  
- **Had to completely redo:** 1/4 outputs
- **Team satisfaction:** 7.5/10

---

## AI Model Performance

### Models We Used
- **ChatGPT-4:** 2 prompts (avg quality: 6/10)
- **Claude:** 2 prompts (avg quality: 8.5/10)
- **Other:** [None this Wave]

### What Worked Best
| Task Type | Best Model | Why |
|-----------|------------|-----|
| Code generation | ChatGPT-4 | Good at following patterns |
| Test writing | Claude | Better edge case thinking |
| Documentation | Claude | Clearer explanations |
| Error handling | Manual | AI too generic for our needs |

---

## Lessons Learned

### Prompts That Worked Well
- **PA-002 (Tests):** Specific examples + clear requirements = excellent output
- **PA-004 (Docs):** Asking for user perspective improved quality
- **General:** Being specific about file structure helps a lot

### Prompts That Didn't Work
- **PA-003 (Errors):** Too vague, AI couldn't understand our specific error cases
- **General:** Generic prompts = generic results

### For Next Wave
- [ ] Reuse PA-002 pattern for all test generation
- [ ] Create better error handling prompt with specific examples  
- [ ] Try Claude for more documentation tasks
- [ ] Avoid generic prompts - always include context and examples

---

## Prompt Library (Best Ones to Reuse)

### Great Prompts to Keep
**PA-002 - Test Generation (9/10):**
*"Create comprehensive Jest tests for [component] that cover: [specific scenarios]. Use this existing test as a pattern: [example]. Include edge cases for [specific situations]."*

**PA-004 - Documentation (8/10):**  
*"Write user-friendly documentation for [feature] explaining: what it does, how to use it, common problems. Write for developers who are new to this codebase."*

### Prompts to Improve
**PA-003 - Error Handling (4/10):**
*Need to add: specific error scenarios, existing code patterns, expected user experience*

---

## Team Feedback

### What Team Liked
- AI helped with test coverage (saved 2+ hours)
- Documentation was clearer than usual
- Good starting point even when code needed fixes

### What Was Challenging
- Hard to write good prompts (takes practice)
- AI doesn't understand our specific business rules
- Still need to review everything carefully

### Team Skills Growing
- Getting better at prompt writing
- Learning which AI models work best for what
- Building prompt patterns we can reuse

---

**Quick Start Guide:**
1. **Before using AI** - Write down exactly what you want (be specific!)
2. **During Wave** - Log each prompt you use in the table above
3. **Rate results honestly** - What worked well vs what didn't?
4. **Save good prompts** - Build your team's prompt library
5. **Learn and improve** - Use lessons for next Wave

**Tips for Better AI Collaboration:**
- Be specific about what you want (examples help!)
- Include context about your project and users
- Give AI examples of your coding style/patterns
- Always review and test AI output
- Save prompts that work well for reuse

**This Tracker Helps You:**
- Build a library of effective prompts for your team
- Learn which AI models work best for different tasks
- Improve your prompt-writing skills over time
- Share successful approaches with teammates

---
**Template Version:** 1.0  
**Last Updated:** October 2025  
**License:** Apache 2.0  
**Copyright:** © 2025 INOVIONIX - D-POAF® Framework