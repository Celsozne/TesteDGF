import random

number = random.randrange(1, 1000)

aposta = int(input("Qual numero de 0 a 1000 o computador está pensando? "))

if aposta == number:
    print(f"Parabens voce acertou o numero {number}")
else:
    print("Voce errou")
