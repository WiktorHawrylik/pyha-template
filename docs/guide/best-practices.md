# Best Practices

This guide covers best practices for using this library.

## Code Organization

### Keep It Simple

- Write small, focused functions
- One function = one responsibility
- Prefer composition over inheritance

### Use Type Hints

```python
# Good
def process(data: list[int]) -> dict[str, float]:
    ...

# Bad
def process(data):
    ...
```

### Write Docstrings

```python
def calculate(x: float, y: float) -> float:
    """Calculate something useful.

    Args:
        x: First value
        y: Second value

    Returns:
        Calculated result
    """
    return x + y
```

## Error Handling

### Be Specific

```python
# Good
try:
    value = int(input_string)
except ValueError as e:
    logger.error(f"Invalid integer: {e}")
    raise

# Bad
try:
    value = int(input_string)
except:
    pass
```

### Provide Context

```python
# Good
if not path.exists():
    raise FileNotFoundError(
        f"Configuration file not found: {path}\n"
        f"Please create it at: {path.absolute()}"
    )

# Bad
if not path.exists():
    raise FileNotFoundError(str(path))
```

## Testing

### Test Edge Cases

```python
def test_empty_input():
    """Test handling of empty input."""
    with pytest.raises(ValueError):
        process_data([])

def test_boundary_values():
    """Test boundary values."""
    assert process_data([0]) == expected_for_zero
    assert process_data([1]) == expected_for_one
```

### Use Descriptive Names

```python
# Good
def test_process_data_raises_error_on_negative_values():
    ...

# Bad
def test1():
    ...
```

## Performance

### Use Generators

```python
# Good - Memory efficient
def read_large_file(path: Path):
    with open(path) as f:
        for line in f:
            yield process_line(line)

# Bad - Loads everything into memory
def read_large_file(path: Path):
    with open(path) as f:
        return [process_line(line) for line in f]
```

### Profile Before Optimizing

```python
import cProfile

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()

    # Your code here
    result = expensive_operation()

    profiler.disable()
    profiler.print_stats(sort='cumulative')
    return result
```

## Data Handling

### Validate Input

```python
from pydantic import BaseModel, Field, field_validator

class DataPoint(BaseModel):
    value: float = Field(ge=0.0, le=1.0)
    timestamp: datetime

    @field_validator('value')
    @classmethod
    def check_value(cls, v: float) -> float:
        if not 0 <= v <= 1:
            raise ValueError(f"Value must be 0-1, got {v}")
        return v
```

### Use Pathlib

```python
# Good
from pathlib import Path

data_path = Path("data") / "raw" / "file.csv"
if data_path.exists():
    content = data_path.read_text()

# Bad
import os

data_path = os.path.join("data", "raw", "file.csv")
if os.path.exists(data_path):
    with open(data_path) as f:
        content = f.read()
```

## Security

### Never Hardcode Secrets

```python
# Good
import os
api_key = os.getenv("API_KEY")

# Bad
api_key = "sk-1234567890abcdef"
```

### Validate User Input

```python
# Good
def load_file(path: Path) -> str:
    # Validate path
    if ".." in str(path):
        raise ValueError("Path traversal not allowed")

    if not path.is_relative_to(ALLOWED_DIR):
        raise ValueError("Path outside allowed directory")

    return path.read_text()

# Bad
def load_file(path: str) -> str:
    return open(path).read()
```

## Documentation

### Document Why, Not What

```python
# Good
def normalize(values: list[float]) -> list[float]:
    """Normalize values to [0, 1] range.

    Uses min-max normalization to ensure all values are comparable
    regardless of their original scale. This is particularly important
    when combining features from different sources.
    """
    ...

# Bad
def normalize(values: list[float]) -> list[float]:
    """Normalizes values."""
    ...
```

### Keep Examples Updated

```python
def process(data: list[int]) -> dict[str, float]:
    """Process data.

    Examples:
        >>> process([1, 2, 3])
        {'mean': 2.0, 'sum': 6}
    """
    # Make sure examples actually work!
    ...
```

## Next Steps

- Read the [API Reference](../api/core.md)
- Review [Contributing Guidelines](../contributing.md)
