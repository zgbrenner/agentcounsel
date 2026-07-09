# Playbooks

A **playbook** is a workflow recipe for a recurring legal task type. It is
richer than a matter pack: where a matter pack is an ordered *sequence of
skills*, a playbook adds the things a recurring task needs to be run well and
safely — default client-position questions, risk-tolerance settings, the source
materials the task requires, the quality checks it must pass, common failure
modes, and source/citation expectations.

Playbooks are process guidance, not legal advice and not legal work product.
Every skill a playbook references still produces **draft legal work product that
a qualified, licensed attorney must review.** A playbook decides nothing: it
does not conclude that a provision is enforceable, state the law, compute a
deadline, approve a signature or filing, or reach a legal conclusion. Those
remain attorney work. Before starting any playbook, read the `core/` operating
rules and the relevant practice profile, and confirm the jurisdiction, governing
law, posture, the client's role, and the relevant date.

## How a playbook differs from the rest of the library

- A **skill** (`skills/`) is one workflow — one step. `WORKFLOW_ROUTER.md`
  routes a single task to the one right skill.
- A **matter pack** (`matter-packs/`) bundles several skills into an ordered
  sequence for a whole matter — "first run this, then this, then this."
- A **matter workspace** (`matter-workspaces/`) is the file (or, via
  `matter-workspaces/_template/`, the multi-file scaffold) that holds one
  specific matter's parties, facts, deadlines, sources, and draft outputs.
- A **review panel** runs several quality-layer checks over a finished draft.
- A **playbook** (this directory) is the recipe for a *recurring task type*. It
  names the default questions to ask the client, the risk-tolerance dials to
  set, the inputs and sources to gather, the primary skills to run, the quality
  checks to pass, and the failure modes to watch for — so the same kind of task
  is run the same disciplined way every time.

A typical recurring matter uses several of these together: pick the playbook for
the task type, open a matter workspace (use `matter-workspaces/_template/` when
the task is multi-step or source-intensive), run the playbook's primary skills,
apply its required quality checks, and keep every output in the workspace until
an attorney reviews it.

## The playbooks

| Playbook | When to use |
|---|---|
| `nda-review.md` | A counterparty NDA or confidentiality agreement needs a first-pass risk read and prioritized redline points. |
| `commercial-contract-review.md` | An MSA, SaaS, services, or supply agreement needs a clause-by-clause risk review against the client's positions. |
| `employment-termination-analysis.md` | A proposed employee separation or termination needs a risk read before any decision is communicated. |
| `litigation-demand-letter.md` | Counsel has supplied a claim theory and wants a draft demand letter prepared for attorney review. |
| `regulatory-rule-change-summary.md` | A new or proposed rule, guidance, or regulation needs a structured plain-language impact summary. |
| `privacy-dpa-review.md` | A data processing agreement or addendum needs review against the client's data-protection positions. |
| `corporate-governance-review.md` | A proposed board or shareholder action needs draft consents/minutes and a governance-authority check. |
| `securities-disclosure-review.md` | An offering document, periodic report, or risk-factor set needs a disclosure-consistency and completeness review. |
| `ip-brand-clearance-and-enforcement.md` | A new brand or mark needs a clearance read, or an infringement / cease-and-desist situation needs a triage and draft response. |
| `ai-governance-use-case-review.md` | A proposed AI/ML use case needs intake, model-risk triage, and routing through governance review. |
| `product-launch-legal-review.md` | A product, feature, or campaign approaching launch needs a pre-launch review of launch issues, marketing claims, and terms of service. |
| `aml-customer-lifecycle-review.md` | A customer needs an AML/BSA lifecycle review — KYC onboarding, sanctions screening, monitoring-alert triage, or enhanced due diligence. |
| `legal-research-memo.md` | A specific legal question needs a scoped, IRAC-structured research memo with synthesized and treatment-checked authority. |
| `legal-intake-response.md` | An inbound business request to the legal team needs triage, a templated or briefed response, and, where relevant, signature routing. |

## Safety posture

Every playbook in this directory follows the non-negotiable rules in `core/`:

- **Draft, do not decide.** Output is a draft for attorney review — never legal
  advice, an opinion, or a final answer.
- **Never invent authority.** No case, statute, regulation, citation,
  quotation, or deadline is asserted unless it traces to a provided or verified
  source. Everything else is a visible placeholder.
- **Never compute a deadline.** Dates are user-supplied or unverified and are
  flagged `[deadline verification required]`.
- **Identify the gates.** Jurisdiction, governing law, posture, client role,
  and the relevant date are confirmed or flagged unknown before substantive
  work.
- **Fictional examples only.** No real client facts appear in a playbook.
- **Attorney review gate is mandatory.** Each playbook ends by reinforcing it.

## Markdown-native, no backend

Every file here is plain Markdown. Playbooks have no runtime, build step,
database, login, or vendor dependency. They work in any text editor, any AI
assistant, and any document system. To add a playbook for another recurring task
type, copy the section structure of an existing file: the twelve H2 sections, in
order, after the H1 title and the disclaimer paragraph. Keep every skill
reference a real `skills/<area>/<skill>/SKILL.md` path.
