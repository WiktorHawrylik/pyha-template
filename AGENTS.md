# Agent Guardrails

These rules are mandatory for any automated agent or human contributor.

## Non-negotiable rules

- Never commit secrets, tokens, or credentials.
- Do **not** add network calls in tests.
- Keep public APIs stable; if an API must change, document the breaking change.
- Write or update tests for any behavior change.
- Prefer small, focused pull requests.
- Update documentation when changing APIs or developer workflows.
- Use Conventional Commits for commit messages (e.g., `feat: add parser`).

## Evaluation checklist (required before proposing changes)

- Read `.pre-commit-config.yaml` to understand enforced checks.
- Run `scripts/check_agents.py` to ensure guardrails remain in place.
- Run linting and formatting checks:
  - `ruff check .`
  - `ruff format .`
- Run type checks: `mypy src`
- Run tests with coverage: `pytest`

## Data change verification

When touching data files or outputs, compare before/after results and call out deltas explicitly in your summary.
