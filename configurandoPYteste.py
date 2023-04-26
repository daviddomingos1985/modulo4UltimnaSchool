'''
Abaixo, veremos nosso primeiro exemplo de como criar um teste unitário:

'''
import pytest

def multiplicação(x, y):
    
    return x*y;

def test_multiplicacao():
    assert multiplicação(10, 2) == 20
    
    
'''
Acima, podemos ver a definição da função multiplicacao, 
na qual recebemos dois valores como parâmetro, 
retornando os dois valores multiplicados. 
Logo após, no método test_multiplicacao, 
fazemos a verificação do método citado anteriormente. 
Para isso, utilizamos a palavra chave assert que irá validar a condição de teste. 
Podemos ver que foram passados 10 e 2 como parâmetros neste teste, 
tendo 20 como resultado. 
Ao comparar com o 21, receberemos uma falha no teste. 
Para isso, vamos rodá-lo através do comando:

pytest test_multiplicacao.py

'''    

'''
Quando falamos em testes, é necessário sabermos a cobertura que esses códigos abrangem, 
pois precisamos cobrir o maior número de funcionalidades possíveis.

No Python temos o pytest-cov, para isso será necessário instalá-lo de forma simples utilizando 
o comando abaixo:

pip install pytest-cov 

Agora para utilizar rodamos o comando pytest -vv --cov= nome_do_arquivo.py, 
dessa maneira verificamos se a rotina de testes está contemplando todas as condições possíveis.


'''