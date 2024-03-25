from fastapi import APIRouter
from .Produto import Produto

router = APIRouter()

@router.get("/produto/", tags=["Produto"])
def get_produtos():
    return {"msg": "Lista dos produtos"}

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    return {"msg": f"Informações do produto com id {id}"}

@router.post("/produto/", tags=["Produto"])
def post_produto(produto: Produto):
    return {"msg": "Produto criado", "produto": produto.dict()}

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, produto: Produto):
    return {"msg": f"Produto com id {id} atualizado", "produto": produto.dict()}

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    return {"msg": f"Produto com id {id} removido"}
