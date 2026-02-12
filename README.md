# Python Library Template

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](http://mypy-lang.org/)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://WiktorHawrylik.github.io/your-package-name/)

Modern Python library template optimized for agentic AI development and data-driven workflows.

- **Pre-configured tooling** - uv, ruff, mypy, pytest
- **AI-ready** - Optimized for GitHub Copilot, Cursor, Claude
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
git clone https://github.com/WiktorHawrylik/python-library-template.git my-project
cd my-project
```

## 📚 Documentation

Complete documentation available at: **[https://WiktorHawrylik.github.io/your-package-name/](https://WiktorHawrylik.github.io/your-package-name/)**

- [Installation Guide](https://WiktorHawrylik.github.io/your-package-name/guide/installation/)
- [Template Usage Guide](https://WiktorHawrylik.github.io/your-package-name/guide/template-usage/)
- [Quick Start](https://WiktorHawrylik.github.io/your-package-name/guide/quickstart/)
- [API Reference](https://WiktorHawrylik.github.io/your-package-name/api/core/)
- [Contributing](https://WiktorHawrylik.github.io/your-package-name/contributing/)

## 🛠️ Requirements

- Python 3.11+
- uv (recommended) or pip
- make (for automation)

## 📄 License

AGPL-3.0 - see [LICENSE](LICENSE)

## 📝 TODO

### 🏗️ Architecture & Design

- [ ] Move `docs/development/_constitution.md` → `docs/design/_constitution.md`
- [ ] Add "Simplicity First" principles to development guide (minimal abstractions)

### 🔧 Configuration & Tooling

- [ ] Consolidate `.editorconfig` settings into `pyproject.toml`
- [ ] Remove `.cursorrules` (replaced by AGENTS.md + _constitution.md)
- [ ] Document `configs/` directory structure and usage
- [ ] Create `customize_template.py` script for easy template initialization

### 🧪 Testing & Quality

- [ ] Rethink testing strategy (unit, integration, E2E patterns)
- [ ] Add E2E data validation examples for larger pipelines
- [ ] Rethink CI/CD workflows (GitHub Actions optimization)

### 📊 Data Engineering

- [ ] Add Spark transformation examples and patterns
- [ ] Clarify data folder conventions (`data/`, `tests/fixtures/`)
- [ ] Document data validation patterns (schema, row-level, aggregates)

### 🤖 Operationalisation Considerations

- [ ] PoC folder in root
- [ ] Design refactor strategy: PoC → operational = agent following dev rules

### 🤖 ML/AI Considerations

- [ ] Evaluate: Separate ML/AI template repo vs. extension guide?
- [ ] Notebooks strategy: PoC → operational workflow
- [ ] Human debugging interfaces for notebooks
- [ ] Notebook best practices and integration patterns

### 📚 Documentation

- [ ] Complete missing guide pages (data-processing.md, testing.md)
- [ ] Add architecture decision record (ADR) examples
- [ ] Document template customization workflow

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for guidelines.

## 📬 Contact

- **Report a problem**: [GitHub Issues](https://github.com/WiktorHawrylik/your-package-name/issues)
- **Ask a question**: [GitHub Discussions](https://github.com/WiktorHawrylik/your-package-name/discussions)
- **Autor**: Wiktor Hawrylik
- **Email**: <wiktor.hawrylik@gmail.com>

---

Made with ❤️ for the Python community
