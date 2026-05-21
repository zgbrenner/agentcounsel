> Shared reference material supporting the AgentCounsel contracts skills, used to help produce draft legal work product for attorney review — not legal advice.

# Redline Output Guidance

This guidance covers how to express suggested contract changes in a review deliverable. It applies to the issue lists and redline points produced by `skills/contracts/contract-risk-review/SKILL.md` and `skills/contracts/nda-review/SKILL.md`, and to any other context where a contracts skill proposes changes to contract language.

The core principle: describe the **direction** of a change, not final drafted clause language. Substantive drafting of new or replacement clause language is an attorney task. A reviewer who drafts specific new clause language is stepping outside the scope of draft legal work product and into legal practice.

---

## 1. Direction, Not Drafting

### What "direction" means

Expressing the direction of a change means describing, in plain language, what the client wants the revised provision to accomplish — what risk it should address, how the allocation should shift, what protection should be added, or what should be removed — without writing the specific words of the revised clause.

Direction is prescriptive about the goal; it is not prescriptive about the exact language. The attorney reads the direction and makes the drafting judgment.

### Direction examples

The following pairs show how to express direction rather than draft language:

**Do not write:**
> "Delete the phrase 'including indirect, incidental, consequential, special, or punitive damages' and replace with 'except for claims arising from a data breach or breach of confidentiality obligations.'"

**Write instead:**
> "Add a carve-out from the consequential-damages waiver for data breach and confidentiality breach claims. The current waiver applies to both parties equally but leaves the client without recovery for its most likely loss type."

---

**Do not write:**
> "Section 8.2 shall be amended to read: 'Vendor shall provide Client with written notice of any Security Incident no later than forty-eight (48) hours after Vendor becomes aware of such Security Incident.'"

**Write instead:**
> "Shorten the breach notification period and tie the trigger to awareness rather than confirmation. The current provision allows notification at a timeline that may be inconsistent with the client's regulatory obligations. `[ATTORNEY TO CONFIRM: applicable notification period requirement under governing law]`"

---

**Do not write:**
> "The definition of 'Confidential Information' shall be amended by inserting the following sentence: 'Confidential Information shall not include information that: (a) is or becomes publicly known through no wrongful act of the receiving party...'"

**Write instead:**
> "Add the standard exclusions to the definition of Confidential Information. The current definition has no exclusions for publicly available information, independently developed information, or information received from third parties without restriction. These are standard receiving-party protections."

---

### Why this rule exists

Writing final clause language in a review deliverable creates several risks:

- The reviewer cannot account for all interaction effects — how new language might affect other provisions, defined terms, or the overall structure of the agreement.
- Final language drafted by an agent without a law license, presented in a deliverable, blurs the line between draft work product and legal advice.
- The attorney needs to exercise independent judgment on the final language. Pre-drafted replacement language can inappropriately anchor that judgment or be lifted and used without adequate review.

When a user or attorney specifically asks for a draft of alternative language, that request should be flagged for the supervising attorney to handle directly, or the attorney should confirm that the deliverable's directional guidance is sufficient for them to draft.

---

## 2. The Preferred Position / Fallback Position Pattern

For every issue raised, express the client's goals in two tiers:

### Preferred Position

The outcome the client would ideally achieve if the counterparty accepts the requested change. This is the opening position — what the client asks for.

Record it as the change direction that fully addresses the identified risk or imbalance. It should be specific enough for the attorney to understand what the client wants, without prescribing exact language.

### Fallback Position

The minimum the client should accept if the counterparty resists the Preferred Position. The Fallback Position represents a partial improvement — it does not fully resolve the issue but meaningfully reduces the risk compared to the current draft.

A Fallback Position acknowledges that the client may not get everything it wants. It gives the attorney a bottom line to work from. Without a Fallback Position, the attorney has no guidance on when to stop pushing.

**Fallback positions require attorney confirmation.** Whether a Fallback Position is actually acceptable depends on the client's risk tolerance, leverage, and priorities — all of which are attorney judgment.

For commonly negotiated clauses, `skills/contracts/references/fallback-language-bank.md` provides sample preferred and fallback positions, organized by clause type, that a reviewer can draw on to articulate the direction of a change. The illustrative drafting skeletons in that bank are a drafting aid for the supervising attorney — they are not final clause language and must not be pasted into a deliverable as finished text.

### Format

Present the Preferred and Fallback positions together, in this pattern:

```
Issue: [brief description of the problem]
Why it matters: [one or two sentences on the risk or imbalance]
Priority: [High / Medium / Low]

Preferred Position:
[Direction of the ideal change — what the client wants the provision to accomplish]

Fallback Position:
[Direction of the minimum acceptable improvement — what partially addresses the risk]

Notes and Verification Items:
[CONFIRM: ...] or [ATTORNEY TO CONFIRM: ...] or [verify jurisdiction], as applicable
```

### Example

```
Issue: Consequential-damages waiver leaves client exposed for its primary loss type
Why it matters: The current mutual waiver excludes all indirect and consequential damages, but
the client's most likely harm from a vendor breach (lost data, business interruption) is
categorically consequential. The vendor's primary risk (unpaid fees) is direct and is not
affected by the waiver.
Priority: High

Preferred Position:
Add mutual carve-outs from the consequential-damages waiver for: data breach or data loss;
breach of confidentiality obligations; and willful misconduct or fraud. This would restore
the client's ability to recover for its most likely loss scenarios while maintaining the
general waiver structure.

Fallback Position:
Add a unilateral carve-out for the client only, covering data breach and confidentiality
breach. If the vendor will not accept a mutual carve-out, securing the carve-out for the
client's most likely exposures is a meaningful improvement.

Notes and Verification Items:
[ATTORNEY TO CONFIRM: whether the Fallback Position (unilateral carve-out only) is
acceptable given the client's risk tolerance and the deal value]
[ATTORNEY TO CONFIRM: enforceability of consequential-damages waivers for this claim
type under the governing law — verify jurisdiction]
```

---

## 3. Priority Ratings

Each issue is rated High, Medium, or Low. These ratings guide which issues to spend negotiating capital on and in what order.

### High

Material risk to the client that should be addressed before execution. A High-priority issue, if unresolved, creates meaningful financial exposure, operational disruption, loss of key rights, or regulatory risk that the client should not accept without a conscious decision. The attorney should address every High-priority issue in negotiation or make an informed decision to accept it.

### Medium

Meaningful issue that warrants attention but is manageable. A Medium-priority issue, if unresolved, creates imbalance or suboptimal risk allocation but is unlikely to be a deal-breaker on its own. It should be raised in negotiation, and the attorney should understand the implications of not resolving it.

### Low

Minor imbalance or suboptimal language. A Low-priority issue may not be worth spending negotiating capital on in most deals, but it is worth flagging so the attorney is aware of it. In high-value or high-stakes deals, the attorney may decide to raise Low-priority items as well.

### How priority and negotiability interact

Priority (from this section) and negotiability (from `skills/contracts/references/negotiability-ratings.md`) answer different questions. Priority measures how much an issue matters — the size of the risk. The negotiability rating — Must Push, Strong Push, Business Call, Acceptable if Balanced, Low Priority, or Do Not Spend Leverage — recommends how the lawyer should handle it. A High-priority issue rated Must Push signals that movement is required, not merely desirable; a High-priority issue rated Strong Push signals that the effort is worth spending and movement is realistic. Record both ratings for each material issue.

Priority ratings are draft assessments for attorney confirmation. The attorney adjusts priorities based on the client's actual risk tolerance, leverage, and strategic objectives.

---

## 4. When to Stop and Route to the Attorney

There are specific circumstances where the correct output is not a redline direction or a Preferred/Fallback Position, but a clear routing instruction: this issue must go to the attorney before proceeding.

### Stop and route when:

**The issue requires legal judgment about enforceability.** If the question is whether a clause is enforceable under the governing law, the answer depends on jurisdiction-specific doctrine that the reviewer cannot supply. Stop, flag the issue, and add a verification item: `[ATTORNEY TO CONFIRM: enforceability of [clause] under governing law — verify jurisdiction]`.

**The issue requires legal judgment about regulatory compliance.** If the clause intersects with data privacy requirements, sector-specific regulation, or mandatory contract terms, the compliance assessment belongs to the attorney. Flag the issue and note that a compliance analysis is outside the scope of this skill.

**The issue requires drafting a new provision.** If the identified risk is best addressed by adding a provision that does not exist in the contract — not revising an existing one — the substantive drafting of that new provision is an attorney task. The reviewer identifies what the provision should accomplish; the attorney drafts it.

**The issue is a Walk-Away item.** If a term hits a Walk-Away threshold (see `skills/contracts/references/negotiability-ratings.md`), the output is an escalation notice, not a redline direction. The attorney must review the issue before the client takes any further action.

**The counterparty's position is unknown and the risk assessment depends on it.** If the reviewer cannot assess whether a clause is a deal risk without knowing more about the counterparty's posture, note the gap and flag for attorney input: `[CONFIRM: counterparty's prior negotiating positions on this term, if available]`.

**The issue arises in a specialized context** (M&A, employment, regulatory, financial services, IP licensing) where specialist counsel should be involved. Route clearly: this issue is outside the scope of a commercial contract review and should be referred to [type of specialist counsel].

### Format for a routing instruction

```
[ROUTE TO ATTORNEY: [brief description of the issue]]
[Reason for routing: enforceability question / compliance assessment / new provision needed /
Walk-Away threshold / specialist context]
[ATTORNEY TO CONFIRM: ...]
```

Routing instructions should appear in the Open Items section of the deliverable and in the Attorney Verification Checklist. They should not be buried in the body of the issue list.

---

## 5. Format Summary

A complete redline point in an issue list has the following components. All are required for High and Medium priority items; Low priority items may omit the Fallback Position if the issue is straightforward.

| Component | Description |
|---|---|
| Issue label | Short name identifying the clause or risk |
| Section reference | Contract section number, as written |
| Current posture | What the contract currently says, in plain language (do not quote at length here; full quotes belong in the risk matrix) |
| Why it matters | One or two sentences on the risk or imbalance |
| Priority | High / Medium / Low |
| Negotiability | Must Push / Strong Push / Business Call / Acceptable if Balanced / Low Priority / Do Not Spend Leverage (from `skills/contracts/references/negotiability-ratings.md`) |
| Preferred Position | Direction of the ideal change |
| Fallback Position | Direction of the minimum acceptable improvement |
| Notes and Verification Items | All `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and routing instructions |

---

## 6. General Style Rules for Redline Points

- Write in plain, direct language. A person reading the issue list should understand the issue and the suggested direction without re-reading the contract.
- Do not use legal jargon unless it is the clearest way to express the point. If you use a term of art, define it or use the contract's own defined term.
- Be specific about what you want changed, even without drafting the language. "Improve the liability cap" is not a direction. "Increase the liability cap to a multiple of annual contract value rather than fees paid in the prior month, and add a minimum floor" is a direction.
- Separate every distinct issue into its own redline point. Do not bundle multiple issues into one entry; they may need to be negotiated independently.
- Distinguish between issues that arise from what the contract says and issues that arise from what the contract is silent on. Both matter, but the attorney addresses them differently.
