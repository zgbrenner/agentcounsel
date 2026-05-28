# Benchmarks

AgentCounsel benchmarks are fictional, cross-practice eval cases designed to
exercise legal-safety behavior across skills and quality checks.

The benchmark suite in `evals/benchmarks/agentcounsel-benchmark.eval.yaml`
borrows only general evaluation ideas from public open-source projects:
structured cases, rubrics, static integrity checks, and coverage reporting.
No third-party benchmark tasks, prompts, examples, or prose are copied.

## Coverage Goals

Benchmark cases should cover:

- missing jurisdiction
- missing deadline or effective date
- unsupported legal citation
- client-role ambiguity
- privilege or confidentiality risk
- professional-responsibility concern
- source-document mismatch
- overconfident legal conclusion
- invented authority risk
- output format failure
- unsupported factual claim
- failure to route to attorney review gate

## Status Labels

`manual-ready` means the case is ready for a reviewer or future model-output
scoring. It does not mean the case passed.

`automated-static` means the case is implemented as deterministic repository
validation, such as metadata, pack, or router reference checks.

`scored` is reserved for cases with actual candidate outputs or recorded
manual scores.

## Borrowing Rules

Use fictional facts unless a public benchmark license clearly permits reuse
and the project owner chooses to attribute and import that material. GPL or
AGPL benchmark content must not be copied into AgentCounsel under the current
license strategy.
