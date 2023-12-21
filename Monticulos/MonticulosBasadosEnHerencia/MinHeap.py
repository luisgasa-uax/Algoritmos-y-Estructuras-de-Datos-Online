class MinHeap(Heap):
    '''
    Clase MinHeap para implementar un montículo mínimo, donde cada nodo padre es menor que sus hijos.
    Hereda de la clase Heap.
    '''

    def __init__(self):
        '''
        Inicializa un montículo mínimo.
        Utiliza una función de comparación donde los padres son menores que sus hijos.
        '''
        super().__init__(lambda parent, child: parent > child)
