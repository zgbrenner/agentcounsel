> Shared reference material supporting the AgentCounsel intellectual-property skills, used to help produce draft legal work product for attorney review — not legal advice.

# Intellectual Property Output Patterns

This file collects the **common rules every IP skill follows** in its Output Format — the cross-cutting discipline that should be true of a trademark clearance triage, an infringement triage, a cease-and-desist response triage, a patent FTO triage, an invention disclosure screen, a DMCA notice or counter-notice, and an open-source license review alike. Each skill's own `SKILL.md` remains the authoritative spec for what that skill produces; this file is a consistency reference, not a substitute.

The IP skills sit unusually close to determinations a layperson — or an under-supervised model — will mistake for legal conclusions ("is this name clear?", "is this infringing?", "can we operate?"). The discipline below exists to prevent that mistake.

---

## Universal rules

- **Every output is a draft.** Each deliverable opens with a clearly visible draft-for-attorney-review label.
- **Every output is not legal advice.** Output never tells a user a mark is clear, a name is available, a product does not infringe, an invention is novel, an open-source obligation is satisfied, or a takedown is warranted.
- **Every triage signal is named as a triage signal.** Output formats use words like "preliminary", "first-pass", "triage signal", "indication", and "for attorney determination". They do not use words like "result", "conclusion", "verdict", "approved", "cleared", or "infringing" as standalone judgments.
- **No deadline is computed.** Statute-of-limitations dates, DMCA counter-notice windows, opposition periods, response deadlines on received letters, and patent-prosecution deadlines are recorded as the source states them and tagged `[deadline verification required]`.
- **Every cited authority is provided or flagged.** Patent numbers, trademark registrations, copyright registrations, DMCA notices, license texts, and contract terms appear only when the user has supplied them or are otherwise marked `[Attorney to insert authority]`.

## Sourcing and search-coverage rules

Many IP outputs reflect a search of some kind — a trademark database, a patent search, a code-component inventory, a prior-art summary. Outputs follow three rules.

- **Search scope is named explicitly.** What was searched, where, when, and over what categories — and what was **not** searched. The skill never implies completeness it did not perform.
- **Hits are recorded as hits, not as conclusions.** A returned mark, patent, or component is recorded with its identifier, owner, status, and source. The skill does not conclude that the hit is or is not blocking.
- **Negative results are bounded.** "Not found in the provided record" is not the same as "does not exist." Outputs distinguish the two.

## What the outputs never do

- They never tell a user that a mark is clear, available, registrable, or non-infringing.
- They never tell a user a product is free to operate, that a feature does not infringe a patent, or that prior art anticipates a claim.
- They never tell a user that an open-source obligation is or is not triggered, or that a license is or is not compatible.
- They never draft a final cease-and-desist response, a final DMCA notice or counter-notice, a final FTO opinion, or a final clearance opinion. Every deliverable goes through the Attorney Verification Checklist before it is sent, filed, recorded, or relied upon.

All output is draft work product for attorney review.
