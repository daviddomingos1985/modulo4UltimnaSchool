def calcular__total_pedido(codigos_pedidos):
    '''
    Calcula o valor total de um pedido, dado uma lista de codigo de produtos.
    
    args:
        codigos_pedidos (list[INT]): lista contendo os codigos dos produtos pedidos.
        
    returns: 
        float: valor total do pedido.
    '''
    
# Dicionário contendo as informações dos produtos disponiveis.
    cardapio = {
        100: ('Cachorro Quente', 9.0),
        101: ('Cachorro Quente Duplo',11.0),
        102: ('X-Egg', 12.0),
        103: ('X-Salada', 12.0),
        104: ('X-bacon', 14.0),
        105: ('X-Tudo', 17.0),
        200: ('Refrigerante lata', 5.0),
        201: ('Sucos', 4.0),
    } 


# Variavel que amazenará o valor total do pedido.
    total = 0.0

# Percorre a lista de codigos de produtos pedidos.
    for codigo in codigos_pedidos:
    # Verifica se o codigo de produto é valido ou seja se consta no cardapio.
        if codigo in cardapio:
        # Recupera as informações do produto a partir do cardapio e adiciona o valor do produto total.
            produto, valor = cardapio[codigo]
            print(f'Você pediu um {produto} no valor de {valor:.2f}')
            total += valor
        else:
            print('Opção invalida!')

    return total    

if __name__ == '__main__':
    
    # Mostra o cardapio.
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código |        Descrição        |  Valor  |
    |   100  |     Cachorro Quente     |   9,00  |
    |   101  |  Cachorro Quente Duplo  |  11,00  |
    |   102  |           X-Egg         |  12,00  |
    |   103  |         X-Salada        |  12,00  |
    |   104  |          X-Bacon        |  14,00  |
    |   105  |           X-Tudo        |  17,00  |
    |   200  |    Refrigerente Lata    |   5,00  |
    |   201  |         Chá Gelado      |   4,00  |
    ----------------------------------------------
    """
    print(cardapio)
    
    # LIsta que armazanara os codigos dos produtos pedidos.
    codigos = []
    
    # Recebe o primeiro codigo de produto do usuario    
    codigo = int(input('Entre com o código desejado: '))
    
    while True:
        # Verifica se o codigo de produto consta no cardapio e adiciona a lista de codigos.
        if codigo in [100, 101, 103, 104, 105, 200, 201]:
            codigos.append(codigo)
        else:
            print('opção invalida!')
            
        print ('Deseja pedir algo mais?')
        print('1 - SIM')
        print('2 - NÃO')
        pedir_mais = int(input())
        
        if pedir_mais == 2:
            break
        
        codigo = int(input('Digite o codigo desejado:'))
        
    total = calcular__total_pedido(codigos)
    print(f'O valor total do seu pedido é de : {total:.2f} R$')
        
