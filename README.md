# API de Estatística Descritiva

API RESTful desenvolvida com FastAPI para realizar cálculos estatísticos e operações vetoriais.

## 📌 Objetivo

Este projeto foi desenvolvido com foco em boas práticas de desenvolvimento backend utilizando Python e FastAPI, contemplando:

- Criação de endpoints REST
- Validação de dados com Pydantic
- Tratamento de erros HTTP
- Documentação automática com Swagger
- Testes automatizados com Pytest

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- Pytest

---

## 📁 Estrutura do Projeto

```text
projeto_estatistica_api/
│── src/
│   ├── api.py
│   ├── algorithms.py
│   └── schemas.py
│
│── tests/
│   ├── test_algorithms.py
│   └── test_api.py
│
│── requirements.txt
│── README.md
```

---

## ⚙️ Instalação

1. Criar ambiente virtual
```bash
python -m venv .venv
```

2. Ativar ambiente virtual

Windows PowerShell
```bash
.\.venv\Scripts\Activate.ps1
```

Linux / Mac
```bash
source .venv/bin/activate
```

3. Instalar dependências
```bash
pip install -r requirements.txt
```

--- 

## ▶️ Execução da API

Na raiz do projeto, execute:
```bash
uvicorn src.api:app --reload
```

Servidor local:
http://127.0.0.1:8000

---

## 📘 Documentação Interativa (Swagger)

Acesse:
http://127.0.0.1:8000/docs

---

## ✅ Testes

Rodar todos os testes
```bash
pytest -v
```

Rodar somente testes da API
```bash
pytest tests/test_api.py -v
```

Rodar somente testes dos algoritmos
```bash
pytest tests/test_algorithms.py -v
```

---

## 🔗 Endpoints Principais

Health Check

GET /

Estatísticas

POST /estatisticas/media

POST /estatisticas/mediana

POST /estatisticas/desvio-padrao

POST /estatisticas/resumo

Vetores

POST /vetores/distancia

POST /vetores/escalar/{valor}

---

## ⚠️ Tratamento de Erros

422 → Erro de validação dos dados

400 → Regra de negócio inválida

500 → Erro interno inesperado

---

## 👨‍💻 Autor

Paulo Gustavo Duarte da Costa
24 de Abril de 2026

