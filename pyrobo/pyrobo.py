# -*- coding: utf-8 -*-
u"""
Pyrobo contiene frases de la película colombiana
La vendedora de rosas, basada en el cuento La vendedora de cerillas
(The little match girl) de Hans Christian Andersen.

"""
from __future__ import print_function
from numpy.random import random_integers

frases = [u"¿Pa' qué zapatos si no hay casa, pa' qué hijueputas?",
          u"¡Abrite que ya perdiste maricona!",
          u"¡Que coma mierda el culo!",
          u"Me la mecatié en cositas.",
          u"Usted está muy engalocha'o.",
          u"Yo le doy lengua a lo mango."]

frases_educadas = [
    u"¿Para qué zapatos sin casa, para qué, prole de meretriz?",
    u"¡Abrite que ya perdiste maricona!",
    u"¡Que ingiera heces el ano!",
    u"La invertí en cosas baladís.",
    u"Aspirar pegamento nubló tu juicio.",
    u"Yo te lamería de la misma forma que lo hago con un mango."]

personajes = ["Chinga", "El Zarco", "El Zarco", "Andrea", u"Mónica", 
              "Alex", ]


def hablame(pos=None):
    u"""Imprime una frase de la vendedora de rosas

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
    msj = u"❝{}❞\n\n{}{}".format(frase, espacios_autor, personaje)
    print(msj)
    return None
