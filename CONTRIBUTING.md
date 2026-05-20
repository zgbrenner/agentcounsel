# Contributing to AgentCounsel

Thank you for helping build AgentCounsel. The library is useful only if it stays consistent, safe, and easy for legal professionals to read. These rules keep it that way.

## Principles

AgentCounsel is **Markdown-first** and **safety-first**. Contributions are evaluated against the core rules in `core/` and the requirements below.

## What we accept

- New skills for legal workflows not yet covered.
- Improvements to existing skills and templates.
- Better templates, clearer wording, and structural fixes.
- Adapter improvements that keep adapters thin.

## Hard requirements for every skill

A skill will not be merged unless it meets all of these.

1. **Markdown-first.** A skill is a `SKILL.md` file plus optional Markdown templates and references. No scripts, no build steps, no runtime.
2. **Follows the standard structure.** `SKILL.md` uses the required frontmatter (`name`, `description`) and these sections, in order: Purpose, Use When, Required Inputs, Do Not Use When, Legal Safety Rules, Workflow, Output Format, Attorney Verification Checklist.
3. **Includes an Attorney Verification Checklist.** Every skill ends with a checklist of items a supervising attorney must confirm.
4. **Preserves confidentiality.** The skill follows `core/confidentiality-and-privilege.md`. Templates and examples use fictional placeholders only — never real client facts, names, or data.
5. **No fake citations.** No invented or unverifiable cases, statutes, regulations, citations, quotations, dates, or deadlines — anywhere, including examples. See `core/source-and-citation-discipline.md`.
6. **No jurisdiction-specific legal claims unless cited and scoped.** Skills supply workflow and structure, not the law. If a contribution states a legal rule, it must cite verifiable authority and clearly state the jurisdiction and date it applies to. Prefer to frame such points as attorney-verification items.
7. **No legal-advice language.** Do not tell users what they "must" do or what "is legal." Use the "draft legal work product for attorney review" framing throughout.
8. **No hidden tool behavior.** A skill must do exactly what it says. No instructions that cause an agent to take actions the user would not expect (sending data, calling tools, fetching URLs) beyond the stated workflow.
9. **No unnecessary scripts.** Do not add code, package managers, or build systems. If a contribution seems to need code, open an issue to discuss first.

## Style

- Clean, plain Markdown. Professional and clear; no hype.
- Never imply the library or an agent replaces a lawyer.
- Keep adapters thin — they point to `skills/`, they do not duplicate it.
- Match the depth and tone of existing skills (`skills/contracts/nda-review/SKILL.md` is a good reference).

## How to contribute

1. Open an issue using the appropriate template — **bug report**, **skill request**, or **skill improvement** — so scope and naming can be agreed. The templates live in `.github/ISSUE_TEMPLATE/`.
2. Create the skill folder under the right practice area in `skills/`, with `SKILL.md` and any `templates/`.
3. Add the skill to `SKILLS_INDEX.md` and, where relevant, `WORKFLOW_ROUTER.md`.
4. Re-read the `core/` rules and self-check against the hard requirements above.
5. If you changed a skill that is part of the Claude Code plugin bundle, run `python scripts/sync_plugin_skills.py`. See `PLUGIN_SYNC.md`.
6. Run `python scripts/validate_repo.py` and resolve any errors it reports. See `VALIDATION.md`.
7. Note any user-facing change under "Unreleased" in `CHANGELOG.md`.
8. Open a pull request and complete the checklist in the pull request template.

## Reviews

Maintainers review contributions for safety, structure, accuracy of framing, and consistency. Expect feedback focused on the safety rules — they are not negotiable. Security concerns are handled per `SECURITY.md`.

## License

By contributing, you agree that your contributions are licensed under the repository's Apache License 2.0.
