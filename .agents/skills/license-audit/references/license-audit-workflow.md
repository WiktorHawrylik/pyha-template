# License Audit Workflow Reference

Use this runbook when you need exact command-level execution details.

## Objective

Verify all of the following before merge:

1. Python source files include the required AGPL header text.
2. Dependency licenses are inventoried and categorized.
3. Disallowed licenses are blocked.
4. Review-required dependency licenses are resolved and documented.
5. Published review-decision documentation is generated from the CSV.
6. Third-party copied/adapted code is attributed.

## Scope

- Python files in `src/`, `tests/`, `scripts/`, and `.agents/skills/license-audit/scripts/`
- Dependencies declared in `pyproject.toml` and resolved in `uv.lock`
- Third-party code copied or adapted into repository files

## Required Tools

- `uv`
- `find`
- `grep`
- `python` via `uv run python`

## Required Header Template

Require every Python module to contain AGPL notice text equivalent to a
top-level module docstring:

```python
"""[Module description]

Copyright (C) [YYYY] [Your Name]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
```

The automated audit validates:

- The header lives in the module docstring.
- A module description appears before the copyright line.
- The copyright line includes a year and copyright holder.
- The required AGPL notice text appears in that docstring.

Require these variable substitutions:

- `[Module description]`: concise module summary
- `[YYYY]`: current year
- `[Your Name]`: contributor full name

## Execution Steps

Run from repository root.

### 1. Prepare Environment

```bash
uv sync --extra all
mkdir -p build/license-compliance
```

### 2. Validate License Headers

```bash
uv run python .agents/skills/license-audit/scripts/license_audit_headers.py \
  --roots src tests scripts .agents/skills/license-audit/scripts \
  --output build/license-compliance/header-audit.csv
```

### 3. Extract Dependency Licenses

```bash
uv run pip-licenses \
  --with-urls \
  --with-authors \
  --from=mixed \
  --format=csv \
  > build/license-compliance/dependency-licenses.csv
```

### 4. Categorize Dependency Licenses

```bash
uv run python .agents/skills/license-audit/scripts/license_audit_dependencies.py \
  --input-csv build/license-compliance/dependency-licenses.csv \
  --output-csv build/license-compliance/dependency-license-audit.csv
```

### 5. Generate Review Decisions Markdown

```bash
uv run python .agents/skills/license-audit/scripts/generate_review_decisions_markdown.py \
  --input-csv docs/development/license-review-decisions.csv \
  --output-md docs/development/license-review-decisions.md
```

### 6. Verify Third-Party Attribution Markers

```bash
: > build/license-compliance/third-party-attribution-grep.txt
for d in src tests scripts .agents/skills/license-audit/scripts; do
  [ -d "$d" ] || continue
  find "$d" \
    \( -name "__pycache__" -o -name "*.egg-info" \) -prune -o \
    -type f ! -name "*.pyc" -print0 |
    xargs -0 grep -n -I -E "Source:|License:|Copyright" \
    >> build/license-compliance/third-party-attribution-grep.txt || true
done
```

### 7. Resolve Review-Required Dependencies

If `dependency-license-audit.csv` contains `REVIEW` rows, document maintainer
decisions in `docs/development/license-review-decisions.csv` with these columns:

- `Name`
- `Version`
- `License`
- `Decision`
- `ReviewedBy`
- `ReviewedOn`
- `Reference`
- `Rationale`

## Output Artifacts

Require these artifacts:

- `build/license-compliance/header-audit.csv`
- `build/license-compliance/dependency-licenses.csv`
- `build/license-compliance/dependency-license-audit.csv`
- `build/license-compliance/third-party-attribution-grep.txt`
- `docs/development/license-review-decisions.md`

## Pass/Fail Criteria

Pass only if:

1. `header-audit.csv` has zero `FAIL` rows.
2. `dependency-license-audit.csv` has zero `BLOCK` rows.
3. `REVIEW` rows are documented and resolved in `docs/development/license-review-decisions.csv`.
4. Copied/adapted third-party code contains attribution comments.

## Recommended Summary Snippet

```text
License compliance audit completed.
- Header violations: <N>
- Blocked dependencies: <N>
- Review-required dependencies: <N>
- Third-party attribution checks: completed
Artifacts: build/license-compliance/*
```

## License Classification Guidance

Block by default:

- Proprietary or closed-source licenses
- CC BY-NC and non-commercial licenses
- GPL-2.0-only
- Custom restrictive licenses with redistribution or field-of-use limits

Generally acceptable:

- AGPL-3.0, GPL-3.0, LGPL
- MIT, BSD (2/3-clause), Apache-2.0, ISC
- Public-domain equivalents (CC0, Unlicense)

Escalate ambiguous, dual-license, or unclear metadata as `REVIEW`.
