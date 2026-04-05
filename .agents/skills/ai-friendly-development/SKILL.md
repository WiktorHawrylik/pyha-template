---
name: ai-friendly-development
description: Build or refactor Python repositories so they are easy for humans and AI agents to extend safely, especially for data pipelines, ML systems, inference services, evaluations, and agentic workflows. Use when implementing or reviewing Python code that touches datasets, model calls, prompts, schemas, experiments, migrations, telemetry, or reproducibility.
---

# AI-Friendly Development

## Overview

Use this skill to produce Python code that is easy to understand, safe to
change, and observable in production.

Favor explicit contracts, small composable modules, reproducible behavior, and
validation that goes beyond unit tests.

## Non-goals

- Pure frontend work
- Throwaway exploration that will not be promoted into repository code
- Large architecture rewrites unless the user explicitly asks for them

## Source Signals

The most useful patterns for this skill are:

- Runtime schemas at system boundaries
- Small, explicit migrations for persisted state changes
- Feature-gated experiments and fallback paths
- Structured latency, usage, and cost telemetry
- Comments that capture operational rationale rather than restating code

Read `references/portable-engineering-patterns.md` when you need the pattern
catalog behind this workflow.

Read `references/ai-friendly-development-workflow.md` when you need the full
delivery checklist and completion template.

## Five-Pass Cycle

Always run this five-pass review loop before calling the work done:

1. Contracts: define the goal, inputs, outputs, invariants, and schema or
   version boundaries.
2. Data and state: model datasets, artifacts, configs, migrations, backfills,
   and reproducibility constraints.
3. Runtime: add structured logging, metrics, and explicit fallback behavior.
4. Validation: add representative tests, eval fixtures, and critical-path
   integration checks.
5. Operations: document how to run, inspect, rerun, and roll back the change,
   then summarize residual risks.

If the request is large, complete the implementation in slices and re-run the
five-pass cycle for each slice.

## Required Practices

- Type every public function and every boundary object.
- Use explicit contracts with `pydantic`, `dataclasses`, `TypedDict`, or
  protocols where appropriate.
- Add concise docstrings for public interfaces when behavior, inputs, or
  failure modes are not obvious from the signature alone.
- Keep pure transformation logic separate from orchestration and I/O.
- Prefer versioned config, schema, dataset, model, and prompt identifiers over
  implicit behavior.
- Make retries, fallbacks, and feature-gated experiments explicit.
- Put operational context in structured logs and metrics, not only in prose.
- Write comments only for rationale, non-obvious invariants, or failure-driven
  guardrails.
- Raise specific exceptions with actionable messages.
- Promote reusable logic out of notebooks and scripts into `src/`.

## Comment Discipline

Default to writing no comments.

Add a comment only when it preserves information that is hard to recover from
the code itself, such as:

- A hidden constraint or invariant
- A security or safety guardrail
- A surprising retry, fallback, or recovery path
- A measured hot-path tradeoff
- The reason a lint, type, or tooling suppression is safe

Delete or avoid comments that:

- Narrate what the code already says clearly
- Mention the current task, ticket, caller, or review request
- Describe deleted code or temporary cleanup history
- Repeat names, types, or tests without adding new information

For multi-line comments, prefer this shape:

1. Name the failure mode or surprising behavior
2. State the invariant that must be preserved
3. Explain why the obvious alternative is unsafe or wrong
4. If relevant, note the safe-direction bias or operational consequence

For suppressions such as `# noqa`, `# type: ignore`, sync I/O exceptions, or
framework escape hatches, add the narrowest possible inline justification.

Preserve existing comments unless the code changed enough to make them wrong or
irrelevant. If a comment may encode past incident knowledge, update it rather
than deleting it by default.

## Repository Notes

In this repository:

- Keep AGPL-sensitive changes compatible with the existing compliance workflow.
- When adding source files or dependencies, pair the work with the
  `license-audit` skill.
- When behavior or workflows change, keep docs and tests in step with the code.

## Data and ML Expectations

- Record dataset or source identifiers, schema versions, model or prompt
  versions, and config hashes when they affect behavior.
- Make pipeline steps idempotent where practical and safe to rerun.
- Treat migrations and backfills as first-class code with telemetry and
  rollback thinking.
- Prefer deterministic seeds and stable fixture data for evaluations.
- Keep offline evaluation, smoke tests, and runtime monitoring aligned to the
  same contracts.
- Avoid mocks for critical data boundaries when a cheap real integration check
  is feasible.

## Validation

Run the smallest relevant command set that proves behavior.

For Python repositories, this usually starts with:

```bash
make format
make lint
make test
```

For data, ML, or agentic changes, also run the most relevant targeted checks,
such as:

- Schema validation commands
- Fixture-based inference or evaluation tests
- Pipeline smoke runs
- Migration or backfill dry-runs
- Focused integration tests against real boundaries

## Output

Always report:

- Which pass of the five-pass cycle drove the key changes
- Which contracts or invariants were added or changed
- Which telemetry, evals, or tests were added
- Whether any comments, suppressions, or rationale blocks were added and why
- Which risks remain around reproducibility, rollout, or operations
