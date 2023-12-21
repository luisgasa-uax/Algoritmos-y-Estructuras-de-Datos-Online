def insertion_sort(arr):
    # Recorremos todos los elementos del arreglo
    for i in range(1, len(arr)):
        key = arr[i]
        # Mueve los elementos de arr[0..i-1], que son
        # mayores que key, a una posición adelante de su
        # posición actual
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Prueba del algoritmo
arr = [12, 11, 13, 5, 6]

insertion_sort(arr)

print("El arreglo ordenado es:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
