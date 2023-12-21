def selection_sort(arr):
    n = len(arr)
    # Recorrer todos los elementos del arreglo
    for i in range(n):
        # Encontrar el mínimo elemento en el arreglo restante
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Intercambiar el elemento mínimo encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Prueba del algoritmo
arr = [64, 25, 12, 22, 11]

selection_sort(arr)

print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
