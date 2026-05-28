# Launch post

Draft copy for announcing the first public release (v0.2.0) on LinkedIn, GitHub,
or social. Tone: serious, open-source builder, not hypey, legally careful. Edit
to fit each channel. Every version makes clear AgentCounsel is **not an AI lawyer**
and that attorney review is required.

---

## Short version (social / X)

> Open-sourcing **AgentCounsel** — a Markdown-native library of legal *workflows*
> for AI agents and the lawyers who supervise them.
>
> It is not an AI lawyer and it does not give legal advice. It produces **draft
> work product for attorney review**: structured intake, review, and drafting
> workflows, with a built-in quality layer (source validation, citation integrity,
> hallucination red-team) and an attorney-review gate on every output.
>
> 186 skills · 20 practice areas · packs for ChatGPT, Claude, Gemini, Cursor &
> Codex · plain Markdown, no backend, no lock-in. Apache-2.0.
>
> [repo link]

---

## Long version (LinkedIn / GitHub Discussions / blog)

**Announcing AgentCounsel v0.2.0 — supervised legal workflows for AI agents.**

I've been building AgentCounsel as an open-source answer to a specific problem:
AI is now in every legal workflow, but most of it is ad-hoc prompting with no
structure, no source discipline, and no clear hand-off to a supervising attorney.

AgentCounsel is a **Markdown-native library of legal skills**. A skill is a
structured workflow — what to scope, what inputs to gather, how to organize the
output, and what an attorney must verify. The whole library is plain Markdown:
no backend, no database, no account, no vendor lock-in. It runs in ChatGPT,
Claude, Gemini, Cursor, Codex, or just a text editor.

What it is **not**, stated plainly: it is not an AI lawyer, it does not give legal
advice, and it does not replace a licensed attorney. Every output is **draft work
product for attorney review**. The design assumes a qualified lawyer reviews and
adopts the work before it is relied upon.

What's in this release:

- **186 skills across 20 practice areas** — contracts, litigation, privacy,
  employment, corporate, M&A, securities, tax, IP, regulatory, and more — each with
  the same eight-section structure and machine-readable metadata.
- **A quality layer.** Nine cross-cutting checks — source validation, citation
  integrity, assumption audit, hallucination red-team, privilege/confidentiality
  review, prose polish, format compliance, jurisdiction/deadline gates, and an
  attorney-review gate. These organize and surface issues for verification; they
  do **not** verify the law automatically.
- **Source and citation discipline by default.** Skills never invent authority or
  compute deadlines; gaps become visible placeholders for an attorney to resolve.
- **An eval system.** 186 eval files and 500+ cases, run by standard-library
  scripts with no API keys. They check structure, routing, and safety signals —
  not legal correctness.
- **Matter workspaces, playbooks, and review panels** for multi-step,
  document-heavy work — all Markdown, all attorney-supervised.
- **Portability across AI tools** via generated platform packs, plus a static
  catalog site and full onboarding docs.

It's Apache-2.0, pre-1.0, and honest about its maturity — see PROJECT_STATUS.md
for what's stable vs. experimental. Contributions, issues, and skeptical legal
eyes are all welcome.

If you build legal-AI tooling, supervise people who use it, or just want to see
what disciplined, reviewable AI legal workflows look like — take a look.

[repo link] · Apache-2.0 · feedback welcome

---

## Phrasing guardrails (for whoever adapts this)

- Always describe output as **draft work product for attorney review** — never as
  legal advice, a legal opinion, or a final answer.
- Never call it an AI lawyer or an autonomous legal agent.
- Don't claim it verifies citations or the law; say it provides a **structured
  source/citation workflow** with **manual verification required**.
- Call newer surfaces (matter workspaces, playbooks, review panels, connectors)
  **experimental** where relevant.
- AgentCounsel is independent and not affiliated with, endorsed by, or sponsored
  by any AI vendor — don't imply otherwise.
