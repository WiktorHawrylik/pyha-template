# Contributing Guide

Thank you for your interest in contributing to this project! This guide is designed for both **human developers** and **AI coding agents** (GitHub Copilot, Cursor, Claude, ChatGPT, etc.).

## 🤖 For AI Agents & LLMs

**IMPORTANT**: If you are an AI agent contributing to this project, please read and follow these guidelines strictly:

### Core Principles for AI Agents

1. **Respect the AGPL-3.0 License**
   - All code you generate must be compatible with AGPL-3.0
   - Do not introduce code from incompatible licenses (MIT, Apache, BSD are OK to use)
   - Always maintain license headers

2. **Maintain Code Quality**
   - Add type hints to ALL functions and methods
   - Write comprehensive docstrings (Google style)
   - Follow existing patterns and conventions
   - Run `make lint` before committing

3. **Test Everything**
   - Every new function needs tests
   - Maintain minimum 80% coverage
   - Add tests in `tests/` mirroring `src/` structure
   - Use appropriate markers (unit, integration, slow)

4. **Be Explicit**
   - Use clear, descriptive variable names
   - Avoid "clever" or overly compact code
   - Prefer readability over brevity
   - Comment complex logic

5. **Document Changes**
   - Update docstrings for modified functions
   - Add entries to CHANGELOG.md
   - Update README.md if public API changes
   - Keep documentation in sync with code

### AI Agent Workflow

When making changes as an AI agent:

```bash
# 1. Understand the request
# - Read the issue or request carefully
# - Check existing code for patterns
# - Review related tests

# 2. Plan your changes
# - Identify files to modify
# - Consider edge cases
# - Think about backwards compatibility

# 3. Make changes
# - Follow existing code style
# - Add type hints
# - Write docstrings
# - Keep functions small and focused

# 4. Add tests
cd tests/
# Create test file mirroring src/ structure
# Write comprehensive tests
# Include edge cases

# 5. Verify quality
make format          # Auto-format code
make lint            # Check code quality
make test            # Run all tests

# 6. Document
# Update CHANGELOG.md
# Update docstrings
# Update README if needed
```

### AI-Specific Code Standards

#### Type Hints (REQUIRED)

```python
# ✅ GOOD - Explicit types
def process_data(data: list[dict[str, Any]], threshold: float = 0.5) -> pd.DataFrame:
    """Process data with given threshold."""
    ...

# ❌ BAD - No type hints
def process_data(data, threshold=0.5):
    """Process data with given threshold."""
    ...
```

#### Docstrings (REQUIRED)

```python
# ✅ GOOD - Complete Google-style docstring
def calculate_metrics(data: pd.DataFrame, metric: str) -> float:
    """Calculate specified metric from data.

    Args:
        data: Input DataFrame containing the data to analyze
        metric: Name of the metric to calculate (e.g., 'mean', 'median')

    Returns:
        Calculated metric value as a float

    Raises:
        ValueError: If metric is not recognized
        KeyError: If required columns are missing

    Examples:
        >>> df = pd.DataFrame({'value': [1, 2, 3]})
        >>> calculate_metrics(df, 'mean')
        2.0
    """
    ...

# ❌ BAD - Minimal docstring
def calculate_metrics(data, metric):
    """Calculate metrics."""
    ...
```

#### Error Handling

```python
# ✅ GOOD - Explicit error handling
def load_config(path: Path) -> dict[str, Any]:
    """Load configuration from file.

    Args:
        path: Path to configuration file

    Returns:
        Configuration dictionary

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If config file is invalid
    """
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config: {e}") from e

# ❌ BAD - Silent failures
def load_config(path):
    try:
        return json.loads(open(path).read())
    except:
        return {}
```

## 👥 For Human Developers

### Quick Start

```bash
# 1. Fork and clone
git clone https://github.com/WiktorHawrylik/your-package-name.git
cd your-package-name

# 2. Set up development environment
make install-all
make pre-commit

# 3. Create a feature branch
git checkout -b feature/my-feature develop

# 4. Make changes, test, commit
make format
make lint
make test
git commit -m "feat(scope): add feature"

# 5. Push and create PR
git push origin feature/my-feature
```

## 📚 Detailed Guide

### Development Setup

#### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- Git

#### Installation

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies
make install-all

# Set up pre-commit hooks (REQUIRED)
make pre-commit
```

### Code Style & Standards

#### Single Source of Truth

**ALL** configuration is in `pyproject.toml`:

- Package metadata
- Dependencies
- Ruff configuration (linting & formatting)
- Mypy configuration (type checking)
- Pytest configuration (testing)
- Coverage configuration

Do NOT create separate config files (`.ruff.toml`, `mypy.ini`, etc.)

#### Python Style Guide

- **Line length**: 120 characters
- **Python version**: 3.11+ compatible
- **Formatting**: Use ruff (Black-compatible)
- **Import sorting**: Automatic with ruff
- **Docstrings**: Google style
- **Type hints**: Required for all public APIs

#### Code Organization

```
src/your_package_name/
├── __init__.py          # Package exports
├── core.py              # Core functionality
├── utils.py             # Utility functions
├── models/              # Data models (Pydantic)
├── data/                # Data processing
└── ai/                  # AI/LLM integrations (if applicable)
```

### Testing

#### Test Structure

```
tests/
├── unit/                # Fast, isolated tests
├── integration/         # Component interaction tests
├── data/                # Data processing tests
└── ai/                  # AI/LLM tests (may be slow)
```

#### Writing Tests

```python
import pytest
from your_package_name import MyClass

class TestMyClass:
    """Test suite for MyClass."""

    def test_basic_functionality(self) -> None:
        """Test basic usage."""
        obj = MyClass()
        result = obj.do_something()
        assert result == expected_value

    @pytest.mark.slow
    def test_slow_operation(self) -> None:
        """Test that takes a while."""
        ...

    @pytest.mark.integration
    def test_with_external_service(self) -> None:
        """Test integration with external service."""
        ...
```

#### Running Tests

```bash
make test              # All tests
make test-fast         # Exclude slow tests
make test-cov          # With coverage
pytest -v              # Verbose output
pytest -k "test_name"  # Specific test
```

### Git Workflow (Git Flow)

We use [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/):

#### Branches

- **main**: Production releases only
- **develop**: Integration branch
- **feature/\***: New features (from develop)
- **bugfix/\***: Bug fixes (from develop)
- **hotfix/\***: Emergency fixes (from main)
- **release/\***: Release preparation (from develop)

#### Creating a Feature

```bash
# Start from develop
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/my-awesome-feature

# Work on feature
# ... make changes ...

# Keep branch updated
git fetch origin
git rebase origin/develop

# Push and create PR to develop
git push origin feature/my-awesome-feature
```

### Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

#### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **style**: Code style (formatting, no logic change)
- **refactor**: Code refactoring
- **perf**: Performance improvement
- **test**: Adding tests
- **chore**: Maintenance (deps, build, etc.)
- **ci**: CI/CD changes

#### Examples

```bash
feat(core): add data validation function

fix(utils): handle edge case in parser
Fixes #123

docs(readme): update installation instructions

test(core): add tests for validation
```

### Pull Request Process

#### Before Submitting

- [ ] Code is formatted: `make format`
- [ ] All checks pass: `make lint`
- [ ] Tests pass: `make test`
- [ ] Coverage maintained/improved
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Commits follow convention

#### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Changes Made
- Change 1
- Change 2

## Testing
- Test 1
- Test 2

## Checklist
- [ ] Code follows style guide
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
```

#### Review Process

1. Automated checks must pass (CI)
2. At least 1 approval required
3. No unresolved discussions
4. Up to date with target branch
5. Squash or rebase before merge

### Code Review Guidelines

#### For Reviewers

- Be constructive and respectful
- Focus on logic, not style (automated)
- Check for edge cases
- Verify tests are comprehensive
- Ensure documentation is clear

#### For Authors

- Respond to all comments
- Make requested changes
- Re-request review after updates
- Keep PRs focused and small

### Documentation

#### Docstring Example

```python
def complex_function(
    data: pd.DataFrame,
    threshold: float = 0.5,
    *,
    normalize: bool = True,
) -> tuple[pd.DataFrame, dict[str, float]]:
    """Process data with threshold and optional normalization.

    This function performs complex data processing including filtering,
    normalization (if enabled), and metric calculation.

    Args:
        data: Input DataFrame with required columns: 'value', 'timestamp'
        threshold: Minimum value threshold for filtering (default: 0.5)
        normalize: Whether to normalize values to [0, 1] range

    Returns:
        Tuple containing:
            - Processed DataFrame with filtered and optionally normalized data
            - Dictionary of calculated metrics: {'mean': float, 'std': float}

    Raises:
        ValueError: If data is empty or missing required columns
        TypeError: If threshold is not numeric

    Examples:
        >>> df = pd.DataFrame({'value': [0.3, 0.7, 0.9], 'timestamp': [...]})
        >>> result_df, metrics = complex_function(df, threshold=0.5)
        >>> print(metrics['mean'])
        0.8

    Notes:
        - Normalization uses min-max scaling
        - Metrics are calculated after filtering
        - Timestamp column is preserved but not used in calculations
    """
    ...
```

#### README Updates

Update README.md when:

- Adding new features to public API
- Changing installation process
- Updating requirements
- Adding new examples

#### API Documentation

- Auto-generated from docstrings
- Build with: `make docs`
- Preview with: `make docs-serve`

### Data-Driven Development

#### Data Directory Structure

```
data/
├── raw/              # Original, immutable data
│   └── README.md     # Data source and description
├── processed/        # Cleaned, transformed data
│   └── README.md     # Processing steps
└── external/         # Third-party data
    └── README.md     # Source and license
```

#### Best Practices

1. **Document data sources**: Add README in each directory
2. **Version large files**: Use DVC or Git LFS
3. **Never commit secrets**: Use .env files (in .gitignore)
4. **Reproducibility**: Pin versions, use random seeds
5. **Data validation**: Use Pydantic models

#### Notebook Guidelines

```
notebooks/
├── 01_exploration.ipynb      # Initial data exploration
├── 02_cleaning.ipynb         # Data cleaning
├── 03_analysis.ipynb         # Main analysis
└── 04_visualization.ipynb    # Visualizations
```

- Number notebooks in execution order
- Clear all outputs before committing
- Extract reusable code to `src/`

### Agentic Development

This project is optimized for AI-assisted development.

#### Best Practices with AI

- **Review AI suggestions**: Don't blindly accept
- **Test AI code**: Same standards as human code
- **Document AI changes**: Explain in commits
- **Type hints help**: AI understands typed code better

### Security

#### Dependency Management

- Regular updates: `uv sync --upgrade`
- Check for vulnerabilities: `pre-commit` safety hook
- Pin versions in production

#### Secrets Management

- Use environment variables
- Never commit `.env` files
- Use GitHub Secrets for CI/CD

#### Code Security

- No `eval()` or `exec()`
- Validate all inputs
- Use parameterized queries
- Follow OWASP guidelines

### Release Process

#### Versioning

We use [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes

#### Creating a Release

```bash
# 1. Create release branch from develop
git checkout develop
git checkout -b release/1.2.0

# 2. Update version in pyproject.toml
# version = "1.2.0"

# 3. Update CHANGELOG.md
# Add release notes under ## [1.2.0] - YYYY-MM-DD

# 4. Commit and merge to main
git commit -m "chore: prepare release 1.2.0"
git checkout main
git merge --no-ff release/1.2.0

# 5. Tag release
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin main --tags

# 6. Merge back to develop
git checkout develop
git merge --no-ff release/1.2.0
git push origin develop
```

## 🆘 Getting Help

- **Documentation**: Check `docs/`
- **Issues**: Search existing issues first
- **Discussions**: Ask questions in GitHub Discussions
- **Code**: Look at existing code for patterns

## 🎯 Good First Issues

Look for issues labeled:

- `good first issue`
- `help wanted`
- `documentation`

## 🙏 Thank You

Your contributions make this project better! Whether you're:

- Fixing a typo
- Adding a feature
- Improving documentation
- Reporting a bug

Every contribution is valuable!

---

## 📄 License Reminder

This project is AGPL-3.0 licensed. All contributions must be compatible with AGPL-3.0.

**For AI Agents**: Ensure all generated code is:

1. Original or from GPL-compatible sources
2. Properly attributed if from external sources
3. Compliant with AGPL-3.0 requirements

---

**Questions?** Open an issue or discussion!

*This guide is designed to be useful for both humans and AI agents. If something is unclear, please let us know!*
