class OrdenaBusca:
    """
    Clase que implementa métodos de ordenación y búsqueda en listas.
    """

    ###########################################################################
    ##  Método genérico para el intercambio de posiciones de elementos en    ##
    #   una lista                                                            ##
    ###########################################################################
    @staticmethod
    def intercambia_posiciones(lista: list, poscion1: int, posicion2: int) -> None:
        """
        Intercambia dos elementos en una lista.

        Args:
            lista (list): Lista de elementos.
            pos_minimo (int): Posición del mínimo actual.
            pos_sig_min (int): Posición del siguiente mínimo.

        Returns:
            None: La lista se modifica in situ.

            
        Complejidad: O(1)O(1)
            Razón: Este método realiza una operación de intercambio constante, independientemente del tamaño de la lista.
        """
        lista[posicion2], lista[poscion1] = lista[poscion1], lista[posicion2]
        # print(lista)
        # print()


    ###########################################################################
    ##  Ordenación por Selección directa - Selection Sort                    ##
    ###########################################################################
    @staticmethod
    def ordenacion_seleccion_directa(lista: list) -> None:
        """
        Ordena una lista utilizando el método de selección directa.

        Args:
            lista (list): Lista de elementos a ordenar.

        Returns:
            None: La lista se modifica in situ
        
            
        Complejidad: O(n^2)
            Razón: El método tiene dos bucles anidados que recorren la lista, donde n es el número de elementos en la lista.
        """
        n = len(lista)
        for i in range(n - 1):
            minimo = lista[i]
            posicion_minimo = i
            for j in range(i + 1, n):
                if lista[j] < minimo:
                    minimo = lista[j]
                    posicion_minimo = j
            OrdenaBusca.intercambia_posiciones(lista, posicion_minimo, i)


    ###########################################################################
    ##  Búsqueda Lineal - Linear Search                                      ##
    ###########################################################################
    @staticmethod
    def busqueda_lineal(lista: list, elemento: any) -> int:
        """
        Realiza una búsqueda lineal en una lista.

        Args:
            lista (list): Lista donde buscar.
            elemento (any): Elemento a buscar en la lista.

        Returns:
            int: Índice del elemento en la lista, o -1 si no se encuentra.

            
        Complejidad: O(n)
            Razón: En el peor de los casos, este método recorrerá toda la lista, donde n es el número de elementos.
        """
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1


    ###########################################################################
    ##  Ordenación por inserción directa - Insertion Sort                    ##
    ###########################################################################
    @staticmethod
    def ordenacion_por_inserccion_directa(lista: list) -> None:
        """
        Ordena una lista utilizando el método de inserción directa.

        Args:
            lista (list): Lista de elementos a ordenar.

        Returns:
            None: La lista se modifica in situ.


        Complejidad: O(n^2)
            Razón: Al igual que la ordenación por selección, utiliza dos bucles anidados para ordenar la lista.            
        """
        n = len(lista)
        for a in range(n):
            for i in range(n - 1, a - 1, -1):
                if lista[i] < lista[i - 1]:
                    lista[i - 1], lista[i] = lista[i], lista[i - 1]


    ###########################################################################
    ##  Búsqueda Binaria - Binary Search                                     ##
    ###########################################################################
    @staticmethod
    def busqueda_binaria(lista: list, elemento: any) -> int:
        """
        Realiza una búsqueda binaria en una lista ordenada.

        Nota:
            La lista debe estar ordenada de menor a mayor.

        Args:
            lista (list): Lista ordenada donde buscar.
            elemento (any): Elemento a buscar en la lista.

        Returns:
            int: Índice del elemento en la lista, o -1 si no se encuentra.


        Complejidad: O(log⁡ n)
            Razón: Este método divide el espacio de búsqueda por la mitad en cada iteración.            
        """
        izqda = 0
        dcha = len(lista) - 1

        while izqda <= dcha:
            centro = (izqda + dcha) // 2
            if lista[centro] == elemento:
                return centro
            elif lista[centro] < elemento:
                izqda = centro + 1
            else:
                dcha = centro - 1

        return -1  # elemento no encontrado


    ###########################################################################
    ##  Ordenación por Burbuja - Bubble Sort                                 ##
    ###########################################################################
    @staticmethod
    def ordenacion_burbuja(lista: list) -> None:
        """
        Ordena una lista utilizando el algoritmo de ordenamiento de burbuja (BubbleSort).

        El algoritmo de burbuja compara elementos adyacentes y los intercambia si están
        en el orden incorrecto. Este proceso se repite hasta que la lista está ordenada.

        Args:
            lista (List): Lista de elementos que serán ordenados.
        Returns:
            None: La lista se modifica in situ.

        Complejidad: O(n^2)
            Razón: Utiliza bucles anidados para comparar e intercambiar elementos adyacentes.            
        """
         
        n = len(lista)

        for i in range(n):
            # Flag para optimizar el algoritmo. Si no hay intercambio es que la lista ya está ordenada.
            hay_intercambio = False

            # Recorremos la lista, excluyendo los elementos ya ordenados en iteraciones anteriores.
            for j in range(0, n-i-1):
                # Comparamos elementos adyacentes.
                if lista[j] > lista[j+1]:
                    # Intercambiamos si el elemento de la izquierda es mayor que el de la derecha.
                    OrdenaBusca.intercambia_posiciones(lista, j, j+1)

                    # Marcamos que ha habido un intercambio.
                    hay_intercambio = True

            # Si no se ha realizado ningún intercambio, la lista ya está ordenada y podemos salir del bucle.
            if not hay_intercambio:
                break

    
    ###########################################################################
    ##  Montículos - Heaps                                                   ##
    ###########################################################################
    @staticmethod
    def monticulo_reorganizar(lista, n, indice_actual_nodo) -> None:
        """
        Algoritmo de reorganización de un montículo una parte de la lista L para mantener la propiedad de montículo.
        
        Args:
            L (List): La lista que representa el montículo.
            n (int): El tamaño del montículo.
            i (int): Índice del nodo actual en el montículo.
        Returns:
            None: La lista se modifica in situ.

            
        Complejidad: O(log⁡ n)
            En el peor de los casos, el método monticulo_reorganizar necesita comparar un nodo con sus hijos y posiblemente intercambiarlo con uno de ellos. Este proceso puede continuar hasta que se alcanza el nivel más bajo del árbol. En un montículo (heap) binario, la altura del árbol es log⁡ n, donde n es el número de nodos en el montículo. Por lo tanto, la complejidad temporal es proporcional a la altura del árbol
        """
        padre = indice_actual_nodo
        esMonticulo = False

        while not esMonticulo:
            # Calculamos los índices de los hijos izquierdo y derecho
            hijoIzqa = 2 * indice_actual_nodo + 1
            hijoDcha = 2 * indice_actual_nodo + 2

            # Verificamos si el nodo actual es una hoja
            if hijoIzqa >= n:
                break  # El nodo es una hoja, salir del bucle
            else:
                # Determinamos cuál hijo es mayor
                if hijoDcha < n and lista[hijoDcha] > lista[hijoIzqa]:
                    max = hijoDcha
                else:
                    max = hijoIzqa

                # Intercambiamos con el padre si el hijo mayor es mayor que el padre
                if lista[max] > lista[padre]:
                    lista[padre], lista[max] = lista[max], lista[padre]
                    padre = max
                else:
                    esMonticulo = True

    @staticmethod
    def monticulo_construir(lista, n) -> None:
        """
        Construye un montículo a partir de una lista dada.

        Args:
            lista (List): Lista para construir el montículo.
            n (int): Tamaño de la lista.
        Returns:
            None: La lista se modifica in situ.

            
        Complejidad: O(n)
            A primera vista, uno podría pensar que la complejidad es O(nlog⁡ n) porque se llama a monticulo_reorganizar, que es O(log⁡ n), n veces. Sin embargo, una inspección más cercana revela que no todos las llamadas a monticulo_reorganizar trabajan con una lista completa de n elementos. Muchas de estas llamadas actúan en niveles más bajos del montículo, con menos elementos.
            
            La cantidad de trabajo realizado por monticulo_reorganizar no es constante y es menor para nodos más bajos en el árbol. Una análisis más detallado muestra que el tiempo total es proporcional a n, resultando en una complejidad de O(n).
        """
        inicio = n // 2 - 1  # Índice del último nodo no hoja

        # Construimos un montículo máximo
        for i in range(inicio, -1, -1):
            OrdenaBusca.monticulo_reorganizar(lista, n, i)

    @staticmethod
    def monticulo_ordenar(lista):
        """
        Realiza el ordenamiento por montículos (Heap Sort) en la lista dada.

        Args:
            L (List): Lista a ordenar.
        Returns:
            None: La lista se modifica in situ.

            
        Complejidad: O(n log n)
            El método comienza construyendo un montículo a partir de la lista dada, lo cual tiene una complejidad de O(n).
            
            Luego, el método extrae el elemento más grande (o más pequeño, dependiendo del tipo de montículo) y lo coloca al final de la lista. Este proceso se repite n−1 veces.

            Cada extracción requiere reorganizar el montículo para mantener la propiedad del montículo, y cada reorganización tiene una complejidad de O(log ⁡n).
            
            Por lo tanto, el proceso de extracción y reorganización se realiza n veces con una complejidad de O(log⁡ n) cada una, resultando en una complejidad total de O(nlog⁡ n) para el método completo.
        """
        n = len(lista)

        # Construimos un montículo máximo
        OrdenaBusca.monticulo_construir(lista, n)

        # Extraemos elementos uno por uno
        for i in range(n - 1, 0, -1):
            lista[i], lista[0] = lista[0], lista[i]  # swap
            OrdenaBusca.monticulo_reorganizar(lista, i, 0)


    ###########################################################################
    ##  Ordenación rápida - Quick Sort                                       ##
    ###########################################################################
    @staticmethod
    def particion(lista, izqda, dcha) -> int:
        """
        Función de partición para el algoritmo de Quick Sort. Su propósito es elegir un pivote y reorganizar los elementos de la lista de tal manera que los elementos menores que el pivote queden a su izquierda y los mayores a su derecha.

        Args:
            L (List): Lista a ser particionada.
            izq (int): Índice inicial de la porción de la lista a ser particionada.
            der (int): Índice final de la porción de la lista a ser particionada.

        Returns:
            int: Índice del punto de partición.

            
        Complejidad: O(n)
            En cada llamada a particion, el método recorre cada elemento del segmento de la lista delimitado por izqda y dcha.
            
            Independientemente del valor del pivote, cada elemento se compara una vez con el pivote y posiblemente se mueve.
            
            Por lo tanto, la complejidad temporal de una llamada a particion es proporcional al número de elementos en el segmento de la lista que se está particionando, lo que resulta en O(n) en el peor caso.
        """
        pivote = lista[dcha]
        indice = izqda

        for i in range(izqda, dcha):
            # Si el elemento actual es menor o igual al pivote
            if lista[i] <= pivote:
                lista[indice], lista[i] = lista[i], lista[indice]  # swap
                indice += 1

        # Intercambiamos el pivote con el elemento en el índice encontrado
        lista[indice], lista[dcha] = lista[dcha], lista[indice]
        return indice
    
    @staticmethod
    def quicksort(lista, izqa, dcha) -> None:
        """
        Implementa el algoritmo QuickSort (tipo divide y vencerás) para ordenar una parte de la lista de forma recursiva.

        Args:
            L (List): La lista a ordenar.
            izq (int): Índice inicial de la parte de la lista a ordenar.
            der (int): Índice final de la parte de la lista a ordenar.
        Returns:
            None: La lista se modifica in situ.

            
        Complejidad: O(n log n) en el caso promedio, O(n^2) en el peor caso.
            En el caso promedio, QuickSort divide la lista en dos mitades aproximadamente iguales en cada nivel de recursión. Esto significa que la altura del árbol de recursión es log⁡ n, y debido a que cada nivel de la recursión implica particionar toda la lista o sublista (lo que cuesta O(n)), la complejidad total es O(n log⁡ n).
            
            Sin embargo, en el peor caso (por ejemplo, cuando la lista ya está ordenada o el pivote es siempre el elemento más pequeño o más grande), QuickSort se comporta como un algoritmo de partición simple. Esto significa que solo divide la lista en una partición de un solo elemento y otra de n−1 elementos, lo que lleva a una altura de árbol de recursión de n y una complejidad temporal total de O(n^2).

            El rendimiento de QuickSort depende en gran medida de la elección de los pivotes. Si los pivotes dividen la lista en partes más o menos iguales (lo que suele suceder en promedio), el algoritmo es muy eficiente con una complejidad de O(n log ⁡n). Sin embargo, en el peor de los casos, su eficiencia disminuye a O(n^2), lo que es significativamente menos eficiente que otros algoritmos de ordenamiento como Merge Sort o Heap Sort. Por esta razón, en la práctica, a menudo se utilizan variantes de QuickSort (como QuickSort aleatorizado o QuickSort con selección de pivote mediano de tres) que tienden a evitar el peor caso en la mayoría de las situaciones prácticas.
        """
        if izqa < dcha:
            # Obtenemos el índice del pivote
            pivote_indice = OrdenaBusca.particion(lista, izqa, dcha)

            # Ordenamos recursivamente los elementos antes y después del particionamiento
            OrdenaBusca.quicksort(lista, izqa, pivote_indice - 1)
            OrdenaBusca.quicksort(lista, pivote_indice + 1, dcha)
    

    
    ###########################################################################
    ##  Ordenación por Mezcla - Merge Sort                                   ##
    ###########################################################################
    @staticmethod
    def mergeSort(lista) -> list:
        """
        Implementa el algoritmo MergeSort para ordenar una lista.

        Args:
            lista (List): La lista a ordenar.

        Returns:
            List: Lista ordenada.

            
        Complejidad: O(n log n) 
            El proceso de dividir la lista en mitades se realiza en O(log n) pasos, ya que en cada paso se divide la lista a la mitad.
            
            En cada nivel de división, la operación de combinación (realizada por el método merge) para todas las sublistas en ese nivel suma hasta O(n). Esto se debe a que cada elemento se procesa y se coloca en su posición final una vez por nivel.
            
            Como el algoritmo tiene log ⁡n niveles (debido a la división a la mitad en cada paso) y cada nivel de fusión cuesta O(n), la complejidad total es O(n log⁡ n).
        """
        n = len(lista)
        if n <= 1:
            return lista

        medio = n // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        izquierda = OrdenaBusca.mergeSort(izquierda)
        derecha = OrdenaBusca.mergeSort(derecha)

        return OrdenaBusca.merge(izquierda, derecha)

    @staticmethod
    def merge(izqda, dcha) -> list:
        """
        Combina dos listas ordenadas en una sola lista ordenada.

        Args:
            izquierda (List): Lista ordenada izquierda.
            derecha (List): Lista ordenada derecha.

        Returns:
            List: Lista combinada y ordenada.

            
        Complejidad: O(n) 
            En cada llamada a merge, el método recorre las dos listas de entrada (izquierda y derecha) una vez, combinándolas en una nueva lista ordenada.
            
            El número total de operaciones es proporcional a la suma de las longitudes de las dos listas, lo que en el peor de los casos es n (donde nn es el número total de elementos en la lista original).
            
            Por lo tanto, la complejidad temporal de merge es lineal respecto al número total de elementos que se están fusionando.    


            El Merge Sort es un algoritmo eficiente y estable para ordenar listas, con una complejidad temporal garantizada de O(n log n). Es particularmente útil y eficiente para listas grandes, y a diferencia de QuickSort, su rendimiento no depende del orden inicial de los elementos en la lista. Sin embargo, una desventaja de Merge Sort es que requiere espacio adicional proporcional al tamaño de la lista, ya que las sublistas se copian en nuevas listas durante el proceso de fusión.    
        """
        resultado = []
        i = j = 0

        # Fusionamos las listas izquierda y derecha
        while i < len(izqda) and j < len(dcha):
            if izqda[i] < dcha[j]:
                resultado.append(izqda[i])
                i += 1
            else:
                resultado.append(dcha[j])
                j += 1

        # Añadimos los elementos restantes de izquierda, si los hay
        while i < len(izqda):
            resultado.append(izqda[i])
            i += 1

        # Añadimos los elementos restantes de derecha, si los hay
        while j < len(dcha):
            resultado.append(dcha[j])
            j += 1

        return resultado