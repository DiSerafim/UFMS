class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)
        print(f"Valor inserido: {x}")

    def remover(self):
        if len(self.data) > 0:
            item = self.data.pop(0)
            print(f"Item excluído: {item}")
        else:
            print("A lista está vazia.")

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not self.data

f = Fila()
f.inserir(1)
f.inserir(2)
f.inserir(3)
f.inserir(6)
f.remover()
f.remover()
f.remover()
f.remover()
f.remover()
