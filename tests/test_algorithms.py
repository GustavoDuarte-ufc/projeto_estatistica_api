from src.algorithms import cal_media, cal_mediana, cal_desvio_padrao, cal_variancia, resumo_estatistico, distancia_euclidiana, multiplicar_escalar
import math 

def test_cal_media():
    assert cal_media([2, 4, 6]) == 4

def test_cal_mediana():
    assert cal_mediana([1, 3, 5]) == 3

def test_cal_mediana_par():
    assert cal_mediana([1, 2, 3, 4]) == 2.5

def test_cal_variancia():
    resultado = 8 / 3
    assert round(cal_variancia([2, 4, 6]), 2) == round(resultado, 2)

def test_cal_desvio_padrao():
    resultado = 8 / 3
    assert round(cal_desvio_padrao([2, 4, 6]), 2) == round(math.sqrt(resultado), 2)

def test_cal_resumo_estatistico():
    resultado = resumo_estatistico([2,4,6])

    assert resultado["media"] == 4
    assert resultado["mediana"] == 4
    assert resultado["minimo"] == 2
    assert resultado["maximo"] == 6
    assert resultado["amplitude"] == 4
    assert round(resultado["variancia"], 2) == 2.67
    assert round(resultado["desvio_padrao"], 2) == 1.63

def test_distancia_euclidiana():
    assert distancia_euclidiana([0,0],[3,4]) == 5

def test_multiplicar_escalar():
    assert multiplicar_escalar([1, 2, 3], 2) == [2,4,6]