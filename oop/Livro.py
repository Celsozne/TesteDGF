class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: str, disponivel: bool = True):
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
    def __init__(self, titulo: str, autor: str, ano_publicacao: str, disponivel: bool, num_paginas: int):
        super().__init__(titulo, autor, ano_publicacao, disponivel)
        self.num_paginas = int(num_paginas)

    def InfoFisico(self) -> str:
        base = super().ExibirInfo()
        return f"{base} Paginas: {self.num_paginas}"


class Ebook(Livro):
    def __init__(
        self, titulo: str, autor: str, ano_publicacao: str, disponivel: bool,
        tamanho_arquivo: str, formato: str
    ):
        super().__init__(titulo, autor, ano_publicacao, disponivel)
        self.tamanho_arquivo = tamanho_arquivo
        self.formato = formato

    def InfoEbook(self) -> str:
        base = super().ExibirInfoxibirInfo()
        return f"{base} Tamanho: {self.tamanho_arquivo} Formato: {self.formato}"


class Biblioteca:
    def __init__(self, livros: Livro):
        self.livros =  [Livro]

    def AdicionarLivro(self, livro: Livro) -> str:
        #Não funciona
        for livro in self.livros:
            if livro.titulo == livro.titulo:
                print(f"O livro '{livro.titulo}' já existe no banco de dados")
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' foi adicionado corretamente")

    def RemoverLivro(self, titulo: str) -> str:
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso")
        print(f"Livro '{titulo}' nao existe no banco de dados")

    def ListarLivrosDisponiveis(self) -> str:
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        if not disponiveis:
            #So da esse resultado, entao nao sei se funciona
            print("Nao existem livros disponiveis")
        print((livro.ExibirInfo() for livro in disponiveis))

    def ExibirInfoTitulo(self, titulo: str) -> str:
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro.ExibirInfo()
        print(f"Livro '{titulo}' nao encontrado")

    def EmprestarLivro(self, titulo: str) -> str:
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.emprestar():
                    print(f"Livro '{titulo}' emprestado com sucesso")
                else:
                    return f"Livro '{titulo}' nao esta disponivel"
        return f"Livro '{titulo}' nao encontrado"

#Como eu devolvo ou empresto um livro?

    
