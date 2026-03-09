import time
from memory_profiler import profile

"""
Implementações em Python para calcular o n-ésimo termo da sequência de Fibonacci:
de forma recursiva e iterativa:
"""
@profile
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Execução
inicio = time.time()
resultado_recursivo_5 = fibonacci_recursivo(5)
resultado_recursivo_10 = fibonacci_recursivo(10)
resultado_recursivo_15 = fibonacci_recursivo(15)
fim = time.time()
tempo_recursivo_5 = fim - inicio
tempo_recursivo_10 = fim - inicio
tempo_recursivo_15 = fim - inicio

print(f"Redultado Recursivo (n=5): {resultado_recursivo_5}") # 5
print(f"Redultado Recursivo (n=10): {resultado_recursivo_10}") # 55
print(f"Redultado Recursivo (n=15): {resultado_recursivo_15}") # 610

print(f"Tempo Recursivo (n=5): {tempo_recursivo_5:.6f} segundos")
print(f"Tempo Recursivo (n=10): {tempo_recursivo_10:.6f} segundos")
print(f"Tempo Recursivo (n=15): {tempo_recursivo_15:.6f} segundos")

# Filename: /home/normal/github/UFMS/algoritmos-e-programacao-2/0-modulo3_unidade_1_v2-recursao-e-algoritmos-recursivos.py

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      8     48.7 MiB     48.7 MiB        1973   @profile
#      9                                         def fibonacci_recursivo(n):
#     10     48.7 MiB      0.0 MiB        1973       if n <= 1:
#     11     48.7 MiB      0.0 MiB         987           return n
#     12                                             else:
#     13     48.7 MiB      0.0 MiB         986           return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Redultado Recursivo (n=5): 5
# Redultado Recursivo (n=10): 55
# Redultado Recursivo (n=15): 610
# Tempo Recursivo (n=5): 23.419869 segundos
# Tempo Recursivo (n=10): 23.419869 segundos
# Tempo Recursivo (n=15): 23.419869 segundos

