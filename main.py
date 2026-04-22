from favoritos import create_favorito, delete_favorito, read_favorito
from produto import create_produto, delete_produto, update_produto, read_produto
from usuario import create_usuario, delete_usuario, update_usuario, read_usuario
from vendedor import create_vendedor, delete_vendedor, update_vendedor, read_vendedor
from compras import create_compra, delete_compra, update_compra, read_compra

acoes_crud = {
    "Usuario":   (create_usuario,  read_usuario,  update_usuario,  delete_usuario),
    "Produto":   (create_produto,  read_produto,  update_produto,  delete_produto),
    "Vendedor":  (create_vendedor, read_vendedor, update_vendedor, delete_vendedor),
    "Compras":   (create_compra,   read_compra,   update_compra,   delete_compra),
    "Favoritos": (create_favorito, read_favorito, None, delete_favorito),
}

def menu_crud(col):
    create, read, update, delete = acoes_crud[col]

    while True:
        print(f"\n{col.upper()}")
        print(f"1. Criar {col}")
        print(f"2. Ler {col}")

        if (update):
            print(f"3. Atualizar {col}")
            print(f"4. Deletar {col}")
            print(f"0. Voltar")
        else:
            print(f"3. Deletar {col}")
            print(f"0. Voltar")

        option = int(input("Escolha uma opção: "))

        if (option == 1):
            create()
        elif (option == 2):
            read()
        elif (option == 3):
            if update:
                update()
            else:
                delete()
        elif (option == 4 and update):
            delete()
        elif (option == 0):
            break
        else:
            print("Opção inválida")

def menu_col():
    while True:
        print("MENU\n")
        print("ESCOLHA A COLLECTION PARA REALIZAR AS AÇÕES CRUD:\n")
        print(
            """
1. Usuario
2. Produto
3. Vendedor
4. Compras
5. Favoritos
0. Sair
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
        elif (option == 0):
            print("Saindo.")
            break
        else:
            print("Opção inválida")
        
menu_col()