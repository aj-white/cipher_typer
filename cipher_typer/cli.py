import click

from cipher import CaeserCipher, CaeserSeedCipher


# A command looks like Class(level).mode "message" "key"
@click.command()
@click.option("--method", default="caeser", type=click.Choice(["caeser", "seed"]))
@click.option(
    "--level", default="all", type=click.Choice(["lower", "upper", "both", "all"])
)
@click.option("--encrypt", "-e", is_flag=True)
@click.option("--decrypt", "-d", is_flag=True)
@click.argument("message", type=str)
@click.argument("key", type=int, default=0)
def main(method, level, encrypt, decrypt, message, key):
    if method == "caeser":
        c = CaeserCipher(level)
    if method == "seed":
        c = CaeserSeedCipher(level)

    if encrypt:
        click.echo(c.encrypt(message, key))
    if decrypt:
        click.echo(c.decrypt(message, key))


if __name__ == "__main__":
    main()
