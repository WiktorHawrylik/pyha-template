# AI Agent README

## For AI Coding Assistants

This file provides essential context for AI coding assistants (GitHub Copilot, Cursor, Claude, ChatGPT, etc.) working on this template.

## Project Identity

**Name**: Python Library Template  
**Purpose**: Modern Python project template for agentic and data-driven development  
**License**: AGPL-3.0 (GNU Affero General Public License v3.0)  
**Based On**: [urzad-regulacji-energetyki](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki)  

## Core Principles

### 1. Code Quality is Non-Negotiable
- **Type hints**: Required on ALL functions and methods
- **Docstrings**: Google-style, comprehensive
- **Tests**: Minimum 80% coverage
- **Formatting**: Automatic with ruff
- **Type checking**: Strict mypy

### 2. Explicit Over Implicit
- Clear variable names
- Obvious logic flow
- Comprehensive error messages
- Well-documented edge cases

### 3. Test Everything
- Unit tests for all functions
- Integration tests for components
- Edge cases and error conditions
- Performance tests for critical paths

### 4. Document Everything
- Module-level docstrings
- Function-level docstrings
- Inline comments for complex logic
- README files in all directories

### 5. License Compliance
- All code must be AGPL-3.0 compatible
- Maintain license headers
- Attribute third-party code
- Never use incompatible licenses

## Project Structure Quick Reference

```
.
├── src/your_package_name/    # Source code (rename for your project)
│   ├── __init__.py           # Package exports
│   ├── core.py               # Core functionality
│   └── utils.py              # Utility functions
├── tests/                    # Tests (mirror src/ structure)
│   ├── test_core.py
│   └── test_utils.py
├── docs/                     # MkDocs documentation
│   ├── index.md
│   ├── guide/                # User guides
│   └── api/                  # API reference (auto-generated)
├── data/                     # Data files
│   ├── raw/                  # Original data
│   ├── processed/            # Processed data
│   └── external/             # Third-party data
├── notebooks/                # Jupyter notebooks
├── scripts/                  # Utility scripts
├── configs/                  # Configuration files
├── .github/
│   ├── workflows/            # CI/CD workflows
│   └── copilot-instructions.md  # Instructions for you!
├── pyproject.toml            # **SINGLE SOURCE OF TRUTH** for config
├── Makefile                  # Development automation
├── .cursorrules              # Cursor AI rules
├── LICENSE                   # AGPL-3.0
└── LICENSE-AI-NOTICE.md      # License guide for AI agents
```

## Configuration Philosophy

**Single Source of Truth**: `pyproject.toml`

All tool configuration lives in `pyproject.toml`:
- Package metadata
- Dependencies
- Ruff (linting & formatting)
- Mypy (type checking)
- Pytest (testing)
- Coverage

**Never create**: `.ruff.toml`, `mypy.ini`, `pytest.ini`, etc.

## Common Tasks

### Before Making Changes
```bash
# Understand the codebase
rg "function_name"          # Search for function
rg "class.*Name"            # Search for class

# Check existing patterns
cat src/your_package_name/core.py
cat tests/test_core.py
```

### While Making Changes
```bash
# Format code automatically
make format

# Check code quality
make lint

# Run tests
make test
make test-fast              # Skip slow tests
```

### After Making Changes
```bash
# Run all checks
make format && make lint && make test

# Update documentation
# - Update docstrings
# - Update README.md if needed
# - Update CHANGELOG.md

# Commit with conventional commits
git commit -m "feat(module): add new feature"
```

## Code Patterns to Follow

### Type Hints (Always!)
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

### Docstrings (Google Style)
```python
def function(param: Type) -> ReturnType:
    """Brief one-line description.

    Longer description if needed.

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

### Error Handling (Explicit)
```python
if not data:
    raise ValueError("Data cannot be empty")

if not path.exists():
    raise FileNotFoundError(f"File not found: {path}")
```

### Testing (Comprehensive)
```python
class TestFunction:
    """Tests for function."""

    def test_basic_case(self) -> None:
        """Test basic usage."""
        result = function(input)
        assert result == expected

    def test_edge_case(self) -> None:
        """Test edge case."""
        with pytest.raises(ValueError):
            function(invalid_input)
```

## What to Avoid

❌ **Don't**:
- Skip type hints
- Use bare `except:`
- Write functions > 50 lines
- Use magic numbers
- Modify data in place without documenting
- Commit code without tests
- Use mutable default arguments
- Import with `*`

✅ **Do**:
- Add type hints everywhere
- Handle specific exceptions
- Keep functions focused and small
- Use named constants
- Document side effects
- Write tests first (TDD)
- Use immutable defaults
- Explicit imports

## Development Workflow for AI Agents

1. **Understand the request**
   - Read the issue/request carefully
   - Check existing code for patterns
   - Identify files to modify

2. **Plan the changes**
   - List files to create/modify
   - Consider edge cases
   - Think about tests

3. **Implement**
   - Follow existing code style
   - Add complete type hints
   - Write comprehensive docstrings
   - Handle errors explicitly

4. **Test**
   - Write unit tests
   - Test edge cases
   - Verify error handling
   - Check coverage

5. **Document**
   - Update module docstrings
   - Update README if needed
   - Add CHANGELOG entry
   - Update examples

6. **Verify**
   ```bash
   make format
   make lint
   make test
   ```

## License Compliance Checklist

Before generating code:
- [ ] Is the code original or from a compatible source?
- [ ] If from external source, is it AGPL/GPL/LGPL/MIT/BSD/Apache?
- [ ] Have I added proper attribution?
- [ ] Have I maintained license headers?
- [ ] Is the code compatible with AGPL-3.0?

## File Templates

### New Python Module
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

### New Test File
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

## Quick Reference

### Commands
- `make help` - Show all available commands
- `make install-dev` - Install development dependencies
- `make format` - Format code
- `make lint` - Check code quality
- `make test` - Run tests
- `make docs-serve` - Preview documentation

### Files to Always Update
- `CHANGELOG.md` - Add entry for changes
- Docstrings - Keep in sync with code
- Tests - Add for new functionality
- README.md - If public API changes

### Never Modify
- `LICENSE` - This is AGPL-3.0
- `.git/` - Git internals
- `__pycache__/` - Python cache

## Questions?

- Read: `.github/copilot-instructions.md`
- Read: `.cursorrules`
- Read: `CONTRIBUTING.md`
- Check: Existing code for patterns

## Success Criteria

Your contribution is successful when:
1. ✅ Code has complete type hints
2. ✅ All functions have docstrings
3. ✅ Tests are comprehensive
4. ✅ `make lint` passes
5. ✅ `make test` passes
6. ✅ Documentation is updated
7. ✅ CHANGELOG.md is updated
8. ✅ License compliance is verified

---

**Remember**: This template prioritizes clarity, quality, and maintainability. When in doubt, be more explicit, more documented, and more tested.
