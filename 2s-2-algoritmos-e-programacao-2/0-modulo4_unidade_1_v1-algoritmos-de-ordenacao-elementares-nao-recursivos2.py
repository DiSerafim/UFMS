def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        # Move os elementos do subconjunto ordenado para a direita.
        # até encontrar a posição correta para a chave
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insere a chave na posição correta
        arr[j + 1] = chave

# Execução
arr = [5, 3, 1, 4, 2]
insertion_sort(arr)
print("Array ordenado: ", arr)