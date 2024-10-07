from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

#Enum dos produtos disponíveis
class ProdutoEnum(str, Enum):
    produto1 = "Gemini"
    produto2 = "ChatGPT"
    produto3 = "Llama3.0"

#Validação dos dados
class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum