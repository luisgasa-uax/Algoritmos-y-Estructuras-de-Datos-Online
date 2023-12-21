
def bubble_sort(books):
    n = len(books)
    for i in range(n):
        # Asumimos que la lista está ordenada; esta variable nos ayudará a optimizar el algoritmo
        already_sorted = True

        # Comparamos los elementos adyacentes
        for j in range(n - i - 1):
            if books[j][1] < books[j + 1][1]:
                # Si el libro actual ha vendido menos que el siguiente libro, los intercambiamos
                books[j], books[j + 1] = books[j + 1], books[j]

                # Como hemos tenido que hacer un intercambio, marcamos la lista como no ordenada
                already_sorted = False

        # Si no se hicieron intercambios en el último paso, la lista ya está ordenada
        if already_sorted:
            break

    return books

# Datos de muestra
books = [("Don Quijote", 120), ("Cien Años de Soledad", 150), ("El Principito", 200), ("1984", 90)]

# Ordenamos los libros y mostramos el resultado
sorted_books = bubble_sort(books)
print(sorted_books)



"""_summary_
Análisis de Complejidad Temporal

    Peor Caso (Worst Case): O(n²)
        Ocurre cuando los elementos están en el orden inverso al deseado. En este caso, cada elemento necesita ser comparado y posiblemente intercambiado con todos los demás elementos en la lista, lo que lleva a n(n-1)/2 comparaciones e intercambios, aproximadamente n² operaciones.

    Mejor Caso (Best Case): O(n)
        Se da cuando los elementos ya están en el orden deseado. El algoritmo solo necesita hacer una pasada completa sin realizar intercambios, lo que lleva a n-1 comparaciones y cero intercambios.

    Caso Promedio (Average Case): O(n²)
        Para una lista desordenada aleatoriamente, se esperaría que el algoritmo realice aproximadamente la mitad del número de intercambios del peor caso, pero aún necesita hacer comparaciones cuadráticas en el número de elementos.

Análisis de Complejidad Espacial

    Peor, Mejor y Caso Promedio: O(1)
        Independientemente del orden de los elementos en la lista, el algoritmo de la burbuja tiene una complejidad espacial constante. Esto se debe a que solo requiere un espacio adicional limitado para variables temporales utilizadas durante el intercambio de elementos. No se crean estructuras de datos adicionales que dependan del tamaño de la entrada, lo que significa que su complejidad espacial es siempre constante.

En resumen, mientras que el algoritmo de la burbuja es fácil de implementar y puede ser eficiente en listas pequeñas o casi ordenadas, su uso es generalmente limitado debido a su ineficiencia en listas grandes, como se refleja en su complejidad temporal cuadrática. Su ventaja principal es su complejidad espacial constante, lo que lo hace de bajo consumo en términos de memoria adicional.

"""