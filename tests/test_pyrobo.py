#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyrobo` package."""

import pytest

from click.testing import CliRunner

from pyrobo import pyrobo
from pyrobo import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--pos', '1'])
    assert result.exit_code == 0
    assert '¡Abrite que ya perdiste maricona!' in result.output

    # Mensaje de ayuda
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'pos INTEGER    Número de la frase deseada.' in help_result.output
    assert '--culto BOOLEAN  Mostrar versión culta de la frase.' in help_result.output
    assert '--help           Muestra este mensaje y termina la ejecución.' in help_result.output


def test_hablame(capsys):
    """We use the capsys argument to capture printing to stdout."""
    assert pyrobo.hablame(1) == None
  
    # Capture the result of the pyrobo.hablame() function call.
    captured = capsys.readouterr()

    # If we check captured, we can see that the ingredients have been printed.
    assert u"❝¡Abrite que ya perdiste maricona!❞" in captured.out
    assert u"\n\n" in captured.out    
    assert u"El Zarco" in captured.out
  

def test_frases():
    assert len(pyrobo.frases) == len(pyrobo.frases_cultas)
    assert len(pyrobo.frases) == len(pyrobo.personajes)   
