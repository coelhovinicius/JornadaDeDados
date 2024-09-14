from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validator, PositiveFloat, PositiveInt
from enum import Enum

#Enum dos produtos disponíveis
class ProdutoEnum(str, Enum):
    produto1 = "Análise com Gemini"
    produto2 = "Análise com ChatGPT"
    produto3 = "Análise com Llama3.0"

#Validação dos dados
class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    #Validador customizável
    #@validator('produto')
    #def categoria_deve_estar_no_enum(cls, v):
    #    return v