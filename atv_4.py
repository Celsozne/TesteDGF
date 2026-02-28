number1 = int(input("Digite um numero: "))
number2 = int(input("Digite outro numero: "))
number3 = int(input("Digite um terceiro numero: "))

if number1 >= number2 and number2 >= number3:
    print(f"Maior numero {number1}, menor numero {number3}")
elif number1 >= number3 and number3 >= number2:
    print(f"Maior numero {number1}, menor numero {number2}")
elif number2 >= number1 and number1 >= number3:
    print(f"Maior numero {number2}, menor numero {number3}")
elif number2 >= number3 and number3 >= number1:
    print(f"Maior numero {number2}, menor numero {number1}")
elif number3 >= number1 and number1 >= number2:
    print(f"Maior numero {number3}, menor numero {number2}")
elif number3 >= number2 and number2 >= number1:
    print(f"Maior numero {number3}, menor numero {number1}")
