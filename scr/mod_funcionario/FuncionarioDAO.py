from fastapi import APIRouter
from mod_funcionario.Funcionario import Funcionario
import requests

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionario():
    return {"msg": "get deu bom"}

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    return {"msg": "get um executado"}

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(f: Funcionario):
    return {"msg": "post executado", "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, f: Funcionario):
    return {"msg": "put executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}

# URL do seu servidor FastAPI
url = "http://localhost:8000/funcionario/"

# Dados do funcionário a serem enviados
data = {
    "nome": "João",
    "cpf": "123.456.789-00",
    "telefone": "123456789"
}

# Enviar a solicitação POST
response = requests.post(url, json=data)

# Verificar a resposta
if response.status_code == 200:
    print("Funcionário criado com sucesso:")
    print(response.json())
else:
    print("Erro ao criar o funcionário:")
    print(response.text)

