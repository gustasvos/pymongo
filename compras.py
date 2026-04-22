from conexao import compras_col, usuario_col, produto_col, vendedor_col, select_collection
import random

def create_compra():
    print("\nSelecione o usuário: ")
    usuario = select_collection(usuario_col)
    if usuario is None:
        return

    print("\nSelecione o produto: ")
    produto = select_collection(produto_col)
    if produto is None:
        return
    
    vendedores = list(vendedor_col.find())
    if vendedores:
        vendedor = random.choice(vendedores)
        vendedor_id = vendedor["_id"]
        vendedor_nome = vendedor["nome"]
    else:
        vendedor_id = None
        vendedor_nome = ""

    frete = float(input("Frete: "))
    produto_preco = float(produto["preco"])

    compra_doc = {
        "usuario_id": usuario["_id"],
        "vendedor_id": vendedor_id,
        "produto_id": produto["_id"],
        "usuario_nome": usuario["nome"],
        "vendedor_nome": vendedor_nome,
        "produto_nome": produto["nome"],
        "produto_preco": produto["preco"],
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

    new_values = {}
    # ignored_fields = ["_id", "valor", "usuario_id", "vendedor_id", "produto_id",
    #                   "usuario_nome", "vendedor_nome", "produto_nome", "produto_preco"]


    print("\nDeseja trocar o usuário? (S/N): ", end="")
    if input().upper() == "S":
        usuario = select_collection(usuario_col)
        if usuario:
            new_values["usuario_id"] = usuario["_id"]
            new_values["usuario_nome"] = usuario["nome"]

    print("Deseja trocar o vendedor? (S/N): ", end="")
    if input().upper() == "S":
        vendedor = select_collection(vendedor_col)
        if vendedor:
            new_values["vendedor_id"] = vendedor["_id"]
            new_values["vendedor_nome"] = vendedor["nome"]

    print("Deseja trocar o produto? (S/N): ", end="")
    if input().upper() == "S":
        produto = select_collection(produto_col)
        if produto:
            new_values["produto_id"] = produto["_id"]
            new_values["produto_nome"] = produto["nome"]
            new_values["produto_preco"] = produto["preco"]


    novo_frete = input(f"Frete [{doc['frete']}]: ").strip()
    if novo_frete:
        new_values["frete"] = float(novo_frete)
    produto_preco = new_values.get("produto_preco", doc["produto_preco"])
    frete = new_values.get("frete", doc["frete"])
    new_values["valor"] = produto_preco + frete


    compras_col.update_one({"_id": doc["_id"]}, {"$set": new_values})
    print("Compra atualizada com sucesso.")


def read_compra():
    print("\nSelecione o documento que deseja visualizar: ")
    doc = select_collection(compras_col)
    if doc is None:
        return
    print(doc)