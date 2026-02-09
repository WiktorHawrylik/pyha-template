# Agent Instructions (Mandatory)

These instructions apply to all humans, bots, and LLMs working in this repository.

## Non-negotiable rules

- **Never commit secrets** (tokens, keys, passwords, credentials, internal URLs).
- **No network calls in tests** (mock external APIs and use local fixtures).
- **Keep public APIs stable**; deprecate before breaking.
- **Write tests for behavior changes** and update existing tests when modifying behavior.
- **Prefer small PRs** focused on a single concern.
- **Update docs when changing APIs** or developer workflow.
- **Follow Conventional Commits** for commit messages and PR titles.

## Evaluation instructions

Before finalizing work:

1. **Read pre-commit hooks** in `.pre-commit-config.yaml` and align changes with them.
2. **Run the quality gates** listed in `README.md` (ruff, mypy, pytest with coverage).
3. **Compare outputs/data** for any scripts you modify (ensure deterministic results).
4. **Update docs and changelog** if you change public APIs or workflows.

## Safety

If you are unsure whether a change is acceptable, stop and ask for guidance.
