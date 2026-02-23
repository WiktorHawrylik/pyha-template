"""Tests for core module.

This module demonstrates comprehensive testing practices including:
unit tests, edge-case checks, and error handling validation.

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

import pytest

from your_package_name.core import ExampleClass, process_data


class TestProcessData:
    """Tests for process_data function."""

    def test_basic_filtering(self) -> None:
        """Test basic data filtering with threshold."""
        data = [{"value": 0.3}, {"value": 0.7}, {"value": 0.9}]
        result = process_data(data, threshold=0.5)
        assert len(result) == 2
        assert result[0]["value"] == 0.7
        assert result[1]["value"] == 0.9

    def test_threshold_boundary(self) -> None:
        """Test that values equal to threshold are included."""
        data = [{"value": 0.5}, {"value": 0.6}]
        result = process_data(data, threshold=0.5)
        assert len(result) == 2

    def test_default_threshold(self) -> None:
        """Test using default threshold value."""
        data = [{"value": 0.3}, {"value": 0.7}]
        result = process_data(data)
        assert len(result) == 1
        assert result[0]["value"] == 0.7

    def test_empty_result(self) -> None:
        """Test when no items meet threshold."""
        data = [{"value": 0.1}, {"value": 0.2}]
        result = process_data(data, threshold=0.5)
        assert len(result) == 0

    def test_all_items_included(self) -> None:
        """Test when all items meet threshold."""
        data = [{"value": 0.8}, {"value": 0.9}]
        result = process_data(data, threshold=0.5)
        assert len(result) == 2

    def test_empty_data_raises_error(self) -> None:
        """Test that empty data raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            process_data([])

    def test_invalid_threshold_too_high(self) -> None:
        """Test that threshold > 1 raises ValueError."""
        with pytest.raises(ValueError, match="between 0 and 1"):
            process_data([{"value": 0.5}], threshold=1.5)

    def test_invalid_threshold_negative(self) -> None:
        """Test that negative threshold raises ValueError."""
        with pytest.raises(ValueError, match="between 0 and 1"):
            process_data([{"value": 0.5}], threshold=-0.1)

    def test_missing_value_key(self) -> None:
        """Test that missing 'value' key raises KeyError."""
        data = [{"name": "test"}]
        with pytest.raises(KeyError, match="missing 'value' key"):
            process_data(data)

    def test_non_numeric_value(self) -> None:
        """Test that non-numeric value raises TypeError."""
        data = [{"value": "not a number"}]
        with pytest.raises(TypeError, match="must be numeric"):
            process_data(data)

    def test_preserves_order(self) -> None:
        """Test that original order is preserved."""
        data = [{"value": 0.9}, {"value": 0.7}, {"value": 0.8}]
        result = process_data(data, threshold=0.5)
        assert result[0]["value"] == 0.9
        assert result[1]["value"] == 0.7
        assert result[2]["value"] == 0.8

    def test_does_not_modify_original(self) -> None:
        """Test that original data is not modified."""
        data = [{"value": 0.3}, {"value": 0.7}]
        original_data = data.copy()
        process_data(data, threshold=0.5)
        assert data == original_data


class TestExampleClass:
    """Tests for ExampleClass."""

    def test_initialization(self) -> None:
        """Test basic initialization."""
        obj = ExampleClass("test", 42.0)
        assert obj.name == "test"
        assert obj.value == 42.0
        assert obj.metadata == {}

    def test_initialization_with_metadata(self) -> None:
        """Test initialization with metadata."""
        metadata = {"key": "value"}
        obj = ExampleClass("test", 10.0, metadata=metadata)
        assert obj.metadata == metadata

    def test_empty_name_raises_error(self) -> None:
        """Test that empty name raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            ExampleClass("", 10.0)

    def test_negative_value_raises_error(self) -> None:
        """Test that negative value raises ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            ExampleClass("test", -5.0)

    def test_increment_basic(self) -> None:
        """Test basic increment functionality."""
        obj = ExampleClass("test", 10.0)
        obj.increment(5.0)
        assert obj.value == 15.0

    def test_increment_default(self) -> None:
        """Test increment with default amount."""
        obj = ExampleClass("test", 10.0)
        obj.increment()
        assert obj.value == 11.0

    def test_increment_negative_raises_error(self) -> None:
        """Test that negative increment raises ValueError."""
        obj = ExampleClass("test", 10.0)
        with pytest.raises(ValueError, match="non-negative"):
            obj.increment(-5.0)

    def test_increment_non_numeric_raises_error(self) -> None:
        """Test that non-numeric increment raises TypeError."""
        obj = ExampleClass("test", 10.0)
        with pytest.raises(TypeError, match="must be numeric"):
            obj.increment("not a number")  # type: ignore[arg-type]

    def test_reset(self) -> None:
        """Test reset functionality."""
        obj = ExampleClass("test", 42.0)
        obj.reset()
        assert obj.value == 0.0

    def test_metadata_returns_copy(self) -> None:
        """Test that metadata property returns a copy."""
        metadata = {"key": "value"}
        obj = ExampleClass("test", 10.0, metadata=metadata)
        retrieved_metadata = obj.metadata
        retrieved_metadata["new_key"] = "new_value"
        # Original metadata should be unchanged
        assert obj.metadata == {"key": "value"}

    def test_repr(self) -> None:
        """Test string representation."""
        obj = ExampleClass("test", 42.0)
        assert repr(obj) == "ExampleClass(name='test', value=42.0)"

    def test_equality(self) -> None:
        """Test equality comparison."""
        obj1 = ExampleClass("test", 42.0)
        obj2 = ExampleClass("test", 42.0)
        obj3 = ExampleClass("test", 43.0)
        obj4 = ExampleClass("other", 42.0)

        assert obj1 == obj2
        assert obj1 != obj3
        assert obj1 != obj4

    def test_equality_with_non_instance(self) -> None:
        """Test equality with non-ExampleClass object."""
        obj = ExampleClass("test", 42.0)
        assert obj != "not an ExampleClass"
        assert obj != 42


@pytest.mark.slow
class TestSlowOperations:
    """Tests marked as slow for optional execution."""

    def test_large_dataset(self) -> None:
        """Test processing large dataset."""
        # Example of slow test that can be skipped
        large_data = [{"value": i / 1000} for i in range(10000)]
        result = process_data(large_data, threshold=0.5)
        # Values from i=500 (0.5) to i=9999 (9.999) inclusive = 9500 items
        assert len(result) == 9500
