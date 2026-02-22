# Python Library Template

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](http://mypy-lang.org/)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://wiktorhawrylik.github.io/your-package-name/)

Wiktor Hawrylik Python library template optimized for agentic AI development and data-driven workflows.

- **Pre-configured tooling** - uv, ruff, mypy, pytest
- **AI-ready** - Optimized for GitHub Copilot, Cursor, Claude
- **Well-documented** - Comprehensive guides and API docs

## 📦 Installation

```bash
# Using uv (recommended)
uv pip install your-package-name

# Or using pip
pip install your-package-name
```

## 🚀 Quick Start

### Basic Usage

```python
from your_package_name import ExampleClass, process_data

# Process data with filtering
data = [{"value": 0.3}, {"value": 0.7}, {"value": 0.9}]
filtered = process_data(data, threshold=0.5)
print(filtered)  # [{"value": 0.7}, {"value": 0.9}]

# Use the example class
obj = ExampleClass("example", 42.0)
obj.increment(5.0)
print(obj.value)  # 47.0
```

### Using the Template

```bash
# Clone this repository
git clone https://github.com/WiktorHawrylik/python-library-template.git my-project
cd my-project
```

## 📚 Documentation

Complete documentation available at: **[https://WiktorHawrylik.github.io/your-package-name/](https://WiktorHawrylik.github.io/your-package-name/)**

- [Installation Guide](https://WiktorHawrylik.github.io/your-package-name/guide/installation/)
- [Template Usage Guide](https://WiktorHawrylik.github.io/your-package-name/guide/template-usage/)
- [Quick Start](https://WiktorHawrylik.github.io/your-package-name/guide/quickstart/)
- [API Reference](https://WiktorHawrylik.github.io/your-package-name/api/core/)
- [Contributing](https://WiktorHawrylik.github.io/your-package-name/contributing/)

## 🛠️ Requirements

- Python 3.11+
- uv (recommended) or pip
- make (for automation)

## 📄 License

AGPL-3.0 - see [LICENSE](LICENSE)

## 📝 TODO

### 🏗️ Architecture & Design

- [ ] Move `docs/development/_constitution.md` → `docs/design/_constitution.md`
- [ ] Add "Simplicity First" principles to development guide (minimal abstractions)
- [ ] Should some files be python agnostic? For migrations? Very limited - only constitution - it can refer to dev guidelines per language?
- [ ] **Database Backend for Agent Memory**
  - [ ] Evaluate DB options: SQLite (local), PostgreSQL (hosted), Redis (cache)
  - [ ] Design schema for conversation history, context, and learned patterns
  - [ ] Implement memory retention policy (TTL, size limits)
  - [ ] Add memory search/retrieval API for agents
  - [ ] Document memory management patterns in `docs/development/agent-memory.md`
  - [ ] Create migration path from file-based to DB-based memory
- [ ] **(optional) Smart Status Management**
  - [ ] Create `status.md` template with sections:
    - Current sprint/iteration goals
    - Active development tasks
    - Blocked items with blockers
    - Recently completed work
    - Key decisions and context
  - [ ] Design GitHub Issues/Projects integration strategy:
    - Auto-sync status.md ↔ GitHub Issues
    - Generate status.md from project boards
    - OR: Use GitHub as source of truth, status.md as cache
  - [ ] Add `.github/workflows/update-status.yml` for auto-sync
  - [ ] Implement status.md auto-loader in AI workspace context
  - [ ] Add status validation: ensure critical sections present
  - [ ] Document when to use status.md vs Issues vs ADRs
- [ ] **Structured Logging Framework**
  - [ ] Design logging schema in `docs/development/logging-design.md`:
    - Agent decisions and reasoning
    - Tool invocations and results
    - Code changes with intent
    - Test execution context
    - Error correlation chains
  - [ ] Implement log levels:
    - `AGENT_DEBUG`: Full reasoning traces
    - `AGENT_INFO`: High-level decisions
    - `AGENT_AUDIT`: All file modifications
  - [ ] Create `configs/logging.yaml`:
    - Development mode: verbose agent traces
    - Production mode: decisions + errors only
  - [ ] Add environment variable: `AGENT_DEV_MODE=true`
  - [ ] Implement structured log output (JSON for parsing)
  - [ ] Create log analysis tools:
    - `scripts/analyze_agent_logs.py` - extract patterns
    - Log viewer for debugging agent behavior
  - [ ] Add logging examples to `docs/guide/agentic-debugging.md`
  - [ ] Integrate with pytest: auto-enable AGENT_DEBUG in test failures
- [ ] **Cross-cutting Concerns**
  - [ ] Link agent memory to logging (trace decisions with context)
  - [ ] Use status.md as default context for agent sessions
  - [ ] Auto-update status.md when agents complete tasks
  - [ ] Log all agent edits to files referenced in status.md
- [ ] **Agent changes validation**
  - [ ] Repository specific framework to test any changes in agents
- [ ] MCP only as in ClawCode through CLI

### 🔧 Configuration & Tooling

- [ ] Consolidate `.editorconfig` settings into `pyproject.toml`
- [ ] Remove `.cursorrules` (replaced by AGENTS.md + \_constitution.md)
- [ ] Document `configs/` directory structure and usage
- [ ] Create `customize_template.py` script for easy template initialization

### 🧪 Testing & Quality

- [ ] Rethink testing strategy (unit, integration, E2E patterns)
- [ ] Add E2E data validation examples for larger pipelines
- [ ] Rethink CI/CD workflows (GitHub Actions optimization)

### 📊 Data Engineering

- [ ] Add Spark transformation examples and patterns
- [ ] Clarify data folder conventions (`data/`, `tests/fixtures/`)
- [ ] Document data validation patterns (schema, row-level, aggregates)
- [ ] For data tasks agents make lot's of silent assumptions, set up checks that e.g. whole dataset was read instead of the sample

### 🤖 Operationalisation Considerations

- [ ] PoC folder in root
- [ ] Design refactor strategy: PoC → operational = agent following dev rules

### 🤖 ML/AI Considerations

- [ ] Evaluate: Separate ML/AI template repo vs. extension guide?
- [ ] Notebooks strategy: PoC → operational workflow
- [ ] Human debugging interfaces for notebooks
- [ ] Notebook best practices and integration patterns

### 📚 Documentation

- [ ] Complete missing guide pages (data-processing.md, testing.md)
- [ ] Add architecture decision record (ADR) examples
- [ ] Document template customization workflow

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for guidelines.

## 📬 Contact

- **Report a problem**: [GitHub Issues](https://github.com/WiktorHawrylik/your-package-name/issues)
- **Ask a question**: [GitHub Discussions](https://github.com/WiktorHawrylik/your-package-name/discussions)
- **Autor**: Wiktor Hawrylik
- **Email**: <wiktor.hawrylik@gmail.com>

---

Made with ❤️ for the Python community
