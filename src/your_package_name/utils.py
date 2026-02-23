"""Utility functions for the package.

This module provides common utility functions used throughout the package.

Copyright (C) 2026 Wiktor Hawrylik

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

from pathlib import Path
from typing import Any, Union


def validate_file_path(path: Union[Path, str]) -> Path:
    """Validate and convert file path to Path object.

    Args:
        path: File path as string or Path object

    Returns:
        Validated Path object

    Raises:
        FileNotFoundError: If file doesn't exist
        TypeError: If path is not string or Path

    Examples:
        >>> validate_file_path("existing_file.txt")
        Path('existing_file.txt')
    """
    if isinstance(path, str):
        path = Path(path)
    elif not isinstance(path, Path):
        raise TypeError(f"Path must be str or Path, got {type(path).__name__}")

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return path


def merge_dicts(*dicts: dict[str, Any]) -> dict[str, Any]:
    """Merge multiple dictionaries with later values overriding earlier ones.

    Args:
        *dicts: Variable number of dictionaries to merge

    Returns:
        Merged dictionary

    Examples:
        >>> merge_dicts({"a": 1}, {"b": 2}, {"a": 3})
        {'a': 3, 'b': 2}

        >>> merge_dicts({})
        {}
    """
    result: dict[str, Any] = {}
    for d in dicts:
        result.update(d)
    return result
