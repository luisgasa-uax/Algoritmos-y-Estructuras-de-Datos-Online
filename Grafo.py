class Grafo:
    '''
    Clase Grafo para implementar una estructura de datos de grafo.

    Atributos:
    nodos (dict): Diccionario que mapea cada nodo a una lista de nodos adyacentes.
    '''

    def __init__(self):
        '''
        Inicializa un grafo vacío.
        '''
        self.nodos = {}

    def agregar_nodo(self, valor):
        '''
        Agrega un nodo al grafo.

        :param valor: Valor del nodo a agregar.
        Si el nodo ya existe en el grafo, no realiza ninguna acción.
        '''
        # Añade el nodo al diccionario si no existe.
        if valor not in self.nodos:
            self.nodos[valor] = []

    def agregar_arista(self, origen, destino):
        '''
        Agrega una arista no dirigida al grafo.

        :param origen: Nodo de origen de la arista.
        :param destino: Nodo de destino de la arista.
        Asegura que tanto el nodo de origen como el de destino existan y que la arista no esté duplicada.
        '''
        # Verifica que ambos nodos existan y que la arista no esté ya presente.
        if origen in self.nodos and destino in self.nodos:
            if destino not in self.nodos[origen]:
                self.nodos[origen].append(destino)
                # Como es un grafo no dirigido, añade la arista en ambos sentidos.
                self.nodos[destino].append(origen)

    def mostrar_grafo(self):
        '''
        Imprime una representación del grafo.
        Muestra cada nodo y sus nodos adyacentes.
        '''
        # Recorre cada nodo y sus nodos adyacentes, imprimiéndolos.
        for nodo in self.nodos:
            print(f"{nodo} -> {', '.join(map(str, self.nodos[nodo]))}")

    def vecinos(self, nodo: Any) -> List[Tuple[Any, float]]:
        '''
        Obtiene los vecinos o nodos adyacentes de un nodo específico en el grafo.
        
        Este método es útil para encontrar todos los nodos que están directamente
        conectados a un nodo dado, junto con el peso de las aristas que los conectan.

        :param nodo: El nodo para el cual se quieren encontrar los vecinos.
        :return: Una lista de tuplas, donde cada tupla representa un vecino y el peso
                 de la arista que conecta al nodo dado con este vecino. Si el nodo no
                 tiene vecinos o no existe en el grafo, se devuelve una lista vacía.
        '''
        return self.grafo.get(nodo, [])
    
    def grado_nodo(self, nodo: Any) -> int: 
        '''
        Calcula el grado total de un nodo en el grafo.

        En un grafo dirigido, el grado de un nodo es la suma de su grado de entrada y su grado de salida.
        El grado de entrada se refiere al número de aristas que llegan al nodo,
        mientras que el grado de salida se refiere al número de aristas que salen del nodo.

        :param nodo: El nodo para el cual se calculará el grado.
        :return: El grado total del nodo especificado. Si el nodo no existe en el grafo, se devuelve 0.
        '''
        return self.grado_entrada_nodo(nodo) + self.grado_salida_nodo(nodo)

