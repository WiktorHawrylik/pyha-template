# Configuration Files

This directory contains configuration files for the application.

## File Formats

### JSON Configuration
```json
{
  "api_key": "${API_KEY}",
  "timeout": 30,
  "debug": false
}
```

### YAML Configuration
```yaml
api:
  base_url: https://api.example.com
  timeout: 30
  retry_attempts: 3

processing:
  batch_size: 100
  normalize: true
```

### TOML Configuration
```toml
[api]
base_url = "https://api.example.com"
timeout = 30

[processing]
batch_size = 100
normalize = true
```

## Using Configuration Files

### With Pydantic
```python
from pathlib import Path
from pydantic import BaseModel
import json

class Config(BaseModel):
    """Application configuration."""
    api_key: str
    timeout: int = 30
    debug: bool = False

config_path = Path("configs/config.json")
config = Config(**json.loads(config_path.read_text()))
```

### With Environment Variables
```python
import os
from pathlib import Path

# Load from file
config_path = Path("configs/config.json")
config = json.loads(config_path.read_text())

# Override with environment variables
config["api_key"] = os.getenv("API_KEY", config["api_key"])
```

## Best Practices

1. **Never commit secrets**
   - Use `.env` files for secrets (in `.gitignore`)
   - Use environment variables in production
   - Use placeholders like `${API_KEY}` in committed configs

2. **Validate configuration**
   - Use Pydantic for validation
   - Provide sensible defaults
   - Document all options

3. **Multiple environments**
   - `config.dev.json` - Development
   - `config.test.json` - Testing
   - `config.prod.json` - Production

4. **Document configuration**
   - Add comments explaining each option
   - Provide example files
   - Document default values

## Example Configuration Files

### config.example.json
```json
{
  "api": {
    "base_url": "https://api.example.com",
    "api_key": "${API_KEY}",
    "timeout": 30
  },
  "processing": {
    "batch_size": 100,
    "max_workers": 4
  },
  "logging": {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  }
}
```

### .env.example
```bash
# API Configuration
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com

# Processing
BATCH_SIZE=100
MAX_WORKERS=4

# Logging
LOG_LEVEL=INFO
```

## Loading Configuration

### Simple Approach
```python
from pathlib import Path
import json

def load_config(config_name: str = "config.json") -> dict:
    """Load configuration from file."""
    config_path = Path("configs") / config_name
    return json.loads(config_path.read_text())
```

### With Environment Override
```python
import os
from pathlib import Path
import json

def load_config(env: str = "dev") -> dict:
    """Load configuration with environment variables."""
    config_path = Path("configs") / f"config.{env}.json"
    config = json.loads(config_path.read_text())

    # Override with environment variables
    for key, value in config.items():
        if isinstance(value, str) and value.startswith("${"):
            env_var = value[2:-1]  # Remove ${ and }
            config[key] = os.getenv(env_var, value)

    return config
```

## Security

- Add `*.secret.*` to `.gitignore`
- Use environment variables for secrets
- Rotate API keys regularly
- Encrypt sensitive configuration files

## Questions?

See the main documentation for more information.
