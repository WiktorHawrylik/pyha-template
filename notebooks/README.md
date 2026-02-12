# Notebooks

This directory contains Jupyter notebooks for data exploration and analysis.

## Naming Convention

Number notebooks in execution order:

- `01_exploration.ipynb` - Initial data exploration
- `02_cleaning.ipynb` - Data cleaning and preparation
- `03_analysis.ipynb` - Main analysis
- `04_visualization.ipynb` - Visualizations and reporting

## Guidelines

### Before Committing

1. **Clear all outputs**: `Kernel` → `Restart & Clear Output`
2. **Run all cells**: Ensure notebook runs from top to bottom
3. **Add documentation**: Use markdown cells to explain your work

### Best Practices

- Keep notebooks focused on exploration and visualization
- Extract reusable code to `src/your_package_name/`
- Use relative paths for data files
- Document assumptions and findings
- Include data sources and dates

### Running Notebooks

Start Jupyter Lab:

```bash
make notebook
```

Or directly:

```bash
uv run jupyter lab
```

## Notebook Template

```python
# Notebook Title
# Author: Your Name
# Date: YYYY-MM-DD
# Purpose: Brief description

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Configuration
%matplotlib inline
pd.set_option('display.max_columns', None)

# Load data
data_path = Path("../data/raw/example.csv")
df = pd.read_csv(data_path)

# Analysis
# ...

# Findings
# Document your findings here
```

## Common Issues

### Kernel Not Found

Install ipykernel:

```bash
uv pip install ipykernel
```

### Missing Dependencies

Install data dependencies:

```bash
uv pip install "your-package-name[data]"
```

## Sharing Notebooks

- Export to HTML: `File` → `Export Notebook As` → `HTML`
- Share on nbviewer: Upload to GitHub and use <https://nbviewer.org/>
- Convert to slides: Use RISE extension

## Questions?

See the main documentation or open an issue.
