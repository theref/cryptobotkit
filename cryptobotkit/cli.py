import click


@click.group()
def crypto():
    pass


@crypto.command()
def buy():
    pass


@crypto.command()
def sell():
    pass
