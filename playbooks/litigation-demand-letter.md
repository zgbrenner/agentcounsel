# Playbook: Litigation Demand Letter

> This playbook is process guidance, not legal advice and not legal work
> product. It standardizes how a recurring demand-letter drafting task is run;
> the skill it references produces a **draft for attorney review.** The claim
> theory, the legal basis, and the decision to send are supplied and made by
> counsel — the playbook drafts, it does not assert that a claim is meritorious
> or that a demand will succeed. Use fictional examples (e.g., "Contoso,"
> "Client A") only.

## When to Use

Counsel has identified a claim theory and wants a structured draft demand letter
prepared — setting out the parties, the facts, the asserted basis (as supplied
by counsel), the relief sought, and a response window — for attorney review and
sending.

Use this playbook only when the claim theory and legal basis come from counsel.
Do not use it to choose a cause of action, assess the merits, or decide whether
to send. Route an active filing or a regulatory complaint elsewhere.

## Required Inputs

| Input | Notes |
|---|---|
| Claim theory and legal basis | Supplied by counsel — the playbook does not select it. |
| Jurisdiction and forum | `[verify jurisdiction]`; governs tone and references. |
| Parties | Sender, recipient, and any represented status. |
| Facts | The factual narrative, each fact attributable to a source. |
| Relief sought | Damages, cure, cease-and-desist, or other remedy. |
| Settlement authority | The range and conditions counsel will authorize. |
| Response window | Treated as user-supplied; never computed. |

If the claim theory or the facts are not provided by counsel, stop and request
them. Do not reconstruct a legal basis from memory.

## Default Client-Position Questions

- What claim theory and legal basis has counsel supplied (the playbook drafts to
  it; it does not choose it)?
- What is the client's objective — payment, performance, cessation of conduct,
  or preservation of a relationship?
- What relief and what dollar figure should the letter demand?
- What settlement authority and conditions has counsel approved?
- What tone is appropriate — firm-but-open, or final-before-suit?
- Is the recipient represented by counsel (affecting how and to whom it is
  sent)?
- What response window does counsel want stated (as supplied, not computed)?

## Risk Tolerance Settings

| Setting | Conservative | Balanced | Aggressive |
|---|---|---|---|
| Tone | Open to resolution | Firm, reserves rights | Litigation imminent |
| Specificity of legal basis | General, reserves theories | States supplied basis | Detailed, with named demands |
| Settlement signal | Invites discussion | States position | Take-it-or-leave-it |
| Deadline framing | Reasonable, flagged | Stated as supplied | Short, flagged for confirmation |

Record the selected column. Any escalation of tone or demand is an explicit,
recorded attorney decision.

## Required Source Materials

- Counsel's statement of the claim theory and legal basis.
- The factual record — contracts, correspondence, invoices, or other documents
  supporting each asserted fact.
- Any prior demand or correspondence with the recipient.
- Shared references in `skills/litigation/references/`.
- No case, statute, or rule text is supplied by the library; any authority is
  either counsel-supplied or a placeholder for attorney verification.

## Recommended Primary Skills

| Skill | Role in the playbook |
|---|---|
| `skills/litigation/demand-letter/SKILL.md` | Core demand-letter drafting. |
| `skills/litigation/matter-intake/SKILL.md` | When parties, facts, and posture need structured intake first. |
| `skills/litigation/litigation-chronology/SKILL.md` | To build the factual timeline the letter relies on. |
| `skills/litigation/claim-chart/SKILL.md` | When mapping facts to elements of the supplied claim. |

Open a workspace from `matter-workspaces/_template/` to hold the chronology,
the source map, and successive drafts.

## Required Quality Checks

- `skills/legal-methodology/source-validation/` — every asserted fact traces to
  a provided document.
- `skills/legal-methodology/citation-integrity-check/` — any authority is
  counsel-supplied or a flagged placeholder; none is invented.
- `skills/legal-methodology/hallucination-red-team/` — challenge any fabricated
  fact, figure, or citation.
- `skills/legal-methodology/legal-prose-polish/` — tighten tone and clarity
  without overstating the claim.
- `skills/legal-methodology/attorney-review-gate/` — checklist ships unchecked.

## Attorney Escalation Triggers

- A demand figure or settlement position outside counsel's stated authority.
- A claim theory the facts in the record do not support.
- A recipient already represented by counsel, or a regulator.
- A response window or limitations concern that requires date verification.
- Any privileged or confidential fact that should not appear in an external
  letter.

## Expected Outputs

- A draft demand letter with parties, factual narrative, the counsel-supplied
  basis, relief sought, and a stated response window (flagged as unverified).
- A source map tying each factual assertion to a document.
- A list of points where counsel must confirm the legal basis or authority.
- An attorney-verification item list and an explicit assumptions list.

## Source and Citation Expectations

Every fact in the letter traces to a provided document; nothing is asserted from
memory. No case, statute, or rule is cited unless counsel supplied it — otherwise
a placeholder (`[Attorney to insert authority]`) stands in. Dates and response
windows are stated as supplied and flagged `[deadline verification required]`;
the playbook never computes a limitations period or a deadline.

## Common Failure Modes

- Inventing a cause of action, a statute, or a damages figure not supplied by
  counsel.
- Overstating the strength of the claim to match the client's hope.
- Computing a response or limitations deadline rather than flagging it.
- Asserting facts not supported by the record.
- Sending tone or demands beyond counsel's authority.
- Including privileged material in a letter destined for the opposing party.

## Final Attorney-Review Gate

This playbook produces a **draft for attorney review only.** No demand letter is
sent, and no settlement position is communicated, until a qualified, licensed
attorney reviews the draft, confirms the claim theory and every authority,
resolves every placeholder and assumption, verifies the response window, and
signs off. The attorney decides whether and what to send; the playbook only
prepares the draft.
