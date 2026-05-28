# Review Panels

A **review panel** (`review-panels/<panel>.md`) is a safe, supervised multi-pass
review workflow. A draft or document is run through a defined sequence of review
passes, each applying one lens, and each producing draft findings for the
supervising attorney. The panel produces **draft legal work product for attorney
review** — never legal advice and never a final decision.

> **Review passes are review passes — not autonomous agents and not lawyers.**
> Each "reviewer" is a structured pass with a specific lens. The passes do not act
> on their own, do not represent licensed attorneys, and do not decide anything.
> The final output remains attorney-supervised draft work product, gated by the
> attorney gatekeeper pass and the matter's attorney-review gate.

## When to use a review panel

Use a panel when a high-risk draft needs more than one review lens before it is
relied upon — for example, a negotiated contract before signing, a litigation
risk assessment, or an external communication. For a single review pass over a
finished draft, run a quality-check skill directly instead.

## Available panels

| Panel | When to use |
|---|---|
| `review-panels/contract-review-panel.md` | Multi-lens review of a contract before signing. |
| `review-panels/litigation-risk-panel.md` | Structured review of a litigation posture or filing. |
| `review-panels/regulatory-risk-panel.md` | Review of a regulatory position or compliance analysis. |
| `review-panels/citation-source-red-team-panel.md` | Adversarial review for invented or unsupported authority. |
| `review-panels/external-communication-review-panel.md` | Review of a communication leaving the organization. |
| `review-panels/deal-diligence-review-panel.md` | Review of diligence findings on a transaction. |

## Review passes (personas)

A panel selects from these passes; the attorney gatekeeper always runs last:

- **Primary drafter** — produces or restates the draft under review.
- **Issue spotter** — surfaces issues, risks, and gaps.
- **Source/citation reviewer** — checks that statements trace to classified
  sources and that authorities are verified or flagged.
- **Client-position reviewer** — checks alignment with the client's role,
  objectives, and risk tolerance.
- **Privilege/confidentiality reviewer** — checks privilege and confidentiality
  exposure.
- **Business-risk reviewer** — surfaces business and commercial friction.
- **Attorney gatekeeper** — the supervised gate; consolidates findings for the
  supervising attorney. Not a substitute for attorney review.

Each pass is a review lens, not an autonomous agent or a lawyer.

## Required sections

Every panel follows the same structure, in order: When to Use, Inputs, Review
Passes, Sequence, Required Quality Checks, Attorney Escalation Triggers, Expected
Outputs, Safety and Supervision Model, Common Failure Modes, Final
Attorney-Review Gate.

## Relationship to other surfaces

- Panels orchestrate the `skills/legal-methodology/` quality layer over a draft.
- Record a panel run in a matter workspace's `quality_checks/` folder.
- A playbook may call for a review panel as part of its required quality checks.

See `WORKFLOW_ROUTER.md` for routing, `docs/QUALITY_LAYER.md` for the underlying
checks, and `docs/SAFETY_MODEL.md` for the supervision model. Panels are plain
Markdown with no backend.
