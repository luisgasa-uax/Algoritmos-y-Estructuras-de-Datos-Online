from typing import Any
from Nodo import Nodo

'''
Montículo máximo: todo nodo es mayor que sus hijos
'''
class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def _parent(self, index) -> int:
        # Su padre está en el índice (i-1) // 2 (división entera)
        # devuelve el índice del padre
        return (index - 1) // 2

    def _bubble_up(self, index ):
        padre = self._parent(index)
        while( padre >= 0 and self.heap[padre] < self.heap[index] ):
            self.heap[padre], self.heap[index] = self.heap[index], self.heap[padre]
            '''
            nodo_aux = self.heap[padre]
            self.heap[padre] = self.heap[index]
            self.heap[index] = nodo_aux
            '''
    # Insertamos nuevo nodo    
    def push(self, val:Nodo) -> None:
        nuevoNodo = Nodo(val)
        self.heap.append(nuevoNodo)
        self._bubble_up(len(self.heap) - 1)

    # Consultamos el valor del nodo raiz
    def peek(self, val: Nodo) -> Nodo:
        if len(self.heap) == 0 :
            # No hay nodos
            return None
        # Devolvemos el nodo raiz, SIN eliminarlo
        return self.heap[0]

    # Extraemos el nodo raiz
    def pop(self): 
        if len(self.heap) == 0 :
            # No hay nodos en el montículo
            return None
        if len(self.heap) == 1:
            # Solo queda un nodo en el montículo
            return self.heap.pop()
        
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        # hundimiento
        self._sink_down(0)
        return raiz
    
    def _left_child(self, index: int):
        # Devuelve el índice del hijo izquierdo de i
        return 2 * index + 1
    
    def _right_child(self, index: int):
        # Devuelve el índice del hermano derecho de i
        return 2 * index + 2

    # Heapify o Hundimiento o recolocación de los nodos. 
    def _sink_down(self, index: int):
        mayor = index
        izqda = self._left_child(index)
        dcha = self._right_child(index)

        if izqda < len(self.heap) and self.heap[izqda] > self.heap[mayor]:
            mayor = izqda
        
        if dcha < len(self.heap) and self.heap[dcha] > self.heap[mayor]:
            mayor = dcha
        
        if mayor != index:
            self.heap[index], self.heap[mayor] = self.heap[mayor], self.heap[index]
            self._sink_down(mayor)

    def size(self) -> int:
        return len(self.heap)
    
    def is_empty(self) -> bool:
        if len(self.heap):
            return True
        return False

    def find_value(self, value: Any ) -> int:
        for index in range(0, len(self.heap)):
            if value == (self.heap[index]).value:
                return index
        return -1
    

    def delete_node(self, value: Any) -> None:
        index = self.find_value(value)
        if index < 0:
            print('Valor no encontrado') 
            return

        # intercambiamos        
        self.heap[index], self.heap[self.size()-1] =  self.heap[self.size()-1] , self.heap[index]

        self.pop()

        for i in range((self.size//2)-1, -1, -1):
            self._sink_down(i)
    
    def increase_value(self, index: int, new_value: Any ) -> None:
        if new_value < self.heap[index].valor:
            raise ValueError("El nuevo valor es menor qeu el actual")

        nuevo_nodo = Nodo(new_value)
        self.heap[index] = nuevo_nodo

        padre = self._parent(index)

        while index != 0 and self.heap[padre] < self.heap[index]:
            self.heap[padre] , self.heap[index] = self.heap[index] , self.heap[padre]
            index = padre
    
    def decrease_value(self, index: int, new_value: Any ) -> None:
        if new_value > self.heap[index].valor:
            raise ValueError("El nuevo valor es menor qeu el actual")
        
        self.heap[index] = Nodo(new_value)
        self._sink_down(index)
    

    def build_heap(self, lista: list):
        longitud = len(lista)
        for index in range(longitud//2 -1, -1, -1):
            self._sink_down(lista, longitud, index)

    def merge_heaps(self, list1: list , list2: list) -> None:
        if list1 == None:
            list1 = self.heap
        new_list = list1 + list2
        self.build_heap(new_list)
    


