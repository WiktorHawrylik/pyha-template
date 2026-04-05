---
name: commit-readiness
description: Prepare a branch for commit by iteratively fixing pre-commit failures, validating with command evidence, and proposing a conventional commit message. Use when the task is to get changes into a commit-ready state, repair lint/type/security hook failures, or summarize what was fixed before committing.
---

# Commit Readiness

## Overview

Use this skill to drive a branch to a clean pre-commit state with minimal,
targeted fixes and a clear completion summary.

This skill is for commit readiness, not broad feature refactors. Documentation
or test changes may be necessary, but only when they are required to satisfy
the quality gates.

## Quick Start

1. Sync the development environment:

```bash
uv sync --extra dev && source .venv/bin/activate
```

2. Establish the baseline:

```bash
SKIP=mkdocs-build,pytest uv run pre-commit run --hook-stage pre-push
```

3. Repair failures iteratively until the hooks pass or a real blocker is
   identified.

## Hard Constraints

- Never modify `.pre-commit-config.yaml`, `pyproject.toml`, `Makefile`, or anything under `.github`.
- Never create config files that disable or relax checks.
- Never suppress errors such as `# type: ignore` without serious justification and explicit user approval.
- Never expand the scope beyond the smallest change needed to satisfy the failing checks.
- Never claim success without command evidence.

## Workflow

1. Run the baseline pre-commit command.
2. Identify failed hooks, affected files, and error categories.
3. Fix issues in this order:
   - Auto-fixable formatting
   - Simple linting/import cleanup
   - Type issues
   - Security issues
   - Complex logic issues
4. Re-run the same pre-commit command after each repair pass.
5. Stop after 10 iterations, or earlier if the same blocker repeats more than 3 times.

Stop and escalate when:

- Acceptance criteria are ambiguous
- Requirements conflict
- A required external dependency is unavailable locally

## Output

Always report:

- Whether commit readiness is `PASSED`, `INCOMPLETE`, or `BLOCKED`
- What categories of issues were resolved
- Which files changed and why
- Any remaining blockers
- How many iterations were needed
- A proposed commit message in conventional format

## Reference

Read `references/commit-readiness-workflow.md` when you need the full
step-by-step runbook and summary template.
