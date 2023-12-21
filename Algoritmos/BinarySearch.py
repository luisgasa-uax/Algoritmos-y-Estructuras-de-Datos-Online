def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Si x está presente en el medio
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Prueba del algoritmo
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, x)

if result != -1:
    print(f"Elemento encontrado en el índice {result}")
else:
    print("Elemento no encontrado")
