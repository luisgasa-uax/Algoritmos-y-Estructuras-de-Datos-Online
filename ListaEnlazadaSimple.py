# -*- coding: utf-8 -*-

class Nodo:
    """
    Representa un nodo en una estructura de datos tipo pila o cola.
    
    Attributes:
        valor (any): El valor almacenado en el nodo.
        siguiente (Nodo, optional): El siguiente nodo en la estructura, inicialmente None.
    """

    def __init__(self, valor) -> None:
        """
        Inicializa un Nodo con el valor dado.

        Args:
            valor (any): El valor que se almacenará en el nodo.
        """
        self.valor = valor
        self.siguiente = None


class ListaEnlazadaSimple:
    """
    Implementa una lista enlazada simple que mantiene una secuencia de nodos.
    
    Attributes:
        primer_nodo (Nodo, optional): Referencia al primer nodo de la lista, inicialmente None.
        tamano (int): La cantidad de nodos en la lista.
    """

    def __init__(self):
        """
        Inicializa una lista enlazada vacía.
        """
        self.primer_nodo = None
        # self.cabeza_ficticia = None  # enlace
        self.tamano = 0  # longitud de la lista

    def insertar(self, dato):
        """
        Inserta un dato en la lista en la posición dada o al final si no se especifica posición.

        Args:
            dato: El dato del nuevo nodo a insertar.
        """
        nuevo_nodo = Nodo(dato)

        if self.es_vacia:  # está vacía
            self.primer_nodo = nuevo_nodo

        else:  # inserción al final
            # recorrer hasta el final
            ultimo_nodo = self.recorrer()
            # e insertar allí
            ultimo_nodo.siguiente = nuevo_nodo

        self.tamano += 1

    def insertar_en_posicion(self, dato: object, posicion: int):
        """
        Inserta un dato en la lista en la posición dada o al final si no se especifica posición.

        Args:
            dato: El dato del nuevo nodo a insertar.
            posicion (int, optional): La posición en la que se debe insertar el nuevo nodo.
                                      Si es None, se insertará al final de la lista.
        """
        nuevo_nodo = Nodo(dato)

        # lista vacía o en primera posición
        if self.es_vacia() or posicion == 0:
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo = nuevo_nodo
            self.tamano += 1
            return

        # el tamaño es menor que la posición
        if posicion > self.tamano:
            print("La posición se encuentra fuera de la lista")
            return

        # inserción en medio
        # if posicion > 0 and posicion < self.tamano:
        if 0 < posicion < self.tamano:
            nodo_previo = self.devolver_nodo_posicion_previa_posicion(posicion)
            nuevo_nodo.siguiente = (
                nodo_previo.siguiente
            )  # importante para no perder los nodos siguientes de la lista
            nodo_previo.siguiente = nuevo_nodo

        # al final de la lista
        if posicion == self.tamano:
            ultimo_nodo = self.recorrer()
            ultimo_nodo.siguiente = nuevo_nodo

        self.tamano += 1

    def devolver_nodo_posicion_previa_posicion(self, posicion: int):
        """
        Devuelve el nodo que está antes de la posición especificada.

        Args:
            posicion (int): La posición de la cual se desea obtener el nodo previo.

        Returns:
            Nodo: El nodo que precede a la posición dada.
        """
        nodo = self.primer_nodo
        iterador = 0
        posicion_previa = posicion - 1
        while nodo.siguiente is not None and iterador < posicion_previa:
            nodo = nodo.siguiente

        return nodo  # nodo previo a la posición

    def devolver_nodo_posicion_previa_criterio(self, criterio):
        """
        Devuelve el nodo que está antes del nodo que cumple con el criterio dado.

        Args:
            criterio: El criterio que debe cumplir el nodo siguiente al que se desea devolver.

        Returns:
            Nodo: El nodo que precede al nodo que cumple con el criterio.
        """
        nodo = self.primer_nodo

        while nodo.siguiente is not None and not nodo.siguiente.dato.equals(criterio) is not False:
            nodo = nodo.siguiente

        return nodo  # nodo previo a la posición

    def recorrer(self):
        """
        Recorre la lista hasta el final y devuelve el último nodo.

        Returns:
            Nodo: El último nodo de la lista enlazada.
        """
        nodo = self.primer_nodo  # punto de entrada a la lista
        while nodo.siguiente is not None:  # no hemos llegado al final
            nodo = nodo.siguiente
        return nodo  # devolvemos el último nodo

    def es_vacia(self):
        """
        Comprueba si la lista enlazada está vacía.

        Returns:
            bool: True si la lista está vacía, False en caso contrario.
        """
        if self.primer_nodo is None:
            return True
        return False

    def tamano_lista(self):
        """
        Calcula el tamaño de la lista enlazada.

        Returns:
            int: El número de nodos en la lista.
        """
        nodo = self.primer_nodo
        tamano = 0
        while nodo.siguiente is not None:
            nodo = nodo.siguiente
            tamano += 1
        return tamano

    def buscar_por_dato(self, criterio):
        """
        Busca en la lista enlazada un nodo cuyo dato cumple con el criterio dado.

        Args:
            criterio: El criterio que debe cumplir el dato del nodo a buscar.

        Returns:
            Nodo: El nodo cuyo dato cumple con el criterio, o None si no se encuentra.
        """
        nodo = self.primer_nodo
        if self.es_vacia:
            return None

        while nodo.siguiente is not None:
            if nodo.dato.equals(criterio):
                return nodo
        return None

    def eliminar(self, criterio):
        """
        Elimina de la lista el nodo cuyo dato cumple con el criterio dado.

        Args:
            criterio: El criterio que debe cumplir el dato del nodo a eliminar.
        """
        nodo_a_eliminar = self.buscar_por_dato(criterio)
        if nodo_a_eliminar is None:
            return

        nodo_previo = self.devolver_nodo_posicion_previa_criterio(criterio)
        nodo_previo.siguiente = nodo_previo.siguiente.siguiente

        del nodo_a_eliminar  # liberamos memoria. No es necesario porque Python tiene recolector de basura

    def invertir(self):
        """
        Invierte el orden de los nodos en la lista enlazada.
        """

        """
        if self.es_vacia:
            return
        """
        nodo_previo = None  # el nuevo inicio de la lista
        nodo_actual = self.primer_nodo  # comenzamos por el primer nodo
        while nodo_actual is not None:  # mientras haya más nodos
            nodo_siguiente = nodo_actual.siguiente  # avanzamos un nodo
            nodo_actual.siguiente = nodo_previo  # le damos la vuelta al enlace
            nodo_previo = nodo_actual  # avanzamos un paso
            nodo_actual = nodo_siguiente  # terminamos el intercambio
        self.primer_nodo = nodo_previo  # una vez que llegamos al último nodo, lo devolvemos como nuevo primero

    def insertar_al_final(self, valor: object) -> None:
        self.insertar_en_posicion(valor, self.tamano)

    def __str__(self) -> str:
        """
        Recorre la lista hasta el final y devuelve el último nodo.

        Returns:
            list: listado de valores almacenados en la lista
        """
        listado_valores = []
        nodo = self.primer_nodo  # punto de entrada a la lista
        while nodo is not None:  # no hemos llegado al final
            listado_valores.append(str(nodo.valor))
            nodo = nodo.siguiente
        return str(listado_valores)
