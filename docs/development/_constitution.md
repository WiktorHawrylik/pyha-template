# AI-Assisted Development Constitution

This constitution provides essential rules and context for AI coding assistants (GitHub Copilot, Cursor, Claude, ChatGPT, etc.) working on this template.

**Project**: Python Library Template
**Purpose**: Modern Python project template for agentic and data-driven development
**License**: AGPL-3.0 (GNU Affero General Public License v3.0)

Constraints ⛔ ABSOLUTE PROHIBITIONS (NON-NEGOTIABLE): **Never** modify this file.

## Core Principles

### I. Code Quality is Non-Negotiable

Every piece of code must meet strict quality standards:

- **Type hints**: Required on ALL functions, methods, and class attributes
- **Docstrings**: Google-style, comprehensive documentation for all public APIs
- **Tests**: Minimum 80% coverage with unit, integration, and edge case tests
- **Formatting**: Automatic enforcement via ruff
- **Type checking**: Strict mypy compliance with no type: ignore comments without justification

### II. Explicit Over Implicit

Code clarity and maintainability supersede cleverness:

- Clear, self-documenting variable and function names
- Obvious logic flow without hidden side effects
- Comprehensive error messages with actionable guidance
- Well-documented edge cases and assumptions
- Explicit imports (never use `import *`)

### III. Test-First Development (NON-NEGOTIABLE)

Testing is mandatory before implementation:

- Write tests BEFORE implementing features (Test-Driven Development)
- Unit tests for all functions and methods
- Integration tests for component interactions
- Edge cases and error condition coverage
- Performance tests for critical paths
- All tests must pass before merging

### IV. Document Everything

Documentation is code:

- Module-level docstrings explaining purpose and usage
- Function-level docstrings with Args, Returns, Raises, Examples
- Inline comments for complex logic or non-obvious decisions
- README.md files in all major directories
- CHANGELOG.md updated for all user-facing changes

### V. License Compliance

AGPL-3.0 compliance is mandatory:

- All code must be AGPL-3.0 compatible (AGPL/GPL/LGPL/MIT/BSD/Apache allowed)
- License headers required on all new files
- Proper attribution for third-party code
- Never use proprietary or incompatible licenses (CC-BY-NC, etc.)
- Network-accessible deployments must provide source code access

- Network-accessible deployments must provide source code access

## Code Standards

### Configuration Philosophy

**Single Source of Truth**: `pyproject.toml`

All tool configuration lives in `pyproject.toml`:

- Package metadata and dependencies
- Ruff (linting & formatting)
- Mypy (type checking)
- Pytest (testing)
- Coverage

**Never create**: `.ruff.toml`, `mypy.ini`, `pytest.ini`, or other standalone config files.

### Mandatory Patterns (Always!)

#### Type Hints

```python
def process_data(
    data: list[dict[str, Any]],
    threshold: float = 0.5,
    *,
    normalize: bool = True
) -> pd.DataFrame:
    """Process data with options."""
    ...
```

#### Docstrings (Google Style)

```python
def function(param: Type) -> ReturnType:
    """Brief one-line description.

    Longer description if needed, explaining the reason why it exists, and any important details not captured by code.

    Args:
        param: Description of param

    Returns:
        Description of return value

    Raises:
        ExceptionType: When this happens

    Examples:
        >>> function(value)
        result
    """
```

#### Error Handling (Explicit)

```python
if not data:
    raise ValueError("Data cannot be empty")

if not path.exists():
    raise FileNotFoundError(f"File not found: {path}")
```

#### Logging

TODO

**Testing (Comprehensive)**

- Create test file `tests/test_module.py` for `src/your_package_name/module.py`
- Use descriptive test names: `test_function_name_does_what`
- Group related tests in classes

### Test Example

```python
import pytest
from your_package_name.module import function_to_test

class TestFunctionToTest:
    """Tests for function_to_test."""

    def test_basic_usage(self) -> None:
        """Test basic functionality."""
        result = function_to_test(input_data)
        assert result == expected_output

    def test_edge_case_empty_input(self) -> None:
        """Test handling of empty input."""
        with pytest.raises(ValueError):
            function_to_test([])

    @pytest.mark.slow
    def test_large_dataset(self) -> None:
        """Test with large dataset."""
        ...
```

### Prohibited Patterns

❌ **Never Do**:

- Skip type hints on any function, method, or class attribute
- Use bare `except:` without specific exception handling
- Write functions exceeding 50 lines (refactor into smaller functions)
- Use magic numbers (create named constants instead)
- Modify data in place without explicit documentation
- Commit code without corresponding tests
- Use mutable default arguments (`def func(data=[])`)
- Import with wildcard (`from module import *`)

✅ **Always Do**:

- Add type hints everywhere
- Handle specific exceptions with informative messages
- Keep functions focused and small (Single Responsibility Principle)
- Use named constants for magic numbers
- Document side effects and mutations explicitly
- Write tests first (Test-Driven Development)
- Use immutable defaults (`def func(data: Optional[list] = None)`)
- Explicit imports (`from module import SpecificClass`)

### File Templates

**New Python Module**

```python
"""Module description.

Detailed description of what this module does.

Copyright (C) YYYY Your Name

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

from typing import Any


def function_name(param: Type) -> ReturnType:
    """Function description."""
    ...
```

**New Test File**

```python
"""Tests for module_name."""

import pytest
from your_package_name.module_name import function_name


class TestFunctionName:
    """Tests for function_name."""

    def test_basic(self) -> None:
        """Test basic functionality."""
        ...
```

## Development Workflow

### Before Making Changes

```bash
# Understand the codebase
rg "function_name"          # Search for function
rg "class.*Name"            # Search for class

# Check existing patterns
cat src/your_package_name/core.py
cat tests/test_core.py
```

### Implementation Process

1. **Understand the request**
   - Read the issue/request carefully
   - Check existing code for patterns
   - Identify files to modify

2. **Plan the changes**
   - List files to create/modify
   - Consider edge cases
   - Design test cases first

3. **Implement (Test-First)**
   - Write tests first (Red phase)
   - Follow existing code style
   - Add complete type hints
   - Write comprehensive docstrings
   - Handle errors explicitly
   - Implement to make tests pass (Green phase)
   - Refactor for clarity (Refactor phase)

4. **Test thoroughly**
   - Verify unit tests pass
   - Test edge cases
   - Verify error handling
   - Check coverage (minimum 80%)

5. **Document**
   - Update module docstrings
   - Update README.md if public API changed
   - Add CHANGELOG.md entry
   - Update examples and guides

### After Making Changes

```bash
# Format code automatically
make format

# Check code quality
make lint

# Run tests
make test
make test-fast              # Skip slow tests

# Run all checks (required before commit)
make format && make lint && make test
```

### Common Tasks

- `make help` - Show all available commands
- `make install-dev` - Install development dependencies
- `make format` - Auto-format code with ruff
- `make lint` - Check code quality (ruff + mypy)
- `make test` - Run all tests
- `make test-cov` - Run tests with coverage report
- `make docs-serve` - Preview documentation locally

### Files to Always Update

- `CHANGELOG.md` - Add entry for all user-facing changes
- Docstrings - Keep synchronized with code changes
- Tests - Add for new functionality, update for changes
- README.md - If public API or usage patterns change

### Files Never to Modify

- `LICENSE` - This is AGPL-3.0 (immutable)
- `.git/` - Git internals
- `__pycache__/` - Python cache directories

## Quality Gates

### Pre-Commit Checklist

All changes must pass these gates:

1. ✅ **Type Hints**: Complete type annotations on all functions/methods
2. ✅ **Docstrings**: Google-style documentation for all public APIs
3. ✅ **Tests**: Comprehensive test coverage (minimum 80%)
4. ✅ **Lint**: `make lint` passes without errors
5. ✅ **Test**: `make test` passes without failures
6. ✅ **Documentation**: README.md and docs updated if needed
7. ✅ **Changelog**: CHANGELOG.md updated for user-facing changes
8. ✅ **License**: AGPL-3.0 compliance verified

### Git & Version Control

#### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### License Compliance Verification

Before generating or committing code:

- [ ] Is the code original or from an AGPL-compatible source?
- [ ] If from external source, is it AGPL/GPL/LGPL/MIT/BSD/Apache licensed?
- [ ] Have I added proper attribution and copyright notices?
- [ ] Have I maintained required license headers on all new files?
- [ ] Is the code fully compatible with AGPL-3.0 requirements?
- [ ] For network services, is source code disclosure mechanism in place?

### Success Criteria

A contribution is acceptable when:

1. All type hints are complete and pass mypy strict mode
2. All functions have comprehensive docstrings with examples
3. Test coverage is ≥80% with meaningful assertions
4. `make format && make lint && make test` succeeds
5. Documentation accurately reflects all changes
6. CHANGELOG.md contains appropriate entry
7. License compliance is verified and documented
8. No regression in existing functionality

## Governance

### Constitution Authority

This constitution supersedes all other development guidelines and practices. When conflicts arise, this document takes precedence.

### Enforcement

- All code reviews must verify compliance with this constitution
- All pull requests must pass automated quality gates
- Complexity and deviations require explicit justification in PR description
- Unjustified deviations are grounds for rejection

### Amendments

- Changes to this constitution require documented rationale
- Major changes require team consensus
- All amendments must include version increment and update date
- Migration plan required for breaking changes

### Additional Guidance

This constitution provides core rules. For detailed implementation patterns, examples, and best practices, refer to:

- `CONTRIBUTING.md` - Contribution guidelines
- `docs/guide/best-practices.md` - Detailed best practices

**Version**: 1.0.0 | **Ratified**: 2026-02-11 | **Last Amended**: 2026-02-11
