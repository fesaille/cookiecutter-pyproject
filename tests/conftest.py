"""Provides the container fixtures for integration tests.
"""
import json
import sys
from pathlib import Path

import docker
import pytest

PYTHON_VERSION = 3.8


def pytest_load_initial_conftests(args):
    """Hook to set the -n option

    Doc at https://docs.pytest.org/en/latest/reference.html#bootstrapping-hooks

    See https://docs.pytest.org/en/stable/example/simple.html#dynamically-adding-command-line-options
    and https://github.com/pytest-dev/pytest/issues/4482
    """
    if "xdist" in sys.modules:  # pytest-xdist plugin
        # pylint:disable=import-outside-toplevel
        import multiprocessing

        num = max(multiprocessing.cpu_count() / 2, 1)
        args[:] = ["-n", str(num)] + args


@pytest.fixture(scope="session", autouse=True)
def container():
    """My doc"""

    SCRIPT = """
        mkdir -p ~/.local/bin

        # cat << EOF > ~/.profile
        # if [ -d "$HOME/.local/bin" ] ; then
        # PATH="$HOME/.local/bin:$PATH"
        # fi
        # EOF
        pip install pipx 
        pipx install pre-commit 
        pipx install cookiecutter --pip-args gitpython pre-commit
    """

    client = docker.from_env()

    client.containers.list(
    _container = client.containers.run(
        f"python:{PYTHON_VERSION}",
        auto_remove=False,
        detach=True,
        mem_limit="64m",
        name="cc-pyproject",
        nano_cpus=1_000_000_000,
        stdin_open=True,
        tty=True,
        volumes={Path().absolute(): {"bind": "/opt/cc", "mode": "ro"}},
    )

    _container.exec_run(SCRIPT)

    yield _container

    _container.stop()


@pytest.fixture(scope="session")
def installation_dir(tmpdir_factory):
    """Temporaty installation path of the cookiecutter"""
    tmp = tmpdir_factory.mktemp("cookie")
    return tmp


@pytest.fixture(scope="session")
def config():
    """Cookiecutter configuration"""

    return json.load(Path("cookiecutter.json").open())
