from typing import Any
from Monticulos.MonticulosSinHerencia.Nodo import Nodo 

class MinHeap:
    '''
    Clase MinHeap para representar un montículo mínimo.
    En un montículo mínimo, cada nodo es menor que sus hijos.
    '''

    def __init__(self) -> None:
        # Inicializa el montículo como una lista vacía
        self.heap = []

    def _sink_down(self, index: int) -> None:
        '''
        Realiza la operación de hundimiento (sink down) para mantener la propiedad del montículo mínimo.
        Mueve un nodo hacia abajo en el montículo hasta que se restablecen las propiedades del montículo mínimo.
        :param index: Índice del nodo que se está hundiendo.
        '''
        menor = index
        izqda = self._left_child(index)
        dcha = self._right_child(index)

        # Comparar con hijo izquierdo
        if izqda < len(self.heap) and self.heap[izqda] < self.heap[menor]:
            menor = izqda

        # Comparar con hijo derecho
        if dcha < len(self.heap) and self.heap[dcha] < self.heap[menor]:
            menor = dcha
        
        if menor != index:
            self.heap[menor], self.heap[index] = self.heap[index], self.heap[menor]
            self._sink_down(menor)
    
    def _bubble_up(self, index: int):
        '''
        Realiza la operación de flotación (bubble up) para mantener la propiedad del montículo mínimo.
        Mueve un nodo hacia arriba en el montículo hasta que se restablecen las propiedades del montículo mínimo.
        :param index: Índice del nodo que se está flotando.
        '''
        padre = self._parent(index)
        while padre > 0 and self.heap[padre] > self.heap[index]:
            self.heap[padre], self.heap[index] = self.heap[index], self.heap[padre]
            index = padre
            padre = self._parent(index)

    def _parent(self, index: int) -> int:
        '''
        Devuelve el índice del padre de un nodo dado.
        :param index: Índice del nodo hijo.
        :return: Índice del nodo padre.
        '''
        return (index - 1) // 2

    def _left_child(self, index: int):
        '''
        Devuelve el índice del hijo izquierdo del nodo dado.
        :param index: Índice del nodo padre.
        :return: Índice del hijo izquierdo.
        '''
        return 2 * index + 1

    def _right_child(self, index: int):
        '''
        Devuelve el índice del hijo derecho del nodo dado.
        :param index: Índice del nodo padre.
        :return: Índice del hijo derecho.
        '''
        return 2 * index + 2

    def push(self, val: Any) -> None:
        '''
        Inserta un nuevo valor en el montículo.
        :param val: Valor a insertar.
        '''
        nuevoNodo = Nodo(val)
        self.heap.append(nuevoNodo)
        self._bubble_up(len(self.heap) - 1)

    def peek(self) -> Nodo:
        '''
        Devuelve el valor del nodo raíz sin eliminarlo.
        :return: Nodo raíz del montículo.
        '''
        if self.is_empty():
            return None
        return self.heap[0]

    def pop(self):
        '''
        Elimina y devuelve el nodo raíz del montículo.
        Reemplaza el nodo raíz con el último nodo y realiza un sink down para mantener las propiedades del montículo.
        :return: Nodo raíz eliminado.
        '''
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return raiz

    def size(self) -> int:
        '''
        Devuelve el número de elementos en el montículo.
        :return: Tamaño del montículo.
        '''
        return len(self.heap)

    def is_empty(self) -> bool:
        '''
        Verifica si el montículo está vacío.
        :return: True si el montículo está vacío, False en caso contrario.
        '''
        return len(self.heap) == 0

    def find_value(self, value: Any) -> int:
        '''
        Busca un valor en el montículo y devuelve su índice.
        :param value: Valor a buscar.
        :return: Índice del valor en el montículo, o -1 si no se encuentra.
        '''
        for index, nodo in enumerate(self.heap):
            if value == nodo.valor:
                return index
        return -1

    def delete_node(self, value: Any) -> None:
        '''
        Elimina un nodo con un valor específico del montículo.
        :param value: Valor del nodo a eliminar.
        '''
        index = self.find_value(value)
        if index < 0:
            print('Valor no encontrado')
            return

        # Intercambia con el último nodo y lo elimina
        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
        self.pop()

        # Reajusta el montículo
        for i in range((self.size() // 2) - 1, -1, -1):
            self._sink_down(i)

    def increase_value(self, index: int, new_value: Any) -> None:
        '''
        Aumenta el valor de un nodo en el montículo.
        :param index: Índice del nodo a aumentar.
        :param new_value: Nuevo valor del nodo.
        '''
        if new_value < self.heap[index].valor:
            raise ValueError("El nuevo valor es menor que el actual")
        self.heap[index].valor = new_value
        self._bubble_up(index)

    def decrease_value(self, index: int, new_value: Any) -> None:
        '''
        Disminuye el valor de un nodo en el montículo.
        :param index: Índice del nodo a disminuir.
        :param new_value: Nuevo valor del nodo.
        '''
        if new_value > self.heap[index].valor:
            raise ValueError("El nuevo valor es mayor que el actual")
        self.heap[index].valor = new_value
        self._sink_down(index)

    def build_heap(self, lista: list) -> None:
        '''
        Construye un montículo a partir de una lista dada.
        :param lista: Lista de valores para construir el montículo.
        '''
        self.heap = [Nodo(item) for item in lista]
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self._sink_down(i)

    def merge_heaps(self, list1: list, list2: list) -> None:
        '''
        Combina dos montículos en uno.
        :param list1: Primer montículo (o lista) a combinar.
        :param list2: Segundo montículo (o lista) a combinar.
        '''
        if list1 is None:
            list1 = self.heap
        new_list = list1 + list2
        self.build_heap(new_list)
