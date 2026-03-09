def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    print("Pivô", pivot)
    left = [x for x in arr if x < pivot]
    print("Esquerda", left)
    middle = [x for x in arr if x == pivot]
    print("Meio", middle)
    right = [x for x in arr if x > pivot]
    print("Direita", right)

    return quick_sort(left) + middle + quick_sort(right)

# Execução
arr = [34, 7, 23, 32, 5, 62, 1, 3]
print("Array não ordenado: ",arr)
print("")

sorted_arr = quick_sort(arr)
print("Array ordenado: ", sorted_arr)
