"""Core functionality for the package.

This module demonstrates best practices for Python development with full
type hints, comprehensive docstrings, and proper error handling.

Copyright (C) 2024 Your Name

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

from typing import Any, Optional


def process_data(data: list[dict[str, Any]], threshold: float = 0.5) -> list[dict[str, Any]]:
    """Process data by filtering based on a threshold value.

    This function demonstrates proper type hints, docstrings, and error handling
    that should be used throughout the codebase.

    Args:
        data: List of dictionaries containing data to process.
              Each dictionary must have a 'value' key with a numeric value.
        threshold: Minimum value to include in results (default: 0.5).
                  Must be between 0 and 1.

    Returns:
        Filtered list of dictionaries where value >= threshold.

    Raises:
        ValueError: If threshold is not between 0 and 1, or if data is empty.
        KeyError: If any dictionary is missing the 'value' key.
        TypeError: If any value is not numeric.

    Examples:
        >>> data = [{"value": 0.3}, {"value": 0.7}, {"value": 0.9}]
        >>> process_data(data, threshold=0.5)
        [{'value': 0.7}, {'value': 0.9}]

        >>> process_data([{"value": 0.3}], threshold=0.2)
        [{'value': 0.3}]

    Notes:
        - Values exactly equal to threshold are included
        - Original data is not modified (returns new list)
        - Maintains original order of items
    """
    if not data:
        raise ValueError("Data list cannot be empty")

    if not 0 <= threshold <= 1:
        raise ValueError(f"Threshold must be between 0 and 1, got {threshold}")

    result = []
    for item in data:
        if "value" not in item:
            raise KeyError(f"Dictionary missing 'value' key: {item}")

        value = item["value"]
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be numeric, got {type(value).__name__}: {value}")

        if value >= threshold:
            result.append(item)

    return result


class ExampleClass:
    """Example class demonstrating Python best practices.

    This class shows proper use of type hints, docstrings, properties,
    and initialization patterns.

    Attributes:
        name: Name of the instance
        value: Numeric value associated with the instance
        metadata: Optional metadata dictionary

    Examples:
        >>> obj = ExampleClass("example", 42)
        >>> obj.name
        'example'
        >>> obj.value
        42
        >>> obj.increment(5)
        >>> obj.value
        47
    """

    def __init__(
        self,
        name: str,
        value: float,
        *,
        metadata: Optional[dict[str, Any]] = None,
    ) -> None:
        """Initialize ExampleClass.

        Args:
            name: Name for this instance
            value: Initial numeric value
            metadata: Optional metadata dictionary

        Raises:
            ValueError: If name is empty or value is negative
        """
        if not name:
            raise ValueError("Name cannot be empty")
        if value < 0:
            raise ValueError(f"Value must be non-negative, got {value}")

        self._name = name
        self._value = value
        self._metadata = metadata or {}

    @property
    def name(self) -> str:
        """Get the instance name."""
        return self._name

    @property
    def value(self) -> float:
        """Get the current value."""
        return self._value

    @property
    def metadata(self) -> dict[str, Any]:
        """Get metadata dictionary (copy to prevent external modification)."""
        return self._metadata.copy()

    def increment(self, amount: float = 1.0) -> None:
        """Increment the value by the specified amount.

        Args:
            amount: Amount to add to current value (default: 1.0)

        Raises:
            ValueError: If amount is negative
            TypeError: If amount is not numeric

        Examples:
            >>> obj = ExampleClass("test", 10)
            >>> obj.increment(5)
            >>> obj.value
            15.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError(f"Amount must be numeric, got {type(amount).__name__}")
        if amount < 0:
            raise ValueError(f"Amount must be non-negative, got {amount}")

        self._value += amount

    def reset(self) -> None:
        """Reset value to zero.

        Examples:
            >>> obj = ExampleClass("test", 42)
            >>> obj.reset()
            >>> obj.value
            0.0
        """
        self._value = 0.0

    def __repr__(self) -> str:
        """Return string representation of the instance."""
        return f"ExampleClass(name={self.name!r}, value={self.value})"

    def __eq__(self, other: object) -> bool:
        """Check equality with another ExampleClass instance."""
        if not isinstance(other, ExampleClass):
            return NotImplemented
        return self.name == other.name and self.value == other.value

    __hash__ = None  # type: ignore[assignment]  # Mutable object should not be hashable
