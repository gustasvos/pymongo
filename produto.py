from conexao import produto_col, select_collection

def create_produto():
    print("\nInserindo um novo produto")

    nome = input("Nome: ")
    descricao = input("Descricao: ")
    preco = float(input("Preço: "))

    produto_doc = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco
    }
    
    new_produto = produto_col.insert_one(produto_doc)
    print("Produto inserido com _id", new_produto.inserted_id)

def delete_produto():
    print("\nSelecione o produto para remover: ")
    doc = select_collection(produto_col)

    if doc is None:
        return
    
    deleted_doc = produto_col.delete_one({"_id": doc["_id"]})
    print("Produto deletado com sucesso", deleted_doc)

def update_produto():
    print("\nSelecione o Produto para atualizar: ")
    doc = select_collection(produto_col)

    if doc is None:
        return
    
    print("Dados do produto:\n", doc)

    ignored_fields = ["_id"]
    new_values = {}

    for field in doc:
        if field in ignored_fields:
            continue
        new_doc = input(f"Novo {field} ({doc[field]}): ").strip()
        if new_doc:
            new_values[field] = new_doc

    produto_col.update_one({"_id": doc["_id"]}, {"$set": new_values})
    print("produto atualizado com sucesso.")

        
def read_produto():
    print("\nSelecione o documento que deseja visualizar: ")
    doc = select_collection(produto_col)

    if doc is None:
        return

    print(doc)

# delete_produto()