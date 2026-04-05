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
DEFAULT_REVIEW_DECISIONS_CSV: Final[Path] = Path("docs/development/license-review-decisions.csv")
APPROVED_REVIEW_DECISIONS: Final[set[str]] = {"ALLOW", "APPROVE", "APPROVED"}


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
    parser.add_argument(
        "--review-decisions-csv",
        type=Path,
        default=DEFAULT_REVIEW_DECISIONS_CSV,
        help="CSV file documenting maintainer decisions for review-required dependencies.",
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


def load_review_rows(audit_csv: Path) -> list[dict[str, str]]:
    """Load dependencies that still require a manual review decision.

    Args:
        audit_csv: Path to `dependency-license-audit.csv`.

    Returns:
        Review-classified dependency rows.
    """
    review_rows: list[dict[str, str]] = []
    with audit_csv.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("Category", "").strip().upper() == "REVIEW":
                review_rows.append(row)
    return review_rows


def load_review_decisions(review_decisions_csv: Path) -> list[dict[str, str]]:
    """Load documented maintainer review decisions when available.

    Args:
        review_decisions_csv: Path to the tracked review decision CSV.

    Returns:
        Parsed review decision rows, or an empty list if the file does not exist.

    Raises:
        ValueError: If required columns are missing or approved rows are incomplete.
    """
    if not review_decisions_csv.exists():
        return []

    with review_decisions_csv.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        required_fields = {
            "Name",
            "Version",
            "License",
            "Decision",
            "ReviewedBy",
            "ReviewedOn",
            "Reference",
            "Rationale",
        }
        missing_fields = sorted(required_fields.difference(fieldnames))
        if missing_fields:
            missing_display = ", ".join(missing_fields)
            raise ValueError(f"Review decisions CSV is missing required columns: {missing_display}")

        decisions = list(reader)

    for decision in decisions:
        normalized_decision = decision.get("Decision", "").strip().upper()
        if normalized_decision not in APPROVED_REVIEW_DECISIONS:
            continue
        missing_values = [
            field
            for field in ("ReviewedBy", "ReviewedOn", "Reference", "Rationale")
            if not decision.get(field, "").strip()
        ]
        if missing_values:
            missing_display = ", ".join(missing_values)
            dependency_name = decision.get("Name", "<unknown dependency>").strip()
            raise ValueError(f"Approved review decisions must include {missing_display}: {dependency_name}")

    return decisions


def normalize_match_field(value: str) -> str:
    """Normalize CSV fields used for review-decision matching."""
    return value.strip().casefold()


def decision_matches_review(
    decision: dict[str, str],
    review_row: dict[str, str],
) -> bool:
    """Return whether a documented decision resolves a review row.

    Name must match exactly (case-insensitive). Version and license fields may be
    left blank in the decision file to cover any matching version or license text.
    """
    if normalize_match_field(decision.get("Name", "")) != normalize_match_field(review_row.get("Name", "")):
        return False

    decision_version = normalize_match_field(decision.get("Version", ""))
    if decision_version and decision_version != normalize_match_field(review_row.get("Version", "")):
        return False

    decision_license = normalize_match_field(decision.get("License", ""))
    if decision_license and decision_license != normalize_match_field(review_row.get("License", "")):
        return False

    return decision.get("Decision", "").strip().upper() in APPROVED_REVIEW_DECISIONS


def resolve_review_rows(
    review_rows: list[dict[str, str]],
    review_decisions: list[dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Split review rows into documented and unresolved sets."""
    resolved: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []

    for review_row in review_rows:
        if any(decision_matches_review(decision, review_row) for decision in review_decisions):
            resolved.append(review_row)
        else:
            unresolved.append(review_row)

    return resolved, unresolved


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
    blocked_count, _ = count_dependency_categories(dependency_audit_csv)
    review_rows = load_review_rows(dependency_audit_csv)
    try:
        review_decisions = load_review_decisions(args.review_decisions_csv)
    except ValueError as exc:
        print(f"[ERROR] {exc}")
        raise SystemExit(1) from exc
    resolved_reviews, unresolved_reviews = resolve_review_rows(review_rows, review_decisions)
    attribution_matches = count_attribution_matches(attribution_txt)

    print("License compliance audit completed.")
    print(f"- Header violations: {header_violations}")
    print(f"- Blocked dependencies: {blocked_count}")
    print(f"- Review-required dependencies: {len(unresolved_reviews)}")
    print(f"- Reviewed dependency decisions: {len(resolved_reviews)}")
    print(f"- Third-party attribution checks: completed ({attribution_matches} matches)")
    print(f"Artifacts: {artifacts_dir.resolve()}/*")

    if unresolved_reviews:
        print(
            "[ERROR] Unresolved review-required dependencies remain. "
            f"Document maintainer decisions in {args.review_decisions_csv.resolve()}."
        )
        for row in unresolved_reviews:
            print(f"- {row.get('Name', '')} {row.get('Version', '')}: {row.get('License', '')}")

    if header_violations > 0 or blocked_count > 0 or unresolved_reviews:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
