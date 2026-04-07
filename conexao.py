from dotenv import load_dotenv
import os

load_dotenv()

from pymongo import MongoClient
from pymongo.server_api import ServerApi

# URI UNICA
uri = os.getenv("MONGO_URI")
 
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["mercadolivre"]
 
# collections
usuario_col = db.usuario
produto_col = db.produto
compras_col = db.compras
vendedor_col = db.vendedor
favoritos_col = db.favoritos

def read_collection(col):
    print(f"\nCollection {col.name}\n")
    docs = list(col.find())

    # cursor = col.find()

    if not docs:
        print("Nenhum documento encontrado")
        return []
    
    for i, doc in enumerate(docs, start=1):
        if col == usuario_col or col == produto_col or col == vendedor_col:
            print(f"{i}. {doc["nome"]}")
        elif col == compras_col:
            print(f"{i}. {doc["valor"]}")
        else:
            print(f"{i}. {doc["produto_nome"]}")
    return docs

def select_collection(col):
    docs = read_collection(col)
    if not docs:
        return None
    
    while True:
        option = int(input("\nSelecione o número do documento: "))
        if 1 <= option <= len(docs):
            return docs[option - 1]
        else:
            print(f"Índice inválido, escolha entre 1 e {len(docs)}.")