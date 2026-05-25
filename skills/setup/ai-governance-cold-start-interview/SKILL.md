---
name: AI Governance Cold-Start Interview
description: "Use when an AI-governance practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to an AI-governance attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled AI-governance practice profile draft for attorney review"
related_skills:
  - skills/ai-governance/ai-use-case-intake/SKILL.md
  - skills/ai-governance/ai-vendor-terms-review/SKILL.md
  - skills/ai-governance/model-risk-triage/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - ai-governance
---

# AI Governance Cold-Start Interview

## Purpose

Conduct a structured, staged interview with an AI-governance practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/ai-governance.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/ai-governance.md` for the first time.
- An AI-governance practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the AI-governance area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the AI-governance practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live AI-governance matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/ai-governance.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific AI-governance matter (use the appropriate matter-level skill for that task).

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Never guess or infer an answer to any interview question. If the interviewee cannot answer a question, record `[CONFIRM: answer required from practice group]` and move on.
- The filled profile is a draft. It must be reviewed and explicitly approved by the supervising attorney or practice group before it governs any AgentCounsel work product.
- Do not invent standard positions, clause preferences, escalation thresholds, or review rules. Record only what the interviewee provides.
- Do not include client-specific facts, client names, matter identifiers, or privileged details in the profile. The profile is a reusable group-level configuration, not a matter record.
- Do not state or imply that any threshold, position, or rule in the profile satisfies a legal requirement under any jurisdiction. Jurisdiction-specific legal obligations are for the attorney to verify.
- Flag every item the interviewee defers or leaves open with a visible `[CONFIRM: ...]` placeholder so the reviewer can see exactly what is unresolved.

## Workflow

**Stage 1 — Jurisdictions**

Ask the interviewee:
- In which jurisdictions are the client's AI systems deployed, trained, or made available — including but not limited to EU (AI Act), US (federal and state, e.g., Colorado, NYC bias audit, California ADMT), UK, China, Brazil, and others?
- Does the group advise on sector-specific AI regimes — FDA, HIPAA, FCRA, FTC, financial services, education, employment?
- Are there jurisdictions where the group's clients face heightened AI regulation (e.g., EU AI Act high-risk-system obligations) that require special handling?
- Are there jurisdictions or sectors the group treats as out of scope, requiring specialist outside counsel?
- Does the group maintain jurisdiction-by-jurisdiction tracking of AI regulatory developments, and where is it stored?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Who are the primary clients of the AI-governance group — product teams, AI engineering, vendor management, executives, board, external clients?
- What types of AI-governance matters does the group handle most frequently — use-case intake, vendor terms review, feature reviews, incident response, policy work, regulatory advice?
- How is the team structured, and how does it coordinate with privacy counsel, security counsel, and product counsel?
- Are there model types (foundation models, fine-tuned models, retrieval-augmented systems, agentic systems) or use cases (employment decisions, biometric, child-facing, healthcare) that require special handling?
- How does the group engage with the client's AI risk committee, ethics board, or analogous governance function?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which use-case categories automatically require escalation — EU AI Act high-risk uses, biometric categorization or remote biometric identification, automated employment decisions, education decisions, lending decisions, child-directed systems?
- What model events trigger escalation — base-model change, training-data source change, deployment to new region, deployment to consumer-facing context?
- When does an AI incident (model failure, hallucination causing harm, prompt-injection-driven action, bias finding) require immediate attorney involvement?
- What vendor-terms scenarios require escalation — vendor training rights on customer data, retention rights, indemnification gaps, sub-processor scope?
- Who is the designated escalation contact for AI-governance matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should AI-governance work product default to AI impact assessment format, use-case intake checklist format, gap analysis, or memo format?
- What level of detail does the practice group expect — executive summary only, full risk register, both layered?
- Are there house style rules for risk ratings, mitigation recommendations, or open questions in AI work product?
- Does the group produce model cards, AI system inventories, or AI registers, and if so, in what format?
- Are there particular deliverable types — vendor terms review, feature launch review, incident memo — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative source of truth for the AI policy, AI principles, and risk-classification taxonomy?
- Is there an authoritative AI use-case register or inventory? Where is it stored, and how is it kept current?
- What document governs the group's vendor-evaluation criteria for AI vendors?
- Is there an AI-incident response playbook, and what document governs it?
- Are there sector-specific reference materials (e.g., FDA AI/ML guidance, HHS guidance on AI in healthcare) the group treats as authoritative?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default posture on training-data sourcing — permissible sources, prohibited sources, due-diligence requirements?
- What is the group's default consent posture for personalization, profiling, or training-data uses involving personal data?
- What is the group's default human-in-the-loop posture for decision-supporting AI vs. decision-making AI?
- What is the group's default logging, audit, and explainability posture for high-risk uses?
- What is the group's default vendor-terms position on training rights, retention rights, and indemnification?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of AI work product become mandatory — at use-case intake, before any model deployment, before any vendor signing, before any high-risk deployment, before any consumer-facing launch?
- Are there matter types for which attorney review is always required regardless of stage — any high-risk system, any biometric system, any automated employment or lending decision?
- What is the designated reviewer's role — AI counsel, supervising attorney, AI risk committee chair, general counsel?
- What is the expected turnaround for standard AI-governance review, and how are urgent reviews (incident, regulator inquiry) handled?
- Is there a formal sign-off step before an AI feature is launched, a vendor agreement is signed, or an incident response is communicated externally?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that training data is lawfully sourced, that a model output is non-hallucinated, that a vendor's model card is current, that a use case is low-risk?
- Are there AI-specific risks — bias, hallucination, prompt injection, data exfiltration, model inversion, IP leakage — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — incidents, regulator inquiries, high-risk deployments?
- Are there prior incidents, regulator findings, or lessons learned that should be encoded as explicit prohibitions for agents working on AI-governance matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/ai-governance.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/ai-governance.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including EU AI Act, US state laws, sector-specific regimes — is accurately recorded `[Verify current law]`.
- [ ] High-risk use-case definitions and escalation triggers are consistent with the EU AI Act framework and any other applicable framework `[verify jurisdiction]`.
- [ ] Vendor-terms default positions reflect the current threat landscape (training rights, data retention, indemnification, sub-processor flow-down).
- [ ] Incident-response posture is current and aligned with applicable breach-notification obligations `[verify jurisdiction]` and all incident deadlines are marked `[deadline verification required]`.
- [ ] AI register / inventory is referenced and the maintenance owner is named.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/ai-governance.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
