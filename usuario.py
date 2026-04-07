from pymongo import MongoClient
from pymongo.server_api import ServerApi
 
uri = "mongodb+srv://gustavo:yQbJQxTZwPH5DThw@dsm-bdnosql.ic9sxoy.mongodb.net/?retryWrites=true&w=majority"
 
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["mercadolivre"]
 
# collections
usuario_col = db.usuario
produto_col = db.produto
compras_col = db.compras
vendedor_col = db.vendedor

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
 

def create_usuario():
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
        if input("Deseja cadastrar um novo endereço? (S/N): ").upper() == "N":
            break
 
    usuario_doc = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "cpf": cpf,
        "endereco": enderecos,
        "cartao": cartao
    }
 
    x = usuario_col.insert_one(usuario_doc)
    print("Documento inserido com _id", x.inserted_id)

def delete_usuario():
    print("\nSelecione o usuario para remover: ")
    doc = select_collection(usuario_col)

    if doc is None:
        return
    
    deleted_doc = usuario_col.delete_one({"_id": doc["_id"]})
    print("Usuário deletado com sucesso", deleted_doc)

def update_usuario():
    print("\nSelecione o usuário para atualizar: ")
    doc = select_collection(usuario_col)

    if doc is None:
        return
    
    print("Dados do usuário:\n", doc)

    ignored_fields = ["_id", "endereco"]
    new_values = {}

    for field in doc:
        if field in ignored_fields:
            continue
        new_doc = input(f"Novo {field} ({doc[field]}): ").strip()
        if new_doc:
            new_values[field] = new_doc
    
    enderecos_atualizados = []
    for i, endereco in enumerate(doc["endereco"], start=1):
        print(f"\nEndereço {i}: {endereco['rua']}, {endereco['numero']} - {endereco['cidade']}/{endereco['estado']}")
        escolha = input("Deseja alterar este endereço? (S para seguir): ")

        if escolha == "s" or escolha == "S":
            new_endereco = {}
            for field in endereco:
                new_doc = input(f"{field} [{endereco[field]}]: ").strip()
                new_endereco[field] = new_doc if new_doc else endereco[field]
            enderecos_atualizados.append(new_endereco)
        else:
            enderecos_atualizados.append(endereco)
    new_values["endereco"] = enderecos_atualizados

    usuario_col.update_one({"_id": doc["_id"]}, {"$set": new_values})
    print("Usuario atualizado com sucesso.")

        



read_collection(usuario_col)
# read_collection(vendedor_col)

# update_usuario()
 
# create_usuario()
 
# Returns all documents, but excludes the _id field
# cursor = usuario_col.find()
# for document in cursor:
#     print(document["nome"] + ' ' + document["email"])
