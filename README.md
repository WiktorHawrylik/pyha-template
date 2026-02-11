# Python Library Template

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](http://mypy-lang.org/)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://your-username.github.io/your-package-name/)

Modern Python library template optimized for agentic AI development and data-driven workflows.

- **Pre-configured tooling** - uv, ruff, mypy, pytest
- **AI-ready** - Optimized for GitHub Copilot, Cursor, Claude
- **Type-safe** - Full mypy strict mode
- **Well-documented** - Comprehensive guides and API docs

## 📦 Installation

```bash
# Using uv (recommended)
uv pip install your-package-name

# Or using pip
pip install your-package-name
```

## 🚀 Quick Start

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

### Using the Template

```bash
# Clone this repository
git clone https://github.com/your-username/python-library-template.git my-project
cd my-project
```

## 📚 Documentation

Complete documentation available at: **[https://your-username.github.io/your-package-name/](https://your-username.github.io/your-package-name/)**

- [Installation Guide](https://your-username.github.io/your-package-name/guide/installation/)
- [Template Usage Guide](https://your-username.github.io/your-package-name/guide/template-usage/)
- [Quick Start](https://your-username.github.io/your-package-name/guide/quickstart/)
- [API Reference](https://your-username.github.io/your-package-name/api/core/)
- [Contributing](https://your-username.github.io/your-package-name/contributing/)

## 🛠️ Requirements

- Python 3.9+
- uv (recommended) or pip
- make (for automation)

## 📄 License

AGPL-3.0 - see [LICENSE](LICENSE)

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for guidelines.

## 📬 Contact

- **GitHub Issues**: [Report a problem](https://github.com/your-username/your-package-name/issues)
- **Discussions**: [Ask a question](https://github.com/your-username/your-package-name/discussions)

---

Made with ❤️ for the Python community