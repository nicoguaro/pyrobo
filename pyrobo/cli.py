# -*- coding: utf-8 -*-

"""Console script for pyrobo."""
import sys
import click
from pyrobo.pyrobo import hablame


@click.command()
@click.argument('pos', type=int, required=False)
def main(pos=None):
    """Console script for pyrobo."""
    hablame(pos)
    return 0


if __name__ == "__main__":
    sys.exit(main())
