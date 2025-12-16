# 🌊 D-POAF Methodology Overview
---

## 🎯 Core Concept

**Three metrics, one formula:**

```
BVS = Business Value Score (1-10)
ERS = Effort & Risk Score (1-10)
PVS = BVS² / ERS (Priority Value Score)
```
---

## 📋 The 5 Essential Ceremonies

D-POAF has **5 ceremonies** that guide you from idea to production:

| # | Ceremony | When | Purpose |
|---|----------|------|---------|
| **1** | [Instruct Session](ceremonies/1-instruct-session.md) | Start of project/cycle | Set context, define constraints |
| **2** | [Alignment Workshop](ceremonies/2-alignment-workshop.md) | Start of Wave | Score features, create roadmap 2D/3D Matrix |
| **3** | [PoD Review](ceremonies/3-pod-review.md) | Feature complete | Validate technical & functional quality |
| **4** | [PoV Review](ceremonies/4-pov-review.md) | After PoD | Validate business value |
| **5** | [Continuous Insight PoR](ceremonies/5-continuous-insight.md) | Weekly | Monitor production, fix issues |

**Flow:** 1 → 2 → Build → 3 → 4 → 5 → Repeat

---

## 🔄 The 3 Phases

D-POAF works in **3 phases** that cycle continuously:

### **Phase 1: [Instruct & Scope](phases/instruct-and-scope.md)**
- Define context and constraints
- Draft initial features with BVS
- Set up AI Mandate

**Output:** Clear scope and feature list

---

### **Phase 2: [Shape & Align](phases/shape-and-align.md)**
- Score features (ERS)
- Calculate priorities (PVS)
- Build optimal roadmap with ODP
- Plan Waves

**Output:** Prioritized roadmap (3D Matrix) & releases path

---

### **Phase 3: [Execute & Evolve](phases/execute-and-evolve.md)**
- Build features
- Validate delivery (PoD)
- Validate value (PoV)
- Monitor and improve (PoR)

**Output:** Working software + learnings

---

## 👥 The 4 Core Roles

| Role | Responsibility |
|------|----------------|
| [Wave Captain](roles/wave-captain.md) | Coordinates delivery cycles |
| [Wave Surfer](roles/wave-surfer.md) | Prompt designer executing tasks |
| [RAGer](roles/rager.md) | Manages knowledge and documentation |
| [Peacekeeper](roles/peacekeeper.md) | Manages knowledge and documentation |
| Community Member | Participates in collective decisions |

---

## 🚀 Quick Start

**1: Instruct Session**
- Define your project context
- List initial features with BVS
- Set constraints & Dynamic laws for governance

**2: Alignment Workshop**
- Score your features (ERS)
- Compute PVS
- Run the prioritization
- Plan your first Wave

**3: Execute & Evolve**
- Build top priority features
- Run PoD Review when done
- Run PoV a,d score 
- Update Dynamic laws (Tenical & Functional)

**4: Continuous Insight**
- Monitor production (PoR)
- Fix issues
- Learn and improve

**Repeat!**

---

## 📊 The 4 Quadrants Matrix

Every feature lands in one quadrant:

| Quadrant | Condition | Action |
|----------|-----------|--------|
| 🟢 **Quick Wins** | High BVS, Low ERS | **Do first** |
| 🔵 **Strategic** | High BVS, High ERS | Plan carefully |
| 🟡 **Nice-to-have** | Low BVS, Low ERS | If time permits |
| 🔴 **To Avoid** | Low BVS, High ERS | Defer or skip |

---

## 🎯 Key Principles

1. **Measure everything** - BVS, ERS, PVS, PoD, PoV
2. **No gut feelings** - evidence drives decisions
3. **Validate twice** - Operational (PoD) then Business (PoV)
4. **Learn continuously** - Update based on reality
5. **Keep it simple** - Start small, add complexity later

---

## 📂 Folder Structure

```
methodology/
├── ceremonies/          # The 5 ceremonies
│   ├── 1-instruct-session.md
│   ├── 2-alignment-workshop.md
│   ├── 3-pod-review.md
│   ├── 4-pov-review.md
│   └── 5-continuous-insight.md
├── phases/              # The 3 phases
│   ├── instruct-and-scope.md
│   ├── shape-and-align.md
│   └── execute-and-evolve.md
├── roles/               # Team roles
│   ├── wave-captain.md
│   ├── wave-surfer.md
│   ├── rager.md
│   └── peacekeeper.md
└── OVERVIEW.md          # This file
```

---

## 🔗 What Makes D-POAF Different?

| Traditional Agile | D-POAF |
|-------------------|--------|
| Story points | BVS/ERS scores (1-10) |
| Gut feeling priority | Mathematical PVS |
| "Definition of Done" | PoD + PoV validation |
| Velocity tracking | Continuous Insight |
| Backlog grooming | ODP optimization |

**Bottom line:** Same workflow, better metrics.

---

## 🛠️ Tools You Need

**Minimum:**
- Spreadsheet (for BVS/ERS scoring)
- GitHub/Jira (for features)
- Discord (for votes)

**Recommended:**
- `dpoaf-prioritization.py` (generates matrix + roadmap)
- Monitoring dashboard (for Continuous Insight)
- AI assistant (for RAGer & Wave Surefer roles)
- 
---

## 📖 Learn More

**Start here:**
1. Read [Instruct Session](ceremonies/1-instruct-session.md)
2. Read [Alignment Workshop](ceremonies/2-alignment-workshop.md)
3. Try scoring 5 features

**Go deeper:**
- [Complete methodology guide](/docs/reference-guide/guide_en_v3.0.pdf)
- [Community Discord](https://discord.gg/J7Mbhx8Awz)

---

## ❓ FAQ

**Q: Do I need to use all 5 ceremonies?**
A: Start with Instruct Session & Alignment Workshop + PoD Review. Add others as needed.

**Q: Can I use D-POAF with Scrum?**
A: Yes! D-POAF ceremonies fit into Scrum sprints.

**Q: How long to learn D-POAF?**
A: 1 hour to understand, 1 wave to practice, 1 month to master.

**Q: Is this just Scrum with extra steps?**
A: No. It's new paradigm 

---

## 🎓 Success Pattern

**Teams succeed when they:**
1. ✅ Start simple Instruct Session (BVS)
2. ✅ Start simple (jus tERS scoring)
2. ✅ Run Alignment Workshop every Wave
3. ✅ Actually validate PoD and PoV
4. ✅ Track reality vs predictions
5. ✅ Adjust based on data

**Teams struggle when they:**
1. ❌ Try to implement everything at once
2. ❌ Skip validation ceremonies
3. ❌ Ignore the data
4. ❌ Over-complicate the process

---

**Ready to start?** Go to [Instruct Session](ceremonies/1-instruct-session.md) 🚀

**Have questions?** Join the [Discord community](https://discord.gg/J7Mbhx8Awz) 💬

**Want to contribute?** Check [CONTRIBUTING.md](../CONTRIBUTING.md) 🤝