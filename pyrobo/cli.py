# -*- coding: utf-8 -*-

"""Script de consola para Pyrobo."""
import sys
import click
from pyrobo.pyrobo import hablame, cuentame


@click.command()
@click.option('--pos', default=None, type=int,
              help='Número de la frase deseada.')
@click.option('--culto', default=False, type=bool,
              help='Mostrar versión culta de la frase.')
@click.help_option(help="Muestra este mensaje y termina la ejecución.")              
def main(pos=None, culto=False):
    """Script de consola para Pyrobo.
    
    Pyrobo contiene frases de la película colombiana
    La vendedora de rosas, basada en el cuento La vendedora de cerillas
    (The little match girl) de Hans Christian Andersen.
    """
    if culto:
        cuentame(pos)
    else:
        hablame(pos)
    return 0


if __name__ == "__main__":
    sys.exit(main())
