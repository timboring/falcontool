from click.testing import CliRunner

from bin import create


class TestCli:

    def test_create(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke()


