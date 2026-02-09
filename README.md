# Python Library Template 🚀

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](http://mypy-lang.org/)

> **A modern Python library template optimized for agentic AI development and data-driven workflows**

This template is designed for rapid project development using AI assistants like GitHub Copilot, Cursor, and Claude. It follows best practices from the [urzad-regulacji-energetyki](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki) project and is specifically structured to help AI coding agents understand and contribute effectively.

## 🎯 Why This Template?

### For Developers
- **Zero Configuration**: Pre-configured with modern Python tooling (uv, ruff, mypy)
- **Best Practices**: Git Flow, semantic versioning, comprehensive testing
- **Fast Development**: Makefile automation, pre-commit hooks, CI/CD ready
- **Type Safety**: Full mypy strict mode for catching bugs early

### For AI Agents & LLMs
- **Clear Structure**: Consistent, predictable project layout
- **Explicit Guidelines**: Comprehensive documentation and coding standards
- **Data-Driven Ready**: Built-in support for data science workflows
- **Agentic Patterns**: Designed for AI-assisted development workflows

## 📦 Quick Start

### 1. Use This Template

Click the "Use this template" button on GitHub or:

```bash
# Clone this repository
git clone https://github.com/your-username/python-library-template.git my-new-project
cd my-new-project

# Initialize your own git repository
rm -rf .git
git init
git add .
git commit -m "Initial commit from template"
```

### 2. Customize for Your Project

Replace all instances of placeholder text:
- `your-package-name` → Your PyPI package name (kebab-case)
- `your_package_name` → Your Python module name (snake_case)
- `Your Name` → Your actual name
- `your.email@example.com` → Your email
- `your-username` → Your GitHub username

Quick find and replace:
```bash
# macOS/Linux
find . -type f -name "*.py" -o -name "*.toml" -o -name "*.md" | xargs sed -i 's/your_package_name/my_actual_package/g'
find . -type f -name "*.toml" -o -name "*.md" | xargs sed -i 's/your-package-name/my-actual-package/g'

# Or use your AI assistant to do this!
```

### 3. Set Up Development Environment

```bash
# Install uv (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies
make install-all

# Set up pre-commit hooks
make pre-commit

# Run tests to verify setup
make test
```

## 🏗️ Project Structure

```
.
├── src/                        # Source code
│   └── your_package_name/      # Your package module
│       ├── __init__.py
│       ├── core.py             # Core functionality
│       └── utils.py            # Utility functions
├── tests/                      # Test files (mirrors src/ structure)
│   ├── __init__.py
│   └── test_core.py
├── docs/                       # Documentation (MkDocs)
│   ├── index.md
│   ├── api/                    # API documentation
│   └── guide/                  # User guides
├── data/                       # Data files (for data-driven projects)
│   ├── raw/                    # Raw, immutable data
│   ├── processed/              # Cleaned, transformed data
│   └── external/               # External data sources
├── notebooks/                  # Jupyter notebooks for exploration
├── scripts/                    # Utility scripts
├── configs/                    # Configuration files
├── .github/                    # GitHub configuration
│   ├── workflows/              # CI/CD workflows
│   └── copilot-instructions.md # Instructions for GitHub Copilot
├── pyproject.toml              # Project configuration (SINGLE SOURCE OF TRUTH)
├── Makefile                    # Development commands
├── .pre-commit-config.yaml     # Pre-commit hooks
├── .python-version             # Python version for pyenv/asdf
├── .cursorrules                # Cursor AI editor rules
├── README.md                   # This file
├── CONTRIBUTING.md             # Contribution guidelines
├── CHANGELOG.md                # Version history
└── LICENSE                     # GPL-3.0 license

```

## 🛠️ Development Workflow

### Common Tasks

```bash
# Install dependencies
make install-dev              # Dev dependencies only
make install-all              # All optional dependencies

# Code quality
make format                   # Auto-format code
make lint                     # Run all checks (ruff + mypy)

# Testing
make test                     # Run all tests
make test-fast                # Quick tests only
make test-cov                 # With coverage report

# Documentation
make docs                     # Build docs
make docs-serve               # Serve locally at http://localhost:8000

# Data science
make notebook                 # Start Jupyter Lab

# Clean up
make clean                    # Remove build artifacts
make data-clean               # Clean data cache
```

### Working with AI Assistants

This template is optimized for AI-assisted development:

1. **GitHub Copilot**: Check `.github/copilot-instructions.md` for custom instructions
2. **Cursor**: See `.cursorrules` for editor-specific guidelines  
3. **Claude/ChatGPT**: Share the `CONTRIBUTING.md` for context

The AI assistant should:
- Follow the existing code structure and patterns
- Add type hints to all functions
- Write tests for new functionality
- Update documentation as needed
- Follow Google-style docstrings

## 📊 Data-Driven Development

This template includes support for data science workflows:

### Directory Structure
- `data/raw/`: Store original, immutable data
- `data/processed/`: Cleaned and transformed data
- `data/external/`: Third-party data sources
- `notebooks/`: Exploratory data analysis

### Workflow
1. Add raw data to `data/raw/`
2. Create processing scripts in `scripts/`
3. Save processed data to `data/processed/`
4. Document findings in `notebooks/`
5. Extract reusable code to `src/your_package_name/`

### Best Practices
- **Version your data**: Use DVC or git-lfs for large files
- **Document everything**: Add README files in data directories
- **Reproducibility**: Pin package versions, use random seeds
- **Never commit secrets**: Use environment variables

## 🤖 Agentic Development Guidelines

This template follows principles that make it easier for AI agents to contribute:

### Code Organization
- **Single Source of Truth**: All config in `pyproject.toml`
- **Clear Conventions**: Consistent naming and structure
- **Type Safety**: Full type hints for better AI understanding
- **Documentation**: Every public function documented

### AI-Friendly Patterns
1. **Explicit over implicit**: Clear variable names, obvious logic
2. **Small functions**: Easy to understand and test
3. **Pure functions**: Predictable, testable, composable
4. **Type hints everywhere**: Helps AI understand intent
5. **Comprehensive tests**: AI can verify changes

### Communication with AIs
- This README explains the "why" behind choices
- CONTRIBUTING.md explains the "how"
- Comments explain the "what" when code isn't clear
- Type hints explain the "types"

## 📝 Git Workflow (Git Flow)

This template uses Git Flow:

### Branches
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `hotfix/*`: Production hotfixes

### Commit Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(scope): add new feature
fix(scope): fix bug
docs(scope): update documentation
test(scope): add tests
refactor(scope): refactor code
chore(scope): update dependencies
```

## 🧪 Testing Strategy

```python
# Unit tests - Fast, isolated
tests/unit/

# Integration tests - Test component interaction
tests/integration/

# Data tests - Validate data processing
tests/data/

# AI tests - Test LLM integrations (if applicable)
tests/ai/
```

Run with markers:
```bash
pytest -m unit                # Only unit tests
pytest -m "not slow"          # Exclude slow tests
pytest -m "integration"       # Only integration tests
```

## 📚 Documentation

Documentation is built with MkDocs Material:

```bash
make docs-serve               # Local preview
make docs-deploy              # Deploy to GitHub Pages
```

Documentation structure:
- `docs/index.md`: Home page
- `docs/guide/`: User guides
- `docs/api/`: API reference
- `docs/contributing/`: Contribution guide

## 🔒 License & Legal

This template is licensed under **AGPL-3.0** (GNU Affero General Public License v3.0). This means:

### For Users
✅ **You CAN**:
- Use this template for any purpose
- Modify and distribute the code
- Use it commercially

⚠️ **You MUST**:
- Disclose source code (including for network services)
- License modifications under AGPL-3.0
- Include original copyright notice
- Provide source to network users

### For AI Agents
**IMPORTANT**: When contributing to projects using this template:
1. Respect the AGPL-3.0 license terms
2. Do not introduce code from incompatible licenses
3. Maintain license headers in new files
4. Document any third-party code sources
5. Remember: Network use triggers source disclosure

See [LICENSE](LICENSE) for full terms.

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Coding standards
- Testing requirements
- Pull request process

For AI assistants: Follow all guidelines in CONTRIBUTING.md strictly.

## 🌟 Features

### Modern Python Tooling
- **uv**: Fast package management (10-100x faster than pip)
- **ruff**: All-in-one linter and formatter (replaces black, isort, flake8)
- **mypy**: Strict type checking
- **pytest**: Comprehensive testing framework

### Code Quality
- Pre-commit hooks for automatic checks
- 100% type coverage requirement
- Minimum 80% test coverage
- Automated formatting and linting

### Developer Experience
- One-command setup: `make install-all`
- Fast feedback loop with pre-commit
- Clear error messages
- Comprehensive documentation

### AI-Ready
- Structured for AI comprehension
- Clear conventions and patterns
- Comprehensive type hints
- Explicit documentation

## 🎓 Learning Resources

### For Developers
- [Python Packaging Guide](https://packaging.python.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Conventional Commits](https://www.conventionalcommits.org/)

### For AI Development
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [AI-Assisted Development](https://github.blog/developer-skills/github/how-to-write-better-prompts-for-github-copilot/)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/your-package-name/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/your-package-name/discussions)

## 🙏 Acknowledgments

This template is based on the excellent work from:
- [urzad-regulacji-energetyki](https://github.com/WiktorHawrylik/urzad-regulacji-energetyki) - Structure and best practices
- [PyPA](https://www.pypa.io/) - Python packaging standards
- [Ruff](https://github.com/astral-sh/ruff) - Fast Python tooling

---

**Made with ❤️ for the agentic development community**

*This template respects AGPL-3.0 licensing and encourages all contributors (human and AI) to do the same.*