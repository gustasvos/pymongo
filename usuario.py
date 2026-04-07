from conexao import usuario_col, select_collection

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
    print("Usuário inserido com _id", x.inserted_id)

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

        
def read_usuario():
    print("\nSelecione o documento que deseja visualizar: ")
    doc = select_collection(usuario_col)

    if doc is None:
        return

    print(doc)

read_usuario()