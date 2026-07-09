# 0002. Every skill has exactly eight fixed H2 sections, in order

## Status

Accepted.

## Context

AgentCounsel is a library of legal workflows meant to be read and relied on
by supervising attorneys, not just executed by an agent. A skill that varies
its own shape from one practice area to the next — sometimes gating inputs
first, sometimes burying safety rules in the middle, sometimes omitting an
attorney checklist — forces every reader to re-learn where to look each time,
and makes it easy for a contributor to skip a safety-critical section without
anyone noticing in review. `CONTRIBUTING.md`'s hard requirements exist
because a skill will not be merged unless it is safe and consistent; a fixed
structure is what makes "safe and consistent" checkable rather than a matter
of individual judgment per skill.

## Decision

Every canonical skill is exactly one `SKILL.md` file with YAML frontmatter
and exactly eight H2 sections, always in this order: **Purpose, Use When,
Required Inputs, Do Not Use When, Legal Safety Rules, Workflow, Output
Format, Attorney Verification Checklist.** No skill adds, removes, reorders,
or renames these sections. `scripts/validate_repo.py` enforces both the
presence and the order of all eight sections on every canonical skill.

## Consequences

- A reader who knows the structure of one skill knows the structure of every
  skill — the Required Inputs gate, the Legal Safety Rules, and the Attorney
  Verification Checklist are always in the same place.
- CI fails a pull request that adds a skill with a missing, renamed, or
  reordered section, so structural drift cannot merge silently.
- The fixed structure imposes real limits: a skill genuinely needing a
  different shape (for example, a playbook that sequences several skills, or
  a review panel that runs multiple passes) is not forced into eight
  sections — those live in `playbooks/` and `review-panels/` instead, each
  with their own fixed structure suited to what they are.
- Improving the model itself (adding a ninth section, splitting one section
  in two) requires updating `_shared`'s required-sections list and every
  existing skill in the same change — a deliberately high bar, by design.

Source: `AGENTS.md`, `CONTRIBUTING.md`.
