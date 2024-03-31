lista_livros = []
id_global = 0

choices = [1, 2, 3, 4] #lista de escolhas

def menu():
    print(50 * "-")
    print("Ecolha a opção desejada: ")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livros(s)")
    print("3 - Remover Livro")
    print("4 - Sair")

    print(50 * "-")
def menu_consultar_livros():
    print(50 * "-")
    print("Ecolha a opção desejada: ")
    print("1 - Consultar Todos")
    print("2 - Consultar por id")
    print("3 - Consultar por Autor")
    print("4 - Retornar ao menu")
    print(50 * "-")

def menu_remover_livro():
    print(50 * "-")
    print("Id do livro a ser removido: ")
    print(50 * "-")

def printBonito(livro:dict):
    #print com melhor legibilidade
    print(f"id {livro["id"]}\nnome: {livro["nome"]}\nAutor: {livro["autor"]}\neditora: {livro["editora"]}")
    print()

def cadastrar_livro(id:int):

    print(f"id do livro: {id}")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora:")
    dict_livros = {}

    dict_livros.update({"id": id})
    dict_livros.update({"nome": nome})
    dict_livros.update({"autor": autor})
    dict_livros.update({"editora": editora})
    lista_livros.append(dict_livros)
    print("Cadastro concluido ")
    print(dict_livros)

def consultar_livro():
    menu_consultar_livros()
    choice = int(input())
    if choice not in choices:
        print("Escolha invalida")
        return
    if len(lista_livros) < 1:
        print("Lista vazia")
        return
    elif choice == 1:
        for l in lista_livros:
            printBonito(l)
    elif choice == 2:
        id_global = int(input("id: "))
        check = 0
        for l in lista_livros:
            if l["id"] == id_global:
                printBonito(l)
                check += 1
        if check == 0:
            print("Id invalido")
            return

    elif choice == 3:
        autor = input("Digite o autor do(s) livros(s): ")
        check = 0
        for l in lista_livros:
            if l["autor"] == autor:
                check += 1
                break
        if check == 0:
            print("Autor inexistente")
            return
        else:
            for l in lista_livros:
                if l["autor"] == autor:
                    printBonito(l)

    else:
        return

def remover():
    menu_remover_livro()
    id_global = int(input())-1
    if id_global > -1 and id_global <= len(lista_livros):
        print(f"Livro :{lista_livros[id_global]["nome"]}")
        lista_livros.pop(id_global)
    else:
        print("Id inexistente")








while True:
    menu()
    choice = int(input("->"))
    if choice not in choices:
        print("Escolha invalida")
        continue
    elif choice == 1:
        cadastrar_livro(len(lista_livros)+1)
    elif choice == 2:
        consultar_livro()
    elif choice == 3:
        remover()

    else:
        print("Volte Logo")
        break



