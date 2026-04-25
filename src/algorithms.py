import math

def cal_media(valores: list[float]) -> float:
    return sum(valores) / len(valores)

def cal_mediana(valores: list[float]) -> float:
    ordenados = sorted(valores)
    n = len(ordenados)
    meio = n // 2

    if n % 2 == 1:
        return ordenados[meio]
    else:
        return (ordenados[meio - 1] + ordenados[meio]) / 2
    
def cal_variancia(valores: list[float]) -> float:
    media = cal_media(valores)
    return sum((x - media) ** 2 for x in valores) / len(valores)

def cal_desvio_padrao(valores: list[float]) -> float:
    return math.sqrt(cal_variancia(valores))

def resumo_estatistico(valores: list[float]) -> dict:
    minimo = min(valores)
    maximo = max(valores)

    return {
        "media": cal_media(valores),
        "mediana": cal_mediana(valores),
        "minimo": minimo,
        "maximo": maximo,
        "amplitude": maximo - minimo,
        "variancia": cal_variancia(valores),
        "desvio_padrao": cal_desvio_padrao(valores)
    }

def distancia_euclidiana(vetor_a: list[float], vetor_b: list[float]) -> list[float]:
    soma = sum((a - b) ** 2 for a, b in zip(vetor_a, vetor_b))
    return math.sqrt(soma)

def multiplicar_escalar(valores: list[float], escalar: float) -> list[float]:
    return [x * escalar for x in valores]