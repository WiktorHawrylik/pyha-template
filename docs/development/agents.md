# Agentic Development Rules

These rules apply to humans and LLMs working in this repository.

## Mandatory Guardrails

- Never commit secrets, credentials, or private keys.
- Do not add network calls in tests (no HTTP, no API calls, no live services).
- Keep public APIs stable; document any breaking changes explicitly.
- Write tests for behavior changes and keep existing tests passing.
- Prefer small, focused PRs.
- Update documentation when changing public APIs or workflows.
- Follow Conventional Commits for commit messages and PR titles.

## Code Quality Standards

- **Type hints**: Required on ALL functions and methods
- **Docstrings**: Google-style, comprehensive
- **Tests**: Minimum 80% coverage
- **Formatting**: Use `make format` before committing
- **Type checking**: Pass `make lint` without errors

## Design Principles

### Keep It Simple

- **Minimal abstractions**: Prefer clear, direct code over clever abstractions
- **Avoid premature optimization**: Write clear code first, optimize only when needed
- **No unnecessary layers**: Don't add middleware, decorators, or wrappers unless truly needed
- **Explicit over implicit**: Make behavior obvious; avoid magic
- **Flat is better than nested**: Avoid deep inheritance hierarchies and nested contexts

### Practical Examples

**✅ Good - Simple and direct:**
```python
def process_data(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Filter and transform data."""
    return [item for item in data if item.get("active")]
```

**❌ Bad - Unnecessary abstraction:**
```python
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> Any: ...

class FilterProcessor(DataProcessor):
    def process(self, data: list[dict]) -> list[dict]:
        return DataFilterStrategy().apply(data)
```

### When Abstractions Are OK

- **Reused 3+ times**: Extract to a function/class
- **External API contracts**: Interfaces for pluggable behavior
- **Testing**: Mocks and test fixtures
- **Framework requirements**: Django models, FastAPI routes, etc.

## Evaluation Checklist

- [ ] Run `make format && make lint && make test`
- [ ] Compare outputs before/after changes for regressions
- [ ] Ensure `.pre-commit-config.yaml` hooks pass
- [ ] Update CHANGELOG.md with changes
- [ ] Update relevant documentation

## Quick Commands

```bash
make format      # Auto-format code
make lint        # Check code quality
make test        # Run tests
make test-cov    # Run tests with coverage
```

## Documentation

For comprehensive guidelines, see:

- **[AI Development Guide](_constitution.md)** - Detailed AI coding patterns
- **[Template Usage](../guide/template-usage.md)** - How to use this template
- **[License Compliance](license-compliance.md)** - AGPL-3.0 requirements
- **[Contributing Guide](../../CONTRIBUTING.md)** - Full contribution guidelines

## License Compliance

This project is AGPL-3.0. All contributions must be compatible. See [License Compliance Guide](license-compliance.md).

---

**Remember**: Quality over speed. Write clear, tested, documented code.
