class Heap:
    '''
    Clase base Heap para implementar la estructura y operaciones comunes de un montículo.

    Atributos:
    heap (list): Lista para almacenar los elementos del montículo.
    compare (function): Función de comparación para determinar el ordenamiento en el montículo.
    '''

    def __init__(self, comparison_func):
        '''
        Inicializa un montículo con una función de comparación específica.

        :param comparison_func: Una función lambda que define la relación de orden entre los elementos del montículo.
        '''
        self.heap = []
        self.compare = comparison_func

    def _parent(self, index):
        '''
        Devuelve el índice del padre de un nodo dado.

        :param index: Índice del nodo hijo.
        :return: Índice del nodo padre.
        '''
        return (index - 1) // 2

    def _left_child(self, index):
        '''
        Devuelve el índice del hijo izquierdo del nodo dado.

        :param index: Índice del nodo padre.
        :return: Índice del hijo izquierdo.
        '''
        return 2 * index + 1

    def _right_child(self, index):
        '''
        Devuelve el índice del hijo derecho del nodo dado.

        :param index: Índice del nodo padre.
        :return: Índice del hijo derecho.
        '''
        return 2 * index + 2

    def _bubble_up(self, index):
        '''
        Realiza la operación de flotación (bubble up) para mantener la propiedad del montículo.
        Mueve un nodo hacia arriba en el montículo hasta que se restablecen las propiedades del montículo.

        :param index: Índice del nodo que se está flotando.
        '''
        parent = self._parent(index)
        while index > 0 and self.compare(self.heap[parent], self.heap[index]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def _sink_down(self, index):
        '''
        Realiza la operación de hundimiento (sink down) para mantener la propiedad del montículo.
        Mueve un nodo hacia abajo en el montículo hasta que se restablecen las propiedades del montículo.

        :param index: Índice del nodo que se está hundiendo.
        '''
        size = len(self.heap)
        element = index

        while True:
            left = self._left_child(index)
            right = self._right_child(index)

            if left < size and self.compare(self.heap[element], self.heap[left]):
                element = left

            if right < size and self.compare(self.heap[element], self.heap[right]):
                element = right

            if element != index:
                self.heap[element], self.heap[index] = self.heap[index], self.heap[element]
                index = element
            else:
                break

    def push(self, item):
        '''
        Inserta un nuevo elemento en el montículo.

        :param item: Elemento a insertar en el montículo.
        '''
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        '''
        Elimina y devuelve el elemento en la cima del montículo.

        :return: Elemento en la cima del montículo. Si el montículo está vacío, devuelve None.
        '''
        if not self.heap:
            return None

        item = self.heap[0]
        last = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last
            self._sink_down(0)

        return item

    def peek(self):
        '''
        Devuelve el elemento en la cima del montículo sin eliminarlo.

        :return: Elemento en la cima del montículo. Si el montículo está vacío, devuelve None.
        '''
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        '''
        Devuelve el número de elementos en el montículo.

        :return: Número de elementos en el montículo.
        '''
        return len(self.heap)

    def is_empty(self):
        '''
        Verifica si el montículo está vacío.

        :return: True si el montículo está vacío, False en caso contrario.
        '''
        return len(self.heap) == 0
