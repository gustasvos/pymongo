from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gustavo:yQbJQxTZwPH5DThw@dsm-bdnosql.ic9sxoy.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["mercadolivre"]

enderecos = []

def create_usuario():
    global db
    mycol = db.usuario
    print("\nInserindo um novo usuário")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")
    cartao = input("Cartão: ")

    enderecos = []
    while True:
        cep = input("CEP: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        rua = input("Rua: ")
        numero = input("Número: ")
        enderecos.append({
            "cep": cep,
            "cidade": cidade,
            "estado": estado,
            "rua": rua,
            "numero": numero
        })
        if input("Adicionar outro endereço? (S/N): ").upper() == "N":
            break

    mydoc = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "cpf": cpf,
        "endereco": enderecos,
        "cartao": cartao
    }

    x = mycol.insert_one(mydoc)
    print("Documento inserido com _id", x.inserted_id)

