#!/usr/bin/env python3
"""Example data processing script.

This script demonstrates best practices for writing scripts in this template:
- Clear documentation
- Type hints
- Error handling
- Logging
- Command-line arguments

Usage:
    python scripts/example_script.py --input data/raw/input.csv --output data/processed/output.csv

Example:
    python scripts/example_script.py --input data/raw/data.csv --threshold 0.5

Copyright (C) 2024 Your Name

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Any

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def process_file(input_path: Path, output_path: Path, threshold: float = 0.5) -> None:
    """Process data from input file and save to output file.

    Args:
        input_path: Path to input CSV file
        output_path: Path to output CSV file
        threshold: Threshold value for filtering (default: 0.5)

    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If threshold is invalid
    """
    logger.info(f"Processing {input_path}")

    # Validate inputs
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if not 0 <= threshold <= 1:
        raise ValueError(f"Threshold must be between 0 and 1, got {threshold}")

    # Example processing logic
    # In a real script, you would:
    # 1. Load data from input_path
    # 2. Process it according to your needs
    # 3. Save results to output_path

    logger.info(f"Using threshold: {threshold}")

    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Placeholder for actual processing
    # df = pd.read_csv(input_path)
    # df_processed = df[df['value'] >= threshold]
    # df_processed.to_csv(output_path, index=False)

    logger.info(f"Results saved to {output_path}")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description="Process data with threshold filtering",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process with default threshold (0.5)
  %(prog)s --input data/raw/input.csv --output data/processed/output.csv

  # Process with custom threshold
  %(prog)s --input data/raw/input.csv --output data/processed/output.csv --threshold 0.7

  # Enable verbose logging
  %(prog)s --input data/raw/input.csv --output data/processed/output.csv --verbose
        """,
    )

    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        required=True,
        help="Path to input CSV file",
    )

    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        required=True,
        help="Path to output CSV file",
    )

    parser.add_argument(
        "--threshold",
        "-t",
        type=float,
        default=0.5,
        help="Threshold value for filtering (default: 0.5)",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    return parser.parse_args()


def main() -> None:
    """Main script entry point."""
    args = parse_args()

    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")

    try:
        process_file(
            input_path=args.input,
            output_path=args.output,
            threshold=args.threshold,
        )
        logger.info("Processing completed successfully")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        sys.exit(1)

    except ValueError as e:
        logger.error(f"Invalid value: {e}")
        sys.exit(1)

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
