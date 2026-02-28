def sort(lista):
    n = len(lista)

    for i in range(n):
        troca = False
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                troca = True
        if lista == False:
            break
    print(lista)


def decisao():
    i = 0
    lista = [i]
    while True:
        lista.append(int(input("Digite um numero:")))

        decisao = input("Você deseja digitar mais um numero? Y(para sim)/N(para nao) ")

        if decisao == "Y":
            i += 1
            print(i)
        elif decisao == "N":
            sort(lista)
            break
        else:
            sort(lista)
            break


decisao()
