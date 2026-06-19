## Função
def calcular_combustivel(tempo_gasto, velocidade_media, consumo_medio):
    distancia = tempo_gasto * velocidade_media
    quantidade_combustivel = distancia / consumo_medio
    return quantidade_combustivel

# Entradas
tempo_gasto = float(input('Qual o tempo gasto? '))
velocidade_media = float(input('Qual a velocidade média? '))
consumo_medio = float(input('Qual o consumo médio? '))

# Execução
quantidade_combustivel = calcular_combustivel(tempo_gasto, velocidade_media, consumo_medio)

# Resultado
print('A quantidade de combustível gasta é:', quantidade_combustivel, 'litros')