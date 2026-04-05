# Release Preparation Workflow

Use this runbook when a release task needs more than the short skill summary.

## Objective

Prepare a release branch or release candidate cleanly, with explicit human
approval at every irreversible step.

## Release Facts to Gather First

Collect and verify:

- Current branch
- Whether the worktree is clean
- Target release version
- Current version in `pyproject.toml`
- Current version in `src/your_package_name/__init__.py`
- Last local release tag, if any
- Package name from `pyproject.toml`
- Whether the package name is still a placeholder

If the target version is not explicitly provided, propose one using SemVer and
ask the user to confirm it before editing release files.

## Repo Process

This repository currently documents:

- SemVer versioning in `CONTRIBUTING.md`
- GitFlow release branches in `CONTRIBUTING.md`
- Changelog release entry rules in `CHANGELOG.md`
- Tag-driven GitHub Actions publishing in `.github/workflows/release.yml`

The documented release path is:

1. Start from `develop`
2. Create `release/x.y.z`
3. Update version files
4. Update `CHANGELOG.md`
5. Merge to `main`
6. Tag `vX.Y.Z`
7. Push the tag to trigger publish
8. Merge back to `develop`

Do not perform steps 5 through 8 without explicit approval.

## Files to Check

Release preparation usually touches:

- `pyproject.toml`
- `src/your_package_name/__init__.py`
- `CHANGELOG.md`

Release-process documentation may also need review:

- `CONTRIBUTING.md`
- `docs/guide/template-usage.md`
- `docs/changelog.md`

Only update release docs when the documented commands, branch names, links, or
trigger behavior are stale.

## Version Consistency Rules

Keep the same release version in every version source you touch.

At minimum, the target version must match:

- `pyproject.toml` project version
- `src/your_package_name/__init__.py` `__version__`
- The `CHANGELOG.md` release header
- The release branch name `release/x.y.z`
- The release tag `vX.Y.Z`

## Changelog Rules

Use the root `CHANGELOG.md` as the canonical release note source.

When preparing a release:

1. Keep `## [Unreleased]` at the top
2. Create `## [X.Y.Z] - YYYY-MM-DD`
3. Move the relevant release items under that concrete section
4. Keep category headings such as `Added`, `Changed`, `Fixed`, and `Docs`
5. Prefer user-facing wording
6. Prefer PR links when they exist
7. If history is commit-shaped rather than PR-shaped, group related commits and
   include a link for each commit

For dates, always use an absolute calendar date like `2026-04-05`.

## Collision Checks

Before creating the tag, check both:

- Local git tags for `vX.Y.Z`
- Published package versions on PyPI when the package name is not a template
  placeholder

If the package name is still a placeholder such as `your-package-name`,
explicitly say the PyPI collision check is not meaningful yet.

## Validation

Default validation set for this repo:

```bash
make lint
make test
uv run mkdocs build --strict
.agents/skills/license-audit/scripts/run_license_audit.sh --repo-root .
```

If any check is skipped, explain why and what residual risk remains.

## Human-Gated Actions

Do not perform these without an explicit yes from the user:

- `git checkout -b release/x.y.z`
- `git merge --no-ff release/x.y.z`
- `git tag -a vX.Y.Z`
- `git push`
- Any action that triggers PyPI publish or GitHub Release creation

When stopped at a gate, state the exact command or action pending next.

## Completion Template

```markdown
## Release Preparation: READY | BLOCKED | AWAITING_HUMAN_GATE

### Target version

- Proposed or confirmed version: X.Y.Z

### Release files

- [path]: [what changed]

### Changelog coverage

- [how unreleased items were grouped]
- [PR links or commit links included]

### Validation

- [command]: passed | failed | skipped

### Collision checks

- Local tag check:
- PyPI version check:

### Pending human gate

- [next irreversible action]
```
