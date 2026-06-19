"""
O máximo divisor comum (MDC) de dois números inteiros x e y é definido da seguinte forma:

Se x é maior que y >> MDC(x,y) = MDC(x-y, y);
Se x é igual y     >> MDC(x,y) = x;
Se x é menor que y >> MDC(x,y) = MDC(y,x).

Utilizando as definições acima, implemente um programa recursivo que recebe dois números inteiros x e y (separados por um espaço), calcula e imprime o MDC de x e y.

Por exemplo:

Teste Entrada Resultado
Caso de teste 1 (Exemplo 1):
12 15
3
Caso de teste 2 (Exemplo 2):
96 72
24
Resposta:(regime de penalidade: 0%)
O editor Ace não está pronto. Talvez recarregar a página?
Retornando à área de texto bruto.
"""

def mdc(x, y):
    if x > y:
        return mdc(x - y, y) 
    elif x == y:
        return x
    elif x < y:
        return mdc(x, y - x)
    else:
        return x
    
# Entrada de dados
entrada = input("Digite dois números inteiros separados por um espaço: ")
x, y = map(int, entrada.split())

# Execução
resultado = mdc(x, y)
print(f"O MDC de {x} e {y} é: {resultado}")

print(mdc(12, 15))
print(mdc(96, 72))
