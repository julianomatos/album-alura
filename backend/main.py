# Importa a classe principal do FastAPI para criação do nosso servidor
from fastapi import FastAPI

# Cria a instância da aplicação FastAPI que gerenciará nossas rotas e requisições
app = FastAPI()

# Define a rota para requisições do tipo GET no caminho raiz ("/")
@app.get("/")
def hello_world():
    # Retorna o dicionário que será convertido automaticamente para JSON pelo FastAPI
    return {"mensagem": "Olá, mundo! 🌍"}

# Define a rota para obter a lista de figurinhas do álbum
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna uma lista de dicionários contendo os dados das figurinhas de exemplo
    return [
        {"id": 1, "nome": "Alan Turing", "categoria": "IA"},
        {"id": 2, "nome": "John McCarthy", "categoria": "IA"}
    ]
