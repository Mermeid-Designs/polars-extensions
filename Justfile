sources:="."

# Lists available commands
help:
    just --list

# Install/update the pre-commit hooks for local development
setup: check-pre-commit
	pre-commit install --install-hooks
	pre-commit autoupdate

# Install/update the local library and associated dependencies
install:
	@poetry -V || pip install poetry
	poetry install

# Clear local caches and build artifacts
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`
	rm -f `find . -type f -name '*~'`
	rm -f `find . -type f -name '.*~'`
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf build
	rm -rf dist
	rm -rf site

# Load the environment variables from the .envrc file
load-env:
	eval "$(direnv export bash)"
	eval "$(direnv hook zsh)"
	direnv allow .

# ==============================================================================
# =========================== CODE QUALITY CHECKS =============================
# ==============================================================================

# Lint python source files
lint: check-ruff check-black
	poetry run black {{sources}} --check
	poetry run ruff check {{sources}}

# Format python source files
format: check-ruff check-black
	poetry run black {{sources}}
	poetry run ruff check --fix {{sources}}

# ------------------------------- PRIVATE COMMANDS -------------------------------

# Check that pre-commit is installed
[private]
check-pre-commit:
	poetry show pre-commit || poetry add pre-commit --group dev

# Check that ruff is installed
[private]
check-ruff: install
	poetry show ruff || poetry add ruff --group formatting

# Check that black is installed
[private]
check-black: install
	poetry show black || poetry add black --group formatting

# ==============================================================================
# =============================== TESTING =====================================
# ==============================================================================

# Run all unit tests
unit-test: check-pytest check-pytest-asyncio
	poetry run pytest -m unit_test

# Run all integration tests
integration-test: check-pytest check-pytest-asyncio
	poetry run pytest -m integration_test

# Run all end-to-end tests
e2e-test: check-pytest check-pytest-asyncio
	poetry run pytest -m end_test

# ------------------------------- PRIVATE COMMANDS -------------------------------

# Check that pytest is installed
[private]
check-pytest: install
	poetry show pytest || poetry add pytest --group test

# Check that pytest-asyncio is installed
[private]
check-pytest-asyncio: install
	poetry show pytest-asyncio || poetry add pytest-asyncio --group test
