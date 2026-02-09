"""Fail if AGENTS.md is missing or empty."""

from pathlib import Path


def main() -> None:
    agents_file = Path("AGENTS.md")
    if not agents_file.exists():
        raise SystemExit("AGENTS.md is required but missing.")
    if not agents_file.read_text(encoding="utf-8").strip():
        raise SystemExit("AGENTS.md must not be empty.")


if __name__ == "__main__":
    main()
