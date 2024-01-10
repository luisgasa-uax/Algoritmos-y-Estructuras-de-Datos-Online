from Heap import Heap
class MaxHeap(Heap):
    '''
    Clase MaxHeap para implementar un montículo máximo, donde cada nodo padre es mayor que sus hijos.
    Hereda de la clase Heap.
    '''

    def __init__(self):
        '''
        Inicializa un montículo máximo.
        Utiliza una función de comparación donde los padres son mayores que sus hijos.
        '''
        super().__init__(lambda parent, child: parent.valor < child.valor)

