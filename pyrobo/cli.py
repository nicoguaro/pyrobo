# -*- coding: utf-8 -*-

"""Script de consola para pyrobo."""
import sys
import click
from pyrobo.pyrobo import hablame


@click.command()
@click.argument('pos', type=int, required=False)
def main(pos=None):
    """Script de consola para pyrobo."""
    hablame(pos)
    return 0


if __name__ == "__main__":
    sys.exit(main())
