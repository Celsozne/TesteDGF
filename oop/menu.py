from Livro import *

biblioteca = Biblioteca(livros)

def menu():
    while True:
        try:
            print("1 - Adicionar Livro")
            print("2 - Remover Livro")
            print("3 - Mostrar Livros Disponiveis")
            print("4 - Pesquisar Informacoes") 
            print("5 - Pegar um Livro emprestado'")
            print("6 - Devolver Livro")
            print("0 - Devolver Livro")

            opcao = input("Digite sua opção: ")

            if opcao == "1":
                AdicionarLivro()
            elif opcao == "2":
                RemoverLivro()
            elif opcao == "3":
                ListarLivrosDisponiveis()
            elif opcao == "4":
                ExibirInfos()
            elif opcao == "5":
                Emprestar()
            elif opcao == "6":
                Devolver()
            elif opcao == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Erro: Entrada inválida. Digite um número.")


def AdicionarLivro():

    ebook_fisico = input("Voce deseja cadastrar um livro Fisico ou um Ebook?(DIgite F para Fisico e E para EBook )")
    if ebook_fisico == "F":
            titulo_livro = input("Titulo do Livro: ")
            autor_livro = input("Autor do Livro: ")
            ano_livro = input("Ano de Publicacao: ")
            livro_disponivel = True
            numero_paginas = input("Quantidade de Paginas do Livro: ")
            LivroFisico(titulo_livro, autor_livro, ano_livro, livro_disponivel, numero_paginas)
    elif ebook_fisico == "E":
            titulo_livro = input("Titulo do Livro: ")
            autor_livro = input("Autor do Livro: ")
            ano_livro = input("Ano de Publicacao: ")
            livro_disponivel = True
            tamanho_arquivo = input("Qual o tamanho do arquivo: ")
            formato_arquivo = input("Qual o formato do arquivo do Ebook")
            Ebook(titulo_livro, autor_livro, ano_livro, livro_disponivel, tamanho_arquivo, formato_arquivo)
    else:
            print("Você digitou uma opção invalida")
            


def RemoverLivro():
    titulo = input("Qual Livro voce quer remover (Escreva o Titulo): ")
    return biblioteca.RemoverLivro(titulo)


def ListarLivrosDisponiveis():
    return biblioteca.ListarLivrosDisponiveis()


def ExibirInfos():
    titulo = input("Titulo do Livro que voce quer as informacoes: ")
    return biblioteca.ExibirInfoTitulo(titulo)


def Emprestar():
    titulo = input("Titulo do livro para emprestar: ")
    return biblioteca.EmprestarLivro(titulo)


def Devolver():
    titulo = input("Titulo do livro para devolver: ")
    return biblioteca.DevolverLivro(titulo)

