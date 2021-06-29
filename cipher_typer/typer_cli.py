from enum import Enum

import typer

from cipher import CaeserCipher, CaeserSeedCipher


class EncryptionMethod(str, Enum):
    caeser = "caeser"
    seed = "seed"


class Mode(str, Enum):
    encrypt = "encrypt"
    decrypt = "decrypt"


class Level(str, Enum):
    lower = "lower"
    upper = "upper"
    both = "bith"
    _all = "all"


def main(
    mode: Mode,
    message: str,
    key: int = typer.Argument(0),
    method: EncryptionMethod = typer.Option(EncryptionMethod.caeser),
    level: Level = typer.Option(Level._all),
):
    if method == "caeser":
        c = CaeserCipher(level)
    if method == "seed":
        c = CaeserSeedCipher(level)

    if mode == "encrypt":
        typer.echo(c.encrypt(message, key))
    if mode == "decrypt":
        typer.echo(c.decrypt(message, key))


if __name__ == "__main__":
    typer.run(main)
