from conexao import favoritos_col, usuario_col, produto_col, select_collection
from produto import select_collection as select_produto

def create_favorito():
    print("\nSelecione o usuario: ")
    usuario = select_collection(usuario_col)
    if usuario is None:
        return
    
    print("\nSelecione o produto: ")
    produto = select_produto(produto_col)
    if produto is None:
        return
    
    favoritos = usuario.get("favoritos", [])
    ja_favoritado = any(fav["produto_id"] == produto["_id"] for fav in favoritos)
    if ja_favoritado:
        print(f"Produto '{produto["nome"]}' já está favoritado")
        return

    favorito = {
        "usuario_id": usuario["_id"],
        "produto_id": produto["_id"],
        "usuario_nome": usuario["nome"],
        "produto_nome": produto["nome"],
        "produto_descricao": produto["descricao"],
        "produto_preco": produto["preco"]
    }


    usuario_col.update_one(
        {"_id": usuario["_id"]},
        {"$push": {"favoritos": favorito}}
    )
    print("Produto " + produto["nome"] + " foi adicionado como favorito para o usuario " + usuario["nome"])


def delete_favorito():
    print("\nSelecione o usuário: ")
    usuario = select_collection(usuario_col)
    if usuario is None:
        return

    fav, _ = select_favorito(usuario)
    if fav is None:
        return

    usuario_col.update_one(
        {"_id": usuario["_id"]},
        {"$pull": {"favoritos": {"produto_id": fav["produto_id"]}}}
    )
    print(f"Favorito '{fav['produto_nome']}' removido com sucesso.")

def select_favorito(usuario):
    favoritos = usuario.get("favoritos", [])
    if not favoritos:
        print("Nenhum favorito encontrado.")
        return None, None

    for i, fav in enumerate(favoritos, start=1):
        print(f"{i}. {fav['produto_nome']} - R$ {fav['produto_preco']}")

    while True:
        option = int(input("\nSelecione o número do favorito: "))
        if 1 <= option <= len(favoritos):
            return favoritos[option - 1], option - 1
        print(f"Índice inválido, escolha entre 1 e {len(favoritos)}.")


# def update_favorito():
#     print("\nSelecione o usuario: ")
#     usuario = select_collection(usuario_col)
#     if usuario is None:
#         return
    
#     fav, idx = select_favorito(usuario)
#     if fav is None:
#         return
    
#     ignored_fields = ["usuario_id", "produto_id", "usuario_nome"]
#     new_values = {}
#     for field in fav:
#         if field in ignored_fields:
#             continue
#         novo = input(f"{field} [{fav[field]}]: ".strip())
#         if novo:
#             new_values[field] = novo

#     usuario_col.update_one(
#         {"_id": usuario["_id"]},
#         {"$set": {f"favoritos.{idx}.{k}": v for k, v in new_values.items()}}
#     )
#     print("Favorito atualizado com sucesso")


def read_favorito():
    print("\nSelecione o usuario: ")
    usuario = select_collection(usuario_col)
    if usuario is None:
        return
    
    favoritos = usuario.get("favoritos")
    if not favoritos:
        print("Nenhum favorito encontrado.")
        return

    fav, _ = select_favorito(usuario)
    if fav is None:
        return
    
    print(fav)    
    # for i, fav in enumerate(favoritos, start=1):
    #     print(f"{i}. {fav["produto_nome"]} - R$ {fav["produto_preco"]}")

