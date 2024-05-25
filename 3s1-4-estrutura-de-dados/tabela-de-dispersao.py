def criaTabela(M):
    tabela = {}
    for chave in range(M):
        tabela[chave] = None
    return tabela

T = criaTabela(5)
print(T)