def selection_sort(arr):
    for i in range(len(arr)):
        # Encontra o índice do elemento mínimo na parte não ordenada
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # troca o elemento mínimo com o elemento na posição atual
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Execução
arr = [64, 25, 12, 22, 11]
print("Array não ordenado: ", arr)
print("")

selection_sort(arr)
print("Array ordenado: ", arr)