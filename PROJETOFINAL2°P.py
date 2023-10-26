import time 
import os

#função para verificar produtos na lista
def verificar_produto_no_deposito(produto, categoria, lista):
    if produto in lista:
        print(f"{produto} está presente na categoria {categoria}.")
    else:
        print(f"{produto} não está presente na categoria {categoria}.")


#função para opções do sistema
def mostrar_opcoes():
    
    print("\n ==================================")
    print("  SEJA BEM-VINDO AO NOSSO SISTEMA")
    print("    DE GERENCIAMENTO DE ESTOQUE    ")
    print(" ==================================")

    print("____________________________________")
    print("\n|     1 - LISTA DE PRODUTOS        |")
    print("\n|     2 - ESTOQUE DE PRODUTOS      |")
    print("\n|     3 - ADICIONAR PRODUTO        |")
    print("\n|     4 - REMOVER PRODUTOS         |")
    print("\n|     5 - EDITAR PRODUTOS          |")
    print("____________________________________")


#função para lista de produtos organizada
def mostrar_lista(categoria, lista):
    print(f"\n{categoria}")
    for i, produto in enumerate(lista, start=1):
        print(f"{i}. {produto}")

#função main
def main():
    lista_frutas_verduras = {"Maçã":100, "Laranja":100, "Batata":100, "Tomate":100, "Abacaxi":100}
    lista_bebidas = {"Água":100, "Refrigerante":100, "Cerveja":100,"Vodka":100,"Suco":100}
    lista_materias_limpeza = {"Detergente":100, "Sabão":100, "Sabão em pó":100, "Esponja":100,"Alcool":100}
    lista_materias_higiene = {"Papel Higienico":100, "Escova de dente":100, "Pasta de dente":100, "Fio dental":100, "Sabonete":100}


#while true - loop 
    while True:
        mostrar_opcoes()
        alternativa = input("\nDIGITE UM NÚMERO DE ACORDO COM O QUE DESEJA FAZER: ")

        
        #PRINTAR LISTA DE PRODUTOS
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
            
            print("\nFRUTAS E VERDURAS")
            for produto_frutas_verduras,estoque_frutas_verduras in lista_frutas_verduras.items():
                print(produto_frutas_verduras,":",estoque_frutas_verduras,"produtos em estoque")
                time.sleep(0.2)
            time.sleep(0.5)
            
            print("\nBEBIDAS")
            for produto_bebidas,estoque_bebidas in lista_bebidas.items():
                print(produto_bebidas,":",estoque_bebidas,"produtos em estoque")
                time.sleep(0.2)
            time.sleep(0.5)

            print("\nMATERIAIS DE LIMPEZA")
            for produto_mlimpeza,estoque_mlimpeza in lista_materias_limpeza.items():
                print(produto_mlimpeza,":",estoque_mlimpeza,"produtos em estoque")
                time.sleep(0.2)
            time.sleep(0.5)
            
            print("\nMATERIAIS DE HIGIENE")
            for produto_mhigiene,estoque_mhigiene in lista_materias_higiene.items():
                print(produto_mhigiene,":",estoque_mhigiene,"produtos em estoque")
                time.sleep(0.2)    
                      
            input("\nPressione <enter> para continuar")
            
            
            os.system('cls' if os.name == 'nt' else 'clear')   
        
        #ADICIONAR PRODUTOS A LISTA
        elif alternativa == '3':
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
                produto_novo = input("\nDigite o nome do produto que deseja adicionar: ")
                estoque_novo = float(input("Quantidade de produtos em estoque: "))
                if lista_frutas_verduras.get(produto_novo):
                    print("\nProduto já existente no estoque!!!!")
                else:
                    lista_frutas_verduras[produto_novo] = round(estoque_novo)
                print("\n")
                for produto_frutas_verduras,estoque_frutas_verduras in lista_frutas_verduras.items():
                    print(produto_frutas_verduras,":",estoque_frutas_verduras,"produtos em estoque")
                    
                input("\nPressione <enter> para continuar")
            
                
                os.system('cls' if os.name == 'nt' else 'clear')   


            elif alternativa_adicionar == '2':
                mostrar_lista("BEBIDAS", lista_bebidas)
                produto_novo = input("\nDigite o nome do produto que deseja adicionar: ")
                estoque_novo = float(input("Quantidade de produtos em estoque: "))
                if lista_bebidas.get(produto_novo):
                    print("\nProduto já existente no estoque!!!!")
                else:
                    lista_bebidas[produto_novo] = round(estoque_novo)
                print("\n")
                for produto_bebidas,estoque_bebidas in lista_bebidas.items():
                    print(produto_bebidas,":",estoque_bebidas,"produtos em estoque")
                    
                input("\nPressione <enter> para continuar")
            
                
                os.system('cls' if os.name == 'nt' else 'clear')   


            elif alternativa_adicionar == '3':
                mostrar_lista("MATERIAS DE LIMPEZA", lista_materias_limpeza)
                produto_novo = input("\nDigite o nome do produto que deseja adicionar: ")
                estoque_novo = float(input("Quantidade de produtos em estoque: "))
                if lista_materias_limpeza.get(produto_novo):
                    print("\nProduto já existente no estoque!!!!")
                else:
                    lista_materias_limpeza[produto_novo] = round(estoque_novo)
                print("\n")
                for produto_mlimpeza,estoque_mlimpeza in lista_materias_limpeza.items():
                    print(produto_mlimpeza,":",estoque_mlimpeza,"produtos em estoque")
                    
                input("\nPressione <enter> para continuar")
            
                
                os.system('cls' if os.name == 'nt' else 'clear') 


            elif alternativa_adicionar == '4':
                mostrar_lista("MATERIAS DE HIGIENE", lista_materias_higiene)
                produto_novo = input("\nDigite o nome do produto que deseja adicionar: ")
                estoque_novo = float(input("Quantidade de produtos em estoque: "))
                if lista_materias_higiene.get(produto_novo):
                    print("\nProduto já existente no estoque!!!!")
                else:
                    lista_materias_higiene[produto_novo] = round(estoque_novo)
                print("\n")
                for produto_mhigiene,estoque_mhigiene in lista_materias_higiene.items():
                    print(produto_mhigiene,":",estoque_mhigiene,"produtos em estoque")
                    
                input("\nPressione <enter> para continuar")
            
                
                os.system('cls' if os.name == 'nt' else 'clear') 
                
                
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

        
        #REMOVER PRODUTOS A LISTA
        elif alternativa == '4':
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
                produtop_remover = input("\nDigite o nome do produto que deseja remover :")
                lista_frutas_verduras.pop(produtop_remover)
                
                print("\nPRODUTO REMOVIDO !!!!")
                
                print("\nLISTA ATUALIZADA DE PRODUTOS")
                
                for produto_frutas_verduras,estoque_frutas_verduras in lista_frutas_verduras.items():
                    print(produto_frutas_verduras,":",estoque_frutas_verduras,"produtos em estoque")
                    
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear') 
                


            elif alternativa_remover == '2':
                mostrar_lista("BEBIDAS", lista_bebidas)
                produtop_remover = input("\nDigite o nome do produto que deseja remover :")
                lista_bebidas.pop(produtop_remover)
                
                print("\nPRODUTO REMOVIDO !!!!")
                
                print("\nLISTA ATUALIZADA DE PRODUTOS")
                
                for produto_bebidas,estoque_bebidas in lista_bebidas.items():
                    print(produto_bebidas,":",estoque_bebidas,"produtos em estoque")
                    
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear') 



            elif alternativa_remover == '3':
                mostrar_lista("MATERIAS DE LIMPEZA", lista_materias_limpeza)
                produtop_remover = input("\nDigite o nome do produto que deseja remover :")
                lista_materias_limpeza.pop(produtop_remover)
                
                print("\nPRODUTO REMOVIDO !!!!")
                
                print("\nLISTA ATUALIZADA DE PRODUTOS")
                
                for produto_mlimpeza,estoque_mlimpeza in lista_materias_limpeza.items():
                    print(produto_mlimpeza,":",estoque_mlimpeza,"produtos em estoque")
                    
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear') 




            elif alternativa_remover == '4':
                mostrar_lista("MATERIAS DE HIGIENE", lista_materias_higiene)
                produtop_remover = input("\nDigite o nome do produto que deseja remover :")
                lista_materias_higiene.pop(produtop_remover)
                
                print("\nPRODUTO REMOVIDO !!!!")
                
                print("\nLISTA ATUALIZADA DE PRODUTOS")
                
                for produto_mhigiene,estoque_mhigiene in lista_materias_higiene.items():
                    print(produto_mhigiene,":",estoque_mhigiene,"produtos em estoque")
                    
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear') 



            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

        
        #EDITAR PRODUTOS
        elif alternativa == '5':
            import os
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("____________________________________")
            print("\n|     1 -    FRUTAS E VERDURAS    |")
            print("\n|     2 -        BEBIDAS          |")
            print("\n|     3 -  MATERIAS DE LIMPEZA    |")
            print("\n|     4 -   MATERIAS DE HIGIENE   |")
            print("____________________________________")
            alternativa_editar = input("\nDIGITE O NÚMERO EQUIVALENTE A CATEGORIA QUE DESEJA REMOVER UM PRODUTO : ")          
            
            if alternativa_editar == "1":
                produtop_editar = input("\nDigite o nome do produto que deseja editar: ")
                estoque_novo = float(input("Novo Estoque : "))

                if produtop_editar in lista_frutas_verduras.keys():
                    lista_frutas_verduras[produtop_editar] = round(estoque_novo)
                else:
                    print("Não existe esse produto!!!")
                for produto_frutas_verduras,estoque_frutas_verduras in lista_frutas_verduras.items():
                    print(produto_frutas_verduras,":",estoque_frutas_verduras,"produtos em estoque")    
                    

         
                                                                                                             
if __name__ == "__main__":
    main()
         
