def fibonnaci():
    n = int(input("Quual termo de Fibonnaci queres saber? "))

    n1, n2 = 0, 1

    contador = 0

    if n <= 0:
        print("so existem termos positivos na sequencia de fibonnaci")
    elif n == 1:
        print(f"Sequencia ate o termo de numero{n}: ")
        print(n1)

    else:
        print(f"Sequencia ate o termo de numero{n}")
        while contador < n:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            contador += 1


fibonnaci()
