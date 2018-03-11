.. highlight:: shell

=========================
¿Cómo contribuir a pyrobo?
=========================

¡Las contribuciones son bienvenidas, y muy apreciadas! Cada detalle
ayuda, y el crédito siempre será dado.

Puedes contribuir de muchas maneras:

Tipos de contribuciones
----------------------

Reportar errores
~~~~~~~~~~~~~~~~

Informando errores en https://github.com/nicoguaro/pyrobo/issues.

Si informa un error, incluya lo siguiente:

* El nombre y la versión de su sistema operativo.
* Cualquier detalle sobre su configuración local que pueda ser útil para solucionar problemas.
* Pasos detallados para reproducir el error.

Corregir errores
~~~~~~~~~~~~~~~~

Consulte los *issues* de GitHub  para encontrar errores. Cualquier cosa etiquetada con "error" y "help wanted" está abierta a quien quiera implementarlo.

Implementar funciones
~~~~~~~~~~~~~~~~~~~~~

Consulte los problemas de GitHub para conocer las características.
Cualquier cosa etiquetada con "enhancement" y "help wanted" está
abierto a quien quiera implementarlo.

Escribir documentación
~~~~~~~~~~~~~~~~~~~~~~

pyrobo siempre podría tener más documentación, ya sea como parte de la
documentos oficiales de pyrobo, en docstrings, o incluso en la web como
publicaciones de blogs, artículos, etc.

Enviar comentarios
~~~~~~~~~~~~~~~~~~

La mejor forma de enviar comentarios es presentar un problema en https://github.com/nicoguaro/pyrobo/issues.

Si está proponiendo una nueva funcionalidad:

* Explica en detalle cómo funcionaría.
* Mantenga el alcance lo más estrecho posible, para que sea más fácil de implementar.
* Recuerde que este es un proyecto impulsado por voluntarios, y que las contribuciones
  son bienvenidos :)

¡Empieza!
---------

¿Listo para contribuir? A continuación se explica cómo configurar `pyrobo` para el desarrollo local.

1. *Fork* el repositorio `pyrobo` en GitHub.
2. Clona tu tenedor localmente ::

    $ git clone git@github.com: tu_nombre_aquí / pyrobo.git

3. Instala tu copia local en un virtualenv. Suponiendo que tienes virtualenvwrapper instalado, así es como configura su tenedor para el desarrollo local ::

    $ mkvirtualenv pyrobo
    $ cd pyrobo /
    $ python setup.py desarrollar

4. Crear una rama para el desarrollo local ::

    $ git checkout -b nombre-de-tu-corrección de errores-o-función

   Ahora puedes hacer tus cambios localmente.

5. Cuando termine de hacer cambios, verifique que sus cambios pasen a flake8 y al
   pruebas, incluida la prueba de otras versiones de Python con tox ::

    Pruebas de $ flake8 pyrobo
    $ python setup.py test o py.test
    $ tox

   Para obtener Flake8 y tox, simplemente pip instálelos en su Virtualenv.

6. Confirme sus cambios y envíe su sucursal a GitHub ::

    $ git add.
    $ git commit -m "Su descripción detallada de sus cambios".
    $ git push origen nombre-de-tu-corrección de errores-o-característica

7. Presente una solicitud de extracción a través del sitio web de GitHub.

Pautas para *Pull Request*
--------------------------

Antes de enviar una solicitud de extracción, verifique que cumpla con estas pautas:

1. La solicitud de extracción debe incluir pruebas.
2. Si la solicitud de extracción agrega funcionalidad, los documentos deben actualizarse. Poner
   su nueva funcionalidad en una función con un docstring, y agregue el
   característica a la lista en README.rst.
3. La solicitud de extracción debería funcionar para Python 2.7, 3.4, 3.5 y 3.6, y para PyPy. Comprobar
   https://travis-ci.org/nicoguaro/pyrobo/pull_requests
   y asegúrese de que las pruebas pasen para todas las versiones compatibles de Python.

Consejos
--------

Para ejecutar un subconjunto de pruebas ::

$ py.test tests.test_pyrobo


Despliegue
----------

Un recordatorio para los mantenedores sobre cómo implementar.

Asegúrese de que se hayan confirmado todos sus cambios (incluida una entrada en HISTORY.rst).
Entonces corre::

Parche de $ bumpversion # posible: mayor / menor / parche
$ git push
$ git push - tags

Travis luego se desplegará en PyPI si pasan las pruebas.
