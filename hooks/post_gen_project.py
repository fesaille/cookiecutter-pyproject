#!/usr/bin/env python

from pathlib import Path


# Init the repo as git directory
if "{{ cookiecutter.init_git }}" == "y":
    from git import Repo
    from pre_commit.main import main as pc

    repo = Repo.init(".")
    # repo.index.add([str(p) for p in Path(".").glob("*")])
    # Install pre-commit
    pc(["install"])

if "{{ cookiecutter.add_travis_config }}" == "n":
    Path(".travis.yml").unlink()

if "{{ cookiecutter.add_gitlab_ci_config }}" == "n":
    Path(".gitlab-ci.yml").unlink()
