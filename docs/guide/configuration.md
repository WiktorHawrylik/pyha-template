# Configuration

This guide explains how to configure your application.

## Configuration Files

Configuration files are stored in the `configs/` directory. See [configs/README.md](https://github.com/WiktorHawrylik/your-package-name/blob/main/configs/README.md) for details.

## Environment Variables

The application can be configured using environment variables:

```bash
# API Configuration
export API_KEY="your-api-key"
export API_BASE_URL="https://api.example.com"
export API_TIMEOUT=30

# Processing
export BATCH_SIZE=100
export MAX_WORKERS=4

# Logging
export LOG_LEVEL=INFO
```

## Using .env Files

Create a `.env` file in the project root:

```bash
# .env
API_KEY=your-api-key
API_BASE_URL=https://api.example.com
BATCH_SIZE=100
```

Load with python-dotenv:

```python
from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Access variables
api_key = os.getenv('API_KEY')
```

## Configuration with Pydantic

Recommended approach using Pydantic v2 with pydantic-settings:

```python
from pydantic import Field
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """Application settings."""

    api_key: str = Field(..., description="API key for service")
    api_base_url: str = Field(
        default='https://api.example.com',
        description="Base URL for API"
    )
    batch_size: int = Field(default=100, description="Batch size for processing")

    model_config = {
        'env_file': '.env',
        'env_file_encoding': 'utf-8',
    }

# Usage
settings = Settings()
print(settings.api_key)
```

## Multiple Environments

Support different configurations per environment:

```python
import os
from pathlib import Path
import json
from typing import Any

def load_config(env: str | None = None) -> dict[str, Any]:
    """Load configuration for specified environment."""
    if env is None:
        env = os.getenv('ENVIRONMENT', 'dev')

    config_file = Path('configs') / f'config.{env}.json'
    return json.loads(config_file.read_text())

# Usage
config = load_config('prod')
```

## Best Practices

1. **Never commit secrets**: Use `.env` files (in `.gitignore`)
2. **Provide defaults**: Sensible defaults for all settings
3. **Validate early**: Validate configuration at startup
4. **Document everything**: Explain all configuration options
5. **Use type hints**: Type all configuration values
