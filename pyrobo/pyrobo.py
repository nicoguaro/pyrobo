# -*- coding: utf-8 -*-
"""
Pyrobo contiene frases de la película colombiana
La vendedora de rosas, basada en el cuento La vendedora de cerillas
(The little match girl) de Hans Christian Andersen.

"""
from __future__ import print_function
from numpy.random import random_integers

frases = ["¿Pa' qué zapatos si no hay casa, pa' qué hijueputas?",
          "¡Abrite que ya perdiste maricona!",
          "¡Que coma mierda el culo!",
          "Me la mecatié en cositas."]
personajes = ["Chinga", "El Zarco", "El Zarco", "Andrea"]


def hablame(pos=None):
    """Imprime una frase de la vendedora de rosas
    
    Parámetros
    ----------
    val : int, opcional
        Posición de la frase en la lista de frases.

    """
    num_frases = len(frases)
    if pos is None or pos >= num_frases:
        pos = random_integers(0, num_frases - 1)
    frase = frases[pos]
    personaje = personajes[pos]
    espacios_autor = (len(frase) - len(personaje))*" "
    msj = "❝{}❞\n\n{}{}".format(frase,espacios_autor, personaje)
    print(msj)
    return None