def bubble_sort(arr):
    n = len(arr)
    # Traversar todos los elementos del arreglo
    for i in range(n):
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Traversar el arreglo de 0 a n-i-1
            # Intercambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Prueba del algoritmo
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
