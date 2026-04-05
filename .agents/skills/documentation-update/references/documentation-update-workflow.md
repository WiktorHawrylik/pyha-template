# Documentation Update Workflow

Use this runbook when you need the detailed documentation-maintenance process.

## Mission

Create and update documentation that is accurate, actionable, and aligned with
repository behavior. The output must help users and contributors complete real
tasks without guessing.

## Scope

Use this workflow when a task requires any of:

- Writing new documentation pages
- Updating existing docs after code, workflow, or API changes
- Improving clarity, structure, navigation, or examples
- Verifying docs consistency with code and tooling

## Source-of-Truth Order

When instructions conflict, resolve in this order:

1. `AGENTS.md`
2. `docs/development/mkdocs.md`
3. `docs/development/_constitution.md`
4. `CONTRIBUTING.md`
5. Repository behavior in `Makefile`, `pyproject.toml`, `mkdocs.yml`, scripts, and tests

If docs and code disagree, code and executable configuration win.

## Core Principles

1. Accuracy over style: never document behavior you cannot verify.
2. Task completion first: optimize for readers to finish a workflow quickly.
3. Minimal ambiguity: include prerequisites, commands, expected outcomes, and failure modes.
4. Single source of truth: avoid duplicate or conflicting instructions.
5. Traceability: every doc change maps to a concrete code or workflow trigger.

## Documentation Workflow

### 1. Intake and Impact Mapping

- Identify the change trigger such as feature, API, workflow, config, bug fix, security, or performance.
- List impacted audiences:
  - End users: `docs/guide/`
  - Contributors: `docs/development/`, `CONTRIBUTING.md`
  - Integrators: `docs/api/`
- Build a file impact list before writing.

### 2. Evidence Collection

Before editing docs, verify facts from repository sources:

- Commands and automation: `Makefile`, scripts, workflows
- Config and defaults: `pyproject.toml`, `mkdocs.yml`, config docs
- API behavior: source modules and tests
- Existing doc standards: `docs/development/mkdocs.md`

Never rely on memory when repository evidence is available.

### 3. Write or Update Content

For each changed page:

- State purpose and audience clearly in the opening section
- Provide prerequisites and assumptions
- Add runnable command blocks
- Include expected output or success criteria
- Include troubleshooting notes for common failures
- Add cross-links to related guides and reference pages

### 4. Navigation and Discoverability

- Ensure new pages are included in `mkdocs.yml` nav.
- Keep page placement consistent with purpose:
  - User workflows: `docs/guide/`
  - Developer standards: `docs/development/`
  - API specifics: `docs/api/`
  - System planning and design: `docs/architecture/`
- Remove or fix stale links to moved or renamed content.

### 5. Validate and Gate

Run required checks:

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

If any check fails, fix documentation or content problems first.
Do not weaken lint, pre-commit, or build configuration.

## Data-Driven Application Documentation Pattern

When documenting data-focused apps, include these sections where relevant:

1. Data contract
   - Input sources, schema, required fields, null rules
   - Output schema and guarantees
2. Transformation logic
   - Processing steps and ordering
   - Deterministic assumptions such as sorting, deduping, or thresholds
3. Data quality checks
   - Row counts, uniqueness constraints, range checks, completeness
4. Reproducibility
   - Exact commands, config files, seed handling, environment requirements
5. Regression validation
   - Before and after comparison metrics and acceptable deltas

Use concrete examples and sample tables instead of abstract claims.

## Writing Standards

### Style

- Use direct, imperative language.
- Prefer short sentences and explicit nouns over pronouns.
- Avoid marketing language and vague promises.
- Explain tradeoffs when there are multiple valid paths.

### Examples

- Examples must be runnable with repository tooling.
- Keep examples minimal but complete.
- When showing files or paths, use real repository paths.
- Do not include fictional scripts or commands.

### Error Guidance

For each critical workflow, include:

- Symptom
- Likely root cause
- Concrete fix command or action

## Documentation Triggers Matrix

- New command or CLI flag:
  - Update `README.md`
  - Update relevant `docs/guide/*.md`
  - Update reference docs under `docs/api/` or developer docs as needed
- Config option or default change:
  - Update `docs/guide/configuration.md`
  - Update any examples containing old defaults
- Public API change:
  - Update API docs
  - Update usage examples
  - Update `CHANGELOG.md`
- Workflow or tooling change:
  - Update `CONTRIBUTING.md`
  - Update `docs/development/*.md`
- Architecture-level decision:
  - Add or update ADR and system docs per `docs/development/mkdocs.md`

## Absolute Prohibitions

- Never invent behavior that is not present in code, config, or tests.
- Never leave broken links or orphaned pages.
- Never bypass quality gates by changing lint, markdown, or mkdocs config.
- Never keep contradictory guidance in multiple files.
- Never document secrets, credentials, or private environment values.

## Done Criteria

Documentation work is complete only when all are true:

- Content is accurate and evidence-backed
- Navigation updated when needed
- `uv run mkdocs build --strict` passes
- Markdown lint passes via the pre-commit hook
- Relevant code-quality checks pass when behavior changed
- `CHANGELOG.md` updated for user-visible changes

## Completion Report Template

```markdown
## Documentation Update: PASSED | BLOCKED

### Scope

- [what changed]

### Files Updated

- [path]: [reason]

### Validation

- `uv run mkdocs build --strict`: pass/fail
- `uv run pre-commit run markdownlint --all-files`: pass/fail
- `make format`: pass/fail (if run)
- `make lint`: pass/fail (if run)
- `make test`: pass/fail (if run)

### Consistency Checks

- Nav updated: yes/no
- Broken links: yes/no
- Commands verified against repository: yes/no

### Residual Risks

- [open issues or follow-ups]
```
