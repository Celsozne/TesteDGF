

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
        self.disponivel = False

    # alterar o atributo de False para True para devolver
    def devolver(self) -> bool:
        self.disponivel = True

    def ExibirInfo(self) -> str:
       print()

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
        base = Livro.ExibirInfo()
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
        print()

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
            livro_disponivel = False
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
        #Remover um objeto da lista livros
        #nao ta apagando
        titulo = input("Titulo do livro que você quer apagar: ")
                
        
        
            
            

    def ListarLivrosDisponiveis(self) -> str:
        disponiveis = filter(lambda w: 'disponivel' == True, self.livros)#ver se tenho de trocar de true pra false
        print(disponiveis) #esta filtrando e printando , só preciso saber como tornar isso em dictionary
        
        
    def ExibirInfoTitulo(self, titulo: str) -> str:
        titulo_input = input("Qual o titulo do livro que você quer saber as informações: ")
        disponiveis = [lambda w: titulo_input in self.livros, self.livros] #erro no filtro mas lê a lista corretamente
        print(disponiveis) 

    def EmprestarLivro(self, titulo: str) -> str:
        titulo_input = input("Titulo do livro para emprestar: ")
        livro_selecionado = [lambda w: titulo_input in self.livros, self.livros ]
        print(livro_selecionado) 
        #transforma de true em false


# Como eu devolvo ou empresto um livro?
