from conexao import compras_col, select_collection

def create_compra():
    print("\nInserindo uma nova compra")
    usuario_nome = input("Nome do usuário: ")
    vendedor_nome = input("Nome do vendedor: ")
    produto_nome = input("Nome do produto: ")
    produto_preco = float(input("Preço do produto: "))
    frete = float(input("Frete: "))

    compra_doc = {
        "usuario_nome": usuario_nome,
        "vendedor_nome": vendedor_nome,
        "produto_nome": produto_nome,
        "produto_preco": produto_preco,
        "frete": frete,
        "valor": produto_preco + frete
    }

    new_compra = compras_col.insert_one(compra_doc)
    print("Compra inserida com _id", new_compra.inserted_id)


def delete_compra():
    print("\nSelecione a compra para remover: ")
    doc = select_collection(compras_col)
    if doc is None:
        return

    compras_col.delete_one({"_id": doc["_id"]})
    print("Compra deletada com sucesso.")


def update_compra():
    print("\nSelecione a compra para atualizar: ")
    doc = select_collection(compras_col)
    if doc is None:
        return

    print("Dados da compra:\n", doc)
    ignored_fields = ["_id", "valor"]
    new_values = {}
    for field in doc:
        if field in ignored_fields:
            continue
        new_doc = input(f"Novo {field} ({doc[field]}): ").strip()
        if new_doc:
            new_values[field] = new_doc

    produto_preco = float(new_values.get("produto_preco", doc["produto_preco"]))
    frete = float(new_values.get("frete", doc["frete"]))
    new_values["valor"] = produto_preco + frete

    compras_col.update_one({"_id": doc["_id"]}, {"$set": new_values})
    print("Compra atualizada com sucesso.")


def read_compra():
    print("\nSelecione o documento que deseja visualizar: ")
    doc = select_collection(compras_col)
    if doc is None:
        return
    print(doc)