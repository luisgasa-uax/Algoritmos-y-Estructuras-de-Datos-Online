class CustomSet:
    '''
    Clase CustomSet para implementar una estructura de conjunto personalizada.

    Atributos:
    elements (dict): Diccionario para almacenar los elementos del conjunto. 
                     Los valores son irrelevantes, se utiliza principalmente la clave.
    '''

    def __init__(self):
        '''
        Inicializa un conjunto vacío.
        '''
        self.elements = {}

    def add(self, value):
        '''
        Agrega un valor al conjunto.

        :param value: Valor a agregar al conjunto.
        '''
        # Añade el valor como clave en el diccionario. El valor asociado no es relevante.
        if value not in self.elements:
            self.elements[value] = True

    def remove(self, value):
        '''
        Elimina un valor del conjunto.

        :param value: Valor a eliminar del conjunto.
        '''
        # Elimina el valor del diccionario si existe.
        if value in self.elements:
            del self.elements[value]

    def contains(self, value):
        '''
        Verifica si un valor está en el conjunto.

        :param value: Valor a verificar.
        :return: True si el valor está en el conjunto, False en caso contrario.
        '''
        # Verifica la presencia del valor en el diccionario.
        return value in self.elements

    def size(self):
        '''
        Devuelve el tamaño del conjunto.

        :return: Número de elementos en el conjunto.
        '''
        # Devuelve la cantidad de claves en el diccionario.
        return len(self.elements)

    def union(self, other_set):
        '''
        Devuelve la unión con otro conjunto.

        :param other_set: Otro objeto CustomSet para realizar la unión.
        :return: Un nuevo CustomSet que es la unión del conjunto actual y other_set.
        '''
        # Crea un nuevo conjunto y añade elementos de ambos conjuntos.
        result = CustomSet()
        for elem in self.elements:
            result.add(elem)
        for elem in other_set.elements:
            result.add(elem)
        return result

    def intersection(self, other_set):
        '''
        Devuelve la intersección con otro conjunto.

        :param other_set: Otro objeto CustomSet para realizar la intersección.
        :return: Un nuevo CustomSet que es la intersección del conjunto actual y other_set.
        '''
        # Crea un nuevo conjunto y añade solo los elementos comunes a ambos conjuntos.
        result = CustomSet()
        for elem in self.elements:
            if elem in other_set.elements:
                result.add(elem)
        return result

    def difference(self, other_set):
        '''
        Devuelve la diferencia con otro conjunto.

        :param other_set: Otro objeto CustomSet para realizar la diferencia.
        :return: Un nuevo CustomSet que contiene elementos que están en el conjunto actual pero no en other_set.
        '''
        # Crea un nuevo conjunto y añade elementos que están solo en el conjunto actual.
        result = CustomSet()
        for elem in self.elements:
            if elem not in other_set.elements:
                result.add(elem)
        return result

    def __str__(self):
        '''
        Representación en cadena del conjunto.

        :return: Una representación en cadena del conjunto, mostrando sus elementos.
        '''
        # Devuelve una cadena con todos los elementos del conjunto, separados por comas.
        return "{" + ", ".join(map(str, self.elements.keys())) + "}"
