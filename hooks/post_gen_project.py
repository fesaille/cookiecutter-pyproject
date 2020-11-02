#!/usr/bin/env python

from pathlib import Path

# fix empty lines within a section of pyproject.toml
for f in ["pyproject.toml", ".pre-commit-config.yaml"]:
    p = Path(f)
    text = p.read_text()
    p.write_text(text.replace("\n\n", "\n").replace("\n[", "\n\n["))

# Init the repo as git directory
if "{{ cookiecutter.init_git }}" == "y":
    from git import Repo
    from pre_commit.main import main as pc

    repo = Repo.init(".")
    # repo.index.add([str(p) for p in Path(".").glob("*")])
    # Install pre-commit
    pc(["install"])

if "{{ cookiecutter.ci_cd }}" != "travis_ci":
    Path(".travis.yml").unlink()

if "{{ cookiecutter.ci_cd }}" != "gitlab_ci":
    Path(".gitlab-ci.yml").unlink()
