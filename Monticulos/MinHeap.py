from Nodo import Nodo 

'''
Montículo mínimo: todo nodo es menor que sus hijos
'''
class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def _sink_down(self, index: int) -> None:
        menor = index
        izqda = self._left_child(index)
        dcha = self._right_child(index)

        if izqda < len(self.heap) and self.heap[izqda] < self.heap[menor]:
            menor = izqda
        if dcha < len(self.heap) and self.heap[dcha] < self.heap[menor]:
            menor = dcha
        
        if menor != index:
            self.heap[menor], self.heap[index] = self.heap[index], self.heap[menor]  
            self._sink_down(menor)
    
    def _bubble_up(self, index : int ):
        padre = self._parent(index)
        while( padre > 0 and self.heap[padre] > self.heap[index] ):
            self.heap[padre], self.heap[index] = self.heap[index], self.heap[padre]
            index = padre
            padre = self._parent(index)

    # Los métodos push, pop, peek se mantienen igual que en el MaxHeap
                
    def _parent(self, index: int) -> int:
        # Su padre está en el índice (i-1) // 2 (división entera)
        # devuelve el índice del padre
        return (index - 1) // 2
   
    def _left_child(self, index: int):
        # Devuelve el índice del hijo izquierdo de i
        return 2 * index + 1
    
    def _right_child(self, index: int):
        # Devuelve el índice del hermano derecho de i
        return 2 * index + 2       
    
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

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        if len(self.heap):
            return True
        return False 

def find_value(self, value: Any) -> int:
        '''
        Busca un valor en el montículo y devuelve su índice.
        :param value: Valor a buscar.
        :return: Índice del valor en el montículo, o -1 si no se encuentra.
        '''
        for index, nodo in enumerate(self.heap):
            if value == nodo.value:
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
        if new_value < self.heap[index].value:
            raise ValueError("El nuevo valor es menor que el actual")
        self.heap[index].value = new_value
        self._bubble_up(index)
    
    def decrease_value(self, index: int, new_value: Any) -> None:
        '''
        Disminuye el valor de un nodo en el montículo.
        :param index: Índice del nodo a disminuir.
        :param new_value: Nuevo valor del nodo.
        '''
        if new_value > self.heap[index].value:
            raise ValueError("El nuevo valor es mayor que el actual")
        self.heap[index].value = new_value
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

