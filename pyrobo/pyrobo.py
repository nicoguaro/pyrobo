# -*- coding: utf-8 -*-
"""
Pyrobo contiene frases de la película colombiana
La vendedora de rosas, basada en el cuento La vendedora de cerillas
(The little match girl) de Hans Christian Andersen.

"""
from numpy.random import random_integers

frases = [
    "¿Pa' qué zapatos si no hay casa, pa' qué hijueputas?",
    "¡Abrite que ya perdiste maricona!",
    "¡Que coma mierda el culo!",
    "Me la mecatié en cositas.",
    "Usted está muy engalocha'o.",
    "Yo le doy lengua a lo mango.",
    "Del paraíso a la misma mierda.",
    "¡Eh, Ave María! ¿Mamacita usted que está haciendo por aquí solita? … con esas piernotas yo me la robo.",
    "¿Hey enano, esa gonorrea porque se encaleta ome, o es que el traído viene enfierrado?",
    "¡Uy esta gonorrea nos dañó el 24 ome!, ¡qué gonorrea ome!",
    "¡Oee, oee, fuck you men gonorreas!",
    "Hágale que todo bien.",
    "¡¿No pues que ya no metías nada ome?!",
    "Tenga la bondad de respetarme si usted quiere que lo respeten, ¡maricón!"]

frases_cultas = [
    "¿De qué sirve el calzado sin morada?, ¡basta de tiquismiquis!",
    "Hoy no es tu día de suerte. ¡Buena mujer!",
    "¡Que ingiera heces el ano!",
    "La invertí en cosas baladís.",
    "Aspirar pegamento nubló tu juicio.",
    "Yo te lamería como a fruto de mangifera.",
    "Del paraíso a la podredumbre.",
    "¡Enhorabuena! Guapa, ¿a qué te dedicas en tan lúgubre lugar? Quisiera continuar esta conversación en mi habitación.",
    "¡Disculpa pequeño! ¿Por qué se esconde? ¿trae el caballo de Troya?",
    "¡Este sujeto arruinó nuestra noche buena!",
    "¡Oigan! ¡bless your hearts, buenos hombres!",
    "Adelante, no hay líos.",
    "Pensaba que practibas la abstinencia.",
    "El respeto dado es la medida del respeto recibido, ¡buen hombre!"]


personajes = ["Chinga",
              "El Zarco",
              "El Zarco",
              "Andrea",
              "Mónica", 
              "Alex",
              "Mónica",
              "Anderson",
              "El Zarco",
              "Don Héctor",
              "Judy",
              "Mónica",
              "Mónica",
              "Andrea"]


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
