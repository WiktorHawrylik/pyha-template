# Python Library Template

## If you are an LLM
Read [AGENTS.md](AGENTS.md) before making changes. It contains mandatory rules, evaluation steps, and guardrails for agentic work on this template.

## Overview
This repository is a reusable template for building Python libraries with a modern toolchain (ruff, mypy, pytest, MkDocs) and agentic development guardrails.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pre-commit install
pytest
```

## Rename the package
The default package name is `python_library_template`. To rename it:
1. Update `project.name` in `pyproject.toml`.
2. Rename `src/python_library_template` to your desired package.
3. Update imports in tests and docs.
4. Update `mkdocs.yml` and any badges/links in `README.md`.

## Development workflow
```bash
ruff check .
ruff format .
mypy src
pytest
mkdocs serve
```

## Release workflow
1. Update the version in `pyproject.toml`.
2. Run `python -m build`.
3. Use `.github/workflows/release.yml` to publish artifacts (configure secrets as documented).

## Documentation
The docs site is powered by MkDocs Material. Start locally with:
```bash
mkdocs serve
```

## Evaluation instructions
- Run the tests and compare outputs before/after changes.
- Review `.pre-commit-config.yaml` for tooling expectations.
- Use the CI workflows as the source of truth for required checks.

## License
GPL-3.0-only. See [LICENSE](LICENSE) and the copyright header guidance in
[COPYRIGHT_HEADER.md](COPYRIGHT_HEADER.md).
