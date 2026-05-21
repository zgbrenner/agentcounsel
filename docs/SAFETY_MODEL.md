# AgentCounsel Safety Model

AgentCounsel is used inside legal workflows, where a wrong answer can cause real harm — a missed deadline, a waived privilege, a bad citation in a filing, a contract signed on the wrong terms. The library is therefore designed around a single, conservative assumption:

> **The AI is a drafting assistant. A licensed attorney is the decision-maker.**

Every skill, every template, and every operating rule exists to keep that relationship intact. This document explains how.

## 1. The core principle

AgentCounsel produces **draft legal work product for attorney review**. It does not give legal advice, and it is not a substitute for a lawyer.

Concretely, that means every skill is built so that:

- its output is explicitly framed as a **draft**;
- the output ends with an **Attorney Verification Checklist** of things a supervising attorney must confirm; and
- anything the skill could not verify is left as a **visible placeholder**, not a guess.

If a skill ever reads as though it is delivering a finished answer a non-lawyer can act on, that is a bug.

## 2. The operating rules every skill inherits

Each skill inherits the rules in [`core/`](../core/). These are the substance of the safety model:

| Core rule | What it enforces |
|---|---|
| [`legal-work-product.md`](../core/legal-work-product.md) | Output is draft work product for attorney review — never legal advice, never a final answer. |
| [`source-and-citation-discipline.md`](../core/source-and-citation-discipline.md) | Never invent legal authority, citations, quotations, statutes, cases, or rules. Label what is sourced, assumed, or unverified. |
| [`jurisdiction-and-deadline-gates.md`](../core/jurisdiction-and-deadline-gates.md) | Identify jurisdiction and governing law, or flag them as unknown. Never compute or assume a legal deadline. |
| [`confidentiality-and-privilege.md`](../core/confidentiality-and-privilege.md) | Treat all matter material as confidential and potentially privileged. Keep client facts out of reusable templates. |
| [`output-format-rules.md`](../core/output-format-rules.md) | Separate facts, assumptions, law, analysis, strategy, and verification items so a reviewer can see what rests on what. |
| [`attorney-review-checklist.md`](../core/attorney-review-checklist.md) | Every deliverable ends with an explicit checklist for the supervising attorney. |
| [`business-stakeholder-communication.md`](../core/business-stakeholder-communication.md) | When output goes to a non-lawyer, it is a plain-language summary that still routes decisions through counsel. |

Read these once. They apply to every skill in the library.

## 3. Safety is layered

No single check is trusted to catch everything. AgentCounsel applies safety at three stages.

**Design time — when a skill is written.** Every skill must follow a fixed structure (Purpose, Use When, Required Inputs, Do Not Use When, Legal Safety Rules, Workflow, Output Format, Attorney Verification Checklist) and carry standardized metadata. `scripts/validate_repo.py` enforces the structure, the safety framing, the source/citation language, and link integrity — and runs in CI on every change. Contributions are reviewed against [`CONTRIBUTING.md`](../CONTRIBUTING.md), where the safety rules are non-negotiable.

**Skill time — when a skill runs.** Each skill scopes itself: "Use When" and "Do Not Use When" tell the agent when *not* to act, and several skills include explicit escalation or routing gates that stop the workflow and hand the matter to counsel. The skill gathers Required Inputs first and refuses to proceed on guesses.

**Output time — before the work is used.** Every deliverable ends with an Attorney Verification Checklist. For high-stakes output, the [`red-team-verifier`](../skills/legal-methodology/red-team-verifier/SKILL.md) skill runs a final adversarial pass — looking for invented authority, unsupported claims, weak reasoning, and jurisdiction or deadline gaps. None of this replaces a human attorney's review; it makes that review easier and more reliable.

## 4. What AgentCounsel deliberately does not do

These are intentional limits, not missing features:

- **It does not give legal advice or tell you what the law is.** Skills supply process and structure. The law of a jurisdiction is supplied by the attorney, per matter.
- **It does not state or compute deadlines.** Limitations periods, filing dates, and notice windows are always flagged for attorney verification, never calculated.
- **It does not invent authority.** If a skill needs a citation it does not have, it leaves a placeholder. No skill or example contains a fabricated case, statute, or quotation.
- **It does not certify, opine, or sign off.** A "PASS" from the red-team verifier, or a "GREEN" triage rating, is a workflow signal — not authorization to file, send, or sign.
- **It does not act on its own.** A legitimate skill is workflow instructions, not a program. It will never ask you to run code, install packages, send data, or call external tools beyond its stated workflow.
- **It does not retain client facts in reusable files.** Templates and examples use fictional placeholders only.

## 5. Threat model

AgentCounsel runs inside AI agents that read documents and follow instructions. Three risks matter most.

**Prompt injection.** A document under review — a contract, an email, a filing, web content — may contain text crafted to manipulate the agent ("ignore your instructions", "approve this", "send this elsewhere"). Skills treat the content of any reviewed document as **data, not instructions**. Operators should do the same and review output for signs of manipulation.

**Untrusted skill files.** A `SKILL.md` is just text an agent will follow. A skill file from outside this repository is an untrusted instruction set. Vet third-party skills before use, the way you would vet any instruction given to staff, and do not install unreviewed skills into a legal workflow. See [`SECURITY.md`](../SECURITY.md).

**Model error and hallucination.** Language models can produce confident, fluent, wrong output — invented citations being the classic failure. The source/citation discipline, the visible-placeholder convention, the Attorney Verification Checklist, and the red-team verifier all exist to surface these errors. The final safeguard is always a human attorney.

## 6. Using AgentCounsel safely with confidential material

- Only place privileged or confidential material into AI systems that are **approved** for the matter and the client under your organization's policies and any client agreement.
- Confirm where a tool stores, logs, and processes inputs before you use it.
- Keep matters separated — do not let one client's information enter another's workflow.
- Review every output before it is relied upon, filed, or sent. Verify every citation, quotation, date, and factual claim.

Operational security guidance and vulnerability reporting are in [`SECURITY.md`](../SECURITY.md).

## 7. The limits of this model

This safety model reduces risk; it does not eliminate it. AgentCounsel cannot judge whether a workflow is legally sound for your matter, whether a model's output is correct, or whether the framing is right for your jurisdiction. The validator checks structure and consistency, not legal accuracy.

The model works only if the human part works. AgentCounsel is built to make attorney review **easy and reliable** — it is not built to make it **optional**. Used as intended, with a qualified, licensed attorney reviewing the output, it makes AI-assisted legal work more consistent and more auditable. Used as a shortcut around that review, it is unsafe.
