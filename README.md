# python-library-template

> **If you are an LLM/agent:** read [AGENTS.md](AGENTS.md) before making changes.

A reusable GitHub template repository for rapid Python library development with agentic tooling.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,docs]"
pre-commit install
pytest
```

## Development workflow

- **Lint/format:** `ruff check --fix .` and `ruff format .`
- **Type-check:** `mypy src`
- **Test:** `pytest`
- **Docs:** `mkdocs serve`

## Release workflow

1. Update the version in `pyproject.toml`.
2. Update `CHANGELOG.md` (create one if you need release notes).
3. Run `python -m build`.
4. Run `twine upload dist/*` (see `.github/workflows/release.yml` for the placeholder).

## Renaming the template package

The default package name is `python_library_template`.

- Rename the folder under `src/`.
- Update `pyproject.toml` (`project.name`, `tool.hatch.build.targets.wheel.packages`).
- Update import paths in `tests/` and docs.

## License & headers

This template is GPL-3.0-only. Include the following header in new source files:

```text
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) YEAR Your Name
```

## Repository layout

```
.
├── src/python_library_template
├── tests
├── docs
├── .github
├── scripts
└── pyproject.toml
```
