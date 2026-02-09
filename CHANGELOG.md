# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project template structure
- Modern Python tooling (uv, ruff, mypy)
- Comprehensive documentation
- GitHub Actions workflows
- Pre-commit hooks configuration
- Data-driven development support
- Agentic AI development guidelines
- LLM instruction files

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

## [0.1.0] - YYYY-MM-DD

### Added
- Initial release
- Basic project structure
- Core functionality
- Tests and documentation
- CI/CD pipeline

---

## Release Notes Template

When creating a new release, copy this template:

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security fixes
```

---

## Guidelines for Maintaining the Changelog

### For Human Developers
- Update this file with each PR
- Add entries under `[Unreleased]` section
- Use present tense ("Add feature" not "Added feature")
- Group changes by type (Added, Changed, etc.)

### For AI Agents
When making changes, ALWAYS update this file:
1. Add entry under appropriate section in `[Unreleased]`
2. Be specific and descriptive
3. Reference issue numbers if applicable
4. Use format: `- Description (#issue-number)`

Example:
```markdown
## [Unreleased]

### Added
- Data validation function for user inputs (#42)
- Support for async operations in core module (#45)

### Fixed
- Edge case in parser for empty strings (#43)
```
