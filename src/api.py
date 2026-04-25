from fastapi import FastAPI, HTTPException, Query
from src.schemas import ListaValores, ListaDesvio, DoisVetores, ResumoEstatistico
from src.algorithms import (
    cal_media,
    cal_mediana,
    cal_desvio_padrao,
    resumo_estatistico,
    distancia_euclidiana,
    multiplicar_escalar
)

app = FastAPI(
    title="API de Estatística Descritiva",
    description="API RESTful para cálculos estatísticos com FastAPI",
    version="0.1.0"
)

@app.get("/", tags=["Health"])
def health():
    return {"status": "ok", "versao": "0.1.0"}

@app.post("/estatisticas/media", tags=["Estatísticas"])
def media(dados: ListaValores):
    try:
        resultado = cal_media(dados.valores)
        return {"media": resultado}

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao calcular média."
        )

@app.post("/estatisticas/mediana", tags=["Estatísticas"])
def mediana(dados: ListaValores):
    try:
        return {"mediana": cal_mediana(dados.valores)}

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao calcular mediana."
        )

@app.post("/estatisticas/desvio-padrao", tags=["Estatísticas"])
def desvio_padrao(dados: ListaDesvio):
    try:
        return {"desvio_padrao": cal_desvio_padrao(dados.valores)}

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao calcular desvio padrão."
        )

@app.post(
    "/estatisticas/resumo",
    tags=["Estatísticas"],
    response_model=ResumoEstatistico
)
def resumo(
    dados: ListaValores,
    decimais: int = Query(2, ge=0, le=6)
):
    try:
        if len(dados.valores) < 2:
            raise HTTPException(
                status_code=400,
                detail="Resumo exige pelo menos 2 valores."
            )

        resultado = resumo_estatistico(dados.valores)

        for chave in resultado:
            resultado[chave] = round(resultado[chave], decimais)

        return resultado

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao gerar resumo."
        )

@app.post("/vetores/distancia", tags=["Vetores"])
def distancia(dados: DoisVetores):
    try:
        return {
            "distancia": round(
                distancia_euclidiana(dados.vetor_a, dados.vetor_b), 2
            )
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao calcular distância."
        )

@app.post("/vetores/escalar/{valor}", tags=["Vetores"])
def escalar(valor: float, dados: ListaValores):
    try:
        return {
            "resultados": multiplicar_escalar(dados.valores, valor)
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao multiplicar vetor por escalar."
        )