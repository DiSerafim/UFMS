while True:
    try:
        num = int(input('Digite um número: '))
        print(f'Você digitou o número {num}.')
    except ValueError:
        print('Isso não é um número inteiro válido. Tente novamente.')

# Para sair do loop, pressione Ctrl+C no teclado ou encerre o programa manualmente.
