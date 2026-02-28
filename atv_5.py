word = str(input("Escreva a palavra para verificar se é um palindromo ou nao"))
i, j = 0, len(word) - 1
palindrome = True

while i < j:
    if word[i] != word[j]:
        palindrome = False
        break
    i += 1
    j -= 1

if palindrome:
    print(f"A palavra {word} é um palindromo")
else:
    print(f"A palavra {word} não é um palindromo")
