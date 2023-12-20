from typing import Any, Tuple, List, Set, Deque
from collections import deque
import heapq


class GrafoDirigidoPonderado:
    """
    Clase que representa un grafo dirigido ponderado.

    Un grafo dirigido ponderado es una estructura de datos que consiste en un conjunto de nodos
    y un conjunto de aristas dirigidas, donde cada arista tiene un peso asociado.

    Atributos:
        grafo (dict): Diccionario que almacena el grafo. Las claves son los nodos y los valores son
                      listas de tuplas, donde cada tupla representa una arista con destino y peso.

    Métodos:
        add_nodo(self, nodo): Agrega un nodo al grafo.
        add_arista(self, origen, destino, peso): Agrega una arista dirigida al grafo.
        display_grafo(self): Muestra el grafo.
        get_neighbors(self, nodo): Obtiene los vecinos de un nodo.
    """

    def __init__(self):
        """
        Inicializa un nuevo grafo dirigido ponderado.
        """
        self.grafo = {}  # Diccionario para almacenar el grafo

    def add_nodo(self, nodo: Any) -> None:
        """
        Agrega un nodo al grafo.

        Si el nodo no existe en el grafo, se añade al diccionario con una lista vacía como valor.

        Parámetros:
            nodo: El nodo a agregar.
        """
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def add_arista(self, origen, destino, peso) -> None:
        """
        Agrega una arista dirigida del nodo origen al nodo destino con el peso especificado.

        Si el nodo origen o destino no existen en el grafo, se agregan.

        Parámetros:
            origen: El nodo de origen de la arista.
            destino: El nodo de destino de la arista.
            peso: El peso de la arista.
        """
        if origen not in self.grafo:
            self.add_nodo(origen)
        if destino not in self.grafo:
            self.add_nodo(destino)

        self.grafo[origen].append((destino, peso))

    def display_grafo(self):
        """
        Muestra una representación del grafo.

        Imprime cada nodo y sus aristas asociadas con sus respectivos pesos.
        """
        for nodo in self.grafo:
            for arista in self.grafo[nodo]:
                print(f"{nodo} -> {arista[0]} [peso: {arista[1]}]")

    def get_vecinos(self, nodo: Any):
        """
        Obtiene los vecinos (nodos de destino) de un nodo específico.

        Parámetros:
            nodo: El nodo del que se quieren obtener los vecinos.

        Retorna:
            Una lista de tuplas, donde cada tupla contiene un nodo de destino y el peso de la arista.
        """
        return self.grafo.get(nodo, [])

    def delete_nodo(self, nodo: Any):
        """
        Elimina un nodo del grafo junto con todas las aristas relacionadas.

        Esta función elimina el nodo especificado del grafo. Si el nodo existe,
        también se eliminan todas las aristas que tienen este nodo como destino
        en otros nodos del grafo.

        Parámetros:
            nodo: El nodo a eliminar.

        Retorna:
            None
        """
        # Eliminar el nodo si existe
        if nodo in self.grafo:
            del self.grafo[nodo]

        # Eliminar aristas que apuntan al nodo eliminado
        for origen in self.grafo:
            self.grafo[origen] = [arista for arista in self.grafo[origen] if arista[0] != nodo]

    def delete_arista(self, origen: Any, destino: Any):
        """
        Elimina una arista específica del grafo.

        Este método elimina una arista dirigida desde el nodo 'origen' hacia el nodo 'destino', si existe.
        Si el nodo de origen no existe en el grafo o si la arista especificada no está presente, 
        la función no realiza ninguna acción.

        Parámetros:
            origen: El nodo de origen de la arista.
            destino: El nodo de destino de la arista.

        Retorna:
            None
        """
        if origen in self.grafo:
            self.grafo[origen] = [arista for arista in self.grafo[origen] if arista[0] != destino]

    def existe(self, nodo: Any, destino=None):
        """
        Verifica la existencia de un vértice o una arista en el grafo.

        Si solo se proporciona el nodo, la función verifica si este vértice existe en el grafo.
        Si se proporcionan tanto el nodo como el destino, la función verifica si existe una arista
        desde el nodo hacia el destino.

        Parámetros:
            nodo: El nodo de origen para verificar su existencia o la existencia de una arista desde él.
            destino (opcional): El nodo de destino de la arista a verificar.

        Retorna:
            bool: True si el vértice o la arista existen en el grafo, False en caso contrario.
        """
        if destino is None:
            # Verificar la existencia del vértice
            return nodo in self.grafo

        # Verificar la existencia de la arista
        return any(arista[0] == destino for arista in self.grafo.get(nodo, []))
    
    def grado_vertice(self, nodo: Any) -> Tuple[int, int]:
        """
        Determina el grado de entrada y salida de un vértice en el grafo.

        En un grafo dirigido, el grado de un vértice se divide en grado de entrada
        (número de aristas entrantes) y grado de salida (número de aristas salientes).
        Este método calcula ambos para el vértice especificado.

        Parámetros:
            nodo: El vértice para el cual se determinará el grado.

        Retorna:
            tuple: Un par (grado_entrada, grado_salida), donde cada elemento es un entero
                   que representa el grado correspondiente. Si el vértice no existe en el grafo,
                   se devuelve (0, 0).
        """
        grado_salida = len(self.grafo.get(nodo, []))
        grado_entrada = sum(nodo in [destino for destino, _ in self.grafo[origen]] for origen in self.grafo)

        return grado_entrada, grado_salida

    def dfs(self, nodo_inicial: Any) -> List[Any]:
        """
        Realiza un recorrido en profundidad (DFS) desde un nodo inicial.

        DFS explora el grafo yendo lo más profundo posible a lo largo de cada rama antes de retroceder,
        lo que es útil para muchas aplicaciones como la búsqueda de componentes conectados,
        ordenamiento topológico, y para encontrar caminos en un grafo.

        Parámetros:
            nodo_inicial: El nodo desde el cual se inicia el recorrido DFS.

        Retorna:
            List[Any]: Una lista de nodos en el orden en que fueron visitados durante el recorrido DFS.
        """
        visitados = set()  # Conjunto para llevar un registro de los nodos visitados
        recorrido = []     # Lista para almacenar el orden de los nodos visitados

        def dfs_recursivo(nodo: Any):
            """ Función auxiliar recursiva para realizar el recorrido DFS. """
            if nodo not in visitados:
                visitados.add(nodo)        # Marcar el nodo como visitado
                recorrido.append(nodo)     # Añadir el nodo al recorrido
                # Recorrer recursivamente todos los nodos vecinos
                for vecino, _ in self.grafo.get(nodo, []):
                    dfs_recursivo(vecino)

        dfs_recursivo(nodo_inicial)
        return recorrido
    
    def bfs(self, nodo_inicial: Any) -> List[Any]:
        """
        Realiza un recorrido en anchura (BFS) desde un nodo inicial.

        BFS explora el grafo nivel por nivel, partiendo del nodo inicial. Este método es útil
        para encontrar el camino más corto en un grafo no ponderado y para la búsqueda de nivel por nivel.

        Parámetros:
            nodo_inicial: El nodo desde el cual se inicia el recorrido BFS.

        Retorna:
            List[Any]: Una lista de nodos en el orden en que fueron visitados durante el recorrido BFS.
        """
        visitados = set()          # Conjunto para llevar un registro de los nodos visitados
        cola: Deque[Any] = deque() # Cola para almacenar los nodos a visitar
        recorrido = []             # Lista para almacenar el orden de los nodos visitados

        # Iniciar el recorrido desde el nodo inicial
        cola.append(nodo_inicial)
        visitados.add(nodo_inicial)

        while cola:
            nodo_actual = cola.popleft()  # Sacar el nodo actual de la cola
            recorrido.append(nodo_actual) # Añadir el nodo al recorrido

            # Añadir todos los vecinos no visitados del nodo actual a la cola
            for vecino, _ in self.grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    visitados.add(vecino) # Marcar como visitado
                    cola.append(vecino)   # Añadir a la cola para visitar más tarde

        return recorrido

    def camino_mas_corto_dijkstra(self, origen: Any, destino: Any) -> Tuple[List[Any], float]:
        """
        Determina el camino más corto desde un nodo origen a un nodo destino usando el algoritmo de Dijkstra.

        Este método encuentra el camino más corto en un grafo dirigido ponderado con pesos positivos.
        Si no existe un camino, devuelve una lista vacía y una distancia infinita.

        Parámetros:
            origen: El nodo de origen.
            destino: El nodo de destino.

        Retorna:
            Tuple[List[Any], float]: Una tupla que contiene el camino más corto como una lista de nodos y
                                     la distancia total del camino. Si no hay camino, la lista estará vacía
                                     y la distancia será infinita.
        """
        distancias: Dict[Any, float] = {nodo: float('inf') for nodo in self.grafo}
        distancias[origen] = 0
        previos: Dict[Any, Any] = {nodo: None for nodo in self.grafo}
        cola = [(0, origen)]

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)

            # Si encontramos el destino, construimos el camino de regreso
            if nodo_actual == destino:
                camino = []
                while nodo_actual is not None:
                    camino.insert(0, nodo_actual)
                    nodo_actual = previos[nodo_actual]
                return camino, distancia_actual

            # Si la distancia actual es mayor a la distancia registrada, se salta la iteración
            if distancia_actual > distancias[nodo_actual]:
                continue

            # Explorar vecinos del nodo actual
            for vecino, peso in self.grafo.get(nodo_actual, []):
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    previos[vecino] = nodo_actual
                    heapq.heappush(cola, (distancia, vecino))

        return [], float('inf')  # No se encontró un camino

    def estan_conectados(self, origen: Any, destino: Any) -> bool:
        """
        Determina si existe un camino entre dos nodos en el grafo.

        Utiliza un recorrido DFS para buscar un camino desde el nodo de origen al nodo de destino.
        Si se encuentra tal camino, devuelve True, lo que indica que los nodos están conectados.
        En caso contrario, devuelve False.

        Parámetros:
            origen: El nodo de origen.
            destino: El nodo de destino.

        Retorna:
            bool: True si los nodos están conectados, False en caso contrario.
        """
        visitados = set()

        def dfs(nodo_actual: Any) -> bool:
            """ Función auxiliar recursiva para realizar el recorrido DFS. """
            if nodo_actual == destino:
                return True
            visitados.add(nodo_actual)
            for vecino, _ in self.grafo.get(nodo_actual, []):
                if vecino not in visitados and dfs(vecino):
                    return True
            return False

        return dfs(origen) if origen in self.grafo else False
    
def a_estrella(self, inicio: Any, objetivo: Any, heuristica: Callable[[Any, Any], float]) -> Tuple[List[Any], float]:
        """
        Implementa el algoritmo A* para encontrar el camino más corto entre dos nodos.

        Este método utiliza una función heurística para estimar el costo de llegar desde
        cada nodo hasta el nodo objetivo, lo que puede resultar en una búsqueda más rápida
        que el algoritmo de Dijkstra en espacios de búsqueda grandes.

        Parámetros:
            inicio: El nodo de inicio.
            objetivo: El nodo objetivo.
            heuristica: Una función que toma dos nodos y devuelve una estimación del costo de ir de uno a otro.

        Retorna:
            Tuple[List[Any], float]: Una tupla que contiene el camino desde el nodo de inicio hasta el nodo objetivo
                                     y el costo total del camino. Si no hay camino, la lista estará vacía y el costo será infinito.
        """
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (0, inicio))
        costos = {inicio: 0}
        predecesores = {inicio: None}

        while cola_prioridad:
            costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == objetivo:
                camino = []
                while nodo_actual:
                    camino.insert(0, nodo_actual)
                    nodo_actual = predecesores[nodo_actual]
                return camino, costo_actual

            for vecino, peso in self.grafo.get(nodo_actual, []):
                nuevo_costo = costos[nodo_actual] + peso
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(vecino, objetivo)
                    heapq.heappush(cola_prioridad, (prioridad, vecino))
                    predecesores[vecino] = nodo_actual

        return [], float('inf')  # No se encontró un camino




# Ejemplo de uso
grafo = GrafoDirigidoPonderado()
grafo.add_arista('A', 'B', 5)
grafo.add_arista('A', 'C', 3)
grafo.add_arista('B', 'C', 4)
grafo.add_arista('C', 'A', 2)

grafo.display_grafo()
