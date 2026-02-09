# SPDX-License-Identifier: GPL-3.0-only

from python_library_template.core import greet


def test_smoke_greet() -> None:
    assert "Hello" in greet("Template")
