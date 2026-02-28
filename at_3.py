number = int(input("Numero natural que o fatorial será calculado: "))
fatorial = 1
if number == 0:
    fatorial = 0
elif number < 0:
    print("Não exite fatorial de numeros negativos")
    int(input("Um numero positivo: "))
else:
    for i in range(number, 1, -1):
        fatorial *= i
print(fatorial)
