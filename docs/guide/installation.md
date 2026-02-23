# Installation

## Requirements

- Python 3.11 or higher
- pip or uv package manager

## Installation Methods

### Using pip (Standard)

```bash
pip install your-package-name
```

### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package manager:

```bash
# Install uv first
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the package
uv pip install your-package-name
```

### From Source

```bash
# Clone the repository
git clone https://github.com/WiktorHawrylik/your-package-name.git
cd your-package-name

# Install in development mode
uv pip install -e .
```

## Optional Dependencies

### Development Dependencies

For contributing or development:

```bash
uv sync --extra dev --extra docs
```

### Documentation Dependencies

For documentation authoring and publishing:

```bash
uv sync --extra docs
```

### All Dependencies

To install everything:

```bash
uv pip install "your-package-name[all]"
```

## Verification

Verify the installation:

```python
import your_package_name
print(your_package_name.__version__)
```

## Troubleshooting

### Python Version Issues

Make sure you have Python 3.11+:

```bash
python --version
```

### Permission Errors

Use `--user` flag:

```bash
pip install --user your-package-name
```

Or use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install your-package-name
```

## Next Steps

- [Quick Start Guide](quickstart.md) - Start using the package
- [Configuration](configuration.md) - Configure the package
