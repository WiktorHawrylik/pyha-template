# Data Directory

This directory contains data files used in the project.

## Structure

- `raw/`: Original, immutable data files
- `processed/`: Cleaned and transformed data
- `external/`: Third-party data sources

## Guidelines

### Raw Data (`raw/`)

- **Never modify** files in this directory
- Keep original data as a reference
- Document data sources in README
- Use version control for small files
- Use DVC or Git LFS for large files

### Processed Data (`processed/`)

- Store output of data processing scripts
- Include processing metadata (date, script version, etc.)
- Document transformation steps

### External Data (`external/`)

- Store data from third-party sources
- Document license and attribution
- Include download/update scripts

## Best Practices

1. **Document Everything**: Add README files explaining:
   - Data source and collection method
   - Data schema and field descriptions
   - Any known issues or limitations
   - Update frequency and last update date

2. **Version Large Files**: Use DVC or Git LFS

   ```bash
   # Initialize DVC
   dvc init

   # Track data file
   dvc add data/raw/large_file.csv
   ```

3. **Never Commit Secrets**:
   - Use `.env` files for API keys
   - Add `.env` to `.gitignore`
   - Use environment variables

4. **Reproducibility**:
   - Document data versions
   - Use checksums to verify data integrity
   - Pin package versions in scripts

## Example Data Processing Workflow

```python
from pathlib import Path
import pandas as pd

# Load raw data
raw_path = Path("data/raw/input.csv")
df = pd.read_csv(raw_path)

# Process data
df_clean = df.dropna()
df_clean["normalized"] = df_clean["value"] / df_clean["value"].max()

# Save processed data
processed_path = Path("data/processed/output.csv")
df_clean.to_csv(processed_path, index=False)
```

## Data Privacy

- Do not commit sensitive or personal data
- Anonymize data before committing
- Follow GDPR and other regulations
- Use encryption for sensitive data

## Questions?

See the main [Contributing Guide](../CONTRIBUTING.md) for more information.
