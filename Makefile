sources = .

.PHONY: .pre-commit  ## Check that pre-commit is installed
.pre-commit:
	@pre-commit -V || pip install pre-commit

.PHONY: .ruff  ## Check that ruff is installed
.ruff:
	@ruff -V || pip install ruff

.PHONY: .black  ## Check that black is installed
.black:
	@black -v || echo 'Please install black: https://github.com/psf/black'

.PHONY: .pytest  ## Check that pytest is installed
.pytest:
	@pytest -V || pip install pytest

.PHONY: .pytest-asyncio  ## Check that pytest is installed
.pytest-asyncio:
	@pip list | grep -i pytest-asyncio || pip install pytest-asyncio

.PHONY: install  ## Install/update the local library and associated dependencies
install:
	pip install .
	direnv allow .

.PHONY: setup  ## Install/update the pre-commit hooks for local development
setup: .pre-commit
	pre-commit install --install-hooks
	pre-commit autoupdate
	direnv allow .

.PHONY: format  ## Auto-format python source files
format: .black .ruff
	black $(sources)
	ruff check --fix $(sources)

.PHONY: lint  ## Lint python source files
lint: .black .ruff
	black $(sources) --check
	ruff check $(sources)

.PHONY: unit-test  ## Run all unit tests
unit-test: .pytest .pytest-asyncio
	pytest -m unit_test

.PHONY: integration-test  ## Run all integration tests
integration-test: .pytest .pytest-asyncio
	pytest -m integration_test

.PHONY: end-test  ## Run all end-to-end tests
end-test: .pytest .pytest-asyncio
	pytest -m end_test

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

.PHONY: help  ## Display this message
help:
	@grep -E \
		'^.PHONY: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".PHONY: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'
