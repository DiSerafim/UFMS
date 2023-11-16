import random # Gera números aleatórios
import time # Usado para medir o tempo gasto

"""
Algoritmo 2: complexidade O(n³)
soma = 0
recebe um valor inteiro n
laço de 1 até n
    laço de 1 até n
        laço de 1 até n
        aleatorio = valor aleatório entre 1 e 1000
        soma = soma + aleatorio
"""

def algoritmo_2(n):
    soma = 0
    for i in range(1, n + 1): # Loop de 1 até n
        for j in range(1, n + 1): # Loop de interno 1 até n
            for k in range(1, n + 1): # Loop de interno 1 até n
                aleatorio = random.randint(1, 1000) # Gera número inteiro aleatório entre
                soma = soma + aleatorio # Soma o nº aleatório + a variável
    return soma # Retorna a soma total

valores_de_n = [10, 100, 1000]

for n in valores_de_n:
    inicia_time = time.time() # Início da contagem de tempo
    resultado = algoritmo_2(n) # Chama o algoritmo
    fim_time = time.time() # Fim da contagem
    tempo_algoritmo = fim_time - inicia_time # Calcula o tempo de execução

    print(f"n = {n}") # Exibe o valor de valores_de_n
    print(f"Tempo de execução do Algoritmo 2: complexidade O(n³): {tempo_algoritmo} segundos")

"""
Resultado da Execução
└─$ python3 0-modulo5_checkout-de-presenca2.py
    n = 10
    Tempo de execução do Algoritmo 2: complexidade O(n³): 0.0006062984466552734 segundos
    n = 100
    Tempo de execução do Algoritmo 2: complexidade O(n³): 0.4692845344543457 segundos
    n = 1000
    Tempo de execução do Algoritmo 2: complexidade O(n³): 526.4349241256714 segundos
"""