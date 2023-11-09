"""
exemplo de memoização para melhorar o desempenho da função recursiva de Fibonacci:
"""
def fibonacci_memoizacao(n, memo={}):
    if n <= 1:
        return n
    
    # Verifica se o resultado já está memoizado
    if n not in memo:
        # Se não estiver, calcula o resultado e armazena no dicionario memo
        memo[n] = fibonacci_memoizacao(n - 1, memo) + fibonacci_memoizacao(n - 2, memo)

    return memo[n]

# Execução
resultado_memoizacao_5 = fibonacci_memoizacao(5)
resultado_memoizacao_10 = fibonacci_memoizacao(10)
resultado_memoizacao_15 = fibonacci_memoizacao(15)

print(resultado_memoizacao_5) # 5
print(resultado_memoizacao_10) # 55
print(resultado_memoizacao_15) # 610

# A memoização é alcançada através do uso de um dicionário (memo). Os resultados intermediários são armazenados nesse dicionário, e antes de calcular o resultado para um determinado n, a função verifica se esse resultado já está memoizado. Se estiver, o valor memoizado é retornado diretamente, economizando o tempo de cálculo.

# A memoização é uma técnica poderosa para melhorar a eficiência de algoritmos recursivos, especialmente em situações onde há muita repetição de cálculos para os mesmos inputs.