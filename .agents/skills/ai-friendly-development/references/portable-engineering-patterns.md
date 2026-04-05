# Portable Engineering Patterns

This reference captures engineering practices that translate well into Python
repositories, especially for data pipelines, ML systems, inference services,
and agentic workflows.

The goal is to preserve engineering discipline without depending on a specific
reference codebase.

## Pattern 1: Runtime schemas at boundaries

Why it matters:

- Validates payloads and config with runtime schemas
- Rejects malformed or partially trusted config
- Uses defaults and fallbacks when parsing fails
- Documents why specific guardrails exist

Python adaptation:

- Validate inbound JSON, settings, queue messages, and config with
  `pydantic` or equivalent runtime parsing
- Fail closed on malformed control-plane input
- Prefer whole-object validation over partially trusting bad config
- Keep boundary validation close to the ingestion point

## Pattern 2: Typed workflow and command contracts

Why it matters:

- Models workflow commands with explicit fields and execution modes
- Separates capabilities, context, and result types

Python adaptation:

- Model service inputs and outputs with typed request and response objects
- Avoid passing large ad hoc dictionaries across layers
- Separate domain models from framework or transport concerns

## Pattern 3: Telemetry for cost, latency, and usage

Why it matters:

- Tracks model usage, latency, retries, and cost as first-class runtime data
- Persists enough state to resume sessions and explain what happened

Python adaptation:

- Emit structured metrics for latency, throughput, errors, retries, and cost
- For LLM systems, record token and model usage per step when feasible
- For data pipelines, record rows processed, rows skipped, retry counts, and
  artifact versions

## Pattern 4: Small explicit migrations

Why it matters:

- Encodes state changes in focused migration functions
- Preserves user intent
- Logs migration success and failure
- Removes legacy state only after the migration succeeds

Python adaptation:

- Treat schema changes, config moves, and backfills as explicit migration code
- Keep migrations idempotent when possible
- Emit audit logs or metrics for success and failure
- Remove legacy behavior only after the new state is written successfully

## Pattern 5: Feature-gated experiments and safe fallbacks

Why it matters:

- Keeps experimental paths visibly gated
- Makes fallback behavior explicit
- Uses telemetry to understand which path executed

Python adaptation:

- Gate risky ML or agentic behavior behind explicit flags or config
- Keep fallback behavior close to the primary path
- Log why a fallback or retry happened
- Avoid hidden behavior switches that make outputs irreproducible

## Pattern 6: Comments that preserve operational rationale

Why it matters:

- Writes comments that explain the failure history behind a guardrail
- Avoids comments that merely restate syntax

Python adaptation:

- Write comments for invariants, incident-driven checks, and tricky sequencing
- Do not comment obvious assignments or control flow
- Keep rationale next to the guardrail so future edits preserve intent

## Pattern 7: Comment generation is a pipeline, not an afterthought

Why it matters:

- High-signal comments usually come from multiple layers of pressure:
  instructions to avoid comments by default, review cleanup that removes weak
  commentary, and explicit justification for exceptional cases
- This produces fewer comments, but the remaining ones carry real operational
  weight

Python adaptation:

- Write the code first, then run a comment pass
- Remove narration comments before finalizing
- Keep comments only when they preserve hidden context
- Require inline justification for suppressions and escape hatches
- Avoid deleting existing rationale comments unless you are sure the underlying
  constraint is gone

## Summary

These patterns point to a clear Python-friendly process:

1. Parse and validate boundaries explicitly.
2. Keep state changes versioned and reviewable.
3. Instrument expensive and failure-prone paths.
4. Test real boundaries where drift is costly.
5. Generate comments through a deliberate filter: default-delete, then keep
   only rationale that would otherwise be lost.
