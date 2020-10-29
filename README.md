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
