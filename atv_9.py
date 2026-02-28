numero = int(input("Você quer consultar qual tabuada? "))


for i in range(numero + 1):
    mult = numero * i
    print(f"{numero} X {i} = {mult}")
