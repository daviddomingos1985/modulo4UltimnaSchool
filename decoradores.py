'''
Seu objetivo é acrescentar responsabilidades a um objeto dinamicamente. 
Ou seja, dar mais uma opção além do uso de subclasses para estender a funcionalidade de uma classe, 
sendo assim mais flexível do que a herança.

Propriedades das funções:

Você pode armazenar funções em variáveis;
Você pode passar uma função como um parâmetro para outra função;
Você pode retornar a função de uma função.

'''

#Ex; Utilizando funções como um objetivo.

def maiusculo(texto):
    return texto.upper()

print(maiusculo("Ultima"))

mensagemMaiusculo = maiusculo

print (mensagemMaiusculo("school"))

'''
SAÍDA:
ULTIMA
SCHOOL

No código acima vemos um bom exemplo: 
a variável mensagemMaiusculo recebe a assinatura do método maiusculo, 
ou seja, não vai chamar a função, mas sim criar um novo nome. 
'''


# Ex: Fução como um argumento

def maiusculo(texto):
    return texto.upper()

def miniusculo(texto):
    return texto.lower()

def mensagem(funcao):
    texto = funcao("Ultima School")
    print (texto)
    
mensagem(maiusculo)
mensagem(miniusculo)

'''
SAÍDA:
ULTIMA SCHOOL
ultima school

Já neste exemplo, a função mensagem recebe outra função como argumento; 
e a que é passada dentro do argumento é chamada para realizar sua operação.

'''

#Ex. Retornar funções da função

def somador(x):
    def soma(y):
        return x+y
    
    return soma

resultado = somador(15)

print(resultado(10))

'''
SAÍDA:
25

Neste último exemplo, temos uma função dentro de outra, 
e retornamos a função criada, ou seja, a variável resultado recebe a função soma com o X = 15, 
imprimindo na linha 9 a soma de X + Y.

Com esses 3 exemplos vimos uma demonstração de alguns conceitos do decorator, 
mas o Python nos permite facilitar essa chamada.


'''

def cumprimento(funcao):
    def saudacao():
        print ("Bom dia !")
        funcao()
        print ("Boa noite !")
    return saudacao

@cumprimento
def boa_tarde():
    print("Boa tarde !")
    
boa_tarde()

'''
Neste exemplo acima, temos uma função chamada cumprimento,
que recebe uma função como argumento. 
Dentro dela há uma função saudacao, que faz uso do argumento passado anteriormente. 
Temos também o método boa_tarde,que serve para definirmos uma saudação. 
Caso se deseje mudar sem alterar o método principal, acima temos a anotação @cumprimento, 
que seria o mesmo que fazer boa_tarde = cumprimento(boa_tarde).

'''