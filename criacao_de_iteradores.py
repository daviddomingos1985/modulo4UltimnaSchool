'''
Um iterador é usado sobre objetos iteráveis, como listas, tuplas, dicionários e conjuntos. Um objeto é considerado iterável se pudermos obter um iterador dele ou fazer um loop sobre ele. 

Um exemplo muito conhecido é o range, método que nos retorna um número como iteração.

for i in range(10):
    print(i)
implementação serão gerados os valores de 0 até o 10.


Também é possível criar um objeto iterável através do protocolo Iterator. 
Para isso, é necessária uma classe que implemente os seguintes métodos:

__init__: o método construtor, responsável pela criação do objeto. 
Nem sempre será necessário utilizá-lo, depende do projeto.


__iter__:  retorna o próprio objeto para ser utilizado nos loops como for.


__next__: retorna o próximo valor da iteração. 
Se a condição de parada for verdadeira, ou seja, quando não existir mais objetos para iterar, 
ela  lançará o erro StopIteration.
'''

class Fibonacci:
    
    def __init__(self, maximo=100000):
        self.elementoAtual, self.proxElemento = 0, 1
        self.maximo = maximo
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.elementoAtual > self.maximo:
            raise StopIteration
        
        valorRetorno = self.elementoAtual
        self.elementoAtual, self.proxElemento = self.proxElemento, self.elementoAtual + self.proxElemento

        return valorRetorno
    