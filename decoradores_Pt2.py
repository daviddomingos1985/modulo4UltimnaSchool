'''
Primeiro declaramos a nossa função primeiro_decorator( ), 
que receberá uma outra função como parâmetro. 
Dentro dela, temos a primeira_func( ), que faz uso da função que recebemos como parâmetro.

Logo após, temos a função que será passada como parâmetro, 
a funcao_utilizadora(). Agora declaramos a variável final, 
que vai receber a declaração da chamada da função e, para finalizar, chamamos final( ). 

'''

def primeiro_decorator(func):
    
    def primeira_func():
        print("Execução antes da função")
        
        func()
        
        print("Execução depois da função")
        
    return primeira_func

def funcao_utilizadora():
    print("Preciso utilizar o decorator")
    
final = primeiro_decorator(funcao_utilizadora)


final()

'''
SAIDA:

Execução antes da função
Preciso utilizar o decorator
Execução depois da função

'''
#Mas podemos melhorar ainda mais esse código. Veja abaixo:

def primeiro_decorator(func):
    
    def primeira_func():
        print("Execução antes da função")
        
        func()
        
        print("Execução depois da função")
        
    return primeira_func

@primeiro_decorator
def funcao_utilizadora():
    print("Preciso utilizar o decorator")
    
funcao_utilizadora()

'''
Desta vez utilizamos a primeira parte do código anterior, 
mas agora fazemos a declaração através do @primeiro_decorator. 
Com isso, não é necessário atribuir a chamada da função a uma variável e depois chamá-la, 
é possível chamar a função direto.
'''