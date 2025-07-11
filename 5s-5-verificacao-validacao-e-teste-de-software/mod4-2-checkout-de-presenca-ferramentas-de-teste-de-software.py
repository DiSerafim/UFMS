
#programa Triangle
#  Leitura dos lados
print("Problema dos Triangulos\n")
ladoA = input('Digite o lado A: ')
ladoB = input('Digite o lado B: ')
ladoC = input('Digite o lado C: ')
#verifica se os valores digitados são válidos
if (ladoA.isdigit() and ladoB.isdigit() and ladoC.isdigit()):
    #testa os lados dos triangulos
    if (ladoA == ladoB) and (ladoA == ladoC):
        print("Triangulo EQUILATERO")
    elif ((ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC)):
        print("Triangulo ISOCELES")
    else:
        print("Triangulo ESCALENO")    
else:
    print("Ha pelo menos uma entrada invalida!!!")
