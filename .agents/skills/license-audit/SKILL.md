---
name: license-audit
description: Execute AGPL-3.0-or-later license compliance audits for Python repositories. Use when asked to run a license audit, verify AGPL file headers, inventory and classify dependency licenses, block incompatible licenses, or confirm third-party attribution before merge or release.
---

# License Audit

## Overview

Run a repeatable AGPL compliance workflow and return pass/fail status with remediation guidance.
Use bundled scripts for deterministic execution and the reference runbook for policy details.

## Quick Start

1. Confirm repository root path. Default to current working directory.
2. Run the orchestrator:

```bash
.agents/skills/license-audit/scripts/run_license_audit.sh \
  --repo-root <repo-root>
```

3. Report:

- Header violations
- Blocked dependency licenses
- Review-required dependency licenses
- Generated artifact paths

## Workflow

1. Prepare environment with `uv sync --extra all` unless the user explicitly asks to skip sync.
2. Validate AGPL headers with `scripts/license_audit_headers.py`.
3. Export dependency metadata with `pip-licenses`.
4. Categorize dependency licenses with `scripts/license_audit_dependencies.py`.
5. Collect attribution markers (`Source:`, `License:`, `Copyright`) under target roots.
6. Summarize and gate with `scripts/summarize_license_audit.py`.

Use defaults when the user does not override:

- Roots: `src,tests,scripts`
- Output directory: `build/license-compliance`

Run with explicit options when needed:

```bash
.agents/skills/license-audit/scripts/run_license_audit.sh \
  --repo-root <repo-root> \
  --roots src,tests,scripts \
  --output-dir build/license-compliance
```

## Output Contract

Always produce:

- `build/license-compliance/header-audit.csv`
- `build/license-compliance/dependency-licenses.csv`
- `build/license-compliance/dependency-license-audit.csv`
- `build/license-compliance/third-party-attribution-grep.txt`

Always include a summary block:

```text
License compliance audit completed.
- Header violations: <N>
- Blocked dependencies: <N>
- Review-required dependencies: <N>
- Third-party attribution checks: completed
Artifacts: <artifact-dir>/*
```

## Gate Criteria

Fail audit when either condition is true:

- `header-audit.csv` contains one or more `FAIL` rows.
- `dependency-license-audit.csv` contains one or more `BLOCK` rows.

Escalate to a human maintainer when either condition is true:

- `dependency-license-audit.csv` contains one or more `REVIEW` rows.
- Copied/adapted third-party code lacks source/license attribution.

## References

Read `references/license-audit-workflow.md` for:

- Full command-level runbook
- Required AGPL header template
- Compatible and incompatible license examples
- Escalation guidance
