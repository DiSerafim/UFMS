import random

def busca_binaria(l, x, inicio, fim):
    meio = (inicio + fim) // 2

    if x == l[meio]:
        return meio
    
    if x < l[meio]:
        return busca_binaria(l, x, inicio, meio - 1)
    
    if x > l[meio]:
        return busca_binaria(l, x, meio + 1, fim)
    
l = random.sample(range(100), 20)
print("Lista não ordenada: ", l)

l.sort()
print("Lista ordenada: ", l)

resultado = busca_binaria(l, 24, 0, 19)
print(resultado)

if resultado != -1:
    print(f'O número 24 está na posição {resultado} da lista.')
else:
    print(f'O número 24 não está na lista.')