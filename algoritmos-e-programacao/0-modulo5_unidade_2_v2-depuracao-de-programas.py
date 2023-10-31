def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)
    

def fatorial_iterativo(n):
    fat = n
    i = n - 1
    while i >= 1:
        fat *= i
        i -= 1
    return fat

número = int(input('Digite um número para descobrir o seu fatorial: '))

print('O fatorial de {} é {} - método recursivo' . format(número, fatorial_recursivo(número)))
print('O fatorial de {} é {} - método iterativo' . format(número, fatorial_iterativo(número)))