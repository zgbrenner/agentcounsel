> Shared reference material supporting the AgentCounsel litigation skills, used to help produce draft legal work product for attorney review — not legal advice.

# Litigation Output Patterns

This file collects the **common rules every litigation skill follows** in its Output Format — the cross-cutting discipline that should be true of a chronology, a claim chart, a demand letter, a hold notice, an intake, a privilege log review, a subpoena triage, a deposition outline, and a brief section alike. Each skill's own `SKILL.md` remains the authoritative spec for what that skill produces; this file is a consistency reference, not a substitute.

Each litigation skill's output is structurally different. There is no shared "Litigation Output Table" the way the newer practice areas have a single dominant output shape — a chronology is not a claim chart is not a hold notice. What is shared is the **operating discipline** that every output must satisfy.

---

## Universal rules

These apply to every deliverable from every skill in `skills/litigation/`.

- **Every output is a draft.** Each deliverable opens with a clearly visible draft-for-attorney-review label. Output never asserts itself as final, approved, served, filed, or sent.
- **Every output is not legal advice.** Each deliverable carries a not-legal-advice notice. Output never tells a user what they "must" do, what a court "will" do, or what "the law" is in a given jurisdiction without an authority placeholder.
- **Every extracted fact cites its source.** A row in a chronology, a cell in a claim chart, a quoted statement in a demand letter, a custodian on a hold notice, a category on a subpoena triage — each traces to a document, a Bates range, a docket entry, or a user-stated fact, labeled as such.
- **Every date is treated as user-supplied or document-supplied.** No deadline is computed. Each compliance, response, or filing date is recorded as the document states it and tagged `[deadline verification required]` or `[CRITICAL — CONFIRM IMMEDIATELY]` for high-urgency items.
- **Every placeholder is visible.** `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[DISPUTED]`, `[deadline verification required]`, and `[verify jurisdiction]` are never silently filled. A gap is preserved as a gap.
- **No invented authority.** No case, statute, rule, citation, quotation, court, judge, party, address, or counsel-of-record is inferred from training memory. Anything not in the provided record is a placeholder.

## Privilege and work-product framing

Litigation deliverables sit closer to privilege than most of the library. Each output makes its privilege posture explicit on its face.

- **Internal-only sections carry a privilege header.** Pre-draft notes, drafting notes, preservation-scope summaries, deposition outlines, intake assessments, and any internal-only deliverable open with **"Privileged & Confidential — Attorney Work Product."**
- **Outbound documents do not.** A demand letter, a hold notice, a discovery response, or any document intended to be served, sent, or produced once finalized must not be drafted carrying a privilege header. Privilege framing applies to the drafting notes about that document, not to the document itself.
- **Mixed documents are split.** When a deliverable carries both an internal section (e.g., scope notes) and an outbound section (e.g., the notice), the outbound section is presented separately and is not labeled work product. The skill never mixes the two on the same page.

## Sourcing and chronology integrity

Litigation skills draw heavily on document records. Every output that organizes facts follows three rules.

- **Verbatim or paraphrase, never invented.** Quoted text appears in quotation marks with a source. Paraphrase is labeled as paraphrase. A fact without a source is not in the chronology, the claim chart, the brief, or the demand letter.
- **Gaps named, not filled.** A missing date, missing custodian, missing exhibit, or missing element is recorded as `not found`, `not provided`, `unknown`, or `[CONFIRM]` — never reconstructed from context.
- **Disputed items flagged.** Where two sources conflict, both are recorded and the item is marked `[DISPUTED]`. The skill does not adjudicate the dispute.

## What the outputs never do

- They never assert that a claim is meritorious, that a defense will succeed, that a witness is credible, that a motion will be granted or denied, that conduct gives rise to liability, or that a settlement value is appropriate.
- They never compute a response deadline, a service date, a statute of limitations, or any other date from a rule, calendar, or holiday calculation.
- They never assert privilege without identifying the basis from the provided record, and they never deny privilege.
- They never approve service, finalization, or transmission. Every deliverable goes through the Attorney Verification Checklist before it leaves the draft state.

All output is draft work product for attorney review.
