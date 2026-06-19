def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Índice final i é ignorado, pois os maiores elementos já estão no lugar certo.
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos se estiverem fora de ordem
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Execução
arr = [5, 3, 1, 4, 2]
bubble_sort(arr)
print("Array ordenado: ", arr)