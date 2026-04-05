# License Compliance Guide

This project is licensed under **AGPL-3.0-or-later**.
This page is the human-facing policy guide for AGPL compliance in this repository.
The executable workflow lives in the self-contained skill under
`.agents/skills/license-audit/`.

Legal note: this is an engineering compliance workflow, not legal advice.
If any result is ambiguous, escalate to a human maintainer for final review.

## Objective

Verify all of the following before merge:

1. Python source files include the required AGPL header text.
2. Dependency licenses are inventoried and categorized.
3. Disallowed licenses are blocked.
4. Review-required dependency licenses are resolved and documented.
5. Third-party code usage is attributed and documented.

## Standard Workflow

Run the orchestrator from repository root:

```bash
.agents/skills/license-audit/scripts/run_license_audit.sh --repo-root .
```

For non-default roots, pass them explicitly:

```bash
.agents/skills/license-audit/scripts/run_license_audit.sh \
  --repo-root . \
  --roots src,tests,scripts,.agents/skills/license-audit/scripts
```

Use the skill when you want the full repeatable workflow:

- Header validation
- Dependency inventory and classification
- Review-decision page generation
- Third-party attribution scan
- Final pass/fail summary

Published review decisions are available in
[License Review Decisions](license-review-decisions.md).

## Required Header Template

Each Python module must contain AGPL notice text equivalent to a top-level
module docstring:

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

- The header lives in the module docstring (not only in comments elsewhere).
- A module description appears before the copyright line.
- The copyright line includes a year and copyright holder.
- The required AGPL notice text is present in that docstring.

Required variables:

- `[Module description]`: concise, module-specific summary.
- `[YYYY]`: current year.
- `[Your Name]`: contributor full name.

## Review Decisions

If the dependency audit produces `REVIEW` rows, record maintainer decisions in
`docs/development/license-review-decisions.csv`.

Required columns:

- `Name`
- `Version`
- `License`
- `Decision`
- `ReviewedBy`
- `ReviewedOn`
- `Reference`
- `Rationale`

Use `Decision=APPROVED` only after a human maintainer has reviewed the license
terms and recorded both the rationale and the reference used for that approval.

The published Markdown page at `development/license-review-decisions/` is
generated from the CSV by
`.agents/skills/license-audit/scripts/generate_review_decisions_markdown.py`.

## Third-Party Attribution

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
3. Any `REVIEW` rows are resolved in `docs/development/license-review-decisions.csv`.
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
