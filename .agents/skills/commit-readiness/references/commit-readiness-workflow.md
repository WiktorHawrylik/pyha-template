# Commit Readiness Workflow

Use this runbook when you need the full detailed execution procedure for
pre-commit repair and commit preparation.

## Objective

Ensure all code changes pass pre-commit quality checks by automatically
detecting and fixing issues through iterative validation cycles.

Prioritize quality over speed. Each fix should be correct and maintainable,
not just check-passing.

## Non-objective

Documentation or test updates are not the primary goal, but they may be
necessary to meet pre-commit requirements. The main focus is code changes
required to pass pre-commit checks.

## Constraints

- Never modify `.pre-commit-config.yaml`, `pyproject.toml`, `Makefile`, or `.github`.
- Never create configuration files to disable, bypass, or relax checks.
- Never suppress errors without strong justification and explicit approval.
- Never add functional refactors or optimizations beyond what is needed to fix the failing checks.
- Never claim completion without command evidence.

## Baseline

Start by syncing the environment:

```bash
uv sync --extra dev && source .venv/bin/activate
```

Establish the baseline:

```bash
SKIP=mkdocs-build,pytest uv run pre-commit run --hook-stage pre-push
```

## Iterative Repair Cycle

Use a strict limit of 10 cycles:

1. Identify issues
2. Categorize issues
3. Prioritize
4. Fix
5. Validate

Stop early and escalate if the same blocker repeats more than 3 times.

Escalate when:

- Acceptance criteria are ambiguous
- Requirements conflict
- Required external dependencies are unavailable locally

### 1. Identify issues

Analyze the output to identify:

- Failed hooks and their error messages
- Affected files and line numbers
- Error categories such as formatting, linting, type checking, and security

### 2. Categorize issues

- Formatting issues
- Linting violations
- Type checking errors
- Security findings

### 3. Prioritize

Address issues in this order:

1. Auto-fixable formatting
2. Simple linting errors
3. Type hint additions or corrections
4. Security issues
5. Complex logic errors

### 4. Fix

- Read the relevant file sections
- Define context, constraints, and requirements
- Prefer the smallest diff that solves the issue cleanly
- Avoid introducing unrelated changes

### 5. Validate

```bash
SKIP=mkdocs-build,pytest uv run pre-commit run --hook-stage pre-push
```

- Exit code `0`: success
- Errors remain: continue to the next iteration
- Same blocker persists more than 3 times: stop and report the blocker

## Completion Checklist

- All targeted pre-commit hooks pass
- Changes are minimal and focused
- Summary clearly documents what was fixed

## Completion Summary Template

```markdown
## Pre-commit Quality Check: PASSED ✅ | INCOMPLETE ⚠️ | Blocked 🚫

### Issues Resolved

- **Formatting**: [count] files reformatted
- **Linting**: [count] violations fixed
- **Type Checking**: [count] type errors resolved
- **Security**: [count] vulnerabilities addressed

### Files Modified

- [path]: [why]
- [path]: [why]

### Functional Behavior Impact (if any)

- [1 line effect summary]

### Remaining Issues (if any)

- [none] OR [file:line - issue] OR [what blocked completion + why]

### Iterations Required

Completed in [X]/10 iterations

### Proposed commit message

```text
<type>(<scope>): <subject>

<body>

<footer>
```

### Next Steps

- Rerun tests to ensure no regressions
- Update documentation and `CHANGELOG.md` when needed
- Push the branch

```
