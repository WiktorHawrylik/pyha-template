# Your Package Name

Welcome to the documentation for **Your Package Name** - a modern Python library template optimized for agentic and data-driven development.

## Features

- ✅ **Modern Python Tooling**: uv, ruff, mypy for fast, quality development
- ✅ **Full Type Safety**: 100% type coverage with strict mypy configuration
- ✅ **Comprehensive Testing**: pytest with coverage tracking
- ✅ **AI-Ready**: Optimized for GitHub Copilot, Cursor, and other AI assistants
- ✅ **Well Documented**: Comprehensive guides and API documentation
- ✅ **CI/CD Ready**: GitHub Actions workflows for testing and releases

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

## Using This Template

This project serves as a template for creating new Python libraries:

1. Clone the repository
2. Run the customization script: `python scripts/customize_template.py`
3. Install dependencies: `make install-all`
4. Start coding!

See the [Template Usage Guide](guide/template-usage.md) for detailed instructions.

## Why This Template?

### For Developers

- **Zero Configuration**: Pre-configured with modern Python tooling
- **Best Practices**: Following industry standards
- **Fast Development**: Makefile automation, pre-commit hooks
- **Type Safety**: Full mypy strict mode

### For AI Agents

- **Clear Structure**: Consistent, predictable project layout
- **Explicit Guidelines**: Comprehensive documentation
- **Type Hints**: Full type coverage for better understanding
- **Well Documented**: Every public function has docstrings

## Documentation Structure

- **[User Guide](guide/installation.md)** - Installation, quickstart, and usage
- **[API Reference](api/core.md)** - Complete API documentation
- **[Development](contributing.md)** - Contributing guidelines and development guides
- **[About](changelog.md)** - Changelog and license information

## Getting Help

- 📖 **Documentation**: Browse the sections above
- 🐛 **Issues**: [GitHub Issues](https://github.com/your-username/your-package-name/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/your-username/your-package-name/discussions)

## License

This project is licensed under the **AGPL-3.0 License**. See [License](license.md) for details.

## Next Steps

- [Installation Guide](guide/installation.md) - Set up your environment
- [Quick Start Guide](guide/quickstart.md) - Get up and running
- [Template Usage](guide/template-usage.md) - Learn how to use this template
- [API Reference](api/core.md) - Explore the API
- [Contributing](contributing.md) - Join the development
