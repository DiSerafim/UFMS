# Busca sequencial
def busca_sequencial(arranjo, alvo):
    for i in range(len(arranjo)):
        if arranjo[i] == alvo:
            return i # Retorna o índice onde o alvo foi encontrado
    
    return -1 # Retorna -1 se o alvo não for encontrado

# Busca Binária (assumindo que o arranjo está ordenado)
def busca_binaria(arranjo, alvo):
    esquerda, direita = 0, len(arranjo) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arranjo[meio] == alvo:
            return meio # Retorna o índice onde o alvo foi encontrado
        elif arranjo[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1 # Retorna -1 se o alvo não for encontrado

# Execução
arranjo = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
print("Arranjo: ", arranjo)

alvo = 23
print("Alvo: ", alvo)

# Busca sequencial
indice_sequencial = busca_sequencial(arranjo, alvo)
if indice_sequencial != -1:
    print(f"Busca Sequencial: O número {alvo} foi encontrado no índice {indice_sequencial}.")
else:
    print(f"Busca Sequencial: O número não foi encontrado no arranjo.")

# Busca Binária
indice_binaria = busca_binaria(arranjo, alvo)
if indice_binaria != -1:
    print(f"Busca Binária: O número {alvo} foi encontrado no índice {indice_binaria}.")
else:
    print(f"Busca Binária: O número não foi encontrado no arranjo.")
