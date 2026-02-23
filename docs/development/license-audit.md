# License Compliance Guide (Agent-Executable, v2)

This project is licensed under **AGPL-3.0-or-later**.
This guide is designed for humans and AI agents to run a repeatable compliance audit.

Legal note: this is an engineering compliance workflow, not legal advice.
If any result is ambiguous, escalate to a human maintainer for final review.

## Objective

Verify all of the following before merge:

1. Python source files include the required AGPL header text.
2. Dependency licenses are inventoried and categorized.
3. Disallowed licenses are blocked.
4. Third-party code usage is attributed and documented.

## Scope

- Python files in `src/`, `tests/`, and `scripts/`
- Dependencies declared in `pyproject.toml` and resolved in `uv.lock`
- Third-party code copied or adapted into this repository

## Required Tools

- `uv`
- `find` (default macOS)
- `grep` (default macOS)
- `python` via `uv run python`

## Required Header Template

Each Python module must contain AGPL notice text equivalent to:

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

Required variables:

- `[Module description]`: concise, module-specific summary.
- `[YYYY]`: current year.
- `[Your Name]`: contributor full name.

## Execution Workflow

Run from repository root.

### Step 1. Prepare Environment

```bash
uv sync --extra all
mkdir -p build/license-compliance
```

### Step 2. Validate License Headers

```bash
uv run python scripts/license_audit_headers.py \
  --roots src tests scripts \
  --output build/license-compliance/header-audit.csv
```

### Step 3. Extract Dependency Licenses

```bash
uv run pip-licenses \
  --with-urls \
  --with-authors \
  --from=mixed \
  --format=csv \
  > build/license-compliance/dependency-licenses.csv
```

### Step 4. Categorize Dependency Licenses

```bash
uv run python scripts/license_audit_dependencies.py \
  --input-csv build/license-compliance/dependency-licenses.csv \
  --output-csv build/license-compliance/dependency-license-audit.csv
```

### Step 5. Verify Third-Party Attribution Markers

```bash
: > build/license-compliance/third-party-attribution-grep.txt
for d in src tests scripts; do
  [ -d "$d" ] || continue
  grep -R -n -E "Source:|License:|Copyright" "$d" \
    >> build/license-compliance/third-party-attribution-grep.txt || true
done
```

If external code was copied or adapted, ensure nearby comments include:

1. Source URL
2. Original license
3. Copyright notice

## Output Artifacts

The audit must generate:

- `build/license-compliance/header-audit.csv`
- `build/license-compliance/dependency-licenses.csv`
- `build/license-compliance/dependency-license-audit.csv`
- `build/license-compliance/third-party-attribution-grep.txt`

## Pass/Fail Criteria

Pass only if:

1. `header-audit.csv` has zero `FAIL` rows.
2. `dependency-license-audit.csv` has zero `BLOCK` rows.
3. Any `REVIEW` rows are resolved by a human maintainer and documented.
4. Third-party copied/adapted code has attribution comments.

## Recommended PR Summary Snippet

```text
License compliance audit completed.
- Header violations: <N>
- Blocked dependencies: <N>
- Review-required dependencies: <N>
- Third-party attribution checks: completed
Artifacts: build/license-compliance/*
```

## Incompatible Examples (Block by Default)

- Proprietary or closed-source licenses
- CC BY-NC and other non-commercial licenses
- GPL-2.0-only
- Custom restrictive licenses with field-of-use or redistribution limits

## Compatible Examples (Generally Acceptable)

- AGPL-3.0, GPL-3.0, LGPL
- MIT, BSD (2/3-clause), Apache-2.0, ISC
- Public-domain equivalents (CC0, Unlicense)

For edge cases, dual licenses, or unclear metadata, mark as `REVIEW` and escalate.
