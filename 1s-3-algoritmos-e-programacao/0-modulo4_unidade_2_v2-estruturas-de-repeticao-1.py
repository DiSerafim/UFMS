nomes = []

while True:
    nome = input('Digite um nome (ou deixe em branco para parar): ')
    if nome == "":
        break  # Sai do loop se o usuário digitar uma string vazia
    nomes.append(nome)

if nomes:
    print('Nomes digitados:')
    for nome in nomes:
        print(nome)
else:
    print('Nenhum nome foi digitado.')
