def busqueda_por_interpolacion(arr, x):
    '''
    Realiza búsqueda por interpolación en un arreglo ordenado.

    Este algoritmo estima la posición del valor buscado utilizando interpolación lineal.
    Funciona mejor cuando los valores en el arreglo están uniformemente distribuidos.

    :param arr: Arreglo ordenado en el que se busca.
    :param x: Valor clave que se busca en el arreglo.
    :return: El índice del valor clave en el arreglo si se encuentra, de lo contrario -1.
    '''

    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin and x >= arr[inicio] and x <= arr[fin]:
        # Estimación de la posición del valor clave
        pos = inicio + int(((fin - inicio) / (arr[fin] - arr[inicio])) * (x - arr[inicio]))

        # Caso: valor encontrado
        if arr[pos] == x:
            return pos

        # Si el valor es mayor, x está en la parte superior
        if arr[pos] < x:
            inicio = pos + 1
        # Si el valor es menor, x está en la parte inferior
        else:
            fin = pos - 1

    return -1

# Ejemplo de uso
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 18
index = busqueda_por_interpolacion(arr, x)

if index != -1:
    print(f"Elemento encontrado en el índice {index}")
else:
    print("Elemento no encontrado en el arreglo")
