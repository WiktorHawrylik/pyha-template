# Agentic development guardrails

These rules apply to all automated agents (LLMs, bots, Copilot, Codex) working in this repo.
They are mandatory and enforced in CI.

## Non-negotiable rules
- Never commit secrets, credentials, or tokens.
- No network calls in tests (unit or end-to-end).
- Keep public APIs stable; if you must change them, document the change and update tests.
- Write or update tests for any behavior change.
- Prefer small PRs with clear scope.
- Update docs when you change APIs or developer workflows.
- Follow Conventional Commits for commit messages.

## Evaluation instructions
- Always run linting, type checking, and tests locally when possible:
  - `ruff check .`
  - `ruff format --check .`
  - `mypy src`
  - `pytest`
- Compare output data only with deterministic fixtures (no live network data).
- Review `.pre-commit-config.yaml` and ensure your changes satisfy those hooks.

## Safety checks
- If you need to modify or remove this file, stop and explain why in the PR.
- CI enforces that this file exists and is non-empty.
