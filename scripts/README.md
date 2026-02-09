# Scripts

This directory contains utility scripts for data processing, automation, and maintenance.

## Script Categories

### Data Processing
- `process_data.py` - Clean and transform raw data
- `download_data.py` - Download external data sources
- `validate_data.py` - Validate data integrity

### Maintenance
- `update_dependencies.py` - Update package dependencies
- `clean_cache.py` - Clean temporary files and caches

### Deployment
- `build_package.py` - Build distribution packages
- `deploy_docs.py` - Deploy documentation

## Script Template

```python
#!/usr/bin/env python3
"""Script description.

This script does X, Y, and Z.

Usage:
    python scripts/script_name.py [options]

Example:
    python scripts/script_name.py --input data/raw/file.csv
"""

import argparse
from pathlib import Path


def main() -> None:
    """Main script function."""
    parser = argparse.ArgumentParser(description="Script description")
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Input file path"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/output.csv"),
        help="Output file path"
    )

    args = parser.parse_args()

    # Script logic here
    print(f"Processing {args.input}...")
    # ...
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
```

## Guidelines

### Script Standards
- Add a shebang line: `#!/usr/bin/env python3`
- Include a docstring with usage examples
- Use argparse for command-line arguments
- Add type hints to all functions
- Handle errors gracefully with helpful messages
- Log progress for long-running scripts

### Error Handling
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    process_data(input_path)
    logger.info("Processing completed successfully")
except FileNotFoundError as e:
    logger.error(f"File not found: {e}")
    sys.exit(1)
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    sys.exit(1)
```

### Testing Scripts
Write tests for scripts in `tests/test_scripts.py`:

```python
def test_process_data_script():
    """Test process_data.py script."""
    # Test logic here
    pass
```

## Running Scripts

### From Command Line
```bash
python scripts/process_data.py --input data/raw/file.csv
```

### From Python
```python
from scripts import process_data
process_data.main()
```

### With uv
```bash
uv run python scripts/process_data.py
```

## Common Patterns

### Reading Config Files
```python
import json
from pathlib import Path

config_path = Path("configs/config.json")
config = json.loads(config_path.read_text())
```

### Progress Bars
```python
from tqdm import tqdm

for item in tqdm(items, desc="Processing"):
    process(item)
```

### Parallel Processing
```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as executor:
    results = list(executor.map(process_item, items))
```

## Questions?

See the main documentation or ask in discussions.
