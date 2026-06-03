# Quality Layer

AgentCounsel's quality layer is a set of reusable legal-methodology skills
that run after a primary skill produces draft work product. The layer improves
reviewability: it audits source support, citations, assumptions, hallucination
risk, privilege/confidentiality, output format, and legal prose before a
qualified attorney relies on the work.

The quality layer does not provide legal advice, certify legal correctness, or
automatically verify current law. It produces draft quality-control work
product for attorney review.

## Checks

| Check | Path | Use when |
|---|---|---|
| Legal Prose Polish | `skills/legal-methodology/legal-prose-polish/SKILL.md` | A draft needs tighter, less AI-sounding legal prose without changing legal meaning. |
| Citation Integrity Check | `skills/legal-methodology/citation-integrity-check/SKILL.md` | Citations, quotations, pin cites, authority status, or unsupported legal propositions need review. |
| Source Validation | `skills/legal-methodology/source-validation/SKILL.md` | Claims need to be classified against source materials available in the session. |
| Assumption Audit | `skills/legal-methodology/assumption-audit/SKILL.md` | The draft may rely on hidden assumptions, missing facts, missing documents, jurisdiction gaps, or deadline gaps. |
| Hallucination Red-Team | `skills/legal-methodology/hallucination-red-team/SKILL.md` | A model-generated draft needs claim-origin separation and unsupported-claim review. |
| Attorney Review Gate | `skills/legal-methodology/attorney-review-gate/SKILL.md` | A high-risk draft needs final pre-attorney-review triage. |
| Privilege and Confidentiality Check | `skills/legal-methodology/privilege-confidentiality-check/SKILL.md` | The draft contains sensitive facts or may be shared outside the legal team. |
| Output Format Compliance Check | `skills/legal-methodology/output-format-compliance-check/SKILL.md` | The draft must match a requested memo, email, demand letter, matrix, chronology, checklist, client update, or research-summary format. |

## Typical Sequence

1. Run the primary practice-area skill.
2. Run `assumption-audit` if facts, documents, jurisdiction, deadlines, or
   client role are incomplete.
3. Run `source-validation` for material factual or legal claims.
4. Run `citation-integrity-check` for legal authorities and quotations.
5. Run `hallucination-red-team` for model-generated or high-risk drafts.
6. Run `privilege-confidentiality-check` before external sharing.
7. Run `output-format-compliance-check` if a strict deliverable structure is
   required.
8. Run `legal-prose-polish` after support and safety issues are visible.
9. Run `attorney-review-gate` before the draft goes to attorney review.

## Metadata And Packs

`scripts/build_skill_index.py` derives `recommended_quality_checks` for every
skill in `metadata/index.json`. High-risk skills recommend the attorney review
gate and assumption audit. Drafting skills recommend prose and format checks.
Research and authority-heavy skills recommend citation integrity and source
validation. Review skills recommend source validation and assumption audit.

`scripts/build_platform_packs.py` rolls those recommendations into
`metadata/packs.json`, so platform packs can disclose which quality checks are
included.

The quality skills are ordinary `SKILL.md` files, so they participate in the
same eval system as other skills under `evals/skills/`. Matter workspaces can
record quality outputs as review artifacts next to the primary draft, source
materials, assumptions, and attorney notes.

Fictional examples live in [`examples/quality-layer/`](../examples/quality-layer/).

## Limits

- The quality layer does not independently verify current law.
- Citation integrity is a structured review workflow, not automated legal
  citation verification.
- Source validation classifies support against provided or session-available
  materials; it does not guarantee legal correctness.
- The attorney review gate means ready for attorney review, not ready for
  reliance or external use.
- A quality check can surface a problem; it cannot make attorney review
  optional.
