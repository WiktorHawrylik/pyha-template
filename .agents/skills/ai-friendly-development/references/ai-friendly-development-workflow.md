# AI-Friendly Development Workflow

Use this runbook when the task needs more than the short skill summary.

## Objective

Deliver Python code that an AI agent can extend safely and that a human team can
operate with confidence in data-heavy, ML-heavy, or agentic systems.

The workflow is intentionally biased toward:

- Explicit contracts
- Reproducibility
- Observability
- Eval-driven validation
- Small, reviewable change sets

## Pass 1: Contracts

Start every task by making the contracts concrete.

Capture:

- The user-facing or system-facing outcome
- Inputs and outputs
- Failure modes
- Invariants
- Versioned boundaries such as schema, model, prompt, or artifact version

Preferred Python tools:

- `pydantic` for inbound or outbound payloads and settings
- `dataclasses` for internal domain objects
- `TypedDict` or protocols for light interface typing

Good outcomes from pass 1:

- A clear function or service boundary
- Parsed and validated inputs instead of unchecked dictionaries
- Fewer hidden assumptions inside business logic

## Pass 2: Data and State

Treat state transitions as part of the design, not cleanup work.

Check:

- Where data enters the system
- Which schema version is expected
- Whether the step is rerunnable
- Whether artifacts, checkpoints, or cached outputs need versioning
- Whether a migration or backfill is required

For pipelines and ML systems:

- Prefer immutable inputs and explicit output locations
- Store enough metadata to reproduce a result later
- Keep notebook exploration separate from production logic
- Extract reusable transformations into importable modules

## Pass 3: Runtime and Observability

If the code fails in production, the team should be able to answer what
happened without reverse engineering the source.

Add the most relevant signals:

- Structured logs with stable identifiers
- Metrics for throughput, latency, retries, failures, and fallbacks
- Cost or token accounting for LLM-backed flows
- Counters for skipped, filtered, or deduplicated records

Prefer logs and metrics that include:

- Dataset or source id
- Schema or model version
- Request or job id
- Retry or fallback cause

## Comment Pass

Do a deliberate comment pass after the code and tests are mostly settled.

Start by assuming every new comment should be deleted. Keep or add one only if
it captures load-bearing context that would otherwise be lost.

Use comments for:

- Hidden invariants
- Incident-driven guardrails
- Security-sensitive parsing or validation logic
- Retry, fallback, or recovery behavior that would surprise a reader
- Measured performance tradeoffs in hot paths
- Narrow justifications for lint or typing suppressions

Avoid comments that:

- Restate obvious control flow
- Narrate the diff or implementation task
- Mention unstable callers or temporary rollout context
- Explain code that already reads clearly through names and structure

For long-form rationale comments, make each sentence earn its place by
answering one of these:

- What fails without this?
- What invariant must hold?
- Why is the simpler-looking alternative wrong?
- What safe-direction approximation are we intentionally choosing?

If you add a suppression, justify it inline and keep the scope narrow.

## Pass 4: Validation and Evaluation

Unit tests are necessary but not sufficient.

Use a layered mix:

- Pure unit tests for deterministic transformations
- Fixture-based tests for parsing, prompt assembly, or model post-processing
- Integration tests for storage, queues, databases, or APIs on critical paths
- Smoke evaluations that exercise the real path on a small representative set

Validation priorities:

1. Prevent silent contract drift
2. Catch real-boundary failures early
3. Keep fixtures stable and explain why they exist
4. Prefer a cheap real integration test over a misleading mock

## Pass 5: Operations and Delivery

Before finalizing, make sure another engineer or agent can operate the change.

Cover:

- How to run it
- How to verify success
- How to rerun safely
- How to recover from partial failure
- What should be documented or highlighted in the summary

For risky changes, include:

- Rollback conditions
- Feature-flag rollout plan
- Migration order
- Data repair or replay notes

## Portable Engineering Practices

Use `references/portable-engineering-patterns.md` when you want the supporting
pattern catalog.

The core adaptations are:

1. Validate configuration and payload boundaries at runtime, not only with type
   hints.
2. Version operational changes and migrations explicitly.
3. Put telemetry on expensive or failure-prone execution paths.
4. Keep experiment gates and fallbacks visible in code.
5. Default to no comments. Add a comment only when it preserves non-obvious context a future
   reader would miss from the code alone: a hidden constraint, subtle invariant, bug workaround,
   or surprising behavior.

## Completion Template

```markdown
## AI-Friendly Development: PASSED | INCOMPLETE | BLOCKED

### Five-pass result

- Pass 1 contracts:
- Pass 2 data and state:
- Pass 3 runtime:
- Pass 4 validation:
- Pass 5 operations:

### Contracts changed

- [path or interface]: [what changed]

### Observability and evaluation

- [metric/log/eval/test added]

### Risks

- [remaining reproducibility, rollout, or data risks]
```
