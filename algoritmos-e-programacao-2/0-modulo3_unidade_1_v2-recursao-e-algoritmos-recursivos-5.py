"""
Calcular a Soma Recursivamente:
"""
def soma_elemento_recursivo(lista):
    # Se a lista estiver vazia, retorna 0
    if not lista:
        return 0
    
    # Passo recursivo: soma o primeiro elemento com a soma do restante da lista
    return lista[0] + soma_elemento_recursivo(lista[1:])

# Execução
lista_teste = [3, 8, 2, 7, 5]
resultado_soma_elemento = soma_elemento_recursivo(lista_teste)
print(f"A soma dos Elementos: {resultado_soma_elemento}") # 25