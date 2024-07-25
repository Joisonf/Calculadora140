import pytest
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

def test_somar_dois_numeros():
  num1 = 5
  num2 = 7
  resultado_esperado = 12

  resultado_obtido = somar_dois_numeros(num1, num2)

  assert resultado_esperado == resultado_obtido


def test_subtrair_dois_numeros():
  num1 = 10
  num2 = 7
  resultado_esperado = 3

  resultado_obtido = subtrair_dois_numeros(num1, num2)

  assert resultado_esperado == resultado_obtido  


def test_multiplicar_dois_numeros():
  num1 = 2
  num2 = 2
  resultado_esperado = 4

  resultado_obtido = multiplicar_dois_numeros(num1, num2)
  assert resultado_esperado == resultado_obtido  


def test_dividir_dois_numeros():
  num1 = 4
  num2 = 2
  resultado_esperado = 2

  resultado_obtido = dividir_dois_numeros(num1, num2)
  assert resultado_esperado == resultado_obtido  