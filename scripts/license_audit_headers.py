#!/usr/bin/env python3
"""Audit Python files for required AGPL license header tokens.

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

from __future__ import annotations

import argparse
import csv
from pathlib import Path

DEFAULT_ROOTS: tuple[str, ...] = ("src", "tests", "scripts")
DEFAULT_OUTPUT: str = "build/license-compliance/header-audit.csv"
REQUIRED_TOKENS: tuple[str, ...] = (
    "GNU Affero General Public License",
    "This program is free software",
    "WITHOUT ANY WARRANTY",
    "https://www.gnu.org/licenses/",
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Audit Python files for required AGPL license header tokens.",
    )
    parser.add_argument(
        "--roots",
        nargs="+",
        default=list(DEFAULT_ROOTS),
        help="Root directories to scan for Python files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(DEFAULT_OUTPUT),
        help="Path to CSV output report.",
    )
    return parser.parse_args()


def collect_python_files(roots: list[Path]) -> list[Path]:
    """Collect Python files recursively from provided roots.

    Args:
        roots: Directories to search.

    Returns:
        Sorted list of discovered Python file paths.
    """
    files: list[Path] = []
    for root in roots:
        if root.exists():
            files.extend(root.rglob("*.py"))
    return sorted(files)


def find_missing_tokens(file_path: Path, required_tokens: tuple[str, ...]) -> list[str]:
    """Find required license tokens missing from a file.

    Args:
        file_path: File to inspect.
        required_tokens: Tokens that must appear in the file.

    Returns:
        List of missing tokens. Empty list means the file passes.
    """
    text = file_path.read_text(encoding="utf-8")
    return [token for token in required_tokens if token not in text]


def write_audit_report(
    files: list[Path],
    output_path: Path,
    required_tokens: tuple[str, ...],
) -> list[tuple[Path, list[str]]]:
    """Write header audit report and return violations.

    Args:
        files: Python files to audit.
        output_path: CSV file destination.
        required_tokens: Tokens that must appear in each file.

    Returns:
        List of `(file_path, missing_tokens)` for files that failed.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    violations: list[tuple[Path, list[str]]] = []

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["file", "status", "missing_tokens"])

        for file_path in files:
            missing_tokens = find_missing_tokens(file_path, required_tokens)
            status = "FAIL" if missing_tokens else "PASS"
            writer.writerow([str(file_path), status, "; ".join(missing_tokens)])
            if missing_tokens:
                violations.append((file_path, missing_tokens))

    return violations


def main() -> None:
    """Run the header audit and exit non-zero on violations."""
    args = parse_args()
    roots = [Path(root) for root in args.roots]
    files = collect_python_files(roots)
    violations = write_audit_report(files, args.output, REQUIRED_TOKENS)

    print(f"Audited files: {len(files)}")
    print(f"Header violations: {len(violations)}")
    if violations:
        for file_path, missing_tokens in violations:
            print(f"- {file_path}: missing {missing_tokens}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
