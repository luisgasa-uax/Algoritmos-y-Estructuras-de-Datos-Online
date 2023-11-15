# -*- coding: utf-8 -*-

from Pelicula import Pelicula

class Nodo: 
    """Implementa la clase Nodo para una estructura de datos tipo Cola.

    Attributes: 
        valor (Object): El valor almacenado en el nodo.
        siguiente (Nodo, optional): El siguiente nodo en la Cola, inicialmente None.
    """
    def __init__(self, valor) -> None:
        """Inicializa un Nodo con un valor dado.

        Args:
            valor (Object): El valor que se almacenará en el nodo.
        """
        self.valor = valor
        self.siguiente = None


class Cola:
    """Implementa una estructura de datos de tipo Cola.

    Attributes: 
        frente (Nodo, optional): El primer nodo de la Cola, inicialmente None.
        final (Nodo, optional): El último nodo de la Cola, inicialmente None.
        tamanio (int): El número de nodos en la Cola, inicialmente 0.
    """
    def __init__(self) -> None:
        """Constructor de la clase Cola que inicializa una Cola vacía."""
        self.frente = None
        self.final = None
        self.tamanio = 0

    def enqueue(self, valor: object):
        """Añade un nuevo elemento al final de la Cola.

        Args:
            valor (object): El valor a encolar.
        """
        nodo = Nodo(valor=valor)
        if self.is_empty():
            self.frente = nodo
            self.final = nodo
        else: 
            self.final.siguiente = nodo  
            self.final = nodo
        self.tamanio += 1

    def dequeue(self):
        """Retira y devuelve el elemento del frente de la Cola.

        Returns:
            object: El valor del elemento retirado o None si la cola está vacía.
        """
        if self.is_empty():
            print("ADVERTENCIA: la cola está vacía")
            return None
        valor_salida = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente == None:     # no hay elementos en la cola
            self.final = None
        self.tamanio -= 1
        return valor_salida
       
    def peek(self):
        """Devuelve el valor del elemento que está en el frente de la Cola sin retirarlo.

        Returns:
            object: El valor del frente de la Cola o None si la cola está vacía.
        """
        if self.is_empty():
            print("ADVERTENCIA: la cola está vacía")
            return None
        valor_salida = self.frente.valor
        return valor_salida

    def size(self) -> int:
        """Devuelve la cantidad de elementos almacenados en la Cola.
        
        Returns:
            int: El tamaño de la Cola.
        """
        return self.tamanio

    def is_empty(self) -> bool:
        """Comprueba si la Cola está vacía.

        Returns:
            bool: True si la Cola está vacía, False en caso contrario.
        """
        if self.tamanio == 0: 
            return True
        return False




