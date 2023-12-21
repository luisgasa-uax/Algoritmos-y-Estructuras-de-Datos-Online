def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontrar el punto medio del array
        L = arr[:mid]  # Dividir los elementos en dos mitades
        R = arr[mid:]

        merge_sort(L)  # Ordenar la primera mitad
        merge_sort(R)  # Ordenar la segunda mitad

        i = j = k = 0

        # Copiar datos a los arrays temporales L[] y R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Comprobar si quedan elementos en L[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Comprobar si quedan elementos en R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Prueba del algoritmo
arr = [12, 11, 13, 5, 6, 7]

merge_sort(arr)

print("El array ordenado es:")
print(arr)
