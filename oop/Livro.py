import json

class Livro:
    def __init__(
        self, titulo: str, autor: str, ano_publicacao: str, disponivel: bool = True
    ):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = bool(disponivel)

    # alterar o atributo de True para False para emprestar
    def emprestar(self) -> bool:
        pass

    # alterar o atributo de False para True para devolver
    def devolver(self) -> bool:
        pass

    def ExibirInfo(self) -> str:
        return (
            f"Titulo: {self.titulo} Autor: {self.autor} "
            f"Ano de Publicacao: {self.ano_publicacao} Disponivel: {self.disponivel}"
        )


class LivroFisico(Livro):
    def __init__(
        self,
        titulo: str,
        autor: str,
        ano_publicacao: str,
        disponivel: bool,
        num_paginas: int,
    ):
        super().__init__(titulo, autor, ano_publicacao, disponivel)
        self.num_paginas = int(num_paginas)

    def InfoFisico(self) -> str:
        base = super().ExibirInfo()
        return f"{base} Paginas: {self.num_paginas}"


class Ebook(Livro):
    def __init__(
        self,
        titulo: str,
        autor: str,
        ano_publicacao: str,
        disponivel: bool,
        tamanho_arquivo: str,
        formato: str,
    ):
        super().__init__(titulo, autor, ano_publicacao, disponivel)
        self.tamanho_arquivo = tamanho_arquivo
        self.formato = formato

    def InfoEbook(self) -> str:
        base = super().ExibirInfoxibirInfo()
        return f"{base} Tamanho: {self.tamanho_arquivo} Formato: {self.formato}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def AdicionarLivro(self,) -> str:
        # Talvez Funciona
        escolha: str = input("Voce deseja cadastrar um livro Fisico ou um Ebook?(DIgite F para Fisico e E para EBook )")
        
    
        if escolha == "F":
            titulo = input("Titulo do Livro: ")
            autor_livro = input("Autor do Livro: ")
            ano_livro = input("Ano de Publicacao: ")
            livro_disponivel = True
            numero_paginas = input("Quantidade de Paginas do Livro: ")     
            #new_book = print(vars(LivroFisico(titulo,livro_disponivel, ano_livro, livro_disponivel, numero_paginas)))#printa certo, tenho que alocar num lugar para salvar
                   
            with open("object.json", "w") as file:
                json.dump(LivroFisico(titulo,livro_disponivel, ano_livro, livro_disponivel, numero_paginas).__dict__, file)
                print(vars(LivroFisico(titulo,livro_disponivel, ano_livro, livro_disponivel, numero_paginas)))#printa certo
        elif escolha == "E":
            titulo_livro = input("Titulo do Livro: ")
            autor_livro = input("Autor do Livro: ")
            ano_livro = input("Ano de Publicacao: ")
            livro_disponivel = True
            tamanho_arquivo = input("Qual o tamanho do arquivo: ")
            formato_arquivo = input("Qual o formato do arquivo do Ebook")
            #vou ter de salvar num json(só salva 1, vou ver dps)
        
            #print(vars(Ebook(titulo_livro, autor_livro, ano_livro, livro_disponivel, tamanho_arquivo, formato_arquivo)))#printa certo, tenho que alocar num lugar para salvar
            with open("object.json", "w") as file:
                json.dump(Ebook(titulo_livro, autor_livro, ano_livro, livro_disponivel, tamanho_arquivo, formato_arquivo).__dict__, file)
            print(vars(Ebook(titulo_livro, autor_livro, ano_livro, livro_disponivel, tamanho_arquivo, formato_arquivo)))#printa certo
        else:
            print("Você digitou uma opção invalida")    
        

    def RemoverLivro(self, titulo: str) -> str:
        #Esse for sera´feito no banco de dados para verificar
        try:
            with open("object.json"):
                data = json.load("object.json")#erro no decoder?
                if titulo in data:
                    if "num_paginas".exist :
                        del data['titulo', 'autor', 'ano_publicacao', 'disponivel', 'num_paginas']
                elif "tamanho_arquivo".exist: 
                    del data['titulo', 'autor', 'ano_publicacao', 'disponivel', 'tamanho_arquivo', 'formato']
        except ValueError:
            print(f"Erro {ValueError}" )
            

    def ListarLivrosDisponiveis(self) -> str:
        try: 
            pass
        except ValueError: 
            print(f"Erro {ValueError}")

    def ExibirInfoTitulo(self, titulo: str) -> str:
        for livro in self.livros:#nao tem base de dados para encontrar
            if livro.titulo == titulo:
                return livro.ExibirInfo()
        print(f"Livro '{titulo}' nao encontrado")

    def EmprestarLivro(self, titulo: str) -> str:
        for livro in self.livros:#tribute error
            if livro.titulo == titulo:
                if livro.emprestar():
                    print(f"Livro '{titulo}' emprestado com sucesso")
                else:
                    return f"Livro '{titulo}' nao esta disponivel"
        return f"Livro '{titulo}' nao encontrado"


# Como eu devolvo ou empresto um livro?
