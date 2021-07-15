# 025200812_cpall_ai_ordering_model
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

<!-- TOC depthFrom:2 depthTo:3 -->

- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Tests](#testing)
  - [Code formatter isort/Black](#run-the-code-formatter)
  - [Linter - pylint](#run-the-linter)
  - [Optional static type checker](#run-the-optional-static-type-checker)
  - [Unit tests - pytest](#run-the-unit-tests)
- [Resources](#resources)

<!-- /TOC -->

## Installation

## Dependencies

Dependencies are managed by [Pipenv](https://docs.pipenv.org/)

### Install dependencies

* With dev dependencies
```bash
$ pipenv sync --dev
```

* Without dev dependencies
```bash
$ pipenv sync
```

### Install dependencies

```bash
$ pipenv install package
```

## Testing

### Run the code formatter

This runs [isort](https://github.com/timothycrosley/isort/) and [Black](https://github.com/ambv/black/), the Python code formatter.
```bash
$ make format
```

Black reformats entire files in place, but doesn't reformat blocks that start with `# fmt: off` and end with `# fmt: on`.

### Run the linter

This test check syntax error and pip8 rules.
```bash
$ make lint
```

### Run the optional static type checker

This runs `mypy`, the static type checker using the [PEP 484](https://www.python.org/dev/peps/pep-0484/) notation.
```bash
$ make mypy
```

### Run the unit tests

```bash
$ make pytest
```

### Run the code formatter, optional static type checker, linter, and unit tests

```bash
$ make test
```

## Resources

- [black](https://github.com/ambv/black/)
- [isort](https://github.com/timothycrosley/isort/)
- [pipenv](https://docs.pipenv.org/)
- [pylint](https://www.pylint.org/)
- [pytest](https://docs.pytest.org/en/latest/)
