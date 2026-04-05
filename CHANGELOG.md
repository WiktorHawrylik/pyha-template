# Changelog

All notable changes to this project are documented in this file.
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Release workflow follows GitFlow release branches (cut from develop, then merge to main and back to develop): [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

## [Unreleased]

### Added

- `ai-friendly-development` skill under `.agents/skills/ai-friendly-development/`:
  patterns and workflow for building Python repositories safe for human and AI extension.
- `commit-readiness` skill under `.agents/skills/commit-readiness/`: iterative
  pre-commit repair workflow with conventional commit message proposal.
- `documentation-update` skill under `.agents/skills/documentation-update/`:
  evidence-driven docs maintenance workflow with strict validation gates.
- `release-preparation` skill under `.agents/skills/release-preparation/`:
  gated SemVer release-prep workflow covering version sources, changelog
  promotion, collision checks, and pre-publish validation.

### Changed

- Migrated commit-readiness workflow from `.github/agents/` and
  `.github/prompts/` to the unified `.agents/skills/` layout.
- Migrated release workflow guidance from `.github/agents/` to the unified
  `.agents/skills/` layout with explicit human approval gates.

### Docs

- Updated template and documentation standards to reflect current repo skill
  discovery and the GitFlow-based release preparation workflow.

---

## [0.0.0] - 0000-00-00

### Added

- Repository initialization.

---

## Changelog Maintenance (AI + Human)

Always update this file when behavior, API, workflow, dependencies, or docs change.
Create or update a concrete release section for each merged release.

When preparing a release:

1. Create `## [X.Y.Z] - YYYY-MM-DD`.
2. Add all relevant items for that release under categories.
3. Keep category headings (`Added`, `Changed`, `Fixed`, `Docs`) even if some are empty.

### Release Entry Template

```markdown
## [X.Y.Z] - YYYY-MM-DD

Release branch: [release/x.y.z](https://github.com/WiktorHawrylik/your-package-name/tree/release/x.y.z)

### Added
- [Short user-visible change] ([#123](https://github.com/WiktorHawrylik/your-package-name/pull/123))

### Changed
- [Behavior/config/workflow change] ([#234](https://github.com/WiktorHawrylik/your-package-name/pull/234))

### Fixed
- [Bug fix with concrete impact] ([#345](https://github.com/WiktorHawrylik/your-package-name/pull/345))

### Docs
- [Documentation-only update] ([#456](https://github.com/WiktorHawrylik/your-package-name/pull/456))
```

### Required Variables

- `X.Y.Z`: must match the released version.
- `YYYY-MM-DD`: release date in calendar format.
- `release/x.y.z`: release branch for that version.
- Pull request links: include when available.

### Precision Rules for AI Agents

1. Use concrete, user-facing wording. Avoid vague text like "minor updates".
2. Prefer one change per bullet.
3. Include impact context when possible (for example: CLI, API, tests, docs).
4. Do not include speculative or unverified items.
5. Do not remove previous release entries.

### Verification Checklist

- Version matches release target.
- Date is valid `YYYY-MM-DD`.
- Entries are categorized correctly.
- Links resolve.
