#Test Programa Triangle

#  Leitura dos lados
def classificar_triangulo(ladoA, ladoB, ladoC):
    if (ladoA.isdigit() and ladoB.isdigit() and ladoC.isdigit()):
        #testa os lados dos triângulos
        if (ladoA == ladoB) and (ladoA == ladoC):
            print("Triangulo EQUILÁTERO")
        elif ((ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC)):
            print("Triangulo ISÓSCELES")
        else:
            print("Triangulo ESCALENO")    
    else:
        print("Ha pelo menos uma entrada invalida!!!")

#Casos de teste
def testar_triangulo():
    testes = [
        # Teste válido
        {"entrada": ("3", "3", "3"), "esperado": "Triangulo EQUILÁTERO"},
        {"entrada": ("5", "5", "3"), "esperado": "Triangulo ISÓSCELES"},
        {"entrada": ("4", "5", "6"), "esperado": "Triangulo ESCALENO"},
        
        # Teste inválido
        {"entrada": ("a", "3", "3"), "esperado": "Ha pelo menos uma entrada invalida!!!"},
        {"entrada": ("0", "0", "3"), "esperado": "Ha pelo menos uma entrada invalida!!!"},
        {"entrada": ("4", "5", "@"), "esperado": "Ha pelo menos uma entrada invalida!!!"},
    ]
    
    for teste in testes:
        resultado = classificar_triangulo(*teste["entrada"])
        status = "✅" if resultado == teste["esperado"] else "❌"
        print(f"Entrada: {teste['entrada']} | Esperado: {teste['esperado']} | Obtido: {resultado} {status}")

#executa os testes
if __name__ == "__main__":
    testar_triangulo()