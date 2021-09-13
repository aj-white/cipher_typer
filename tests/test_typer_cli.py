from typer.testing import CliRunner

from cipher_typer.typer_cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["encrypt", "Meet me at 6pm", "23"])
    assert result.exit_code == 0
    assert "+BBQwJBwxQwsMJ" in result.stdout
