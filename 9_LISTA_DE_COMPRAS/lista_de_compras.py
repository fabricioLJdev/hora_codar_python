"""
    Listas de compras funções:

    Adicionar um item a uma lista
    Remover item
    Visualizar Lista
    Limpar lista
"""

# Função exibir menu
def exibir_menu():
    print("Gerenciador Lista de Compras")
    print("1 - Adicionar item")
    print("2 - Remover um item")
    print("3 - Visualizar a lista")
    print("4 - Limpar a lista")
    print("5 - Sair")

# Adicionar item a lista
def adicionar_item(lista):
    item = input("Digite o item para adicionar na lista: ")
    lista.append(item)
    print("O item foi adicionado a sua lista!")

# Remover um item
def remover_item(lista):
    if len(lista) == 0:
        print("Sua lista está vazia.")
        return # o return faz que a função (remover_item) encerre fazendo que o programa volte para o menu
    
    item = input("Escolha o item para ser deletado: ")

    if item in lista: #(if item in lista) se o item está na lista
        lista.remove(item)
        print(f"O item {item} foi removido da lista.")

    else:
        print(f"O item {item} não está na sua lista.")


# Visualizar todos os itens da lista
def visualizar_lista(lista):
    if len(lista) == 0:
        print("Sua lista está vazia!")

    else:
        for i, item in enumerate(lista): # iteração com indice devesse usar o enumerete
            print(f"{i +1}° - {item}")


def limpar_lista(lista):
    if len(lista) == 0:
        print("Sua lista já está vazia!")
    else:
        lista.clear()
        print("Todos os itens da sua lista foram deletados.")

# Função principal
def gerenciador_lista_de_compras():

    lista_compras = []

    while True: #lanço que sempre ira se repetir ao terminar uma operação 
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item(lista_compras)

        elif opcao == "2":
            remover_item(lista_compras)

        elif opcao == "3":
            visualizar_lista(lista_compras)

        elif opcao == "4":
            limpar_lista(lista_compras)
        elif opcao == "5":
            print("Obrigado por utilizar o Gerenciador!")
            break
            
        else:
            print("Digite uma opção válida")


# Iniciar programa
if __name__ == "__main__":
    gerenciador_lista_de_compras()