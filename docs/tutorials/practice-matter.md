# Practice Matter: Your First Skill Run, End to End

A guided walkthrough for running a single AgentCounsel skill for the first
time, start to finish. It follows a **tabletop-exercise** structure — stated
objectives, a scenario, staged "injects" that test how you react mid-run, and
an after-action review — adapted from the public-domain structure CISA uses
for its Cyber Tabletop Exercise Packages (CTEP), applied here to a legal
workflow instead of an incident response.

> **Everything below is fictional.** The company, the counterparty, the deal,
> and every fact are invented for this walkthrough. Nothing here is legal
> advice, and the "output" shown is illustrative — not a real deliverable.

## Objectives

By the end of this walkthrough you should be able to:

1. Use `WORKFLOW_ROUTER.md` to find the right skill for a task.
2. Recognize a skill's Required Inputs gate and supply what you have.
3. Watch missing facts turn into visible `[CONFIRM: ...]` placeholders,
   instead of the AI guessing.
4. React correctly to two common mid-run "injects" — a cited case, and a
   date — before you have verified either one.
5. Run the after-action checklist that confirms the draft is safe to hand to
   a supervising attorney.

## Scenario

**Riverbend Consulting**, a fictional 40-person management-consulting firm,
just received a vendor NDA. A prospective data-analytics vendor,
**Meridian DataWorks**, wants Riverbend to sign a mutual NDA before sharing a
product demo that will touch some of Riverbend's client data. Priya, the
Riverbend operations lead, forwards you the NDA and asks: "Can you take a
first pass at this before I loop in outside counsel?"

You have never run an AgentCounsel skill before. Here is how the first run
goes.

### The fictional facts you have

- The counterparty is Meridian DataWorks, Inc.; Riverbend Consulting LLC is
  the other party.
- The NDA is labeled "mutual," but the document Meridian sent is Meridian's
  own standard form.
- Riverbend's role: the deal is a vendor evaluation, not M&A, employment, or
  investment — a stand-alone commercial NDA.
- The NDA defines "Confidential Information" broadly, with no carve-out for
  information already public or independently developed.
- The term is 5 years from disclosure, with a 3-year post-termination
  survival period for confidentiality obligations.
- There is a broad injunctive-relief clause allowing Meridian to seek an
  injunction without posting a bond.
- Governing law is stated as Meridian's home state, with exclusive venue
  there.
- Riverbend has no formal NDA playbook; this is their first vendor NDA this
  quarter.
- `[missing]` — the signature block is undated, so no one has confirmed the
  effective date of the agreement.
- `[missing]` — no one has confirmed whether the "mutual" obligations are
  actually symmetric, since only Meridian's standard-form language has been
  skimmed, not the full document.

The two `[missing]` items above are deliberate. They are exactly the kind of
gap a skill should surface as a placeholder rather than fill in — watch for
them in the output below.

## Step 1 — Route the task

Open `WORKFLOW_ROUTER.md` and search for "NDA." The router's worked-example
table maps "Review this NDA" to `skills/contracts/nda-review/SKILL.md`, and
flags the mandatory quality checks for it: `source-validation-check` for any
cited authority, `assumption-audit`, `legal-prose-polish`, and
`attorney-review-gate`. This is your skill for the task — not
`contract-risk-review` (that is for non-NDA commercial contracts) and not a
playbook (Riverbend does not review NDAs often enough yet to warrant one; see
`docs/PLAYBOOKS.md` if that changes).

## Step 2 — Gather Required Inputs

Open `skills/contracts/nda-review/SKILL.md` and read its **Required Inputs**
section. It asks for: the full NDA text, Riverbend's role (here, receiving —
Riverbend is the one being asked to review before signing, evaluating a
vendor relationship), the business context, and optionally a playbook.
Riverbend has no playbook, so the skill proceeds without one and says so.

Because the effective date and the symmetry of the "mutual" obligations are
unconfirmed, you do not guess. You tell the skill what you know and flag the
rest — this is the Required Inputs gate working as intended: it asks before
substantive work, not after.

## Step 3 — What a good output looks like

The skill's Output Format (see `skills/contracts/nda-review/SKILL.md`) walks
through a Triage Rating, a Red Flags Quick Scan, a Key Terms Table, a Scope
Check, a Risk Table (`skills/contracts/nda-review/templates/nda-risk-table.md`),
a Negotiability Table, Market Practice Notes, Prioritized Redline Points, a
Business-Friendly Summary, an Internal Consistency Check, Attorney
Verification Items, and Assumptions — in that order. There is no dedicated
NDA example file in `examples/`, but `examples/contract-review-example.md`
shows the same shape (risk table, prioritized issues, visible placeholders)
for a sibling contracts skill — read it to see the pattern before your first
real run.

For Riverbend's facts, a good draft output would flag, among other things:

- **Triage rating: YELLOW** — the injunctive-relief clause and the
  unconfirmed symmetry of "mutual" obligations are not dealbreakers, but they
  need negotiation attention before signature.
- **Effective date:** `[CONFIRM: effective date — signature block undated]`.
- **Mutuality:** `[CONFIRM: whether obligations are symmetric — only the
  counterparty's standard-form language has been reviewed, not confirmed
  against Riverbend's own disclosure obligations]`.
- **Governing law and venue:** flagged for attorney review, since it favors
  the counterparty's home state.

Notice that both deliberately missing facts from Step 2 came back as visible
placeholders, not as invented answers. That is the discipline this library
exists to enforce — see `core/output-format-rules.md`.

## Two injects

An "inject" is a tabletop-exercise term for an event dropped into the
scenario mid-run to test your response. Here are two you are likely to meet
on a real first run.

### Inject 1 — the draft cites a case

Suppose the draft output states, in the Attorney Verification Items section,
something like: "the injunctive-relief clause may be enforceable without a
bond requirement, citing *Smith v. Jones*." **What do you do?** Stop. No
skill in this library is permitted to invent a case citation (see "Never
invent authority" in `AGENTS.md`), and this fictional walkthrough does not
supply any such case. Treat any bare citation the model produced without a
source you provided as unverified. Route it through
`skills/legal-methodology/citation-integrity-check/SKILL.md` or
`skills/legal-methodology/source-validation/SKILL.md`, or simply strike it and
mark the point `[VERIFY: authority for this enforceability point]`. Never let
an unverified citation stay in the draft as though it were confirmed.

### Inject 2 — a date appears

Suppose the draft states "the term runs through March 2029." **What do you
do?** Treat every date as unverified unless it traces to the document or a
fact you supplied (see "Never compute a deadline" in `AGENTS.md`). Check it
against the actual NDA text — the 5-year term stated in the fictional facts
above, from whatever effective date is eventually confirmed — and if the
draft computed or assumed a date instead of quoting one, flag it
`[deadline verification required]` rather than accepting it at face value.

## After-action review

Before handing the draft to Priya or to outside counsel, check:

- [ ] Did every fact you did not supply (the effective date, the mutuality
      question) come back as a visible `[CONFIRM: ...]` placeholder, rather
      than a filled-in guess?
- [ ] Was any citation in the draft either traced to a real source you
      provided, or flagged `[VERIFY: ...]` — never presented as settled?
- [ ] Was any date treated as unverified unless it came from the document or
      your own input, with no deadline silently computed?
- [ ] Does the draft state Riverbend's role, the transaction context (a
      vendor evaluation, not M&A/employment/investment), and governing law —
      or flag them as unknown?
- [ ] Is the Attorney Verification Checklist at the end of
      `skills/contracts/nda-review/SKILL.md` attached to the deliverable,
      **unchecked**? The AI never checks these boxes — only the supervising
      attorney does, after review.
- [ ] Is the whole draft still labeled "draft legal work product for
      attorney review — not legal advice"?

If every box above is true, the draft is ready to go to the attorney who will
actually review it — not to Meridian, and not to signature.

## Where to go next

- `QUICKSTART.md` — the five-minute path for any platform.
- `docs/CHOOSE_YOUR_WORKFLOW.md` — when a task needs more than one skill (a
  matter workspace, a playbook, a review panel).
- `docs/QUALITY_LAYER.md` — the quality-check skills referenced in the injects
  above, and when each one is mandatory.
- `docs/ATTORNEY_REVIEW_GATE.md` — the final gate every deliverable passes
  through before anyone relies on it.
- `skills/contracts/nda-review/SKILL.md` — the skill this walkthrough ran, in
  full.
