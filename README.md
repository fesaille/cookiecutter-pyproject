# Cookiecutter pyproject

This cookiecutter provides a basis configuration for python developement based
on [`pyproject.toml` within a poetry](https://python-poetry.org/docs/pyproject)
[build frontend](https://www.python.org/dev/peps/pep-0517/#terminology-and-goals)

This is a **work on progress**.

## Dependencies

- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [gitpython](https://github.com/gitpython-developers/GitPython)
- [pre-commit](https://github.com/pre-commit/pre-commit)

Installation can be done e.g. with [**pipx**](https://github.com/pipxproject/pipx):

```bash
pipx install cookiecutter --pip-args gitpython pre-commit
pipx install pre-commit
```

## Usage

```bash
cookiecutter gh:fesaille/cookiecutter-pyproject
```

## `pre-commit` hooks

- Generic, md and yaml
  - [markdownlint](https://github.com/markdownlint/markdownlint)
  - [yamllint](https://github.com/adrienverge/yamllint)

- Python related
  - [autoflake](https://github.com/myint/autoflake) removes unused imports and
    unused variables from Python code.  - [black](https://github.com/psf/black)
    is a code formatter whose gain is to avoid noisy diffs.
  - [isort](https://github.com/PyCQA/isort) sorts import.
  - [pylint](https://github.com/PyCQA/pylint) is a static code analysis tool.
  - [mypy](https://github.com/python/mypy) is a static type checker
  - [bandit](https://github.com/PyCQA/bandit) is a tool designed to find common
     security issues in Python code.
