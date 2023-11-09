class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return None

    def vazia(self):
        return len(self.itens) == 0

    def esvaziar(self):
        self.itens = []

# Função para imprimir o conteúdo da pilha
def imprimir_pilha(p):
    while not p.vazia():
        print(p.desempilhar(), end=' ')
    print()

# Função principal
def main():
    pilha = Pilha()

    while True:
        entrada = input()
        valores = entrada.split(' ')

        if valores[0] == 'E':
            pilha.empilhar(valores[1])
        elif valores[0] == 'D':
            pilha.desempilhar()
        elif valores[0] == 'S':
            imprimir_pilha(pilha)
            break

if __name__ == '__main__':
    main()
