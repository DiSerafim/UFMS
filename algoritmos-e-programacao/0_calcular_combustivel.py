# Entrada de dados
tempo_gasto = float(input("Informe o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Informe a velocidade média do veículo (em km/h): "))

# Cálculo da distância percorrida
distancia = tempo_gasto * velocidade_media

# Cálculo da quantidade de combustível gasto
combustivel = distancia

# Saída de dados
print(f"Distância percorrida: {distancia} km")
print(f"Quantidade de combustível gasto: {combustivel} litros")