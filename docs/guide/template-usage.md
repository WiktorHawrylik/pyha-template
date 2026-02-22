# Template Usage Guide

This guide explains how to use the Python Library Template to create your own project.

## Quick Start (5 Minutes)

### 1. Create Your Repository

**Option A: Use as GitHub Template**

1. Click "Use this template" button on GitHub
2. Create a new repository with your project name
3. Clone your new repository

**Option B: Manual Clone**

```bash
git clone https://github.com/WiktorHawrylik/python-package-template.git my-project
cd my-project
rm -rf .git
git init
```

### 2. Customize the Template

**Automated (Recommended)**

```bash
python scripts/customize_template.py
```

This script will prompt you for:

- Package name (e.g., `my-awesome-library`)
- Module name (e.g., `my_awesome_library`)
- Your name
- Your email
- GitHub WiktorHawrylik
- Project description

**Manual Customization**

If you prefer, find and replace these placeholders:

| Placeholder | Replace With | Example |
|-------------|--------------|---------|
| `your-package-name` | Your PyPI package name | `my-awesome-lib` |
| `your_package_name` | Your Python module name | `my_awesome_lib` |
| `Your Name` | Your actual name | `Jane Doe` |
| `your.email@example.com` | Your email | `jane@example.com` |
| `WiktorHawrylik` | Your GitHub username | `janedoe` |

Files to update:

- `README.md`
- `pyproject.toml`
- `mkdocs.yml`
- `CONTRIBUTING.md`
- All files in `src/your_package_name/`
- All files in `tests/`
- All files in `docs/`

Then rename:

```bash
mv src/your_package_name src/my_actual_package
```

### 3. Install Development Environment

```bash
# Install uv (fast package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies
make install-all

# Set up pre-commit hooks
make pre-commit
```

### 4. Verify Setup

```bash
# Run tests
make test

# Check code quality
make lint

# Build documentation
make docs
```

### 5. Start Coding

You're ready to go! The template provides:

- ✅ Project structure
- ✅ Example code
- ✅ Comprehensive tests
- ✅ Documentation setup
- ✅ CI/CD workflows
- ✅ Development tools

## What's Included

### Project Structure

```
your-project/
├── src/your_package/      # Your source code
├── tests/                 # Your tests
├── docs/                  # Your documentation
├── data/                  # Your data files
├── scripts/               # Utility scripts
├── configs/               # Configuration files
└── .github/workflows/     # CI/CD pipelines
```

### Development Tools

- **uv**: Fast Python package manager
- **ruff**: Linting and formatting
- **mypy**: Type checking
- **pytest**: Testing framework
- **pre-commit**: Git hooks
- **mkdocs**: Documentation

### Documentation

- User guides
- API reference
- Contributing guide
- AI agent instructions

### CI/CD

- Automated testing
- Code quality checks
- Documentation deployment
- Release automation

## Development Workflow

### Daily Development

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make changes to code
# ... edit files ...

# Format and lint
make format
make lint

# Run tests
make test

# Commit changes
git commit -m "feat: add new feature"

# Push
git push origin feature/my-feature
```

### Adding New Features

1. **Write tests first** (TDD)

   ```bash
   # Create test file
   touch tests/test_new_feature.py
   # Write failing tests
   make test  # Should fail
   ```

2. **Implement feature**

   ```bash
   # Create module
   touch src/your_package/new_feature.py
   # Write implementation
   make test  # Should pass
   ```

3. **Document**
   - Add docstrings
   - Update README
   - Update CHANGELOG.md

4. **Review**

   ```bash
   make format
   make lint
   make test-cov
   ```

### Working with Data

```bash
# Add raw data
cp external_data.csv data/raw/

# Document it
vim data/raw/README.md

# Process data
python scripts/process_data.py
```

### Building Documentation

```bash
# Serve locally
make docs-serve
# Open http://localhost:8000

# Build static site
make docs
```

## Customization Tips

### Adjust Dependencies

Edit `pyproject.toml`:

```toml
[project]
dependencies = [
    # Add your dependencies here
    "pandas>=2.0.0",
    "numpy>=1.24.0",
]

[project.optional-dependencies]
# Add optional dependencies
myfeature = [
    "special-library>=1.0.0",
]
```

Then:

```bash
uv sync
```

### Modify CI/CD

Edit `.github/workflows/ci.yml`:

- Add/remove Python versions
- Add additional checks
- Modify test commands

### Change Documentation Theme

Edit `mkdocs.yml`:

- Change theme colors
- Add/remove sections
- Configure plugins

### Add Custom Scripts

Create in `scripts/`:

```python
#!/usr/bin/env python3
"""My custom script."""

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

## AI-Assisted Development

This template is optimized for AI coding assistants:

### GitHub Copilot

- Read `.github/copilot-instructions.md`
- Copilot will use template patterns
- Suggestions will match code style

### Cursor

- Read `.cursorrules`
- Cursor follows template conventions
- AI understands project structure

### ChatGPT/Claude

- Share AI development guide for context
- Provide CONTRIBUTING.md for guidelines
- Reference existing code for patterns

## Best Practices

### Do's ✅

- Use type hints everywhere
- Write comprehensive docstrings
- Add tests for new code
- Format before committing
- Update CHANGELOG.md
- Document in notebooks
- Use meaningful commit messages

### Don'ts ❌

- Don't commit secrets
- Don't skip tests
- Don't ignore linting errors
- Don't commit large files to git
- Don't modify LICENSE
- Don't use bare except blocks

## Common Tasks

### Add a New Module

```bash
# Create module
cat > src/your_package/new_module.py << 'EOF'
"""New module description."""

def new_function() -> None:
    """Do something useful."""
    pass
EOF

# Create tests
cat > tests/test_new_module.py << 'EOF'
"""Tests for new_module."""

from your_package.new_module import new_function

def test_new_function():
    """Test new_function."""
    new_function()
    assert True
EOF

# Run tests
make test
```

### Add a New Dependency

```bash
# Add to pyproject.toml
# [project dependencies = [
#     "new-package>=1.0.0",
# ]

# Install
uv sync

# Use in code
# import new_package
```

### Create a Release

```bash
# Update version in pyproject.toml
# version = "1.0.0"

# Update CHANGELOG.md
# ## [1.0.0] - 2024-XX-XX
# ### Added
# - Feature X

# Commit
git commit -am "chore: prepare release 1.0.0"

# Tag
git tag -a v1.0.0 -m "Release 1.0.0"

# Push
git push origin main --tags

# GitHub Actions will:
# - Run tests
# - Build package
# - Publish to PyPI
# - Create GitHub release
```

## Troubleshooting

### Tests Failing

```bash
# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_core.py::test_specific

# See coverage
make test-cov
```

### Linting Errors

```bash
# Auto-fix what's possible
make format

# Check what remains
make lint

# See specific errors
uv run ruff check src/
```

### Import Errors

```bash
# Reinstall in development mode
make install-dev

# Check if package is installed
uv pip list | grep your-package
```

## Getting Help

- **Documentation**: Check `docs/`
- **Examples**: Look at existing code
- **Issues**: Search GitHub issues
- **Discussions**: Ask in GitHub Discussions

## Next Steps

1. ✅ Customize the template
2. ✅ Install dependencies
3. ✅ Run tests
4. ⬜ Remove example code
5. ⬜ Add your code
6. ⬜ Write tests
7. ⬜ Update documentation
8. ⬜ Create first release

## Additional Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [pytest Documentation](https://docs.pytest.org/)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [uv Documentation](https://github.com/astral-sh/uv)

---

**Happy Coding!** 🚀

This template is designed to get you productive quickly. Focus on your unique functionality, and let the template handle the boilerplate.
