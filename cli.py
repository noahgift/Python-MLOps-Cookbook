#!/usr/bin/env python
import click

def marco(name):
    if name == "Marco":
        return "Polo"
    return "No!"

@click.command()
@click.option(
    "--name",
    prompt="Pass in a name",
    help="This is the name you pass into the Marco Polo function",
)
def func(name):
    """A command-line tool that accepts a name and returns a respons"""

    result = marco(name)
    if result == "Polo":
        click.echo(click.style(result, bg="green", fg="white"))
    else:
        click.echo(click.style(result, bg="red", fg="white"))

if __name__ == "__main__":
    func()