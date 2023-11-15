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


class Pila:
    """
    Implementa una estructura de datos tipo Pila (LIFO - Last In, First Out).

    Attributes:
        tope (Nodo, optional): El nodo superior en la pila, inicialmente None.
    """

    def __init__(self) -> None:
        """
        Constructor de la clase Pila que inicializa una Pila vacía.
        """
        self.tope = None    # elemento superior
        #self.lista = Lista()

    
    def push(self, valor) -> None:
        """
        Añade un nuevo elemento al tope de la Pila.

        Args:
            valor (any): El valor a añadir a la Pila.
        """

        nodo = Nodo(valor=valor)
        nodo.siguiente = self.tope  # importante mantener el orden
        self.tope = nodo            # para no perder el resto de elementos de la pila

    def pop(self):
        """
        Extrae el elemento del tope de la Pila y lo devuelve.

        Returns:
            any: El valor del elemento extraído o None si la pila está vacía.
        """

        if self.is_empty():
            print("Error: la pila está vacía")
            return None
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        return valor
    
    def peek(self) -> object:
        """
        Muestra el valor del último elemento introducido en la Pila sin extraerlo.

        Returns:
            any: El valor del elemento en el tope de la Pila. Si la pila está vacía, 
                 se muestra un mensaje de error y se devuelve None.
        """
        
        if self.is_empty():
            print("Error: la pila está vacía")
            return None
        valor = self.tope.valor
        #self.tope = self.tope.siguiente
        return valor

    def is_empty(self) -> bool:
        """
        Determina si la Pila está vacía.

        Returns:
            bool: True si la Pila no tiene elementos, False en caso contrario.
        """
        if self.tope == None:
            return True
        return False
    
    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de los elementos de la Pila.
        
        Crea una lista con los valores de los nodos de la Pila y los une en una cadena,
        separados por '->', representando la dirección de la Pila.
        
        Returns:
            str: Una representación en cadena de los elementos de la Pila.
        """
        elementos = []
        str_elementos = ""
        nodo_actual = self.tope
        while nodo_actual:
            elementos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        #return str_elementos
        return "->".join(elementos)
    
