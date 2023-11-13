def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        # Chamada recursiva para dividir e ordenar as metades
        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        # Intercalação das metades ordenadas
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1

        # Verifica se há elementos restantes em ambas as metades
        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1

# Execução
arr = [38, 27, 23, 3, 9, 82, 10]
print("Array nã ordenado: ", arr)
print("")

merge_sort(arr)
print("Array ordenado: ", arr)