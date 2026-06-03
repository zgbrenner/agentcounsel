---
name: Output Format Compliance Check
description: "Use when checking whether draft legal work product matches the requested format, required sections, labels, tables, chronology, checklist, matrix, memo, email, demand letter, client update, or research-summary structure."
practice_area: legal-methodology
task_type: verification
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The draft output to check"
  - "The requested format or originating AgentCounsel skill"
  - "Any required sections, table columns, templates, or client formatting instructions"
outputs:
  - "Output format compliance report"
  - "Corrected skeleton or missing-section checklist"
related_skills:
  - skills/legal-methodology/legal-prose-polish/SKILL.md
  - skills/legal-methodology/attorney-review-gate/SKILL.md
  - skills/legal-methodology/assumption-audit/SKILL.md
tags:
  - legal-methodology
  - output-format
  - format-check
  - quality-control
  - verification
---

# Output Format Compliance Check

## Purpose

Check whether draft legal work product follows the requested format and includes required sections, labels, tables, and verification items. The skill can review memos, emails, demand letters, risk tables, contract review matrices, chronologies, checklists, client updates, and research summaries.

It identifies missing sections and produces a corrected skeleton if needed. It does not decide whether the legal substance is correct.

## Use When

- A draft may not match the requested output format.
- A draft should follow an AgentCounsel skill's Output Format but appears incomplete.
- The user asks to check formatting, sections, table columns, chronology structure, checklist structure, or memo/email/demand-letter format.
- A platform pack or one-off prompt output needs a deterministic structure check before attorney review.

## Required Inputs

- The draft output to check.
- The requested format, originating skill, template, or client formatting instructions.
- Any required sections, table columns, headings, labels, or checklist items.

If the requested format is unknown, infer the likely format from the draft type only as a provisional check and state the limitation.

## Do Not Use When

- The task is substantive legal review, source validation, or citation checking.
- The user wants formatting to override legal safety labels or attorney-review checklists.
- The task requires finalizing or sending the draft.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Follow `core/output-format-rules.md`.
- Follow `core/source-and-citation-discipline.md`; do not invent legal authority, citations, quotations, facts, or deadlines.
- Do not remove draft labels, attorney-review warnings, placeholders, or verification checklists for style reasons.
- Do not fill missing substantive sections with invented analysis. Provide a skeleton and mark missing content.
- Preserve privilege and confidentiality labels.

## Workflow

1. **Identify expected format.** Determine whether the output should be a memo, email, demand letter, risk table, contract review matrix, chronology, checklist, client update, research summary, or another format.
2. **Identify required structure.** Use the originating skill's Output Format, provided template, or client instructions to define required sections and columns.
3. **Check universal labels.** Confirm draft legal work product label, not-legal-advice framing, assumptions/open items, source/citation placeholders, and attorney verification checklist.
4. **Check format-specific elements.**
   - Memo: question presented, facts, assumptions, law/authority, analysis, conclusion, verification items.
   - Email/client update: audience-appropriate subject, concise context, decision needed, next steps, caveats.
   - Demand letter: parties, factual basis, requested action, deadline flag, reservation/caveat language, attorney review.
   - Risk table/matrix: issue, source, risk level, rationale, recommendation, owner, verification item.
   - Chronology: date, event, source, relevance, uncertainty, privilege flag.
   - Checklist: task, owner, source, status, due date flag, verification item.
   - Research summary: issue, source list, authority status, analysis limits, current-law verification.
5. **Flag missing or malformed sections.** Identify omissions, wrong order, missing columns, inconsistent labels, and mixed facts/analysis.
6. **Produce corrected skeleton.** Provide headings and table columns with placeholders, not invented content.

## Output Format

Deliver:

1. **Draft Label** — "Draft legal work product for attorney review. Not legal advice."
2. **Expected Format**
3. **Compliance Summary** — Compliant / Partially compliant / Noncompliant.
4. **Missing or Defective Elements Table**

   | Element | Required? | Present? | Defect | Correction |
   |---|---|---|---|---|

5. **Corrected Skeleton** — Headings, table columns, and placeholders needed to bring the draft into format compliance.
6. **Attorney Verification Checklist**

## Attorney Verification Checklist

- [ ] The draft matches the requested format or the originating skill's Output Format.
- [ ] Required sections and columns are present.
- [ ] No safety label, placeholder, or verification checklist was removed.
- [ ] Missing substantive content remains marked as missing; no analysis was invented.
- [ ] Facts, assumptions, authority, analysis, recommendations, and verification items are separated.
