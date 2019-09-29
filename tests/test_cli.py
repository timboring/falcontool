import os

from click.testing import CliRunner
import pytest

from commands import BASEDIRS
from commands import BASEFILES
from commands import create


expected_output = """created directory foo
created directory tests
created directory src
created file requirements.txt
created file README.md
created file src/api.py
created file CODEOWNERS
"""

expected_docker_output = expected_output + 'created file Dockerfile\n'
expected_models_output = expected_docker_output + 'created file src/models.py\n'
expected_resources_output = expected_models_output + 'created file src/resources.py\n'
expected_tox_output = expected_resources_output + 'created file tox.ini\n'



class TestCli:

    @pytest.mark.parametrize(
        'input, output', [
            (['foo'], expected_output),
            (['foo', '-d'], expected_docker_output),
            (['foo', '-d', '-m'], expected_models_output),
            (['foo', '-d', '-m', '-r'], expected_resources_output),
            (['foo', '-d', '-m', '-r', '-t'], expected_tox_output)
        ],
    )
    def test_create(self, input, output):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(create, input)
            assert result.exit_code == 0
            assert result.stdout == output

            for dir in BASEDIRS:
                assert os.path.exists(dir)

            for file in BASEFILES:
                assert os.path.exists(file)

            if '-d' in input:
                assert os.path.exists('Dockerfile')

            if '-m' in input:
                assert os.path.exists('src/models.py')

            if '-r' in input:
                assert os.path.exists('src/resources.py')

            if '-t' in input:
                assert os.path.exists('tox.ini')


