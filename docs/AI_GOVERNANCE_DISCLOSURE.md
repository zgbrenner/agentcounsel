# AI Governance Disclosure

A firm's risk, compliance, or information-security function is often asked to
assess a new AI-related tool against the firm's governance program before
adoption. This document is written for that reader. It maps AgentCounsel's
own mechanisms to the questions such a review typically asks, so the firm can
place AgentCounsel correctly within an assessment it is already running for
its AI tooling — rather than treating AgentCounsel as a separate system that
needs its own certification.

**This document does not certify or claim compliance with any framework.**
It is a mapping to help a firm's own risk and compliance function reach its
own conclusion. Every row below states plainly what remains the firm's
responsibility.

## 1. What AgentCounsel is — and is not

**AgentCounsel is a Markdown-native library of legal skills.** A skill is a
structured instruction file (`SKILL.md`) that tells an AI agent, or a person,
how to approach a legal drafting task: what inputs to gather, what steps to
follow, and how to format the output. See `AGENTS.md` and `docs/SAFETY_MODEL.md`
for the full operating model.

**AgentCounsel is not:**

- **A runtime.** There is no server, service, or process that executes.
  `scripts/` contains Python standard-library helpers that validate the
  repository's own structure (see §4) — they do not run when a skill is used.
- **A model.** AgentCounsel supplies no language model, no inference, and no
  scoring. Whatever AI tool the firm points at this library — Claude, ChatGPT,
  Gemini, a repo-based coding agent, or another assistant — supplies the model.
- **A data processor or data collector.** The library holds no client data,
  logs no inputs, retains no session content, and has no storage layer. It
  cannot process, transmit, or leak a matter fact, because it never receives
  one — only the AI tool a firm chooses to run it in does.
- **A vendor with its own security posture.** There is no account, no
  authentication, no hosting, and no service-level agreement. AgentCounsel is
  files a firm downloads, clones, or copies into its own environment.

**The consequence for a governance review:** most of the questions a firm
would normally ask about an "AI tool" — where is data stored, what is logged,
what is the model's training data, what is the incident-response process,
what is the uptime SLA — are questions about **the AI tool the firm runs
AgentCounsel inside of**, not about AgentCounsel itself. This document says,
mechanism by mechanism, which questions belong to AgentCounsel's own content
and which belong to that other surface.

## 2. Controls mapping

The table below lists each AgentCounsel mechanism, the governance question it
is designed to answer, how it maps to the NIST AI Risk Management Framework's
four functions (Govern, Map, Measure, Manage), what — carefully stated — its
relevance to the EU AI Act is, a typical vendor-diligence-style question it
speaks to, and what remains the firm's own responsibility regardless.

| Mechanism (file) | Governance question it answers | NIST AI RMF function | EU AI Act relevance | Typical vendor-diligence question | Remains the firm's responsibility |
|---|---|---|---|---|---|
| Required Inputs gate (every `SKILL.md`'s "Required Inputs" and "Do Not Use When" sections) | How does the workflow prevent acting on incomplete or out-of-scope information? | Map (context and scope established before use) | Not an AI-system control — this is a content instruction inside a Markdown file, not a technical safeguard built into an AI system. Any input-validation obligation attaches to the AI tool that reads the file, not to the file itself. | Does the process validate required inputs before producing output? | Confirming the operator actually supplies the listed inputs, and does not let the agent proceed on a guess. |
| Jurisdiction and deadline gates (`core/jurisdiction-and-deadline-gates.md`) | How are jurisdiction-specific and time-sensitive determinations handled? | Map, Manage | Not an AI-system control. Relevant only insofar as an AI tool used for regulated legal determinations may itself carry deployer obligations — those obligations run to the tool, not to this instruction file. | Does the system flag jurisdiction- and deadline-sensitive output rather than resolving it automatically? | Supplying the actual jurisdiction and governing law, and independently computing and verifying every deadline. AgentCounsel never computes one. |
| Never-invent-authority rule (`core/source-and-citation-discipline.md`) | What controls exist against fabricated citations, quotations, or legal propositions? | Measure (testing for factual accuracy and failure modes), Manage | Not an AI-system control. Output accuracy and robustness obligations attach to the AI system generating the text, not to the instruction telling it what to do. | How does the vendor test for and mitigate hallucinated or fabricated output? | Independently verifying every citation, quotation, and legal proposition before relying on it. A Markdown instruction cannot verify anything on its own. |
| Placeholder discipline (`core/source-and-citation-discipline.md`, `core/output-format-rules.md`) | How are unknowns and gaps made traceable rather than silently resolved? | Map, Measure | Not an AI-system control. It is a content convention for marking uncertainty visibly. | Are unresolved data gaps flagged rather than filled by inference? | Resolving every `[CONFIRM: ...]`, `[VERIFY: ...]`, and `[ATTORNEY TO CONFIRM: ...]` placeholder before the draft is relied upon. |
| Layer-labeled outputs (`core/output-format-rules.md`) | Can a reviewer tell what a statement rests on — a source, an assumption, or an inference? | Govern, Map | Not an AI-system control. This is a documentation/formatting convention, not an explainability feature of a model. | Does the output separate factual claims from generated analysis? | Reading the layered output and confirming the labeling is accurate for the actual matter facts. |
| Attorney Verification Checklist (`core/attorney-review-checklist.md`) | Is there a mandatory human-in-the-loop step before output is relied upon? | Govern, Manage | Human oversight is a substantive obligation for higher-risk AI use under the EU AI Act, but that obligation attaches to how the firm's AI tool is deployed and governed — this checklist is a content-level prompt for that review, not the technical oversight mechanism itself. | Is there a required human review step before AI-assisted output is used downstream? | Actually performing the review, every time. The checklist ships unchecked; nothing in this library checks a box or substitutes for the reviewing attorney. |
| Capacity and vulnerable-party rule (`core/capacity-and-vulnerable-parties.md`) | Are there safeguards for output touching vulnerable individuals — capacity, safety, minors? | Govern, Manage (harm to individuals) | Relevant to fundamental-rights and prohibited-practice considerations that attach to how an AI system is used with vulnerable people — a deployer-level obligation, not something this instruction file discharges on its own. | Does the process prevent automated conclusions about protected or vulnerable individuals? | The substantive capacity, safety, or welfare judgment itself, and any mandatory reporting obligations the matter triggers. |
| Confidentiality and privilege rules (`core/confidentiality-and-privilege.md`) | How is confidential and privileged information handled? | Govern, Map | Distinct from the EU AI Act — this is a data-protection and professional-privilege question, not an AI-system risk-classification question. | How is client-confidential data protected in transit, at rest, and in processing? | Choosing an approved, vetted AI tool with its own confidentiality and data-handling controls. AgentCounsel holds no data and has no controls of its own to diligence here — the tool hosting it does. |
| Prompt-injection / documents-as-data rule (`core/legal-work-product.md`, rule 8) | How are adversarial instructions embedded in reviewed documents handled? | Map, Measure, Manage | Robustness and cybersecurity obligations for adversarial-input handling attach to the AI system processing the document, not to the instruction telling it to treat documents as data. | How are prompt-injection and data-exfiltration risks tested and mitigated? | Monitoring the agent's actual behavior in the firm's own tool and reviewing output for signs of manipulation, per `docs/SAFETY_MODEL.md` §5. |
| Validation CI (`scripts/validate_repo.py`, `.github/workflows/validate.yml`) | Is there change-management and quality control over the content itself? | Govern, Manage | Not an AI-system control — this is software-engineering process control over a Markdown content repository, run on every pull request. | Is there a defined change-management process for updates to the product? | Adopting the library through the firm's own change-management process — for example, pinning a reviewed release rather than always pulling the latest commit — since AgentCounsel's CI governs the library's own repository, not the firm's adoption of it. |
| Eval coverage (`evals/`, `reports/eval-coverage.md`) | What test evidence exists for a skill's structure, routing, and formatting? | Measure | Not an AI-system control. These are lightweight, no-API checks of the repository's own content — they do not measure a deployed AI system's outputs and are not a substitute for the AI system-level testing the EU AI Act contemplates for higher-risk systems. | What testing evidence supports the product's quality claims? | Understanding the limits of eval coverage — it evaluates structure and routing, not the legal correctness of any output a given model produces, and treating it as such in any internal testing record. |
| Practice-profile and matter-workspace configuration (`practice-profiles/`, `matter-workspaces/`) | How is the tool configured per team, and how is one matter's information kept separate from another's? | Govern, Map | Not an AI-system control. These are optional, plain-Markdown configuration and organization files a firm populates itself; they carry no data-processing function of their own. | Does the product support tenant or matter-level data segregation? | Populating and maintaining these files accurately, and enforcing separation between matters in whatever tool actually stores and processes the content — this library provides only the labeled structure, not the enforcement. |

## 3. Residual risk — what this library cannot control

This mapping reduces certain risks; it does not eliminate them. Plainly:

- **Model behavior.** AgentCounsel supplies no model. Whatever AI tool a firm
  uses can still misread a skill, blend a fact with an assumption, produce a
  fluent but wrong answer, or behave inconsistently across runs. The
  mechanisms above are designed to make such errors easier to catch — they
  cannot make a given model run error-free.
- **Confidentiality of the hosting tool.** AgentCounsel has no data
  controls of its own to audit, because it holds no client data. All actual
  confidentiality, access-control, logging, and retention questions belong to
  the AI tool the firm has approved for the matter. Diligence that tool
  directly; this document cannot substitute for that review.
- **A user or agent skipping a gate.** A `SKILL.md` file is text an agent
  follows voluntarily — there is no enforcement layer that stops an agent
  from ignoring the Required Inputs gate, guessing at a citation, or skipping
  the checklist. `scripts/validate_repo.py` checks that every skill *states*
  these gates; it cannot check that a given run of the skill *honored* them.
- **Coverage and currency.** The library covers a defined set of skills and
  practice areas; a gap in coverage is not itself a defect, but a firm should
  not assume the library addresses every workflow it needs. `jurisdictions`
  is empty by design in nearly every skill (see `docs/SKILL_METADATA_STANDARD.md`)
  — AgentCounsel deliberately supplies no jurisdiction-specific legal content,
  so no governance review of this library substitutes for the firm's own
  jurisdictional legal review.
- **Evals test structure, not legal correctness.** The checks in `evals/`
  and `reports/eval-coverage.md` confirm that a skill is structured,
  routed, and formatted correctly. They do not verify that a given
  model-generated output is legally correct for a given matter.

## 4. How to verify the claims in this document

Do not take this mapping on faith. Every claim above is checkable directly:

- Read the cited `core/` file for each control row — the actual rule text is
  short and is quoted or closely paraphrased above.
- Run `python scripts/validate_repo.py` (or the fuller `python
  scripts/check_all.py`) and read the output. These are the same checks
  `.github/workflows/validate.yml` runs on every pull request; they confirm
  that every skill in the repository actually declares the structure this
  document describes.
- Read `docs/SAFETY_MODEL.md` for the full threat model and the limits
  AgentCounsel operates under.
- Read `docs/SKILL_METADATA_STANDARD.md` to confirm the metadata fields
  (including `jurisdictions` and `requires_attorney_review`) referenced above.

If a firm's assessment needs a different framing, mapping, or level of
detail than this document provides, that is a gap to raise with the firm's
own AI governance function, not a gap this library can close on its own —
AgentCounsel is content for that function to evaluate, not a party to the
evaluation.
