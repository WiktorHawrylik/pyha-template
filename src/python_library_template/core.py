# SPDX-License-Identifier: GPL-3.0-only
"""Core functionality for the template package."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting.

    Args:
        name: Name to greet.
    """
    return f"Hello, {name}!"
