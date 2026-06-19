""" Converte um número decimal em sua representação binária usando uma pilha: """
class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def is_empty(self):
        return len(self.items) == 0
    
def deciaml_para_binario(decimal):
    pilha = Pilha()

    while decimal > 0:
        resto = decimal % 2
        pilha.push(resto)
        decimal = decimal // 2

    binario = ""
    while not pilha.is_empty():
        binario += str(pilha.pop())

    return binario
    
numero_decimal = int(input("Digite um número decimal: "))
binario = deciaml_para_binario(numero_decimal)
print(f"A representação binária de {numero_decimal} é {binario}.")
    
"""
Neste programa, a função decimal_para_binario recebe um número decimal e usa uma pilha para calcular sua representação binária. O programa solicita ao usuário um número decimal, chama a função e exibe o resultado como uma string binária.
"""