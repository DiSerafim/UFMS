import time
from memory_profiler import profile

"""
Implementações em Python para calcular o n-ésimo termo da sequência de Fibonacci:
de forma recursiva e iterativa:
"""
@profile
def fibonacci_iterativo(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# Execução
inicio = time.time()
resultado_iterativo_5 = fibonacci_iterativo(5)
resultado_iterativo_10 = fibonacci_iterativo(10)
resultado_iterativo_15 = fibonacci_iterativo(15)
fim = time.time()
fim_iterativo_5 = fim - inicio
fim_iterativo_10 = fim - inicio
fim_iterativo_15 = fim - inicio


print(f"Resultado Iterativo (n=5): {resultado_iterativo_5}") # 5
print(f"Resultado Iterativo (n=10): {resultado_iterativo_10}") # 55
print(f"Resultado Iterativo (n=15): {resultado_iterativo_15}") # 610

print(f"Tempo Iterativo (n=5): {resultado_iterativo_5:.6f} segundos")
print(f"Tempo Iterativo (n=10): {resultado_iterativo_10:.6f} segundos")
print(f"Tempo Iterativo (n=15): {resultado_iterativo_15:.6f} segundos")

# Filename: /home/normal/github/UFMS/algoritmos-e-programacao-2/0-modulo3_unidade_1_v2-recursao-e-algoritmos-recursivos-2.py

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      8     48.7 MiB     48.7 MiB           1   @profile
#      9                                         def fibonacci_iterativo(n):
#     10     48.7 MiB      0.0 MiB           1       if n <= 1:
#     11                                                 return n
#     12                                             
#     13     48.7 MiB      0.0 MiB           1       a, b = 0, 1
#     14                                             
#     15     48.7 MiB      0.0 MiB          15       for _ in range(2, n + 1):
#     16     48.7 MiB      0.0 MiB          14           a, b = b, a + b
#     17                                         
#     18     48.7 MiB      0.0 MiB           1       return b


# Resultado Iterativo (n=5): 5
# Resultado Iterativo (n=10): 55
# Resultado Iterativo (n=15): 610
# Tempo Iterativo (n=5): 5.000000 segundos
# Tempo Iterativo (n=10): 55.000000 segundos
# Tempo Iterativo (n=15): 610.000000 segundos
