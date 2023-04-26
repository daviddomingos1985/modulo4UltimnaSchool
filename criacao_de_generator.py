'''

Generators
Um generator é uma forma mais simples e rápida de implementar o protocolo Interator, 
pois não se faz necessária uma classe e, além disso, ela salva o estado da função no último retorno. 
Para criação de um generator, precisamos definir uma função utilizando yield no lugar do return. 
Vamos utilizar o exemplo anterior para entendermos melhor:

'''

def fibonacci(maximo):

    elementoAtual, proximoElemento = 0, 1

    while elementoAtual < maximo:
        yield elementoAtual

        elementoAtual, proximoElemento = proximoElemento, elementoAtual + proximoElemento


'''
Na primeira execução da função, serão executadas as linhas de 1 a 6. 
Já nas chamadas subsequentes, ele continuará o código a partir do While, 
atualizando os valores das variáveis acima. 

Como vimos acima, para realizar a iteração utilizamos o StopIteration, 
para avisar que não existem mais valores. Já nesta implementação não será retornado um valor, 
e o Python entende que as iterações foram encerradas, e então finaliza o loop.

O generator permite uma economia na memória, 
pois não é necessário iniciar toda iteração novamente para obter o próximo valor, 
além de não requerer uma variável.

'''