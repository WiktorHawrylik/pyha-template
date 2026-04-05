---
name: release-preparation
description: Prepare this Python repository for a SemVer release by verifying the target version, updating version sources and changelog entries, checking GitFlow release-branch rules, validating release docs, and stopping for explicit human approval before tagging, pushing, or publishing. Use when cutting a release branch, bumping versions, drafting release notes, or checking release readiness for GitHub and PyPI.
---

# Release Preparation

## Overview

Use this skill to bring the repository to a release-ready state without
silently performing irreversible publish actions.

This skill is for release preparation and release verification. It is not a
"ship without asking" workflow.

## Human Gates

Always pause for explicit user approval before:

- Choosing a release version that the user did not explicitly provide
- Creating or pushing a `release/x.y.z` branch
- Creating or pushing a Git tag
- Merging to `main` or back to `develop`
- Triggering or confirming any publish action to PyPI or GitHub Releases

If the repository is dirty or the branch state is surprising, surface that
before making branch or tag changes.

## Repository Facts

Use these repo-specific sources of truth:

- `CONTRIBUTING.md`: SemVer and GitFlow release branch process
- `CHANGELOG.md`: release entry format and changelog precision rules
- `.github/workflows/release.yml`: tag-driven build, PyPI publish, and GitHub
  release automation
- `pyproject.toml`: package version and package metadata
- `src/your_package_name/__init__.py`: runtime package version
- `docs/guide/template-usage.md`: public release example that may need
  updates when the release process changes

## Workflow

1. Gather facts: current branch, worktree state, target version, current
   version sources, last tag, and package name.
2. Confirm the SemVer bump with the user if the version was not provided.
3. Check for collisions:
   - local tags like `vX.Y.Z`
   - existing published package version on PyPI when the package name is real
4. Prepare the release branch if requested:
   - branch name must be `release/x.y.z`
   - branch source must be `develop`
5. Update all version sources together.
6. Promote release notes from `## [Unreleased]` into a concrete release entry in
   `CHANGELOG.md` using `YYYY-MM-DD`.
7. Group release notes by user-visible topic. Prefer PR links when available.
   If work was merged without a clean PR boundary, group related commits and
   include a link for each commit.
8. Check whether release guidance is stale in repo docs and update only the
   pages that actually mention the release flow.
9. Run release validation.
10. Summarize readiness and stop at the next human gate.

## Validation

For this repository, release readiness should normally include:

```bash
make lint
make test
uv run mkdocs build --strict
.agents/skills/license-audit/scripts/run_license_audit.sh --repo-root .
```

If release preparation changed only docs or metadata, explain any narrower
validation scope explicitly.

## Output

Always report:

- Release status: `READY`, `BLOCKED`, or `AWAITING_HUMAN_GATE`
- Target version and whether it was confirmed
- Files updated for the release
- Validation commands run and their outcomes
- Any PyPI/tag collision findings
- The exact next human-gated action still pending

## Reference

Read `references/release-preparation-workflow.md` for the detailed runbook,
file checklist, and completion template.
