# Agentic development rules

These rules apply to humans and LLMs working in this repository.

## Mandatory guardrails
- Never commit secrets, credentials, or private keys.
- Do not add network calls in tests (no HTTP, no API calls, no live services).
- Keep public APIs stable; document any breaking changes explicitly.
- Write tests for behavior changes and keep existing tests passing.
- Prefer small, focused PRs.
- Update documentation when changing public APIs or workflows.
- Follow Conventional Commits for commit messages and PR titles.

## Evaluation checklist
- Run the commands in the "Testing" section of the README.
- Compare outputs before/after changes for regressions.
- Review `.pre-commit-config.yaml` and ensure hooks pass.
- Ensure `scripts/check_agents.sh` succeeds (AGENTS.md must be present and non-empty).
