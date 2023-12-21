class GrafoPonderado:
    '''
    Clase GrafoPonderado para representar un grafo ponderado.

    Atributos:
    grafo (dict): Diccionario que representa el grafo, donde las claves son los vértices y los valores son diccionarios
                  que mapean los vértices adyacentes y sus pesos asociados.
    '''

    def __init__(self):
        '''
        Inicializa un grafo ponderado vacío.
        '''
        self.grafo = {}

    def agregar_vertice(self, vertice: Any) -> None:
        '''
        Agrega un nuevo vértice al grafo.

        :param vertice: El vértice a agregar.
        Si el vértice ya existe, no se realiza ninguna acción.
        '''
        if vertice not in self.grafo:
            self.grafo[vertice] = {}

    def agregar_arista(self, vertice1: Any, vertice2: Any, peso: float) -> None:
        '''
        Agrega una arista ponderada entre dos vértices.

        :param vertice1: El primer vértice de la arista.
        :param vertice2: El segundo vértice de la arista.
        :param peso: El peso de la arista.
        '''
        self.agregar_vertice(vertice1)
        self.agregar_vertice(vertice2)
        self.grafo[vertice1][vertice2] = peso
        self.grafo[vertice2][vertice1] = peso  # Omitir en caso de un grafo dirigido.

    def eliminar_vertice(self, vertice: Any) -> None:
        '''
        Elimina un vértice del grafo, junto con todas sus aristas adyacentes.

        :param vertice: El vértice a eliminar.
        '''
        if vertice in self.grafo:
            del self.grafo[vertice]
            for v in self.grafo:
                if vertice in self.grafo[v]:
                    del self.grafo[v][vertice]

    def eliminar_arista(self, vertice1: Any, vertice2: Any) -> None:
        '''
        Elimina una arista entre dos vértices.

        :param vertice1: El primer vértice de la arista.
        :param vertice2: El segundo vértice de la arista.
        '''
        if vertice1 in self.grafo and vertice2 in self.grafo:
            if vertice2 in self.grafo[vertice1]:
                del self.grafo[vertice1][vertice2]
            if vertice1 in self.grafo[vertice2]:
                del self.grafo[vertice2][vertice1]

    def obtener_vertices(self) -> List[Any]:
        '''
        Devuelve una lista de todos los vértices en el grafo.

        :return: Lista de vértices del grafo.
        '''
        return list(self.grafo.keys())

    def obtener_aristas(self) -> List[Tuple[Any, Any, float]]:
        '''
        Devuelve una lista de todas las aristas en el grafo, junto con sus pesos.

        :return: Lista de tuplas, cada una representando una arista y su peso.
        '''
        aristas = []
        for vertice1 in self.grafo:
            for vertice2, peso in self.grafo[vertice1].items():
                aristas.append((vertice1, vertice2, peso))
        return aristas

    def obtener_peso_arista(self, vertice1: Any, vertice2: Any) -> float:
        '''
        Obtiene el peso de una arista específica.

        :param vertice1: El primer vértice de la arista.
        :param vertice2: El segundo vértice de la arista.
        :return: El peso de la arista. Si la arista no existe, devuelve None.
        '''
        if vertice1 in self.grafo and vertice2 in self.grafo[vertice1]:
            return self.grafo[vertice1][vertice2]
        else:
            return None

    def __str__(self) -> str:
        '''
        Representación en cadena del grafo.

        :return: Una cadena que representa el grafo, mostrando cada arista y su peso.
        '''
        resultado = ""
        for vertice1 in self.grafo:
            for vertice2, peso in self.grafo[vertice1].items():
                resultado += f"{vertice1} --({peso})--> {vertice2}\n"
        return resultado
