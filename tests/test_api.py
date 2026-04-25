from fastapi.testclient import TestClient
from src.api import app

cliente = TestClient(app)

def test_health_sucesso_200():
    response = cliente.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_media_sucesso_200():
    response = cliente.post(
        "/estatisticas/media",
        json={"valores": [2,4,6]}
    )

    assert response.status_code == 200
    assert response.json()["media"] == 4

def test_media_erro_422():
    response = cliente.post(
        "/estatisticas/media",
        json={"valores": []}
    )

    assert response.status_code == 422

def test_resumo_erro_400():
    response = cliente.post(
        "/estatisticas/resumo",
        json={"valores": [10]}
    )

    assert response.status_code == 400

def test_desvio_padrao_erro_422():
    response = cliente.post(
        "/estatisticas/desvio-padrao",
        json={"valores": [5,5,5]}
    )

    assert response.status_code == 422

def test_distancia_sucesso_200():
    response = cliente.post(
        "/vetores/distancia",
        json={
            "vetor_a": [0,0],
            "vetor_b": [3,4]
        }
    )

    assert response.status_code == 200
    assert response.json()["distancia"] == 5

def test_escalar_sucesso_200():
    response = cliente.post(
        "/vetores/escalar/2",
        json={"valores": [1,2,3]}
    )

    assert response.status_code == 200
    assert response.json()["resultados"] == [2,4,6]

def test_escalar_erro_422():
    response = cliente.post(
        "/vetores/escalar/abc",
        json={"valores": [1,2,3]}
    )

    assert response.status_code == 422
