def senha():
    senha = input(
        "Escreva uma senha ao menos 8 caracteres, uma letra minuscula, uma maiuscula, um numero e um caractere especial"
    )
    validar(senha)


def validar(senha):
    characteres_esp = ""  # $%^&*()-+?!_=,<>/""
    if senha.islower():
        print("sua senha não cumpre os requisitos")
    elif senha.isupper():
        print("sua senha não cumpre os requisitos")
    elif senha.isdigit():
        print("sua senha não cumpre os requisitos")
    elif len(senha) < 8:
        print("sua senha não cumpre os requisitos")
    elif any(c in characteres_esp for c in senha):
        pass
    else:
        print("Sua senha é valida")


senha()
