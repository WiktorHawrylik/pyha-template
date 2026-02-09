# Your Package Name

Welcome to the documentation for **Your Package Name** - a modern Python library template optimized for agentic and data-driven development.

## Features

- ✅ **Modern Python Tooling**: Uses uv, ruff, and mypy for fast, quality development
- ✅ **Full Type Safety**: 100% type coverage with strict mypy configuration
- ✅ **Comprehensive Testing**: pytest with coverage tracking and multiple test categories
- ✅ **AI-Ready**: Optimized for GitHub Copilot, Cursor, and other AI assistants
- ✅ **Data-Driven**: Built-in support for data science workflows
- ✅ **Well Documented**: Comprehensive guides and API documentation
- ✅ **CI/CD Ready**: GitHub Actions workflows for testing, docs, and releases

## Quick Start

### Installation

```bash
pip install your-package-name
```

Or with uv (recommended):

```bash
uv pip install your-package-name
```

### Basic Usage

```python
from your_package_name import ExampleClass, process_data

# Process data with filtering
data = [{"value": 0.3}, {"value": 0.7}, {"value": 0.9}]
filtered = process_data(data, threshold=0.5)
print(filtered)  # [{"value": 0.7}, {"value": 0.9}]

# Use the example class
obj = ExampleClass("example", 42.0)
obj.increment(5.0)
print(obj.value)  # 47.0
```

## Why This Template?

This template is specifically designed for:

1. **Rapid Development**: Pre-configured tooling means you can start coding immediately
2. **AI Assistance**: Clear structure and documentation that AI assistants understand
3. **Data Science**: Built-in support for notebooks, data directories, and common workflows
4. **Quality Code**: Enforced type hints, testing, and documentation standards
5. **Open Source**: GPL-3.0 licensed with clear contribution guidelines

## What's Included?

### Development Tools
- **uv**: Fast Python package manager (10-100x faster than pip)
- **ruff**: All-in-one linter and formatter
- **mypy**: Strict type checking
- **pytest**: Comprehensive testing with coverage
- **pre-commit**: Automatic code quality checks

### Project Structure
```
your-package-name/
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
├── data/             # Data files
├── notebooks/        # Jupyter notebooks
├── scripts/          # Utility scripts
└── configs/          # Configuration files
```

### Documentation
- **User Guides**: Step-by-step tutorials
- **API Reference**: Auto-generated from docstrings
- **Development Guides**: For contributors
- **AI Instructions**: For coding assistants

## Getting Help

- 📖 **Documentation**: You're reading it!
- 🐛 **Issues**: [GitHub Issues](https://github.com/your-username/your-package-name/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/your-username/your-package-name/discussions)

## License

This project is licensed under the **AGPL-3.0 License**. See [License](license.md) for details.

## Next Steps

- [Installation Guide](guide/installation.md) - Detailed installation instructions
- [Quick Start Guide](guide/quickstart.md) - Get up and running quickly
- [API Reference](api/core.md) - Complete API documentation
- [Contributing](contributing.md) - How to contribute to this project
