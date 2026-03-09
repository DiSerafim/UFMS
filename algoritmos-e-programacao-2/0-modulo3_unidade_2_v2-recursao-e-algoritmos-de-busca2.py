class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Criando uma lista de objetos
lista_livros = [
    Livro("Dom Quixote", "Miguel de Cervantes"),
    Livro("1984", "George Orwell"),
    Livro("O Grande Gatsby", "F. Scott Fitzgerald"),
    Livro("Cem Anos de Solidão", "Gabriel García Márquez"),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry"),
]

# Função para buscar um livro por título
def busca_livro_por_titulo(lista, titulo_alvo):
    for livro in lista:
        if livro.titulo == titulo_alvo:
            return livro # Retorna o objeto Livro se o titulo corresponder
        
    return None # Retorna None se o título não for encontrado

# Título do livro que queremos buscar
titulo_alvo = "1984"

# Realiza a busca
livro_encontrado = busca_livro_por_titulo(lista_livros, titulo_alvo)

# Verifica se o livro foi encontrado
if livro_encontrado is not None:
    print(f"O livro '{titulo_alvo}' foi encontrado. Autor: {livro_encontrado.autor}")
else:
    print(f"O livro '{titulo_alvo}' não foi encontrado na lista de livros.")