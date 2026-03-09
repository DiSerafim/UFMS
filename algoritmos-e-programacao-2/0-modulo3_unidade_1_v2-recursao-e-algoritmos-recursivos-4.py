"""
Encontrar o Maior Elemento Recursivamente:
"""
def maior_elemento_recursivo(lista):
    # Caso base: se a lista estiver vazia, retorna None
    if not lista:
        return None
    
    # Caso base: se houver apenas um elemento, retorna esse elemento
    if len(lista) == 1:
        return lista[0]
    
    # Passo recursivo: compara o primeiro elemento com o máximo do restante da lista
    max_resto = maior_elemento_recursivo(lista[1:])
    return lista[0] if lista[0] > max_resto else max_resto

# Execução
lista_teste = [3, 8, 2, 7, 5]
resultado_maior_elemento = maior_elemento_recursivo(lista_teste)
print(f"Maior Elemento: {resultado_maior_elemento}") # 8