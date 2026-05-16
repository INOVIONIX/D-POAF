<!--
D-POAF® Pull Request Template
Per Dynamic Law DL-002 (No Blind Acceptance) and DL-005 (AI Output Attribution).
-->

## What does this PR change?

<!-- Brief description of the change -->

## Wave reference

<!-- Link the Wave Scope issue -->
Closes #

## D-POAF Compliance Checklist

### AI involvement in this PR

- [ ] No AI-generated content (skip the rest of this section)
- [ ] AI was used, **commit messages carry `[AI:<model>:<PA-ID>]` tag** (per DL-005)
- [ ] All AI Prompt Actions are logged in the PromptRegister BEFORE invocation (per DL-006)
- [ ] All AI-generated outputs have been reviewed by a second human role (per DL-002 + DL-011)

### Prompt Actions in this PR

<!-- List the PA-IDs that produced code/docs/tests in this PR -->
- PA-XXX: <short title>: #<PA issue number>
- PA-XXX: <short title>: #<PA issue number>

### Model + configuration

<!-- For each PA, confirm model identity is logged in the PromptRegister -->
- [ ] Model provider + name + version recorded for every PA (DL-003)
- [ ] Model config (temperature, system prompt hash, tools) recorded for every PA
- [ ] Context source (RAG snapshot, doc version) recorded for every PA

### Traceability Thread

<!-- Confirm that any artifact in this PR can be traced back to its origin -->
- [ ] Every AI-touched file has a corresponding PA-ID in commit history
- [ ] PA-IDs are linked to the Wave Scope issue
- [ ] Reviewer can reproduce the AI generation from PromptRegister entry

### Approved AI tools

- [ ] All AI tools used appear in the Wave Scope §B (DL-001: Approved AI Tools)
- [ ] No undisclosed AI tools were used

## Reviewer notes

<!-- For the reviewer: pay extra attention to AI-touched code -->
- [ ] AI-generated code reviewed line by line (not skim-reviewed)
- [ ] Tests cover the AI-generated logic, including edge cases the AI may have missed
- [ ] No leaked secrets, no hallucinated APIs, no unreviewed deps
