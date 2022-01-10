"""
The command handler
"""

import logging
import click
from mypackage.utils import setup_logging, do_utility_things, do_more_utility_things
from mypackage.main import do_something, do_something_else


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def cli(*args, **kwargs):
    """
    This is the main entry point for the CLI.
    """
    setup_logging(kwargs["debug"])
    ctx = args[0]
    ctx.obj = {}
    ctx.obj["debug"] = kwargs["debug"]
    ctx.obj["logger"] = logging.getLogger("mypackage")
    ctx.obj["logger"].info("Debug mode is %s", kwargs["debug"])


@cli.command()
@click.pass_context
def hello(ctx):
    """
    Prints 'Hello World'
    """
    ctx.obj["logger"].debug("Hello World from debug")
    ctx.obj["logger"].info("Hello World from info")


@cli.command()
@click.pass_context
def goodbye(ctx):
    """
    Prints 'Goodbye World'
    """
    ctx.obj["logger"].debug("Goodbye World")


@cli.command()
def do_utility_things_cmd():
    """
    Prints 'Doing utility things'
    """
    do_utility_things()
    do_more_utility_things()


@cli.command()
def do_something_cmd():
    """
    Prints 'Doing something'
    """
    do_something()
    do_something_else()


if __name__ == "__main__":
    cli()
