from enum import Enum

import typer

from cipher_typer.cipher import CaeserCipher, CaeserSeedCipher

app = typer.Typer()


class EncryptionMethod(str, Enum):
    caeser = "caeser"
    seed = "seed"


class Level(str, Enum):
    lower = "lower"
    upper = "upper"
    both = "both"
    _all = "all"


@app.command()
def encrypt(
    message: str,
    key: int = typer.Argument(
        0, help="This is the encryption key, to decrypt message key must be identical"
    ),
    method: EncryptionMethod = typer.Option(EncryptionMethod.caeser),
    level: Level = typer.Option(Level._all),
):
    """
    Encrypt message with user defined key
    """
    if method == "caeser":
        c = CaeserCipher(level)
    if method == "seed":
        c = CaeserSeedCipher(level)

    typer.echo(c.encrypt(message, key))


@app.command()
def decrypt(
    message: str,
    key: int = typer.Argument(0),
    method: EncryptionMethod = typer.Option(EncryptionMethod.caeser),
    level: Level = typer.Option(Level._all),
):
    if method == "caeser":
        c = CaeserCipher(level)
    if method == "seed":
        c = CaeserSeedCipher(level)

    typer.echo(c.decrypt(message, key))


if __name__ == "__main__":
    app()
