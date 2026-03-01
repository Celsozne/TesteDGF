class Livro:
    def __init__(self,titulo, autor, ano_publicacao,disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = bool(disponivel)
    #alterar o atributo de true para false para um livro
    def Emprestar(self):
        pass

    #alterar o atributo de false para true para um livro
    def Devolver(self):
        pass

    def ExibirInfo(self):
        return f"Titulo: {self.titulo} Autor: {self.autor} Ano de Publicacao{self.ano_publicacao} Disponivel {self.disponivel}"
    
class LivroFisico(Livro):
        def __init__(self, titulo, autor, ano_publicacao, disponivel, num_paginas):
             super().__init__(titulo, autor, ano_publicacao, disponivel)
             self.num_paginas = int(num_paginas)

        def ExibirInfoFisico(self):
                return super().ExibirInfo()

class Ebook(Livro):
    def __init__(self, titulo, autor, ano_publicacao, disponivel, tamanho_arquivo, formato):
        super().__init__(titulo, autor, ano_publicacao, disponivel)
        self.tamanho_arquivo = tamanho_arquivo
        self.formato = formato



class Biblioteca:
    def __init__(self, livros):
        self.livros = []
    
    def AdicionarLivro(self, titulo, autor, ano_publicacao, disponivel):
        #tem que criar um livro e adicionar as informações do livro em algum arquivo ou array(csv e uma opcao)
        for Livro in self.livros:
            if Livro.titulo == titulo:
                return f"O livro {titulo} já existe no banco de dados"
            novo_livro = Livro()
            self.livros.append(novo_livro)
            return f"Livro {titulo} foi adicionado corretamente"

    

    def RemoverLivro(self, titulo):
        #tem que remover o livro pelo titulo dele da lista de livros
        for Livro in self.livros:
            if Livro.titulo == titulo:
                self.livros.remove(titulo)
                return f"Livro {titulo} removido com sucesso"
            else:
                return f"Livro {titulo} nao existe no banco de dados"
        pass
    def ListarLivrosDisponiveis(self, Livro):

        for Livro in self.livros:
            if Livro.disponivel == True:
                return f"{self.titulo} esta disponivel"
            else:
                return "Nao existem livros no banco de dados"

        #tem que mostrar todos os livros que estao com a propriedade disponivel true
    
    def ExibirInfoTitulo(self, titulo):
        for Livro in self.livros:
            if Livro.titulo == titulo:
                Livro.ExibirInfo()

    
