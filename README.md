# python-library-template

## If you are an LLM or agent
Read and follow the repository guardrails in [AGENTS.md](AGENTS.md) before making any changes.

A reusable GitHub Template repository for rapid Python library development with Codex/Copilot
and other agentic coding tools.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Run the full quality gate locally:
```bash
ruff check .
ruff format --check .
mypy src
pytest
```

## Development workflow
1. Create a feature branch.
2. Make changes in `src/` and update tests in `tests/`.
3. Run pre-commit hooks and the quality gate.
4. Open a PR with a small, focused scope.

## Release workflow
1. Update the version in `pyproject.toml`.
2. Update `CHANGELOG.md` (if you maintain one).
3. Tag a release (`git tag vX.Y.Z`) and push.
4. CI builds artifacts; publishing requires adding credentials in the release workflow.

## Package renaming
The placeholder package name is `python_library_template` (folder) and
`python-library-template` (project). To rename:
1. Rename the `src/python_library_template` folder and update imports.
2. Update `pyproject.toml` `project.name` and metadata.
3. Update references in this README, docs, and workflows.

## License
GPL-3.0-only. See [LICENSE](LICENSE).

## Copyright header guidance
Add this header (and update the year/name) to new source files:
```
# Copyright (C) 2024 Your Name
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
```
