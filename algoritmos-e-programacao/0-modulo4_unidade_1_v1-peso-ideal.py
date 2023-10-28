altura = input('Digite sua altura: ')
sexo = input('Digite h para homens e m para mulheres: ')
convert_altura = eval(altura)

if sexo == 'h':
    peso = (72.7 * convert_altura) - 58
else:
    peso = (62.1 * convert_altura) - 44.7

print('Seu peso ideal é: ', peso)