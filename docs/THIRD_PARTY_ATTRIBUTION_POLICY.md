# Third-Party Attribution Policy

AgentCounsel is Apache-2.0 and Markdown-native. Open-source projects may
influence AgentCounsel, but external code, prose, examples, schemas, prompts,
and templates must not be copied or closely adapted unless the license allows
that reuse and the source is attributed.

## Recording OSS Influence

When an external project influences AgentCounsel, record the influence in the
smallest place that gives future maintainers context:

| Reuse type | Where to record it |
|---|---|
| General inspiration only | `docs/OSS_BORROWING_MAP.md` |
| Architecture or implementation pattern adapted without copying protectable expression | Relevant design doc or PR description |
| Code, prose, schema, prompt, template, eval case, or example copied or closely adapted | `NOTICE`, plus a source note in the affected file when useful |
| Third-party dependency added to tooling or a future app | Dependency manifest, `NOTICE` when required, and the implementation PR description |

## Copy, Adapt, Or Cite As Inspiration

Use these classifications before bringing any external material into the
repository:

| Classification | Meaning | Allowed action |
|---|---|---|
| Copy | Reuse the original text, code, schema, prompt, template, or data with only mechanical edits | Allowed only for license-compatible material with attribution and license preservation |
| Adapt | Rework the idea into AgentCounsel's own structure while remaining close enough that attribution is appropriate | Allowed only for license-compatible material with attribution |
| Cite as inspiration | Learn from the public idea, then independently design an AgentCounsel-native implementation | Allowed for any public project, including GPL/AGPL/no-license projects, without copying protected expression |
| Avoid | Do not use the project as a source for AgentCounsel work | Required where license, safety, provenance, or domain fit is unacceptable |

## License Compatibility Rules

AgentCounsel currently accepts direct reuse only from sources that are
compatible with Apache-2.0 distribution.

| Source license | Default treatment |
|---|---|
| Apache-2.0 | Compatible. Preserve notices and attribution. |
| MIT / BSD / ISC | Generally compatible. Preserve copyright and license notices. |
| CC0 | Compatible for public-domain-style content, but still record attribution when it materially influenced the project. |
| CC-BY | Usually compatible for documentation/content with attribution; review before mixing with code. |
| CC-BY-SA | Inspiration only unless the project adopts a share-alike-compatible strategy for the affected material. |
| GPL / LGPL | Inspiration only for AgentCounsel source unless counsel approves a project-specific strategy. |
| AGPL | Inspiration only. Do not copy code, prompts, templates, UI text, schemas, or examples into AgentCounsel. |
| Modified commercial/open-core license | Inspiration only unless the license is reviewed and approved for the exact reuse. |
| No license file or unclear license | Inspiration only. Public source is viewable, not reusable. |

## GPL And AGPL Prohibition

Do not copy or closely adapt GPL, LGPL, or AGPL code or content into
AgentCounsel unless the project license strategy changes and the maintainers
explicitly approve the reuse. This prohibition covers source code, prompts,
skill text, eval cases, workflows, examples, schemas, and UI copy.

GPL, LGPL, and AGPL projects may be studied for high-level concepts only. Any
implementation inspired by them must be independently written and recorded as
inspiration, not direct reuse.

## Required Attribution Format

When material is copied or closely adapted, add an entry to `NOTICE` in this
format:

```text
<Project name>
<Repository URL>
License: <SPDX identifier or license name>
Material used: <code/prose/schema/eval/template/etc.>
Affected AgentCounsel files: <repo-relative paths>
Use type: <copied/adapted>
Notes: <required notice text, modifications, or limitations>
```

Where the source license requires keeping a copyright notice, preserve that
notice with the attribution entry or in the copied file as appropriate.

## Current Documentation-Only PRs

If a PR only documents OSS influence and does not copy or directly adapt
external material, do not update `NOTICE`. State in the PR summary that no
third-party material was copied or directly adapted.
