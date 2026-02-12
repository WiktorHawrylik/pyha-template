# Quick Start

This guide will get you up and running with your-package-name in minutes.

## Basic Example

```python
from your_package_name import ExampleClass, process_data

# Process data with filtering
data = [
    {"value": 0.3},
    {"value": 0.7},
    {"value": 0.9}
]

# Filter data above threshold
filtered = process_data(data, threshold=0.5)
print(filtered)
# Output: [{"value": 0.7}, {"value": 0.9}]
```

## Working with Classes

```python
from your_package_name import ExampleClass

# Create an instance
obj = ExampleClass(name="example", value=42.0)

# Access properties
print(obj.name)   # "example"
print(obj.value)  # 42.0

# Modify value
obj.increment(5.0)
print(obj.value)  # 47.0

# Reset
obj.reset()
print(obj.value)  # 0.0
```

## Error Handling

The package provides clear error messages:

```python
from your_package_name import process_data

# This will raise a ValueError
try:
    process_data([], threshold=0.5)
except ValueError as e:
    print(e)  # "Data list cannot be empty"

# This will raise a ValueError
try:
    process_data([{"value": 0.5}], threshold=1.5)
except ValueError as e:
    print(e)  # "Threshold must be between 0 and 1, got 1.5"
```

## Next Steps

- [API Reference](../api/core.md) - Detailed API documentation
- [Best Practices](best-practices.md) - Recommended patterns
