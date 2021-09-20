from enum import Enum

import typer

from cipher_typer.cipher import CaeserCipher, CaeserSeedCipher

app = typer.Typer()


class EncryptionMethod(str, Enum):
    caeser = "caeser"
    seed = "seed"


@app.command()
def encrypt(
    message: str,
    key: int = typer.Argument(
        0, help="This is the encryption key, to decrypt message key must be identical"
    ),
    method: EncryptionMethod = typer.Option(EncryptionMethod.caeser),
):
    """
    Encrypt message with user defined key
    """
    if method == "caeser":
        c = CaeserCipher()
    if method == "seed":
        c = CaeserSeedCipher()

    typer.echo(c.encrypt(message, key))


@app.command()
def decrypt(
    message: str,
    key: int = typer.Argument(0),
    method: EncryptionMethod = typer.Option(EncryptionMethod.caeser),
):
    if method == "caeser":
        c = CaeserCipher()
    if method == "seed":
        c = CaeserSeedCipher()

    typer.echo(c.decrypt(message, key))


if __name__ == "__main__":
    app()
