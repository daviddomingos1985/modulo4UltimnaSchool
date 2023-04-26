from exercicio3 import validar_medida, \
    calcular_preco_volume, \
        calcular_multiplicador_peso, \
            calcular_multiplicador_rota, \
                calcular_frete
import pytest

# TESTE FUNÇAO VALIDAR MEDIDA PARA ENTRADA NUMERICA
def testValidarMedidaNumero():
    assert validar_medida('5') == 5
    
#TESTE DA FUNÇÃO VALIDAR MEDIDA PARA ENTRADA NÃO NUMERICA
def testValidarMedidaNaoNumero():
    assert validar_medida('abc') == -1

#TESTE DA FUNÇÃO CALCULAR PREÇO VOLUME COM VOLUME MENOR QUE 1000
def testCalcularPrecoVolumeMenorQue1000():
    assert calcular_preco_volume(500) == 10.0
    
#TESTE DA FUNÇÃO CALCULAR PREÇO DO VOLUME COM VOLUME ENTRE 1000 E 10000
def testCalcularPrecoVolume1000entre10000():
    assert calcular_preco_volume(5000) == 20.0

#TESTE DA FUNÇAO CALCULAR PREÇO VOLUME ENTRE 10000 E 30000
def testCalcularPrecoVolumeEntre10000e30000():
    assert calcular_preco_volume(15000) == 30.0
   
#TESTE DA FUNÇAO CALCULAR PREÇO VOLUME ENTRE 30000 E 100000
def testCalcularPrecoVolumeEntre30000e100000():
    assert calcular_preco_volume(50000) == 20.0
   
#TESTE DA FUNÇAO CALCULAR PREÇO VOLUME MAIOR QUE 100000
def testCalcularPrecoVolumeMaiorQue100000():
    assert calcular_preco_volume(150000) == 00.0
   
#TESTE PARA OBJETO COM PESO DE 0.05KG
def testCalcularMutiplicadorPeso50g():
    assert calcular_multiplicador_peso(0.05) == 1.0
    
#TESTE PARA OBJETO COM PESO DE 0,5kg
def testCalcularMutiplicadorPeso500g():
    assert calcular_multiplicador_peso(0.5) == 1.5
    
#TESTE PARA OBJETO COM PESO DE 5KG
def testCalcularMutiplicadorPeso5kg():
    assert calcular_multiplicador_peso(5) == 2.0
    
#TESTE PARA OBJETO COM PESO DE 20KG
def testCalcularMutiplicadorPeso20kg():
    assert calcular_multiplicador_peso(20) == 3.0
    
#TESTE PARA OBJETO COM PESO DE 31KG
def testCalcularMutiplicadorPeso31kg():
    assert calcular_multiplicador_peso(31) == 0        
    
#TESTE PARA OBJETO COM PESO ACIMA DO PERMITIDO
def calcularMultiplicadorPesoForaDoLimite():
    assert calcular_multiplicador_peso(31) == 0
    
#TESTE DE VERIFICAÇÃO DA FUNÇÃO SIGLA 'BR'
def testCalculadorDeRotaBR():
    assert calcular_multiplicador_rota('br') == 1.5
    
#TESTE DE VERIFICAÇÃO DA FUNÇÃO SIGLA 'rs'
def testCalculadorDeRotaRS():
    assert calcular_multiplicador_rota('rs') == 1.0    
    
#TESTE DE VERIFICAÇÃO DA FUNÇÃO SIGLA 'SB'
def testCalculadorDeRotaSB():
    assert calcular_multiplicador_rota('SB') == 1.2
    
def testeCalcularFrete():
    assert calcular_frete(1000, 1.5, 1.0) == 1500
    assert calcular_frete(2000, 2.0, 1.2) == 4800
    assert calcular_frete(5000, 3.0, 1.5) == 22500
       