

class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: str, disponivel: bool
):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    # alterar o atributo de True para False para emprestar
    def emprestar(self) -> bool:
        setattr(Livro, self.disponivel, False)

    # alterar o atributo de False para True para devolver
    def devolver(self) -> bool:
        setattr(Livro, self.disponivel, True)

    def ExibirInfo(self) -> str:
       print(vars(Livro))

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
        print(vars(LivroFisico(Livro)))


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
        print(vars(Ebook(Livro)))

class Biblioteca:
    def __init__(self):
        self.livros = [] #funcionando
        

    def AdicionarLivro(self,) -> str:
        #Funciona
        escolha: str = input("Voce deseja cadastrar um livro Fisico ou um Ebook?(DIgite F para Fisico e E para EBook )")
        
    
        if escolha == "F":
            titulo = input("Titulo do Livro: ")
            autor_livro:str = str(input("Autor do Livro: "))
            ano_livro = input("Ano de Publicacao: ")
            livro_disponivel = True
            numero_paginas = input("Quantidade de Paginas do Livro: ")     
            
            
            self.livros.append(LivroFisico(titulo,livro_disponivel, ano_livro, livro_disponivel, numero_paginas).__dict__)
            print(self.livros)
        
        
        elif escolha == "E":
            titulo_livro = input("Titulo do Livro: ")
            autor_livro: str = str(input("Autor do Livro: "))
            ano_livro = input("Ano de Publicacao: ")
            livro_disponivel = True
            tamanho_arquivo = input("Qual o tamanho do arquivo: ")
            formato_arquivo = input("Qual o formato do arquivo do Ebook")
            
            self.livros.append(Ebook(titulo_livro, autor_livro, ano_livro, livro_disponivel, tamanho_arquivo, formato_arquivo).__dict__)
            print(self.livros)
            
        else:
            print("Você digitou uma opção invalida")    
        

    def RemoverLivro(self, titulo: str) -> str:
        titulo = input("Titulo do livro que você quer apagar: ")
        remover =self.livros.remove(list(filter(lambda livro: livro['titulo'] == titulo, self.livros)))
        print(f"O livro {titulo} foi exlcuido com sucesso")
                       

    def ListarLivrosDisponiveis(self) -> str:
        disponiveis = list(filter(lambda livro: livro['disponivel'] == True, self.livros))
        print(disponiveis)
        
        
    def ExibirInfoTitulo(self, titulo: str) -> str:
        livro_escolhido = list(filter(lambda livro: livro['titulo'] == titulo, self.livros)) 
        print(livro_escolhido)

    def EmprestarLivro(self, titulo: str) -> str:
        
        livro_selecionado:dict = list(filter(lambda livro: livro['titulo'] == titulo, self.livros)) 
        try:
            if livro_selecionado[0].get('disponivel') == True:
                livro_selecionado[0]['disponivel'] = False
                print(f" O Livro {titulo} foi emprestado com sucesso ")
            else:
                print("Livro indisponivel")
        except IndexError:#nao consigo capturar o erro
            print("Esse livro nao existe na biblioteca")


    def DevolverLivro(self, titulo: str):
        livro_escolhido:dict = list(filter(lambda livro: livro['titulo'] == titulo, self.livros)) 
        try:
            if livro_escolhido[0].get('disponivel') == False:
                livro_escolhido[0]['disponivel'] = True
                print(f" O Livro {titulo} foi emprestado com sucesso ")
            else:
                print("Livro indisponivel")
        except IndexError:#nao consigo capturar o erro
            print("Esse livro nao existe na biblioteca")

# Como eu devolvo ou empresto um livro?
