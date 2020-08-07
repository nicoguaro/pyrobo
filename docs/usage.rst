===
Uso
===

Para usar pyrobo en un proyecto::

    >>> from pyrobo.pyrobo import hablame
    >>> hablame()
    ❝¿Pa' qué zapatos si no hay casa, pa' qué hijueputas?❞

                                              Chinga

Si el proyecto requiere que el lenguaje sea "apropiado",
se puede usar::

    >>> from pyrobo.pyrobo import cuentame
    >>> cuentame()
    ❝¿De qué sirve el calzado sin morada?, ¡basta de tiquismiquis!❞,

                                                            Chinga


pyrobo también cuenta con una interfaz de línea de comandos. El comando es
``pyrobo``, y se usa de la siguiente manera.

.. code:: bash

    $ pyrobo --help

    Usage: pyrobo [OPTIONS]

    Script de consola para Pyrobo.

    Pyrobo contiene frases de la película colombiana La vendedora de rosas,
    basada en el cuento La vendedora de cerillas (The little match girl) de
    Hans Christian Andersen.

    Options:
    --pos INTEGER    Número de la frase deseada.
    --culto BOOLEAN  Mostrar versión culta de la frase.
    --help           Muestra este mensaje y termina la ejecución.

Por ejemplo,

.. code:: bash

    $ pyrobo
    ❝Yo le doy lengua a lo mango.❞

                            Alex
