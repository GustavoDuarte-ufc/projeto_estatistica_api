from pydantic import BaseModel, Field, model_validator
from typing import List

class ListaValores(BaseModel):
    valores: List[float] = Field(
        min_length=1,
        description="Lista de números reais",
        examples=[[8.0, 10, 7.5]]
    )

class ListaDesvio(BaseModel):
    valores: List[float] = Field(
        min_length=2,
        examples=[[8.0, 10, 7.5]])

    @model_validator(mode="after")
    def validar_valores(self):
        if len(set(self.valores)) == 1:
            raise ValueError("Todos os são iguais.")
        return self

class DoisVetores(BaseModel):
    vetor_a: List[float] = Field(min_length=1)
    vetor_b: List[float] = Field(min_length=1)

    @model_validator(mode="after")
    def validar_mesmo_tamanho(self):
        if len(self.vetor_a) != len(self.vetor_b):
            raise ValueError("Os vetores devem ter o mesmo tamanho.")
        return self
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "vetor_a": [1.0, 2.0, 3.0],
                "vetor_b": [4.0, 5.0, 6.0]
            }
        }
    }
    
class ResumoEstatistico(BaseModel):
    media: float
    mediana: float
    minimo: float
    maximo: float
    amplitude: float
    variancia: float
    desvio_padrao: float
