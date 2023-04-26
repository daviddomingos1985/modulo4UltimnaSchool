'''
atividade M4S1 da ultima school sobre iterador e gereador!!!

'''




import requests

# Instanciando a URL e o User-Agent
url_marcas = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
headers = {
    "User-Agent": "MyApp/1.0"
}

# Obtendo informações da API através do método GET
response = requests.get(url_marcas, headers=headers)

# Salvando a resposta da API
marcas = response.json()

# Obtendo o tipo da nossa variável
#type(marcas)

# Iterando sobre a lista que contém o nome da marca 
# e seu respectivo código
for marca in marcas:
    print("Marca:", marca["nome"], "Codigo:", marca["codigo"])


# Instanciando a URL para obter os modelos através do ID da marca
# selecionada
url_carros = "https://parallelum.com.br/fipe/api/v1/carros/marcas/59/modelos"

# Obtendo informações da API através do método GET
response = requests.get(url_carros, headers=headers)

# Salvando a resposta da API
carros = response.json()

# Obtendo o tipo da nossa variável
#type(carros)

# Por se tratar de um Dict, iremos obter as Chaves desse dict
# para analisarmos qual temos interesse
carros.keys()

# Analisando nosso Dict para a Chave 'modelos'
carros['modelos']

# Instanciando nossa classe para Iterar em nossa lista de Dicts

class FipeIterator:
    """
    Classe que itera sobre uma lista de dicionários de modelos de carros obtidos de uma API.
    
    Atributos:
        modelos (list): Lista de dicionários com informações sobre modelos de carros.
        current (int): Índice atual da lista de modelos.
        end (int): Tamanho da lista de modelos.
    
    Métodos:
        __iter__: Implementação padrão do método mágico __iter__.
        __next__: Implementação padrão do método mágico __next__.
    """
    def __init__(self, id_value: str):
        """
        Construtor da classe.
        
        Argumentos:
            id_value (str): Valor do ID da marca de carros a ser usado na URL da API.
        """
        
        # Desenvolvendo nossa URL com o ID passado
        url = "https://parallelum.com.br/fipe/api/v1/carros/marcas/{}/modelos"
        url = url.format(id_value)
        
        # Obtendo informações da API através do método GET
        response = requests.get(url_carros, headers=headers)

        # Salvando a resposta da API
        carros = response.json()
        
        # Obtendo valores para o Dict `modelos`
        self.modelos = carros['modelos']
        
        # Instanciando nosso estado atual e final
        self.current = 0
        self.end = len(self.modelos)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.modelos[self.current]
        self.current += 1
        return result


# Obtendo nosso iterador
iterator = FipeIterator("6")

# Iterando sobre nosso iterador
for modelo in iterator:
    print(modelo)






    # Desenvolvendo um Gerador a partir o Iterador acima
def fipe_generator(modelos):
    for modelo in modelos:
        yield modelo
for modelo in fipe_generator(carros['modelos']):
    print(modelo)