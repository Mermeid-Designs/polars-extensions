sources = .

.PHONY: help  ## Display this message
help:
	@grep -E \
		'^.PHONY: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".PHONY: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'

.PHONY: setup  ## Install/update the pre-commit hooks for local development
setup: check-pre-commit
	pre-commit install --install-hooks
	pre-commit autoupdate


.PHONY: install  ## Install/update the local library and associated dependencies
install:
	@poetry -V || pip install poetry
	poetry install

.PHONY: clean  ## Clear local caches and build artifacts
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

.PHONY: load-env  ## Load the environment variables from the .envrc file
load-env:
	eval "$(direnv export bash)"
	eval "$(direnv hook zsh)"
	direnv allow .

# ==============================================================================
# =========================== CODE QUALITY CHECKS =============================
# ==============================================================================

.PHONY: lint  ## Lint python source files
lint: check-black check-ruff
	poetry run black $(sources) --check
	poetry run ruff check $(sources)

.PHONY: format  ## Auto-format python source files
format: check-black check-ruff
	poetry run black $(sources)
	poetry run ruff check --fix $(sources)

# ------------------------------- PRIVATE COMMANDS -------------------------------

## Check that pre-commit is installed
check-pre-commit: install
	@poetry show pre-commit || poetry add pre-commit --group dev

## Check that ruff is installed
check-ruff: install
	@poetry show ruff || poetry add ruff --group formatting

## Check that black is installed
check-black: install
	@poetry show black || poetry add black --group formatting

# ==============================================================================
# =============================== TESTING =====================================
# ==============================================================================

.PHONY: unit-test  ## Run all unit tests
unit-test: check-pytest check-pytest-asyncio
	poetry run pytest -m unit_test

.PHONY: integration-test  ## Run all integration tests
integration-test: check-pytest check-pytest-asyncio
	poetry run pytest -m integration_test

.PHONY: end-test  ## Run all end-to-end tests
end-test: check-pytest check-pytest-asyncio
	poetry run pytest -m end_test

# ------------------------------- PRIVATE COMMANDS -------------------------------

## Check that pytest is installed
check-pytest: install
	@poetry show pytest || poetry add pytest --group test

## Check that pytest-asyncio is installed
check-pytest-asyncio: install
	@poetry show pytest-asyncio || poetry add pytest-asyncio --group test
