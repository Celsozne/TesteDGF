def menu():
    while True:
        try:
            print("Menu:")
            print("1 - Soma")
            print("2 - Subtrair")
            print("3 - Multiplicar")
            print("4 - Dividir")
            print("0 - Sair")

            opcao = input("Digite sua opção: ")

            if opcao == "1":
                somar()
            elif opcao == "2":
                subtrair()
            elif opcao == "3":
                multiplicar()
            elif opcao == "4":
                dividir()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Erro: Entrada inválida. Digite um número.")


def somar():
    valor1 = float(input("Qual o primeiro valor: "))
    valor2 = float(input("Qual o segundo valor: "))
    print(f"A soma entre {valor1} e {valor2} é {valor1 + valor2}")
    input()
    menu()


def subtrair():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print(f"A subtração entre {valor1} e {valor2} é {valor1 - valor2}")
    input()
    menu()


def multiplicar():
    valor1 = float(input("Qual o primeiro valor: "))
    valor2 = float(input("Qual o segundo valor: "))
    print(f"O valor de {valor1} vezes {valor2} é {valor1 * valor2}")
    input()
    menu()


def dividir():
    valor1 = float(input("Qual o valor a ser dividido: "))
    valor2 = float(input("Qual será o número divisor: "))
    if valor2 != 0:
        print(f"A divisão entre {valor1} e {valor2} é {valor1 / valor2}")
    else:
        print("Impossível dividir por zero")
    input()
    menu()


def resto_div():
    valor1 = float(input("Qual o valor a ser dividido: "))
    valor2 = float(input("Qual o valor do divisor: "))
    if valor2 != 0:
        print(f"O resto de {valor1}/{valor2} é: {valor1 % valor2}")
    else:
        print("Impossível dividir por zero")
    input()
    menu()


def potencia():
    valor1 = float(input("Qual será o valor da base: "))
    valor2 = float(input("Qual o valor do expoente: "))
    if valor2 == 0:
        print(1)
    else:
        print(f"{valor1} elevado a {valor2} é {valor1**valor2}")
        input()
        menu()


if __name__ == "__main__":
    menu()
