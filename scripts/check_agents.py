#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
"""Fail if AGENTS.md is missing or empty."""

from __future__ import annotations

from pathlib import Path
import sys


def main() -> int:
    agents_file = Path("AGENTS.md")
    if not agents_file.exists():
        print("AGENTS.md is missing.")
        return 1
    if not agents_file.read_text(encoding="utf-8").strip():
        print("AGENTS.md is empty.")
        return 1
    print("AGENTS.md is present and non-empty.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
