#!/usr/bin/env python3
"""Template customization script.

This script helps you customize the template for your specific project by
replacing placeholder text with your actual project information.

Usage:
    python scripts/customize_template.py

The script will prompt you for:
- Project name (PyPI package name)
- Module name (Python import name)
- Author name
- Author email
- GitHub username
- Project description

It will then update all relevant files with your information.

Copyright (C) 2024 Template Authors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import sys
from pathlib import Path


def prompt_user() -> dict[str, str]:
    """Prompt user for project information.

    Returns:
        Dictionary containing project configuration
    """
    print("=" * 60)
    print("Python Library Template Customization")
    print("=" * 60)
    print()
    print("This script will customize the template with your project details.")
    print()

    config = {}

    # Package name (kebab-case for PyPI)
    config["package_name"] = input("Package name (kebab-case, e.g., my-awesome-lib): ").strip()

    # Module name (snake_case for Python imports)
    default_module = config["package_name"].replace("-", "_")
    module = input(f"Module name (snake_case) [{default_module}]: ").strip()
    config["module_name"] = module if module else default_module

    # Author information
    config["author_name"] = input("Author name: ").strip()
    config["author_email"] = input("Author email: ").strip()

    # GitHub username
    config["github_user"] = input("GitHub username: ").strip()

    # Project description
    config["description"] = input("Project description: ").strip()

    print()
    print("Configuration summary:")
    print("-" * 60)
    for key, value in config.items():
        print(f"  {key}: {value}")
    print("-" * 60)

    confirm = input("Proceed with customization? (y/n): ").strip().lower()
    if confirm != "y":
        print("Customization cancelled.")
        sys.exit(0)

    return config


def replace_in_file(file_path: Path, replacements: dict[str, str]) -> None:
    """Replace placeholders in a file.

    Args:
        file_path: Path to file to modify
        replacements: Dictionary of {old_text: new_text}
    """
    if not file_path.exists():
        return

    content = file_path.read_text()
    modified = content

    for old, new in replacements.items():
        modified = modified.replace(old, new)

    if modified != content:
        file_path.write_text(modified)
        print(f"  ✓ Updated: {file_path}")


def customize_template(config: dict[str, str]) -> None:
    """Customize all template files.

    Args:
        config: Project configuration dictionary
    """
    print()
    print("Customizing template files...")
    print()

    # Define replacements
    replacements = {
        "your-package-name": config["package_name"],
        "your_package_name": config["module_name"],
        "Your Name": config["author_name"],
        "your.email@example.com": config["author_email"],
        "WiktorHawrylik": config["github_user"],
        "A modern Python library template": config["description"],
    }

    # Files and directories to process
    files_to_process = [
        "README.md",
        "pyproject.toml",
        "mkdocs.yml",
        "CONTRIBUTING.md",
        "docs/index.md",
    ]

    # Process specific files
    for file_name in files_to_process:
        file_path = Path(file_name)
        replace_in_file(file_path, replacements)

    # Process all Python files
    for py_file in Path("src").rglob("*.py"):
        replace_in_file(py_file, replacements)

    for py_file in Path("tests").rglob("*.py"):
        replace_in_file(py_file, replacements)

    # Process documentation files
    for md_file in Path("docs").rglob("*.md"):
        replace_in_file(md_file, replacements)

    # Rename source directory
    old_src = Path("src/your_package_name")
    new_src = Path(f"src/{config['module_name']}")

    if old_src.exists() and old_src != new_src:
        old_src.rename(new_src)
        print(f"  ✓ Renamed: {old_src} → {new_src}")

    print()
    print("=" * 60)
    print("Customization complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Review the changes: git diff")
    print("  2. Install dependencies: make install-dev")
    print("  3. Run tests: make test")
    print("  4. Start coding!")
    print()


def main() -> None:
    """Main entry point."""
    try:
        config = prompt_user()
        customize_template(config)
    except KeyboardInterrupt:
        print("\n\nCustomization cancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
