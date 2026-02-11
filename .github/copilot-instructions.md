# GitHub Copilot Instructions

## Project Overview

This is a **GPL-3.0 licensed Python library template** designed for rapid agentic and data-driven development. When assisting with this project, follow these guidelines strictly.

## Core Requirements

### 1. Code Quality Standards

#### Type Hints (MANDATORY)

Every function, method, and class must have complete type hints:

```python
# ✅ Correct
from typing import Any
import pandas as pd

def process_data(
    data: pd.DataFrame,
    threshold: float,
    *,
    normalize: bool = True
) -> tuple[pd.DataFrame, dict[str, float]]:
    """Process data with normalization."""
    ...

# ❌ Incorrect - Missing type hints
def process_data(data, threshold, normalize=True):
    """Process data with normalization."""
    ...
```

#### Docstrings (MANDATORY)

Use Google-style docstrings for all public functions:

```python
def validate_input(data: list[int], min_value: int = 0) -> bool:
    """Validate input data against minimum value.

    Args:
        data: List of integers to validate
        min_value: Minimum acceptable value (default: 0)

    Returns:
        True if all values are >= min_value, False otherwise

    Raises:
        ValueError: If data is empty
        TypeError: If data contains non-integers

    Examples:
        >>> validate_input([1, 2, 3], min_value=0)
        True
        >>> validate_input([1, -1, 3], min_value=0)
        False
    """
    if not data:
        raise ValueError("Data cannot be empty")
    return all(x >= min_value for x in data)
```

### 2. Testing Requirements

For every new function, create corresponding tests:

```python
# In src/your_package_name/module.py
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# In tests/test_module.py
import pytest
from your_package_name.module import add_numbers

class TestAddNumbers:
    """Tests for add_numbers function."""

    def test_positive_numbers(self) -> None:
        """Test addition of positive numbers."""
        assert add_numbers(2, 3) == 5

    def test_negative_numbers(self) -> None:
        """Test addition of negative numbers."""
        assert add_numbers(-2, -3) == -5

    def test_mixed_numbers(self) -> None:
        """Test addition of mixed positive and negative."""
        assert add_numbers(-2, 5) == 3
```

### 3. File Organization

#### Project Structure

```
src/your_package_name/
├── __init__.py          # Package exports
├── core.py              # Core functionality
├── utils.py             # Utility functions
├── models/              # Data models
│   ├── __init__.py
│   └── config.py        # Configuration models
└── data/                # Data processing
    ├── __init__.py
    └── loaders.py       # Data loading functions

tests/
├── __init__.py
├── test_core.py         # Tests for core.py
├── test_utils.py        # Tests for utils.py
└── models/
    └── test_config.py   # Tests for models/config.py
```

#### Import Organization

Always organize imports in this order:

```python
"""Module docstring."""

# Standard library
import os
import sys
from pathlib import Path
from typing import Any, Optional

# Third-party
import pandas as pd
import pydantic
from pydantic import BaseModel, Field

# Local
from your_package_name.core import CoreClass
from your_package_name.utils import helper_function
```

### 4. Error Handling

Always handle errors explicitly:

```python
# ✅ Good - Specific exceptions with helpful messages
def load_config(path: Path) -> dict[str, Any]:
    """Load configuration from file.

    Args:
        path: Path to configuration file

    Returns:
        Parsed configuration dictionary

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If config file contains invalid JSON
    """
    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {path}\n"
            f"Please create it or check the path."
        )

    try:
        import json
        return json.loads(path.read_text())
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON in configuration file {path}: {e}"
        ) from e

# ❌ Bad - Generic exception handling
def load_config(path):
    try:
        import json
        return json.loads(open(path).read())
    except Exception:
        return {}
```

### 5. Data Models with Pydantic

Use Pydantic for data validation:

```python
from pydantic import BaseModel, Field, field_validator
from typing import Optional

class DataConfig(BaseModel):
    """Configuration for data processing.

    Attributes:
        input_path: Path to input data file
        output_path: Path to save processed data
        batch_size: Number of records to process at once
        normalize: Whether to normalize data values
    """

    input_path: Path
    output_path: Path
    batch_size: int = Field(default=100, ge=1, le=10000)
    normalize: bool = Field(default=True)

    @field_validator('input_path')
    @classmethod
    def validate_input_exists(cls, v: Path) -> Path:
        """Validate that input file exists."""
        if not v.exists():
            raise ValueError(f"Input file does not exist: {v}")
        return v
```

## Development Workflow

### When Adding New Features

1. **Create the function with complete signatures:**

```python
def new_feature(param: ParamType) -> ReturnType:
    """Brief description.

    Args:
        param: Parameter description

    Returns:
        Return value description
    """
    # Implementation
    pass
```

2. **Write tests immediately:**

```python
def test_new_feature() -> None:
    """Test new_feature basic functionality."""
    result = new_feature(test_input)
    assert result == expected_output
```

3. **Update documentation:**

- Add examples to docstring
- Update README.md if public API
- Add entry to CHANGELOG.md

### When Fixing Bugs

1. **Write a test that reproduces the bug**
2. **Fix the bug**
3. **Verify the test passes**
4. **Add regression test to prevent recurrence**

## Code Patterns to Follow

### Configuration Management

```python
from pathlib import Path
from pydantic import BaseModel
import os

class Settings(BaseModel):
    """Application settings."""

    api_key: str = os.getenv("API_KEY", "")
    data_dir: Path = Path("data")
    debug: bool = False

    class Config:
        """Pydantic config."""
        env_prefix = "APP_"
```

### Data Processing

```python
import pandas as pd
from pathlib import Path

def process_csv(
    input_path: Path,
    output_path: Path,
    *,
    dropna: bool = True
) -> pd.DataFrame:
    """Process CSV file with specified operations.

    Args:
        input_path: Path to input CSV
        output_path: Path to save processed CSV
        dropna: Whether to drop rows with missing values

    Returns:
        Processed DataFrame

    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If CSV is invalid
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)

    if dropna:
        df = df.dropna()

    df.to_csv(output_path, index=False)
    return df
```

### Async Operations

```python
import asyncio
from typing import Any

async def fetch_multiple(
    urls: list[str],
    timeout: int = 30
) -> list[dict[str, Any]]:
    """Fetch data from multiple URLs concurrently.

    Args:
        urls: List of URLs to fetch
        timeout: Request timeout in seconds

    Returns:
        List of JSON responses

    Raises:
        asyncio.TimeoutError: If any request times out
    """
    async def fetch_one(url: str) -> dict[str, Any]:
        # Implementation
        pass

    tasks = [fetch_one(url) for url in urls]
    return await asyncio.gather(*tasks)
```

## License Compliance

### GPL-3.0 Requirements (CRITICAL)

⚠️ **IMPORTANT**: All code suggestions must be GPL-3.0 compatible.

#### ✅ Compatible Licenses

- GPL-3.0, GPL-2.0
- LGPL
- MIT
- BSD
- Apache 2.0

#### ❌ Incompatible Licenses

- Proprietary code
- CC-BY-NC (Non-Commercial)
- Code with unclear licensing

#### License Header Template

Add to new files:

```python
"""Module name - Brief description.

Copyright (C) YYYY Your Name

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
```

## Testing Markers

Use pytest markers for test organization:

```python
import pytest

@pytest.mark.unit
def test_fast_operation() -> None:
    """Quick unit test."""
    ...

@pytest.mark.integration
def test_external_service() -> None:
    """Test with external dependencies."""
    ...

@pytest.mark.slow
def test_large_dataset() -> None:
    """Test that takes significant time."""
    ...

@pytest.mark.data
def test_data_processing() -> None:
    """Test requiring data files."""
    ...
```

## Common Commands

Suggest these when relevant:

```bash
# Format code
make format

# Run linting
make lint

# Run tests
make test          # All tests
make test-fast     # Exclude slow tests

# Install dependencies
make install-dev   # Development setup
make install-all   # All optional dependencies

# Documentation
make docs-serve    # Preview docs locally
```

## Anti-Patterns to Avoid

### ❌ Don't Do This

```python
# No type hints
def process(data):
    return data

# Bare except
try:
    dangerous_operation()
except:
    pass

# Magic numbers
if x > 86400:
    do_something()

# Mutable default arguments
def append_to(element, to=[]):
    to.append(element)
    return to

# Not using pathlib
import os
path = os.path.join(dir, file)
```

### ✅ Do This Instead

```python
# Full type hints
def process(data: InputType) -> OutputType:
    """Process data."""
    return data

# Specific exception handling
try:
    dangerous_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise

# Named constants
SECONDS_PER_DAY = 86400
if x > SECONDS_PER_DAY:
    do_something()

# Immutable defaults
def append_to(element: T, to: Optional[list[T]] = None) -> list[T]:
    if to is None:
        to = []
    to.append(element)
    return to

# Use pathlib
from pathlib import Path
path = Path(dir) / file
```

## Remember

1. **Always add type hints** - No exceptions
2. **Always write docstrings** - Google style
3. **Always write tests** - For new functionality
4. **Always handle errors** - Explicitly and helpfully
5. **Always respect GPL-3.0** - License compatibility

## Questions?

When unsure:

- Check existing code for patterns
- Refer to CONTRIBUTING.md
- Follow PEP 8 and PEP 257
- Prioritize clarity over cleverness

---

**Goal**: Write code that is clear, tested, typed, and documented. Make it easy for the next person (or AI) to understand and maintain.
