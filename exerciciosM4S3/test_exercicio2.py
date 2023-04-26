import pytest
from exercicio2 import calcular__total_pedido

def test_calcular_total_do_pedido():
    # Teste com apenas um pedido
    assert calcular__total_pedido([100]) == 9.0

def test_calcular_varios_pedidos():
    # Teste com varios pedidos
    assert calcular__total_pedido([100, 101, 105, 201]) == 41.0
    
def test_calcular_pedido_invalido():
    # Teste com pedido invalido
    assert calcular__total_pedido([200, 300, 104]) == 19.0

def test_calcular_pedido_vazio():
    #teste com pedido vazio
    assert calcular__total_pedido([]) == 0.0
    
def test_calcular_pedido_repetido():
    # Teste com pedido repetido
    assert calcular__total_pedido([100, 100, 105, 200, 201, 201]) == 48.0
    
def test_calcular_todos_pedidos_do_cardapio():
    # Teste com todos os produtos do cardapio
    assert calcular__total_pedido([100, 101, 102, 103, 104, 105, 200, 201]) == 84.0
    
def tet_calcular_total_do_pedido_produto_inexistente():
    # Teste com um produto inexistente no cardapio
    assert calcular__total_pedido([500]) == 0.0
     
