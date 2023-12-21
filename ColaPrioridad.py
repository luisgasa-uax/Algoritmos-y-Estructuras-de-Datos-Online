import heapq

class PriorityQueue:
    '''
    Clase PriorityQueue para implementar una cola de prioridades.

    Atributos:
    queue (list): Lista para almacenar los elementos de la cola de prioridades.
    index (int): Índice secuencial para mantener un orden estable en elementos con igual prioridad.
    '''

    def __init__(self):
        '''
        Inicializa la cola de prioridades.
        '''
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        '''
        Inserta un elemento en la cola de prioridades con una prioridad dada.

        :param item: Elemento a insertar en la cola.
        :param priority: Prioridad del elemento (un número mayor indica mayor prioridad).
        '''
        # El módulo heapq en Python implementa un montículo mínimo por defecto.
        # Usamos negación para simular una cola de prioridad máxima.
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        '''
        Elimina y devuelve el elemento con la máxima prioridad de la cola.

        :return: El elemento con la máxima prioridad.
        :raises Exception: Si la cola está vacía.
        '''
        if self.queue:
            _, _, item = heapq.heappop(self.queue)
            return item
        raise Exception("Cola vacía")

    def peek(self):
        '''
        Devuelve el elemento con la máxima prioridad sin eliminarlo de la cola.

        :return: El elemento con la máxima prioridad.
        :raises Exception: Si la cola está vacía.
        '''
        if self.queue:
            _, _, item = self.queue[0]
            return item
        raise Exception("Cola vacía")

    def is_empty(self):
        '''
        Verifica si la cola de prioridades está vacía.

        :return: True si la cola está vacía, False en caso contrario.
        '''
        return not self.queue

# Uso de la cola de prioridad
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("Tarea 1", 1)
    pq.push("Tarea 2", 4)
    pq.push("Tarea 3", 2)

    while not pq.is_empty():
        print(pq.pop())


