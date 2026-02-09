# SPDX-License-Identifier: GPL-3.0-only

from python_library_template import greet


def test_greet_includes_name() -> None:
    assert greet("Codex") == "Hello, Codex!"
