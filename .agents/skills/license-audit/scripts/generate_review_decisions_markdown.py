#!/usr/bin/env python3
"""Generate Markdown documentation from license review decisions CSV.

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

DEFAULT_INPUT_CSV: Final[Path] = Path("docs/development/license-review-decisions.csv")
DEFAULT_OUTPUT_MD: Final[Path] = Path("docs/development/license-review-decisions.md")
FIELDNAMES: Final[tuple[str, ...]] = (
    "Name",
    "Version",
    "License",
    "Decision",
    "ReviewedBy",
    "ReviewedOn",
    "Reference",
    "Rationale",
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed CLI arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate Markdown from license review decision CSV data.",
    )
    parser.add_argument(
        "--input-csv",
        type=Path,
        default=DEFAULT_INPUT_CSV,
        help="CSV file containing documented license review decisions.",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=DEFAULT_OUTPUT_MD,
        help="Markdown file to generate for published documentation.",
    )
    return parser.parse_args()


def load_rows(input_csv: Path) -> list[dict[str, str]]:
    """Load review decision rows from CSV.

    Args:
        input_csv: CSV path to read.

    Returns:
        Parsed rows, or an empty list when the file does not exist.

    Raises:
        ValueError: If the CSV is missing required columns.
    """
    if not input_csv.exists():
        return []

    with input_csv.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = tuple(reader.fieldnames or ())
        missing_fields = [field for field in FIELDNAMES if field not in fieldnames]
        if missing_fields:
            missing_display = ", ".join(missing_fields)
            raise ValueError(f"Review decisions CSV is missing required columns: {missing_display}")
        return list(reader)


def escape_cell(value: str) -> str:
    """Escape a Markdown table cell value."""
    return value.replace("|", r"\|").replace("\n", " ").strip()


def format_reference(value: str) -> str:
    """Format the reference cell as a Markdown link when present."""
    reference = value.strip()
    if not reference:
        return ""
    return f"[Source]({reference})"


def build_markdown(rows: list[dict[str, str]], input_csv: Path) -> str:
    """Render the published Markdown page.

    Args:
        rows: Review decision rows.
        input_csv: Source CSV path used to generate the page.

    Returns:
        Markdown document text.
    """
    approved_count = sum(1 for row in rows if row.get("Decision", "").strip().upper() == "APPROVED")
    pending_count = len(rows) - approved_count
    lines = [
        "# License Review Decisions",
        "",
        "> This page is generated from "
        f"`{input_csv.as_posix()}` by "
        "`.agents/skills/license-audit/scripts/generate_review_decisions_markdown.py`.",
        "> Edit the CSV, then rerun the license audit workflow to refresh this page.",
        "",
        "## Summary",
        "",
        f"- Documented decisions: {len(rows)}",
        f"- Approved decisions: {approved_count}",
        f"- Other decisions: {pending_count}",
        "",
    ]

    if not rows:
        lines.extend(
            [
                "## Decisions",
                "",
                "No documented review decisions yet.",
                "",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            "## Decisions",
            "",
            "| Name | Version | License | Decision | Reviewed By | Reviewed On | Reference | Rationale |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_cell(row.get("Name", "")),
                    escape_cell(row.get("Version", "")),
                    escape_cell(row.get("License", "")),
                    escape_cell(row.get("Decision", "")),
                    escape_cell(row.get("ReviewedBy", "")),
                    escape_cell(row.get("ReviewedOn", "")),
                    format_reference(row.get("Reference", "")),
                    escape_cell(row.get("Rationale", "")),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def write_markdown(output_md: Path, contents: str) -> None:
    """Write the generated Markdown file."""
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(contents, encoding="utf-8")


def main() -> None:
    """Generate the published Markdown page from the decision CSV."""
    args = parse_args()
    try:
        rows = load_rows(args.input_csv)
    except ValueError as exc:
        print(f"[ERROR] {exc}")
        raise SystemExit(1) from exc

    contents = build_markdown(rows, args.input_csv)
    write_markdown(args.output_md, contents)
    print(f"Generated review decisions page: {args.output_md.resolve()}")


if __name__ == "__main__":
    main()
