from pydantic import BaseModel
from decimal import Decimal

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    valor_unitario: Decimal
    foto: bytes = None
