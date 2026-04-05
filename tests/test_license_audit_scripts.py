"""Tests for the license-audit helper scripts.

This module exercises the script-level compliance workflow so the repository
does not rely on untested license-audit behavior.

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

import csv
import importlib.util
import sys
from pathlib import Path
from textwrap import dedent
from types import ModuleType

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path: str, module_name: str) -> ModuleType:
    """Load a script module directly from a repository path."""
    module_path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


LICENSE_HEADERS = load_module(
    ".agents/skills/license-audit/scripts/license_audit_headers.py",
    "license_audit_headers",
)
LICENSE_DEPENDENCIES = load_module(
    ".agents/skills/license-audit/scripts/license_audit_dependencies.py",
    "license_audit_dependencies",
)
LICENSE_SUMMARY = load_module(
    ".agents/skills/license-audit/scripts/summarize_license_audit.py",
    "summarize_license_audit",
)
LICENSE_REVIEW_MARKDOWN = load_module(
    ".agents/skills/license-audit/scripts/generate_review_decisions_markdown.py",
    "generate_review_decisions_markdown",
)


def write_file(path: Path, contents: str) -> Path:
    """Write text to a test file and return the created path."""
    path.write_text(dedent(contents).lstrip(), encoding="utf-8")
    return path


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> Path:
    """Write CSV rows for audit-script fixtures."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def create_summary_artifacts(tmp_path: Path) -> Path:
    """Create the minimum artifact set consumed by the summary script."""
    artifacts_dir = tmp_path / "build" / "license-compliance"
    write_csv(
        artifacts_dir / "header-audit.csv",
        ["file", "status", "missing_tokens"],
        [{"file": "src/example.py", "status": "PASS", "missing_tokens": ""}],
    )
    write_csv(
        artifacts_dir / "dependency-licenses.csv",
        ["Name", "Version", "License", "Author", "URL"],
        [{"Name": "example", "Version": "1.0.0", "License": "MPL-2.0", "Author": "", "URL": ""}],
    )
    write_csv(
        artifacts_dir / "dependency-license-audit.csv",
        ["Name", "Version", "License", "Category", "Author", "URL"],
        [
            {
                "Name": "example",
                "Version": "1.0.0",
                "License": "MPL-2.0",
                "Category": "REVIEW",
                "Author": "",
                "URL": "",
            }
        ],
    )
    write_file(artifacts_dir / "third-party-attribution-grep.txt", "")
    return artifacts_dir


def test_find_missing_requirements_accepts_valid_module_docstring(tmp_path: Path) -> None:
    """A complete module docstring header should pass the header audit."""
    file_path = write_file(
        tmp_path / "valid_header.py",
        '''
        """Example module description.

        Copyright (C) 2026 Example Maintainer

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
        ''',
    )

    assert (
        LICENSE_HEADERS.find_missing_requirements(
            file_path,
            LICENSE_HEADERS.REQUIRED_TOKENS,
        )
        == []
    )


def test_find_missing_requirements_checks_module_docstring_only(tmp_path: Path) -> None:
    """License text outside the module docstring should not satisfy the audit."""
    file_path = write_file(
        tmp_path / "misplaced_header.py",
        '''
        """Example module description.

        Copyright (C) 2026 Example Maintainer
        """

        # GNU Affero General Public License
        # This program is free software
        # WITHOUT ANY WARRANTY
        # https://www.gnu.org/licenses/
        ''',
    )

    assert LICENSE_HEADERS.find_missing_requirements(
        file_path,
        LICENSE_HEADERS.REQUIRED_TOKENS,
    ) == [
        "missing_token:GNU Affero General Public License",
        "missing_token:This program is free software",
        "missing_token:WITHOUT ANY WARRANTY",
        "missing_token:https://www.gnu.org/licenses/",
    ]


def test_find_missing_requirements_requires_description_before_copyright(tmp_path: Path) -> None:
    """The header should require a module description before copyright text."""
    file_path = write_file(
        tmp_path / "missing_description.py",
        '''
        """Copyright (C) 2026 Example Maintainer

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
        ''',
    )

    assert "module_description_missing" in LICENSE_HEADERS.find_missing_requirements(
        file_path,
        LICENSE_HEADERS.REQUIRED_TOKENS,
    )


@pytest.mark.parametrize(
    ("license_text", "expected"),
    [
        ("GNU Affero General Public License v3 or later (AGPLv3+)", "ALLOW"),
        ("AGPL-3.0-only", "ALLOW"),
        ("Mozilla Public License 2.0 (MPL 2.0)", "REVIEW"),
    ],
)
def test_classify_license_handles_agpl_variants(license_text: str, expected: str) -> None:
    """Dependency classification should recognize common AGPL spellings."""
    assert LICENSE_DEPENDENCIES.classify_license(license_text) == expected


def test_build_audit_rows_deduplicates_identical_entries(tmp_path: Path) -> None:
    """Duplicate pip-licenses rows should collapse into one audit row."""
    input_csv = write_csv(
        tmp_path / "dependency-licenses.csv",
        ["Name", "Version", "License", "Author", "URL"],
        [
            {
                "Name": "your-package-name",
                "Version": "0.1.0",
                "License": "GNU Affero General Public License v3 or later (AGPLv3+)",
                "Author": "Example Maintainer",
                "URL": "https://example.invalid",
            },
            {
                "Name": "your-package-name",
                "Version": "0.1.0",
                "License": "GNU Affero General Public License v3 or later (AGPLv3+)",
                "Author": "Example Maintainer",
                "URL": "https://example.invalid",
            },
        ],
    )

    rows = LICENSE_DEPENDENCIES.build_audit_rows(input_csv)

    assert len(rows) == 1
    assert rows[0]["Category"] == "ALLOW"


def test_build_markdown_renders_review_decisions_table() -> None:
    """The generated review page should contain summary counts and a table."""
    markdown = LICENSE_REVIEW_MARKDOWN.build_markdown(
        [
            {
                "Name": "certifi",
                "Version": "2026.1.4",
                "License": "Mozilla Public License 2.0 (MPL 2.0)",
                "Decision": "APPROVED",
                "ReviewedBy": "Example Maintainer",
                "ReviewedOn": "2026-04-05",
                "Reference": "https://example.invalid/mpl-review",
                "Rationale": "Compatible in this distribution model.",
            }
        ],
        Path("docs/development/license-review-decisions.csv"),
    )

    assert "# License Review Decisions" in markdown
    assert "- Documented decisions: 1" in markdown
    assert "[Source](https://example.invalid/mpl-review)" in markdown
    assert "| certifi | 2026.1.4 | Mozilla Public License 2.0 (MPL 2.0)" in markdown


def test_main_generates_review_decisions_markdown(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The generator should write a Markdown page from the decision CSV."""
    input_csv = write_csv(
        tmp_path / "license-review-decisions.csv",
        ["Name", "Version", "License", "Decision", "ReviewedBy", "ReviewedOn", "Reference", "Rationale"],
        [
            {
                "Name": "hypothesis",
                "Version": "6.151.6",
                "License": "MPL-2.0",
                "Decision": "APPROVED",
                "ReviewedBy": "Example Maintainer",
                "ReviewedOn": "2026-04-05",
                "Reference": "https://example.invalid/hypothesis-review",
                "Rationale": "Test-only dependency.",
            }
        ],
    )
    output_md = tmp_path / "license-review-decisions.md"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "generate_review_decisions_markdown.py",
            "--input-csv",
            str(input_csv),
            "--output-md",
            str(output_md),
        ],
    )

    LICENSE_REVIEW_MARKDOWN.main()

    markdown = output_md.read_text(encoding="utf-8")
    assert "hypothesis" in markdown
    assert "Test-only dependency." in markdown


def test_summary_main_fails_for_unresolved_review_rows(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Unresolved review rows should keep the audit in a failing state."""
    artifacts_dir = create_summary_artifacts(tmp_path)
    review_decisions_csv = write_csv(
        tmp_path / "docs" / "development" / "license-review-decisions.csv",
        ["Name", "Version", "License", "Decision", "ReviewedBy", "ReviewedOn", "Reference", "Rationale"],
        [],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "summarize_license_audit.py",
            "--artifacts-dir",
            str(artifacts_dir),
            "--review-decisions-csv",
            str(review_decisions_csv),
        ],
    )

    with pytest.raises(SystemExit, match="1"):
        LICENSE_SUMMARY.main()

    assert "Unresolved review-required dependencies remain" in capsys.readouterr().out


def test_summary_main_accepts_documented_review_decisions(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Approved review decisions should resolve matching REVIEW rows."""
    artifacts_dir = create_summary_artifacts(tmp_path)
    review_decisions_csv = write_csv(
        tmp_path / "docs" / "development" / "license-review-decisions.csv",
        ["Name", "Version", "License", "Decision", "ReviewedBy", "ReviewedOn", "Reference", "Rationale"],
        [
            {
                "Name": "example",
                "Version": "1.0.0",
                "License": "MPL-2.0",
                "Decision": "APPROVED",
                "ReviewedBy": "Example Maintainer",
                "ReviewedOn": "2026-04-05",
                "Reference": "https://example.invalid/review",
                "Rationale": "Reviewed and accepted.",
            }
        ],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "summarize_license_audit.py",
            "--artifacts-dir",
            str(artifacts_dir),
            "--review-decisions-csv",
            str(review_decisions_csv),
        ],
    )

    LICENSE_SUMMARY.main()


def test_load_review_decisions_rejects_incomplete_approved_rows(tmp_path: Path) -> None:
    """Approved review decisions should require maintainer documentation fields."""
    review_decisions_csv = write_csv(
        tmp_path / "license-review-decisions.csv",
        ["Name", "Version", "License", "Decision", "ReviewedBy", "ReviewedOn", "Reference", "Rationale"],
        [
            {
                "Name": "example",
                "Version": "1.0.0",
                "License": "MPL-2.0",
                "Decision": "APPROVED",
                "ReviewedBy": "",
                "ReviewedOn": "2026-04-05",
                "Reference": "https://example.invalid/review",
                "Rationale": "Reviewed and accepted.",
            }
        ],
    )

    with pytest.raises(ValueError, match="ReviewedBy"):
        LICENSE_SUMMARY.load_review_decisions(review_decisions_csv)
