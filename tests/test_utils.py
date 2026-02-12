"""Tests for utils module."""

import tempfile
from pathlib import Path

import pytest

from your_package_name.utils import merge_dicts, validate_file_path


class TestValidateFilePath:
    """Tests for validate_file_path function."""

    def test_valid_path_as_string(self) -> None:
        """Test validation with valid string path."""
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name

        try:
            result = validate_file_path(tmp_path)
            assert isinstance(result, Path)
            assert result.exists()
        finally:
            Path(tmp_path).unlink()

    def test_valid_path_as_path_object(self) -> None:
        """Test validation with valid Path object."""
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = Path(tmp.name)

        try:
            result = validate_file_path(tmp_path)
            assert isinstance(result, Path)
            assert result.exists()
        finally:
            tmp_path.unlink()

    def test_nonexistent_file_raises_error(self) -> None:
        """Test that nonexistent file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError, match="File not found"):
            validate_file_path("nonexistent_file.txt")

    def test_invalid_type_raises_error(self) -> None:
        """Test that invalid type raises TypeError."""
        with pytest.raises(TypeError, match="must be str or Path"):
            validate_file_path(123)  # type: ignore


class TestMergeDicts:
    """Tests for merge_dicts function."""

    def test_merge_two_dicts(self) -> None:
        """Test merging two dictionaries."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        result = merge_dicts(dict1, dict2)
        assert result == {"a": 1, "b": 2, "c": 3, "d": 4}

    def test_merge_with_override(self) -> None:
        """Test that later values override earlier ones."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        result = merge_dicts(dict1, dict2)
        assert result == {"a": 1, "b": 3, "c": 4}

    def test_merge_multiple_dicts(self) -> None:
        """Test merging more than two dictionaries."""
        dict1 = {"a": 1}
        dict2 = {"b": 2}
        dict3 = {"c": 3}
        result = merge_dicts(dict1, dict2, dict3)
        assert result == {"a": 1, "b": 2, "c": 3}

    def test_merge_empty_dicts(self) -> None:
        """Test merging empty dictionaries."""
        result = merge_dicts({}, {})
        assert result == {}

    def test_merge_no_dicts(self) -> None:
        """Test calling with no arguments."""
        result = merge_dicts()
        assert result == {}

    def test_original_dicts_unchanged(self) -> None:
        """Test that original dictionaries are not modified."""
        dict1 = {"a": 1}
        dict2 = {"b": 2}
        original_dict1 = dict1.copy()
        original_dict2 = dict2.copy()

        merge_dicts(dict1, dict2)

        assert dict1 == original_dict1
        assert dict2 == original_dict2
