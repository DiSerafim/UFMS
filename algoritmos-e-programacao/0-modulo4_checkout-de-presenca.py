def cadastra_produtos():
    n = int(input())
    produtos = {}

    for _ in range(n):
        nome = input()
        preco = float(input())
        if nome.lower() not in produtos:
            produtos[nome.lower()] = preco
        else:
            print("Produto já cadastrado")

    return produtos

def busca_preco(produtos):
    while True:
        produto = input()
        if produto == "Fim":
            break
        preco = produtos.get(produto.lower(), "Produto nao cadastrado")
        print(preco)

def checagem():
    produtos = cadastra_produtos()
    busca_preco(produtos)

if __name__ == "__main__":
    checagem()