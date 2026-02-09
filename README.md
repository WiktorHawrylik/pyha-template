# python-library-template

> **If you are an LLM**: read and follow [AGENTS.md](AGENTS.md) before making changes. It contains mandatory guardrails, evaluation steps, and commit requirements.

A reusable GitHub template for rapid Python library development with Codex/Copilot and other agentic tools.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Development workflow

1. Create a feature branch.
2. Install tooling and enable pre-commit hooks:

   ```bash
   pre-commit install
   ```

3. Run checks locally:

   ```bash
   ruff check .
   ruff format .
   mypy src
   pytest
   ```

## Release workflow

1. Update `version` in `pyproject.toml`.
2. Tag the release (`git tag vX.Y.Z`).
3. Push tags to trigger `.github/workflows/release.yml`.
4. Publish artifacts when secrets are configured (see workflow for details).

## Renaming the package

The default import path is `python_library_template`. To rename:

1. Rename `src/python_library_template` to your new package name.
2. Update imports in `tests/`.
3. Update the package name in `pyproject.toml` (`[project].name`).

## License and copyright headers

This template is licensed under GPL-3.0-only. For new source files, add an SPDX header like:

```text
# SPDX-License-Identifier: GPL-3.0-only
```

## Documentation

MkDocs configuration lives in `mkdocs.yml` with docs in `docs/`.
Run locally with:

```bash
mkdocs serve
```
