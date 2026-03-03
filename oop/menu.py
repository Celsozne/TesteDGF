from Livro import *

biblioteca = Biblioteca()

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
    
    biblioteca.AdicionarLivro()



def RemoverLivro():
    titulo = ''
    return biblioteca.RemoverLivro(titulo)


def ListarLivrosDisponiveis():
    return biblioteca.ListarLivrosDisponiveis()


def ExibirInfos():
    titulo = ''
    return biblioteca.ExibirInfoTitulo(titulo)


def Emprestar():
    titulo = ''
    return biblioteca.EmprestarLivro(titulo)


def Devolver():
    titulo = input("Titulo do livro para devolver: ")
    return biblioteca.DevolverLivro(titulo)
