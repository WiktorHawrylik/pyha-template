# License Audit Workflow Reference

Use this runbook when you need exact command-level execution details.

## Objective

Verify all of the following before merge:

1. Python source files include the required AGPL header text.
2. Dependency licenses are inventoried and categorized.
3. Disallowed licenses are blocked.
4. Third-party copied/adapted code is attributed.

## Scope

- Python files in `src/`, `tests/`, and `scripts/`
- Dependencies declared in `pyproject.toml` and resolved in `uv.lock`
- Third-party code copied or adapted into repository files

## Required Tools

- `uv`
- `find`
- `grep`
- `python` via `uv run python`

## Required Header Template

Require every Python module to contain AGPL notice text equivalent to:

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
uv run python scripts/license_audit_headers.py \
  --roots src tests scripts \
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
uv run python scripts/license_audit_dependencies.py \
  --input-csv build/license-compliance/dependency-licenses.csv \
  --output-csv build/license-compliance/dependency-license-audit.csv
```

### 5. Verify Third-Party Attribution Markers

```bash
: > build/license-compliance/third-party-attribution-grep.txt
for d in src tests scripts; do
  [ -d "$d" ] || continue
  grep -R -n -E "Source:|License:|Copyright" "$d" \
    >> build/license-compliance/third-party-attribution-grep.txt || true
done
```

## Output Artifacts

Require these artifacts:

- `build/license-compliance/header-audit.csv`
- `build/license-compliance/dependency-licenses.csv`
- `build/license-compliance/dependency-license-audit.csv`
- `build/license-compliance/third-party-attribution-grep.txt`

## Pass/Fail Criteria

Pass only if:

1. `header-audit.csv` has zero `FAIL` rows.
2. `dependency-license-audit.csv` has zero `BLOCK` rows.
3. `REVIEW` rows are escalated to a human maintainer and resolved.
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
