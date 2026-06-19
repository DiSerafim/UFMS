'''
num = eval(input('Digite um número positivo: '))
while num < 0:
    num = eval(input('Digite um número positivo: '))
print('Valeu *^*')
'''

'''
num = eval(input('Digite um número positivo: '))

while num < 0:
    num = eval(input('Digite um número positivo: '))

print('Valeu *^*')
'''

while True:
    try:
        num = int(input('Digite um número positivo: '))
        if num >= 0:
            break  # Sai do loop se o número for não negativo
        else:
            print('Por favor, digite um número positivo.')
    except ValueError:
        print('Isso não é um número inteiro válido. Tente novamente.')

print('Valeu *^*')
