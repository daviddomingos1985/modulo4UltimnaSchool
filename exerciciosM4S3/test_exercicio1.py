import pytest
from exercicio1 import calcular_valor_total

def test_calculo_quantidade_menor_que_10():
    assert calcular_valor_total(10.0, 5) == (50.0, 50.0)

def test_calculo_quantidade_entre_10_e_99():
    assert calcular_valor_total(10.0, 50) == (500.0, 475.0)

def test_calculo_quantidade_entre_100_e_999():
    assert calcular_valor_total(10.0, 999) == (9990.0, 8991.0)

def test_calculo_quantidade_maior_999():
    assert calcular_valor_total(10.0, 1000) == (10000.0, 8500.0)

def tes_calculo_quantidade_limite_int32():
    assert calcular_valor_total(10.0, 214748647) == (21474836470.0, 182536610999.5)
    