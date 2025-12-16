# 📋 D-POAF Templates

**Ready-to-use templates for implementing D-POAF in your project**

---

## 🚀 Quick Start

### **Pick Your Starting Point:**

**New to D-POAF?**
→ Start with [Feature Block](artifacts/1-feature-block.md) + [Feedback](artifacts/3-feedback.md)

**Using AI tools?**
→ Add [Prompt Action](artifacts/2-prompt-action.md)

**Need team alignment?**
→ Use [Team Rule](artifacts/4-team-rule.md)

---

## 📁 Available Templates

### **Work Artifacts** (`artifacts/`)

| Template | When to Use | Time |
|----------|-------------|------|
| **[Feature Block](artifacts/1-feature-block.md)** | Define what to build | 5 min |
| **[Prompt Action](artifacts/2-prompt-action.md)** | Instruct AI collaboration | 5 min |
| **[Feedback](artifacts/3-feedback.md)** | Report bugs/improvements | 3 min |
| **[Dynamic Law](artifacts/4-team-rule.md)** |  Living governance agreement | 10 min |
| **[AI Mandate](artifacts/ai-mandate.md)** | Define AI boundaries | 15 min |

### **Validation Reports** (`artifacts/`)

| Template | When to Use | Time |
|----------|-------------|------|
| **[PoD Report](artifacts/pod-report.md)** | Validate technical & Functional delivery | 10 min |
| **[PoV Report](artifacts/pov-report.md)** | Validate business value | 15 min |
| **[PoR Report](artifacts/por-report.md)** | Track reliability metrics | 10 min |

---

## 💡 How to Use

### **1. Copy Template**
```bash
# From templates folder
cp artifacts/1-feature-block.md ../features/FB-AUTH-001.md
```

### **2. Fill It Out**
```markdown
# Feature Block: User Login

## What & Why
Users need to log in to access protected features.

## Value (BVS)
Score: 9/10
- Critical for security
- Blocks other features

## Effort (ERS)
Score: 3/10
- OAuth library exists
- 3-5 days work
```

### **3. Use It**
- Add to Scope
- Score in Alignment Workshop
- Track in Wave

---

## 📊 Template Workflow

### **Planning a Feature:**
```
1. Create Feature Block (define what)
2. Score BVS/ERS (prioritize)
3. Plan in Wave
```

### **Building with AI:**
```
1. Create Prompt Action (instruct AI)
2. AI generates code
3. Review and refine
```

### **Validating Work:**
```
1. Complete feature
2. Fill PoD Report (technical & functional check)
3. Fill PoV Report (business check)
```

### **Tracking Issues:**
```
1. Find bug/improvement
2. Create Feedback
3. Prioritize and fix
```

---

## 🎯 Naming Convention

**Feature Blocks:**
```
FB-[MODULE]-[NUMBER].md
Examples: FB-AUTH-001.md, FB-PAY-015.md
```

**Prompt Actions:**
```
PA-[MODULE]-[TYPE]-[NUMBER].md
Examples: PA-AUTH-CODE-001.md, PA-PAY-DOC-003.md
```

**Feedback:**
```
FD-[YEAR]-[NUMBER].md
Examples: FD-2025-001.md, FD-2025-042.md
```

**Dynamic Laws:**
```
TR-[YEAR]-[NUMBER].md
Examples: TR-2025-001.md, TR-2025-008.md
```

---

## 📂 Suggested Project Structure

```
your-project/
├── features/           # Feature Blocks
│   ├── FB-AUTH-001.md
│   ├── FB-PAY-001.md
│   └── FB-USER-001.md
│
├── ai-prompts/         # Prompt Actions (if using AI)
│   ├── PA-AUTH-001.md
│   └── PA-PAY-001.md
│
├── feedbacks/          # Bugs & improvements
│   ├── FD-2025-001.md
│   └── FD-2025-002.md
│
├── dynamic-rules    
│   ├── TR-2025-001.md
│   └── TR-2025-002.md
│
└── validation/         # PoD/PoV/PoR reports
    ├── POD-W001.md
    ├── POV-W001.md
    └── POR-W001.md
```

---

## ✅ Best Practices

### **DO:**
- ✅ Fill templates honestly
- ✅ Use plain language
- ✅ Keep it simple
- ✅ Update as you learn

### **DON'T:**
- ❌ Overthink scores (1-10 is fine)
- ❌ Skip templates to "save time"
- ❌ Fill templates after the fact
- ❌ Make it bureaucratic

---

## 🎓 Quick Examples

### **Example: Feature Block**
```markdown
# FB-AUTH-001: User Login

## Value (BVS): 9/10
Everyone needs this to access the app.

## Effort (ERS): 3/10
OAuth library, 3 days work.

## Acceptance Criteria:
- [ ] User can login with email/password
- [ ] "Remember me" checkbox works
- [ ] Error messages clear
```

### **Example: Prompt Action**
```markdown
# PA-AUTH-001: Login Component

## AI Prompt:
Create a React login form with:
- Email/password fields
- Remember me checkbox
- Error handling
- Tailwind CSS styling

## Expected Output:
- LoginForm.jsx
- LoginForm.test.jsx
```

### **Example: Feedback**
```markdown
# FD-2025-001: Login timeout too short

## Impact: High
Users getting logged out every 5 minutes.

## Priority: 🔴 Critical

## Solution:
Increase session timeout to 30 minutes.
```

---

## 📖 Learn More

**Complete methodology:**
→ [D-POAF Overview](../methodology/OVERVIEW.md)

**Ceremonies:**
→ [Alignment Workshop](../methodology/ceremonies/2-alignment-workshop.md)

**Community:**
→ [Discord](https://d-poaf.org)

---

## ❓ FAQ

**Q: Do I need all templates?**
A: No. Start with Feature Block + Feedback.

**Q: Can I modify templates?**
A: Yes! Adapt to your needs.

**Q: How do I integrate with Jira/GitHub?**
A: Use these as definitions, link from tickets.

**Q: Are these templates required?**
A: No. They're tools to help. Use what works.

---

**Ready to start?** 

Copy a template and try it on your next feature!