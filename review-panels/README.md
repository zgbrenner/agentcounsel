# Review Panels

A **review panel** is a safe, supervised multi-pass review workflow: a single
document or draft is run through a defined *sequence of review passes*, each
with a specific lens, producing draft findings the supervising attorney
consolidates. The panel surfaces issues; it never decides anything.

Review panels are not legal advice and not legal work product. They are process
guidance. Every pass a panel runs produces draft work product that a qualified,
licensed attorney must review and adopt.

> **The passes are not lawyers and not autonomous agents.** Each "reviewer"
> named in a panel is a structured *review pass* — a persona, a lens, a defined
> question — run over the draft to surface issues. A pass does not act on its
> own, does not communicate with anyone, does not approve or send anything, and
> is not a licensed attorney. The output of every panel is attorney-supervised
> draft work product, and the final call always belongs to the supervising
> attorney.

## What a review panel is — and what it is not

A panel orchestrates the existing quality layer (`skills/legal-methodology/`)
into a repeatable multi-lens review of one draft. It does not introduce new
analysis engines, a backend, or any runtime. It is plain Markdown a person
follows by hand.

- A **skill** (`skills/`) is one workflow — one step that produces a draft.
- A **quality check** (`skills/legal-methodology/...`) is one verification pass
  over a draft — citation integrity, privilege, assumptions, the final gate.
- A **playbook / matter pack** (`matter-packs/`) bundles several *skills* into
  an ordered sequence for a whole matter.
- A **matter workspace** (`matter-workspaces/`) holds one matter's parties,
  facts, deadlines, and the draft work product the skills produce.
- A **review panel** (this directory) takes *one finished or near-finished
  draft* and runs it through several *review passes* — each a persona with a
  distinct lens — to surface issues for the attorney before reliance. Where a
  matter pack sequences production skills, a panel sequences review lenses over
  a single deliverable.

A typical use: a skill or matter pack produces a draft; the draft is stored in a
matter workspace; a review panel is run over it; the consolidated findings go to
the supervising attorney through the attorney-review gate.

## The eight panels

| Panel | When to use |
|---|---|
| `contract-review-panel.md` | A drafted or marked-up contract needs a multi-lens issue, position, and risk review before it goes back to the client or counterparty. |
| `litigation-risk-panel.md` | A litigation-bound draft (memo, demand, brief section) needs an issue-spotting and risk review before filing or sending. |
| `regulatory-risk-panel.md` | A regulatory-facing draft (filing, policy, compliance memo) needs a compliance, business-risk, and source review. |
| `citation-source-red-team-panel.md` | Any draft that relies on cited authority needs a focused source and citation red-team before reliance. |
| `external-communication-review-panel.md` | A draft leaving the firm (client letter, counterparty email, public statement) needs a client-position, privilege, and tone review. |
| `deal-diligence-review-panel.md` | A diligence work product (issue list, gap matrix, summary) needs a completeness, position, and risk review before it informs a deal decision. |
| `individual-client-capacity-panel.md` | An individual-client draft (family-law or trusts-and-estates) needs a capacity, safety, confidentiality, and plain-language review before it reaches the client. |
| `deadline-critical-bankruptcy-panel.md` | A deadline-sensitive bankruptcy or restructuring draft needs a deadline-discipline, automatic-stay, and no-conclusions review before it informs a filing. |

## How to use a review panel

1. Read the `core/` operating rules and the relevant practice profile.
2. Pick the panel whose "When to Use" fits the draft in hand.
3. Confirm the panel's Inputs are available; gather what is missing or flag it.
4. Run the review passes in the panel's stated Sequence, carrying each pass's
   draft findings forward as context for the next.
5. Run the panel's Required Quality Checks (the `skills/legal-methodology/...`
   passes it references).
6. Consolidate every pass's findings and hand them to the supervising attorney
   through the Final Attorney-Review Gate, unchecked.

A panel is a recommended path, not a rule. Add, drop, or reorder passes when the
draft calls for it — and route anything a panel does not cover through
`WORKFLOW_ROUTER.md`.

## Safety and supervision model

- **Passes surface; the attorney decides.** No pass approves, signs, sends,
  files, or certifies anything. Each produces draft findings only.
- **No pass is autonomous.** A pass is a lens applied by the person running the
  panel; it does not run itself, talk to anyone, or take any action.
- **No pass is a lawyer.** A persona name ("client-position reviewer") describes
  the lens, not a licensed professional. None of them practices law.
- **Markdown-native, no backend.** Every panel is plain Markdown that works in
  any text editor or AI assistant. There is no runtime, login, or vendor
  dependency. See `core/legal-work-product.md` and the repository `README.md`.

The attorney gatekeeper pass that ends most panels is itself a *review pass*
that organizes issues for the supervising attorney — it is not the attorney and
does not replace the attorney's independent judgment.
