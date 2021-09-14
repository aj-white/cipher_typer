from typer.testing import CliRunner

from cipher_typer.typer_cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["encrypt", "Meet me at 6pm", "23"])
    assert result.exit_code == 0
    assert "+BBQwJBwxQwsMJ" in result.stdout


def test_app_decrypt():
    result = runner.invoke(app, ["decrypt", "+BBQwJBwxQwsMJ", "23"])
    assert result.exit_code == 0
    assert "Meet me at 6pm" in result.stdout


def test_app_seed():
    result = runner.invoke(
        app, ["encrypt", "6000 feet underwater !?", "67", "--method", "seed"]
    )
    assert result.exit_code == 0
    assert "%666}I##p}mw)#&Njp#&};r" in result.stdout


def test_app_seed_decrypt():
    result = runner.invoke(
        app, ["decrypt", "%666}I##p}mw)#&Njp#&};r", "67", "--method", "seed"]
    )
    assert result.exit_code == 0
    assert "6000 feet underwater !?" in result.stdout
