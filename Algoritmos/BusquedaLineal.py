def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Prueba del algoritmo
arr = [5, 8, 1, 15, 6, 3]
x = 15

result = linear_search(arr, x)

if result != -1:
    print(f"Elemento encontrado en el índice {result}")
else:
    print("Elemento no encontrado")
