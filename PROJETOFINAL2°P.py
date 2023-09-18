def verificar_produto_no_deposito(produto, categoria, lista):
    if produto in lista:
        print(f"{produto} está presente na categoria {categoria}.")
    else:
        print(f"{produto} não está presente na categoria {categoria}.")


def mostrar_opcoes():
    
    print("\n ==================================")
    print("  SEJA BEM-VINDO AO NOSSO SISTEMA!")
    print(" ==================================")

    print("____________________________________")
    print("\n|     1 - VER LISTA DE PRODUTOS    |")
    print("\n|     2 - ADICIONAR PRODUTO        |")
    print("\n|     3 - REMOVER PRODUTOS         |")
    print("\n|     4 - VERIFICAR PRODUTOS       |")
    print("____________________________________")

def mostrar_lista(categoria, lista):
    print(f"\n{categoria}")
    for i, produto in enumerate(lista, start=1):
        print(f"{i}. {produto}")

def main():
    lista_frutas_verduras = ["Maçã", "Laranja", "Batata", "Tomate", "Abacaxi"]
    lista_bebidas = ["Água", "Refrigerante", "Cerveja"]
    lista_materias_limpeza = ["Detergente", "Sabão", "Sabão em pó", "Esponja"]
    lista_materias_higiene = ["Papel Higienico", "Escova de dente", "Pasta de dente", "Fio dental", "Sabonete"]

    while True:
        mostrar_opcoes()
        alternativa = input("\nDIGITE UM NÚMERO DE ACORDO COM O QUE DESEJA FAZER: ")

        if alternativa == '1':
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            print("____________________________________")
            print("\n|     1 -    FRUTAS E VERDURAS    |")
            print("\n|     2 -        BEBIDAS          |")
            print("\n|     3 -  MATERIAS DE LIMPEZA    |")
            print("\n|     4 -   MATERIAS DE HIGIENE   |")
            print("____________________________________")
            alternativa_lista = input("\nDIGITE UM NÚMERO DE ACORDO COM QUAL TIPO DE PRODUTO DESEJA: ")

            if alternativa_lista == '1':
                mostrar_lista("FRUTAS E VERDURAS", lista_frutas_verduras)
            elif alternativa_lista == '2':
                mostrar_lista("BEBIDAS", lista_bebidas)
            elif alternativa_lista == '3':
                mostrar_lista("MATERIAS DE LIMPEZA", lista_materias_limpeza)
            elif alternativa_lista == '4':
                mostrar_lista("MATERIAS DE HIGIENE", lista_materias_higiene)
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

        elif alternativa == '2':
            import os
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("____________________________________")
            print("\n|     1 -    FRUTAS E VERDURAS    |")
            print("\n|     2 -        BEBIDAS          |")
            print("\n|     3 -  MATERIAS DE LIMPEZA    |")
            print("\n|     4 -   MATERIAS DE HIGIENE   |")
            print("____________________________________")
            alternativa_adicionar = input("\nDIGITE O NÚMERO EQUIVALENTE A CATEGORIA QUE DESEJA ADICIONAR UM PRODUTO : ")

            if alternativa_adicionar == '1':
                mostrar_lista("FRUTAS E VERDURAS", lista_frutas_verduras)
                produtoP_adicionar = input("\nDigite o produto que deseja adicionar: ")
                lista_frutas_verduras.append(produtoP_adicionar)
            elif alternativa_adicionar == '2':
                mostrar_lista("BEBIDAS", lista_bebidas)
                produtoP_adicionar = input("\nDigite o produto que deseja adicionar: ")
                lista_bebidas.append(produtoP_adicionar)
            elif alternativa_adicionar == '3':
                mostrar_lista("MATERIAS DE LIMPEZA", lista_materias_limpeza)
                produtoP_adicionar = input("\nDigite o produto que deseja adicionar: ")
                lista_materias_limpeza.append(produtoP_adicionar)
            elif alternativa_adicionar == '4':
                mostrar_lista("MATERIAS DE HIGIENE", lista_materias_higiene)
                produtoP_adicionar = input("\nDigite o produto que deseja adicionar: ")
                lista_materias_higiene.append(produtoP_adicionar)
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

        elif alternativa == '3':
            import os
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("____________________________________")
            print("\n|     1 -    FRUTAS E VERDURAS    |")
            print("\n|     2 -        BEBIDAS          |")
            print("\n|     3 -  MATERIAS DE LIMPEZA    |")
            print("\n|     4 -   MATERIAS DE HIGIENE   |")
            print("____________________________________")
            alternativa_remover = input("\nDIGITE O NÚMERO EQUIVALENTE A CATEGORIA QUE DESEJA REMOVER UM PRODUTO : ")

            if alternativa_remover == '1':
                mostrar_lista("FRUTAS E VERDURAS", lista_frutas_verduras)
                produtoP_remover = input("\nDigite o produto que deseja remover: ")
                if produtoP_remover in lista_frutas_verduras:
                    lista_frutas_verduras.remove(produtoP_remover)
                else:
                    print("Produto não encontrado na lista.")
            elif alternativa_remover == '2':
                mostrar_lista("BEBIDAS", lista_bebidas)
                produtoP_remover = input("\nDigite o produto que deseja remover: ")
                if produtoP_remover in lista_bebidas:
                    lista_bebidas.remove(produtoP_remover)
                else:
                    print("Produto não encontrado na lista.")
            elif alternativa_remover == '3':
                mostrar_lista("MATERIAS DE LIMPEZA", lista_materias_limpeza)
                produtoP_remover = input("\nDigite o produto que deseja remover: ")
                if produtoP_remover in lista_materias_limpeza:
                    lista_materias_limpeza.remove(produtoP_remover)
                else:
                    print("Produto não encontrado na lista.")
            elif alternativa_remover == '4':
                mostrar_lista("MATERIAS DE HIGIENE", lista_materias_higiene)
                produtoP_remover = input("\nDigite o produto que deseja remover: ")
                if produtoP_remover in lista_materias_higiene:
                    lista_materias_higiene.remove(produtoP_remover)
                else:
                    print("\nProduto não encontrado na lista.")
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

        elif alternativa == '4':
                import os
                os.system('cls' if os.name == 'nt' else 'clear')      
                                     
                produto_verificar = input("\nDigite o nome do produto que deseja verificar: ")

                verificar_produto_no_deposito(produto_verificar, "FRUTAS E VERDURAS", lista_frutas_verduras)
                verificar_produto_no_deposito(produto_verificar, "BEBIDAS", lista_bebidas)
                verificar_produto_no_deposito(produto_verificar, "MATERIAS DE LIMPEZA", lista_materias_limpeza)
                verificar_produto_no_deposito(produto_verificar, "MATERIAS DE HIGIENE", lista_materias_higiene)
                                                                                                             
if __name__ == "__main__":
    main()
         