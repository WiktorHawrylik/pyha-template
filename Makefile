.PHONY: help install install-dev test test-cov lint format clean docs pre-commit notebook data-clean

# Default target
help:
	@echo "Python Library Template - Development Commands"
	@echo ""
	@echo "Available targets:"
	@echo "  install        - Install package in development mode"
	@echo "  install-dev    - Install package with development dependencies"
	@echo "  install-all    - Install all optional dependencies (dev, docs, test, data, ai)"
	@echo "  test           - Run tests"
	@echo "  test-cov       - Run tests with coverage report"
	@echo "  test-fast      - Run fast tests only (exclude slow and integration)"
	@echo "  lint           - Run all code quality checks (ruff + mypy)"
	@echo "  format         - Format code with ruff"
	@echo "  format-check   - Check code formatting without modifying"
	@echo "  clean          - Clean build artifacts and caches"
	@echo "  docs           - Build documentation with MkDocs"
	@echo "  docs-serve     - Serve documentation locally"
	@echo "  docs-deploy    - Deploy documentation to GitHub Pages"
	@echo "  pre-commit     - Install pre-commit hooks"
	@echo "  notebook       - Start Jupyter Lab for data exploration"
	@echo "  data-clean     - Clean data cache and temporary files"

install:
	uv pip install -e .

install-dev:
	uv sync --extra dev --extra test --extra docs

install-all:
	uv sync --all-extras

test:
	uv run pytest

test-cov:
	uv run pytest --cov=your_package_name --cov-report=html --cov-report=term

test-fast:
	uv run pytest -m "not slow and not integration"

lint:
	@echo "Running code quality checks..."
	@echo "→ Checking with ruff..."
	uv run ruff check src tests
	@echo "→ Checking formatting..."
	uv run ruff format --check src tests
	@echo "→ Type checking with mypy..."
	uv run mypy src
	@echo "✓ All checks passed!"

format:
	@echo "Formatting code..."
	uv run ruff check --fix src tests
	uv run ruff format src tests
	@echo "✓ Code formatted!"

format-check:
	uv run ruff format --check src tests

clean:
	@echo "Cleaning build artifacts and caches..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "✓ Cleaned!"

docs:
	@echo "Building documentation with MkDocs..."
	uv run mkdocs build

docs-serve:
	@echo "Serving documentation locally at http://127.0.0.1:8000"
	@lsof -ti :8000 | xargs kill -9 2>/dev/null || true
	uv run mkdocs serve

docs-deploy:
	@echo "Deploying documentation to GitHub Pages..."
	uv run mkdocs gh-deploy --force

pre-commit:
	uv run pre-commit install
	@echo "✓ Pre-commit hooks installed!"

notebook:
	@echo "Starting Jupyter Lab..."
	uv run jupyter lab

data-clean:
	@echo "Cleaning data cache and temporary files..."
	find data/ -name "*.tmp" -delete 2>/dev/null || true
	find data/ -name ".cache" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Data cache cleaned!"
