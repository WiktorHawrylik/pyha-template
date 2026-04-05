---
name: documentation-update
description: Update repository documentation so it matches current code, tooling, workflows, and navigation. Use when writing new docs pages, revising existing docs after code or process changes, improving clarity or discoverability, or validating documentation against repository behavior.
---

# Documentation Update

## Overview

Use this skill when a task requires accurate, actionable documentation that
matches repository behavior and helps readers complete real tasks without
guessing.

## Source of Truth

When instructions conflict, resolve them in this order:

1. `AGENTS.md`
2. `docs/development/mkdocs.md`
3. `docs/development/_constitution.md`
4. `CONTRIBUTING.md`
5. Repository behavior in code and executable config

If docs and code disagree, code and executable configuration win.

## Workflow

1. Identify the documentation trigger and impacted audiences.
2. Verify facts from repository evidence before editing.
3. Update only the necessary pages and keep guidance non-duplicative.
4. Update `mkdocs.yml` navigation when new pages are added or moved.
5. Validate with strict docs checks, then run broader quality checks if
   behavior changed.

## Principles

- Accuracy over style
- Task completion first
- Minimal ambiguity
- Single source of truth
- Traceability from code/workflow change to docs update

## Validation

Always run:

```bash
uv run mkdocs build --strict
uv run pre-commit run markdownlint --all-files
```

If code or public workflow changed, also run:

```bash
make format
make lint
make test
```

## Output

Always report:

- Whether the documentation update passed or was blocked
- Which files changed and why
- Which validation commands were run and whether they passed
- Whether nav and links were updated
- Any residual risks or follow-up work

## Reference

Read `references/documentation-update-workflow.md` for the full runbook,
trigger matrix, and completion report template.
