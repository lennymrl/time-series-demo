help:
	@echo "format - format Python code with isort/Black"
	@echo "lint - check style with flake8"
	@echo "pytest - run the tests and measure the code coverage"
	@echo "test - run the code formatter, linter, type checker, tests and coverage"
	@echo "ci-test - run the Continuous Integration (CI) pipeline (check-only)"
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"

.PHONY: format
format:
	isort src tests
	black --line-length 100 src tests

.PHONY: lint
lint:
	mkdir -p reports
	pylint src tests

.PHONY: pytest
pytest:
	python -m pytest

.PHONY: test
test: format lint pytest

.PHONY: ci-test
ci-test:
	isort --check-only src tests
	black --line-length 100 --check src tests
	make lint
	make pytest

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr reports/
