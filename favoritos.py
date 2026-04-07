from conexao import favoritos_col, select_collection

def create_favorito():
    print("\nInserindo um novo favorito")
    usuario_nome = input("Nome do usuário: ")
    produto_nome = input("Nome do produto: ")
    produto_descricao = input("Descrição do produto: ")
    produto_preco = float(input("Preço do produto: "))

    favorito_doc = {
        "usuario_nome": usuario_nome,
        "produto_nome": produto_nome,
        "produto_descricao": produto_descricao,
        "produto_preco": produto_preco
    }

    new_favorito = favoritos_col.insert_one(favorito_doc)
    print("Favorito inserido com _id", new_favorito.inserted_id)


def delete_favorito():
    print("\nSelecione o favorito para remover: ")
    doc = select_collection(favoritos_col)
    if doc is None:
        return

    favoritos_col.delete_one({"_id": doc["_id"]})
    print("Favorito deletado com sucesso.")


def update_favorito():
    print("\nSelecione o favorito para atualizar: ")
    doc = select_collection(favoritos_col)
    if doc is None:
        return

    print("Dados do favorito:\n", doc)
    ignored_fields = ["_id"]
    new_values = {}
    for field in doc:
        if field in ignored_fields:
            continue
        new_doc = input(f"Novo {field} ({doc[field]}): ").strip()
        if new_doc:
            new_values[field] = new_doc

    favoritos_col.update_one({"_id": doc["_id"]}, {"$set": new_values})
    print("Favorito atualizado com sucesso.")


def read_favorito():
    print("\nSelecione o documento que deseja visualizar: ")
    doc = select_collection(favoritos_col)
    if doc is None:
        return
    print(doc)