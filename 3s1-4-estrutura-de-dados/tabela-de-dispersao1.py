def dispersao(dado, m):
    k = dado % m
    return k

chave = dispersao(12, 5)
print(chave)