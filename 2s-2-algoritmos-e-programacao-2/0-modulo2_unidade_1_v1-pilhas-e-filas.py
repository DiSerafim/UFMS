""" Avaliar uma expressão matemática em notação polonesa reversa (RPN): """
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
        
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.items) == 0
    
def avaliar_rpn(expressao_rpn):
    pilha = Pilha()
    tokens = expressao_rpn.split()

    for token in tokens:
        if token.isdigit():
            pilha.push(int(token))
        else:
            segundo_operando = pilha.pop()
            primeiro_operando = pilha.pop()
            if primeiro_operando is not None and segundo_operando is not None:
                if token == '+':
                    resultado = primeiro_operando + segundo_operando
                elif token == '-':
                    resultado = primeiro_operando - segundo_operando
                elif token ==   '*':
                    resultado = primeiro_operando * segundo_operando
                elif token ==   '/':
                    resultado = primeiro_operando / segundo_operando
                pilha.push(resultado)

    if not pilha.is_empty():
        return pilha.pop()
    else:
        return None
    
expressao = "3 4 + 2 *"
resultado = avaliar_rpn(expressao)
print("Resultado da expressão RPN: ", resultado)
    
"""
A notação polonesa reversa (RPN), também conhecida como notação pós-fixa, é uma forma de escrever expressões matemáticas onde os operadores seguem seus operandos. Em vez de usar parênteses para determinar a ordem de avaliação das operações, na notação RPN, a ordem é determinada pela posição dos operadores.

Por exemplo, na notação infixa tradicional, a expressão "3 + 4" é escrita com o operador "+" entre os operandos 3 e 4. Na notação RPN, essa mesma expressão é escrita como "3 4 +". Os operandos (números) aparecem primeiro, seguidos pelo operador.

A principal vantagem da notação RPN é que ela permite avaliar expressões de forma direta e sem a necessidade de parênteses para definir a ordem das operações. Isso facilita a implementação de calculadoras e interpretadores de expressões matemáticas.

A avaliação de uma expressão em notação RPN é realizada seguindo estas etapas:

Percorra a expressão da esquerda para a direita, processando cada elemento (número ou operador).
Quando um número é encontrado, coloque-o na pilha.
Quando um operador é encontrado, retire os dois números superiores da pilha, aplique a operação e coloque o resultado de volta na pilha.
Continue até que todos os elementos da expressão sejam processados.
O resultado final estará no topo da pilha.
A notação RPN é usada em algumas calculadoras científicas e linguagens de programação, como a linguagem Forth. Ela simplifica a avaliação de expressões matemáticas e elimina a ambiguidade associada à notação infixa tradicional.
"""