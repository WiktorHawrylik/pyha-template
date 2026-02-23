#!/usr/bin/env python3
"""Summarize license compliance audit artifacts and enforce fail gates.

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
from typing import Final

HEADER_ARTIFACT: Final[str] = "header-audit.csv"
DEPENDENCY_AUDIT_ARTIFACT: Final[str] = "dependency-license-audit.csv"
DEPENDENCY_LIST_ARTIFACT: Final[str] = "dependency-licenses.csv"
ATTRIBUTION_ARTIFACT: Final[str] = "third-party-attribution-grep.txt"


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Summarize license audit artifacts and exit non-zero on fail gates.",
    )
    parser.add_argument(
        "--artifacts-dir",
        type=Path,
        default=Path("build/license-compliance"),
        help="Directory containing generated audit artifacts.",
    )
    return parser.parse_args()


def count_header_violations(header_csv: Path) -> int:
    """Count `FAIL` rows in the header audit report.

    Args:
        header_csv: Path to `header-audit.csv`.

    Returns:
        Number of header violations.
    """
    violations = 0
    with header_csv.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("status", "").strip().upper() == "FAIL":
                violations += 1
    return violations


def count_dependency_categories(audit_csv: Path) -> tuple[int, int]:
    """Count blocked and review dependency rows.

    Args:
        audit_csv: Path to `dependency-license-audit.csv`.

    Returns:
        Tuple of `(blocked_count, review_count)`.
    """
    blocked = 0
    review = 0
    with audit_csv.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            category = row.get("Category", "").strip().upper()
            if category == "BLOCK":
                blocked += 1
            elif category == "REVIEW":
                review += 1
    return blocked, review


def count_attribution_matches(attribution_txt: Path) -> int:
    """Count attribution marker matches.

    Args:
        attribution_txt: Path to grep output artifact.

    Returns:
        Number of matched lines.
    """
    with attribution_txt.open(encoding="utf-8") as handle:
        return sum(1 for _ in handle)


def require_artifacts(artifacts_dir: Path) -> tuple[Path, Path, Path, Path]:
    """Validate required artifacts exist.

    Args:
        artifacts_dir: Directory containing audit artifacts.

    Returns:
        Paths to required artifacts.

    Raises:
        FileNotFoundError: If any required artifact is missing.
    """
    header_csv = artifacts_dir / HEADER_ARTIFACT
    dependency_list_csv = artifacts_dir / DEPENDENCY_LIST_ARTIFACT
    dependency_audit_csv = artifacts_dir / DEPENDENCY_AUDIT_ARTIFACT
    attribution_txt = artifacts_dir / ATTRIBUTION_ARTIFACT

    required_paths = (
        header_csv,
        dependency_list_csv,
        dependency_audit_csv,
        attribution_txt,
    )
    missing = [path for path in required_paths if not path.exists()]
    if missing:
        missing_display = ", ".join(str(path) for path in missing)
        raise FileNotFoundError(f"Missing required artifacts: {missing_display}")

    return header_csv, dependency_list_csv, dependency_audit_csv, attribution_txt


def main() -> None:
    """Load artifacts, print summary snippet, and enforce fail gates."""
    args = parse_args()
    artifacts_dir = args.artifacts_dir

    try:
        header_csv, _, dependency_audit_csv, attribution_txt = require_artifacts(artifacts_dir)
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")
        raise SystemExit(1) from exc

    header_violations = count_header_violations(header_csv)
    blocked_count, review_count = count_dependency_categories(dependency_audit_csv)
    attribution_matches = count_attribution_matches(attribution_txt)

    print("License compliance audit completed.")
    print(f"- Header violations: {header_violations}")
    print(f"- Blocked dependencies: {blocked_count}")
    print(f"- Review-required dependencies: {review_count}")
    print(f"- Third-party attribution checks: completed ({attribution_matches} matches)")
    print(f"Artifacts: {artifacts_dir.resolve()}/*")

    if header_violations > 0 or blocked_count > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
