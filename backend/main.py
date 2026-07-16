# Importa a classe principal do FastAPI para criação do nosso servidor
from fastapi import FastAPI
# Importa o StaticFiles para servir arquivos estáticos como imagens
from fastapi.staticfiles import StaticFiles
# Importa o módulo os para trabalhar com caminhos de diretório
import os

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define o caminho absoluto da pasta de imagens para o servidor encontrar a pasta independente de onde for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura os arquivos estáticos: monta a pasta PASTA_IMAGENS na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Mapeamento completo dos metadados das figurinhas (nome e categoria) por ID com base no index.html
METADADOS = {
    1: {"nome": "Alan Turing", "categoria": "IA"},
    2: {"nome": "John McCarthy", "categoria": "IA"},
    3: {"nome": "Sam Altman", "categoria": "IA"},
    4: {"nome": "Geoffrey Hinton", "categoria": "IA"},
    5: {"nome": "Yann LeCun", "categoria": "IA"},
    6: {"nome": "Guido van Rossum", "categoria": "PYTHON"},
    7: {"nome": "Tim Peters", "categoria": "PYTHON"},
    8: {"nome": "Raymond Hettinger", "categoria": "PYTHON"},
    9: {"nome": "Travis Oliphant", "categoria": "PYTHON"},
    10: {"nome": "Wes McKinney", "categoria": "PYTHON"},
    11: {"nome": "Edgar F. Codd", "categoria": "BANCO DE DADOS"},
    12: {"nome": "Larry Ellison", "categoria": "BANCO DE DADOS"},
    13: {"nome": "Michael Widenius", "categoria": "BANCO DE DADOS"},
    14: {"nome": "Salvatore Sanfilippo", "categoria": "BANCO DE DADOS"},
    15: {"nome": "Eliot Horowitz", "categoria": "BANCO DE DADOS"},
    16: {"nome": "Linus Torvalds", "categoria": "SISTEMAS OPERACIONAIS"},
    17: {"nome": "Dennis Ritchie", "categoria": "SISTEMAS OPERACIONAIS"},
    18: {"nome": "Richard Stallman", "categoria": "SISTEMAS OPERACIONAIS"},
    19: {"nome": "Bill Gates", "categoria": "SISTEMAS OPERACIONAIS"},
    20: {"nome": "Steve Jobs", "categoria": "SISTEMAS OPERACIONAIS"},
    21: {"nome": "Paulo Silveira", "categoria": "BRASIL"},
    22: {"nome": "Guilherme Silveira", "categoria": "BRASIL"},
    23: {"nome": "Gustavo Guanabara", "categoria": "BRASIL"},
    24: {"nome": "Maurício Aniche", "categoria": "BRASIL"},
    25: {"nome": "Andre David", "categoria": "BRASIL"},
    26: {"nome": "Guilherme Lima", "categoria": "BRASIL"},
    27: {"nome": "Gi Space Coding", "categoria": "BRASIL"},
    28: {"nome": "Vinicius Neves", "categoria": "BRASIL"},
    29: {"nome": "Rafaela Ballerini", "categoria": "BRASIL"},
    30: {"nome": "Você", "categoria": "BRASIL"}
}

# Função que analisa a pasta de figurinhas e gera a lista dinamicamente
def carregar_figurinhas():
    figurinhas_list = []
    ids_adicionados = set()
    
    if os.path.exists(PASTA_IMAGENS):
        # Lista e ordena os arquivos para consistência
        arquivos = sorted(os.listdir(PASTA_IMAGENS))
        for arquivo in arquivos:
            # Separa o nome do arquivo para extrair o ID (ex: "01-alan-turing.jpg" -> "01")
            partes = arquivo.split("-")
            if partes and partes[0].isdigit():
                id_fig = int(partes[0])
                # Garante que não adicionamos IDs duplicados e que o ID existe nos metadados
                if id_fig in METADADOS and id_fig not in ids_adicionados:
                    meta = METADADOS[id_fig]
                    figurinhas_list.append({
                        "id": id_fig,
                        "nome": meta["nome"],
                        "categoria": meta["categoria"],
                        "imagem_url": f"/imgs/{arquivo}"
                    })
                    ids_adicionados.add(id_fig)
                    
    # Ordena a lista pelo ID da figurinha
    figurinhas_list.sort(key=lambda x: x["id"])
    return figurinhas_list

# Cria a lista de figurinhas com base nos arquivos presentes na pasta figurinhas
figurinhas = carregar_figurinhas()

# Define a rota GET "/figurinhas" que retorna a lista de figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas


