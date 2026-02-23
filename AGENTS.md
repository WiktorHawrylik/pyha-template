# Agentic Development Rules

These rules apply to LLMs working in this repository.

## Mandatory Guardrails

- Never modify protected files

### Protected files

- `AGENTS.md`
- `.pre-commit-config.yaml`
- `docs/development/_constitution.md`
- `LICENSE`

## Definition of done

Before opening or merging a change, confirm all of the following:

- Make sure AGPL-3.0 compliance audit passes
- Documentation is up to date and follow guidelines
- Tests are up to date and follow guidelines
- Branch name, commit message and PR title follow guidelines

## Skills

A skill is a set of local instructions stored in a `SKILL.md` file.

### Available skills

- license-audit: Run AGPL-3.0 compliance audits (headers, dependency license classification, and third-party attribution checks). Use when asked to perform or verify license compliance. (file: .agents/skills/license-audit/SKILL.md)

## Comprehensive guidelines

Use comprehensive guidelines to solve any ambiguities, see:

- **[AI Development Guide](docs/development/_constitution.md)** - Detailed AI coding patterns
- **[Template Usage](docs/guide/template-usage.md)** - How to use this template
- **[License Compliance](docs/development/license-audit.md)** - AGPL-3.0 requirements
- **[Contributing Guide](CONTRIBUTING.md)** - Full contribution guidelines

## License Compliance

This project is AGPL-3.0. All contributions must be compatible. See [License Compliance Guide](docs/development/license-audit.md).

---

**Remember**: Quality over speed. Write clear, tested, documented code.
