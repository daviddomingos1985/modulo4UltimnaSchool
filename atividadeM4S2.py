def decorator_imprimir(funcao):
    """
    Decorator que imprime os parâmetros e o resultado de uma função.
    """
    def mensagem(*args, **kwargs):
        """
        Função interna que é responsável por imprimir os parâmetros e o resultado da função original.
        """
        # Armazena os argumentos da função original em variáveis separadas.
        capital, taxa, tempo = args
        
        # Mesma coisa que:
        #capital = args[0]
        #taxa = args[1]
        #tempo = args[2]
        
        # Executa a função original.
        result = funcao(*args, **kwargs)
        
        # Imprime os parâmetros e o resultado da função original.
        #print(f"CAPITAL: {capital}, TAXA: {taxa}, TEMPO: {tempo}, RESULTADO: {result}")
        
        # Retorna o resultado da função original.
        return print(f"CAPITAL: {capital}, TAXA: {taxa}, TEMPO: {tempo}, RESULTADO: {result}")
    return mensagem

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    """
    Função que calcula juros simples.
    """
    return capital * (taxa / 100) * tempo


#def decorador_imprimir (funcao):
#    def mensagem (*args, **kwargs):
#        funcao (*args, **kwargs)
#        print (f"Capital: R${capital}, Taxa: {taxa}, Tempo: {tempo}")
#        print (f"Resultado: R$ {funcao(*args, **kwargs):.2f}")
#    return mensagem
#
#
#@decorador_imprimir
#def juros_simples(capital, taxa, tempo):
#    juros_simples = capital * (taxa/100) * tempo    
#    return juros_simples
