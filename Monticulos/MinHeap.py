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
