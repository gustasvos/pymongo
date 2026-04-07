from conexao import vendedor_col, select_collection

def create_vendedor():
    print("\nInserindo um novo vendedor")

    nome = input("Nome: ")
    cnpj = input("CNPJ: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

    print("\nEndereço:")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    rua = input("Rua: ")
    numero = input("Número: ")

    vendedor_doc = {
        "nome": nome,
        "cnpj": cnpj,
        "email": email,
        "senha": senha,
        "endereco": {
            "cep": cep,
            "cidade": cidade,
            "estado": estado,
            "rua": rua,
            "numero": numero
        }
    }
    
    new_vendedor = vendedor_col.insert_one(vendedor_doc)
    print("vendedor inserido com _id", new_vendedor.inserted_id)

def delete_vendedor():
    print("\nSelecione o vendedor para remover: ")
    doc = select_collection(vendedor_col)

    if doc is None:
        return
    
    deleted_doc = vendedor_col.delete_one({"_id": doc["_id"]})
    print("vendedor deletado com sucesso", deleted_doc)

def update_vendedor():
    print("\nSelecione o vendedor para atualizar: ")
    doc = select_collection(vendedor_col)

    if doc is None:
        return
    
    print("Dados do vendedor:\n", doc)

    ignored_fields = ["_id"]
    new_values = {}

    for field in doc:
        if field in ignored_fields:
            continue
        new_doc = input(f"Novo {field} ({doc[field]}): ").strip()
        if new_doc:
            new_values[field] = new_doc

        print(f"\nEndereço atual: {doc['endereco']['rua']}, {doc['endereco']['numero']} - {doc['endereco']['cidade']}/{doc['endereco']['estado']}")
        escolha = input("Deseja alterar este endereço? (S para seguir): ")

        if escolha == "s" or escolha == "S":
            new_endereco = {}
            for field in doc["endereco"]:
                new_doc = input(f"{field} [{doc['endereco'][field]}]: ").strip()
                new_endereco[field] = new_doc if new_doc else doc["endereco"][field]
            new_values["endereco"] = new_endereco

    vendedor_col.update_one({"_id": doc["_id"]}, {"$set": new_values})
    print("vendedor atualizado com sucesso.")

        
def read_vendedor():
    print("\nSelecione o documento que deseja visualizar: ")
    doc = select_collection(vendedor_col)

    if doc is None:
        return

    print(doc)

# delete_vendedor()