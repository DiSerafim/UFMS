"""
Função para cadastrar produtos e preços.
Armazena os produtos e preços em uma lista.
Retorna a lista de produtos.
"""
def cadastra_produtos():
    n = int(input()) # Solicita um número inteiro n, para a quantidade de produtos.
    produtos = {} # Armazena os produtos e preços em uma lista.

    for _ in range(n): # Cria um loop para cadastrar os produtos.
        nome = input() # Solicita o nome do produto.
        preco = float(input()) # Solicita o preço do produto.
        if nome.lower() not in produtos: # Verifica se o produto já está cadastrado.
            produtos[nome.lower()] = preco # Adiciona o produto e preço na lista
        else:
            print("Produto já cadastrado") # Se o produto já estiver cadastrado, exibe a mensagem.

    return produtos # retorna a lista de produtos

"""
Função para buscar preços dos produtos.
Permite inserir o nome do produto e obter seu preço.
Permite encerrar quando o usuário escrever 'Fim'
"""
def busca_preco(produtos):
    while True: # Loop para buscar preços
        produto = input() # Solicita o nome do produto buscado
        if produto == "Fim": # Verifica se deseja encerrar
            break
        preco = produtos.get(produto.lower(), "Produto não cadastrado") # Procura o preço do produto na lista.
        print(preco) # exibe o preço do produto ou a mensagem 'Produto não cadastrado'

"""
Função principal que chama as funções;
cadastra_produtos,
busca_preco
"""
def checagem():
    produtos = cadastra_produtos() # Chama a função cadastra_produtos
    busca_preco(produtos) # Chama a função busca_preco

"""
Verifica se está sendo executado como função principal
"""
if __name__ == "__main__":
    checagem() # Chama a função principal