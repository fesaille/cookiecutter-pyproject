"""General tests"""
from cookiecutter.main import cookiecutter


def test_install(tmpdir):
    """Test cookiecutter default installation """
    cookiecutter("gh:fesaille/cookiecutter-pyproject", no_input=True, output_dir=tmpdir, default_config=True)
