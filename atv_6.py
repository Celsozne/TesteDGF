number = int(input("Digite um numero para verificar se ele é primo ou não: "))

for i in range(2, number):
    if number % i == 0:
        print(f"O numero {number} não é primo pois é divisil por {i}")
        break
    else:
        print(f"O numero {number} é primo")
        break
