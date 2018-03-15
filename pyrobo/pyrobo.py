# -*- coding: utf-8 -*-
u"""
Pyrobo contiene frases de la película colombiana
La vendedora de rosas, basada en el cuento La vendedora de cerillas
(The little match girl) de Hans Christian Andersen.

"""
from __future__ import print_function
from numpy.random import random_integers

frases = [
    u"¿Pa' qué zapatos si no hay casa, pa' qué hijueputas?",
    u"¡Abrite que ya perdiste maricona!",
    u"¡Que coma mierda el culo!",
    u"Me la mecatié en cositas.",
    u"Usted está muy engalocha'o.",
    u"Yo le doy lengua a lo mango.",
    u"Del paraíso a la misma mierda.",
    u"¡Eh, Ave María! ¿Mamacita usted que está haciendo por aquí solita? … con esas piernotas yo me la robo.",
    u"¿Hey enano, esa gonorrea porque se encaleta ome, o es que el traído viene enfierrado?",
    u"¡Uy esta gonorrea nos dañó el 24 ome!, ¡qué gonorrea ome!",
    u"¡Oee, oee, fuck you men gonorreas!",
    u"Hágale que todo bien.",
    u"¡¿No pues que ya no metías nada ome?!",
    u"Tenga la bondad de respetarme si usted quiere que lo respeten, ¡maricón!"]

frases_cultas = [
    u"¿De qué sirve el calzado sin morada?, ¡basta de tiquismiquis!",
    u"Hoy no es tu día de suerte. ¡Buena mujer!",
    u"¡Que ingiera heces el ano!",
    u"La invertí en cosas baladís.",
    u"Aspirar pegamento nubló tu juicio.",
    u"Yo te lamería como a fruto de mangifera.",
    u"Del paraíso a la podredumbre.",
    u"¡Enhorabuena! Guapa, ¿a qué te dedicas en tan lúgubre lugar? Quisiera continuar esta conversación en mi habitación.",
    u"¡Disculpa pequeño! ¿Por qué se esconde? ¿trae el caballo de Troya?",
    u"¡Este sujeto arruinó nuestra noche buena!",
    u"¡Oigan! ¡bless your hearts, buenos hombres!",
    u"Adelante, no hay líos.",
    u"Pensaba que practibas la abstinencia.",
    u"El respeto dado es la medida del respeto recibido, ¡buen hombre!"]

    

personajes = ["Chinga", "El Zarco", "El Zarco", "Andrea", u"Mónica", 
              "Alex", u"Mónica", "Anderson", "El Zarco", u"Don Héctor",
              "Judy", u"Mónica", u"Mónica", "Andrea"]


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
