def inserir(dado, chave, tabela):
    if tabela[chave] == None:
        tabela[chave] == dado
    else:
        print('Colisão d =', dado, 'k =', chave)
T = {0: None, 1: None, 2: 12, 3: 13, 4: 14}
inserir(17, 2, T)
print(T)