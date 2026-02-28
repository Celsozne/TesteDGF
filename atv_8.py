def media(notas):
    n = len(notas)
    soma = 0
    for i in range(n):
        soma += notas[i]
    media: float = soma / n
    print(media)


def decisao():
    i = 0
    nota = [i]
    while True:
        nota.append(int(input("Digite uma nota:")))

        decisao = input("Você deseja digitar mais uma nota? Y(para sim)/N(para nao) ")

        if decisao == "Y":
            i += 1
        elif decisao == "N":
            media(nota)
            break
        else:
            media(nota)
            break


decisao()
