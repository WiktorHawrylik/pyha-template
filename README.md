# Python Library Template

[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://wiktorhawrylik.github.io/your-package-name/)
[![CI](https://github.com/WiktorHawrylik/your-package-name/workflows/CI/badge.svg)](https://github.com/WiktorHawrylik/your-package-name/actions)
[![codecov](https://codecov.io/gh/WiktorHawrylik/pyha-template/branch/main/graph/badge.svg)](https://codecov.io/gh/WiktorHawrylik/your-package-name)
[![PyPI version](https://img.shields.io/pypi/v/your-package-name.svg)](https://pypi.org/project/your-package-name/)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Wiktor Hawrylik Python library template optimized for agentic AI development and data-driven workflows.

## Installation

```bash
# Using uv (recommended)
uv pip install your-package-name

# Or using pip
pip install your-package-name
```

## Quick Start

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

1. Clone this repository

```bash
git clone https://github.com/WiktorHawrylik/python-library-template.git my-project
cd my-project
```

1. Modify
   1. Name python module, now "your_package_name"
   2. Name python package, now "your-package-name"

## Documentation

Complete documentation available at: **[https://WiktorHawrylik.github.io/your-package-name/](https://WiktorHawrylik.github.io/your-package-name/)**

- [Installation Guide](https://WiktorHawrylik.github.io/your-package-name/guide/installation/)
- [Template Usage Guide](https://WiktorHawrylik.github.io/your-package-name/guide/template-usage/)
- [Quick Start](https://WiktorHawrylik.github.io/your-package-name/guide/quickstart/)
- [API Reference](https://WiktorHawrylik.github.io/your-package-name/api/core/)
- [Contributing](https://WiktorHawrylik.github.io/your-package-name/contributing/)

## Requirements

- Python 3.11+
- uv (recommended) or pip
- make (for automation)

## Roadmap

To review planned work or exploratory follow-ups use
[Roadmap](docs/architecture/roadmap.md).

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for guidelines.

## License

AGPL-3.0 - see [LICENSE](LICENSE)

## Contact

- **Report a problem**: [GitHub Issues](https://github.com/WiktorHawrylik/your-package-name/issues)
- **Ask a question**: [GitHub Discussions](https://github.com/WiktorHawrylik/your-package-name/discussions)
- **Autor**: Wiktor Hawrylik
- **Email**: <wiktor.hawrylik@gmail.com>

---

Made with joy for the community
