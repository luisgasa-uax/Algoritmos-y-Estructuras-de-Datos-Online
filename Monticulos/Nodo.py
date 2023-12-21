class Nodo:
    '''
    Clase Nodo para representar un nodo en estructuras de datos basadas en árboles.

    Atributos:
    valor (Any): El valor almacenado en el nodo.
    hijo_izquierda (Nodo): Referencia al hijo izquierdo del nodo.
    hijo_derecha (Nodo): Referencia al hijo derecho del nodo.
    '''

    def __init__(self, valor):
        '''
        Inicializa un nuevo nodo.

        :param valor: El valor a almacenar en el nodo.
        '''
        self.valor = valor           # Almacena el valor del nodo
        self.hijo_izquierda = None   # Inicialmente no tiene hijo izquierdo
        self.hijo_derecha = None     # Inicialmente no tiene hijo derecho
