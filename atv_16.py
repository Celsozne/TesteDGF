def menu():
    array = [12, 54, 68, 486, 45, 87, 54]
    while True:
        try:
            print("Menu:")
            print("1 - Adicionar um item")
            print("2 - Excluir um item")
            print("3 - Move um item")
            print("0 - Sair")

            opcao = input("Digite sua opção: ")

            if opcao == "1":
                adicionar(array)
            elif opcao == "2":
                excluir(array)
            elif opcao == "3":
                troca(array)
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Numero ou posicao inexistente")


def adicionar(array):

    print(array)
    numero = int(input("Digite um numero para ser adicionado:"))
    array.append(numero)
    print(array)


def excluir(array):
    print(array)
    numero = int(input("Digite o valor que queres excluir:"))
    array.remove(numero)
    print(array)


def troca(array):
    try:
        print(array)
        pos_inicial = int(
        input("Qual a posicao do item que você quer trocar de lugar(contagem comeca com 0): "))
        if pos_inicial < 0 or pos_inicial > len(array):
            print("Posicao inicial inexistente")
        else:
            pos_final = int(
                    input("Com qual posicao voce quer troca(contagem comeca com 0): ")
                    )
            if pos_final < 0 or pos_final > len(array):
                print("Posicao inicial inexistente")
            else:
                array[pos_inicial], array[pos_final] = (
                        array[pos_final],
                        array[pos_inicial],
                        )
        print(array)
    except ValueError:
        print("Posicoes inexistentes")


menu()
