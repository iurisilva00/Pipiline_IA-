from datetime import datetime
from typing import Tuple

from pydantic import BaseModel,PositiveFloat,PositiveInt, EmailStr, validate_call
from enum import Enum
class ProdutoEnum(str,Enum):        
    produto1="Zapflow com Gemini"
    produto2="Zapflow com ChatGpt"
    produto3="Zapflow com Llama"

class Vendas(BaseModel):
    email: EmailStr
    data:datetime
    valor:PositiveFloat
    quantidade:PositiveInt
    produto:ProdutoEnum
