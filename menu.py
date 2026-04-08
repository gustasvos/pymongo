from favoritos import create_favorito, delete_favorito, update_favorito, read_favorito
from produto import create_produto, delete_produto, update_produto, read_produto
from usuario import create_usuario, delete_usuario, update_usuario, read_usuario
from vendedor import create_vendedor, delete_vendedor, update_vendedor, read_vendedor
from compras import create_compra, delete_compra, update_compra, read_compra

def menu_crud(col):
    print(
        f"""
        1. Criar + {col}
        2. Ler + {col}
        3. Atualizar + {col}
        4. Deletar + {col}
        """
    )
    option = int(input("Escolha uma opção: "))

    if (option == 1):
        
    elif (option == 2):
        menu_crud("Produto")
    elif (option == 3):
        menu_crud("Vendedor")
    elif (option == 4):
        menu_crud("Compras")
    elif (option == 5):
        menu_crud("Favoritos")

def menu_col():
    print("MENU\n")
    print("ESCOLHA A COLLECTION PARA REALIZAR AS AÇÕES CRUD:\n")
    print(
        """
        1. Usuario
        2. Produto
        3. Vendedor
        4. Compras
        5. Favoritos
        """
    )
    option = int(input("Escolha uma opção: "))

    if (option == 1):
        menu_crud("Usuario")
        return "usuario"
    elif (option == 2):
        menu_crud("Produto")
    elif (option == 3):
        menu_crud("Vendedor")
    elif (option == 4):
        menu_crud("Compras")
    elif (option == 5):
        menu_crud("Favoritos")
    
