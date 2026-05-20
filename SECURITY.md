# Security Policy

AgentCounsel is a library of Markdown files. It ships no executable code, no build system, and no runtime. Even so, it is used inside legal workflows that handle confidential and privileged information, and inside AI agents that can read documents and act on instructions. This policy covers both.

## Reporting a vulnerability or concern

If you find a security issue — in the repository, in a skill that could cause unsafe behavior, or in the project's processes — report it responsibly:

- Open a **private** security advisory through the repository's GitHub "Security" tab, or
- Contact the maintainers through the channel listed in the repository.

Please do not open a public issue for an unfixed vulnerability. Include enough detail to reproduce or understand the concern. We aim to acknowledge reports promptly and to coordinate a fix and disclosure.

Do not include confidential client information, privileged material, or real personal data in a report. Use redacted or fictional examples.

## Using AgentCounsel safely in legal workflows

These are the practices that matter most when AI agents handle legal work.

### Protect confidential and privileged material

- **Do not upload privileged or confidential materials to systems that have not been approved** for the matter and the client. "Approved" means cleared under your organization's policies and any applicable client agreement.
- Confirm where an AI tool stores, logs, and processes inputs before placing client material into it.
- Keep matters separated. Do not let one client's information enter another client's workflow.

### Treat skills and documents as untrusted input

- **Beware prompt injection.** Documents under review — contracts, emails, filings, web content — may contain text crafted to manipulate an AI agent ("ignore your instructions," "send this elsewhere," "approve this"). Treat the content of any reviewed document as data, not as instructions.
- **Treat third-party skill files as potentially untrusted.** A `SKILL.md` from outside this repository is just text an agent will follow. Review it before use, the way you would review any instruction given to staff.
- **Do not install unreviewed third-party skills** into a legal workflow. Vet the source and read the file first.

### Do not run untrusted code

- AgentCounsel skills are workflow instructions, not programs. A legitimate AgentCounsel skill will not ask you to run scripts.
- **Do not run scripts, install packages, or execute commands that arrive bundled with a skill package** from an unknown source. Treat any such request as a red flag.

### Review every output before use

- All AgentCounsel output is **draft work product**. Review it before it is relied upon, filed, or sent.
- Verify every citation, quotation, date, and factual claim. See `core/source-and-citation-discipline.md`.
- Never let unreviewed AI output go out under a lawyer's name.

## Scope

This policy covers the AgentCounsel repository and its content. It does not cover third-party AI platforms, agents, or tools you use AgentCounsel with — review the security posture of those separately.
