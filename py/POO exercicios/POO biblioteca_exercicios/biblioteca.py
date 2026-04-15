from thefuzz import process

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca "{self.nome}".')

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f'Livro "{livro.titulo}" removido da biblioteca "{self.nome}".')
                return
        print(f'Livro com ISBN {isbn} não encontrado na biblioteca "{self.nome}".')

    def listar_livros(self):
        if not self.livros:
            print(f'A biblioteca "{self.nome}" não tem livros.')
        else:
            print(f'Livros na biblioteca "{self.nome}":')
            for livro in self.livros:
                print(f'- {livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')

    def buscar_livros(self):
        busca_livro = input("Digite o livro que deseja: ")

        titulos = [livro.titulo for livro in self.livros]
        resultado = process.extractOne(busca_livro, titulos)

        if resultado is None:
            print("Nenhum livro encontrado.")
            return

        melhor_titulo, score = resultado

        if score < 60:
            print(f'Nenhum livro semelhante encontrado para "{busca_livro}".')
            return

        for livro in self.livros:
            if livro.titulo == melhor_titulo:
                print(f'º Nome do Livro: {livro.titulo}\n'
                      f'º Autor do Livro: {livro.autor}\n'
                      f'º ISBN: {livro.isbn}')
                return


# Testando as classes

# Criando alguns livros
livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', '1234567890')
livro2 = Livro('1984', 'George Orwell', '0987654321')
livro3 = Livro('O Apanhador no Campo de Centeio', 'J.D. Salinger', '1122334455')

# Criando uma biblioteca
biblioteca = Biblioteca('Biblioteca Central')

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando todos os livros na biblioteca
biblioteca.listar_livros()

# Procurando um livro na Biblioteca
print("+"*30)
biblioteca.buscar_livros()
print("+"*30)


# Removendo um livro da biblioteca
biblioteca.remover_livro('0987654321')

# Listando todos os livros na biblioteca após a remoção
biblioteca.listar_livros()