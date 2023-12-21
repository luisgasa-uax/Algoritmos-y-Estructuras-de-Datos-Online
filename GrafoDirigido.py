class GrafoDirigido:
    '''
    Clase GrafoDirigido para representar un grafo dirigido.

    Atributos:
    nodos (dict): Diccionario que representa el grafo, mapeando cada nodo a una lista de nodos a los que se dirige.
    '''

    def __init__(self):
        '''
        Inicializa un grafo dirigido vacío.
        '''
        self.nodos = {}

    def agregar_nodo(self, valor: Any) -> None:
        '''
        Agrega un nuevo nodo al grafo si aún no existe.

        :param valor: Valor o identificador del nodo a agregar.
        Si el nodo ya existe en el grafo, no se realiza ninguna acción.
        '''
        if valor not in self.nodos:
            self.nodos[valor] = []

    def agregar_arista(self, origen: Any, destino: Any) -> None:
        '''
        Agrega una arista dirigida del nodo 'origen' al nodo 'destino'.

        :param origen: Nodo desde el cual se origina la arista.
        :param destino: Nodo al cual se dirige la arista.
        Asegura que tanto el nodo de origen como el de destino existan y que la arista no esté duplicada.
        '''
        if origen in self.nodos and destino in self.nodos:
            if destino not in self.nodos[origen]:
                self.nodos[origen].append(destino)

    def mostrar_grafo(self) -> None:
        '''
        Imprime una representación del grafo.

        Muestra cada nodo junto con una lista de nodos a los cuales se dirige.
        Esta representación ayuda a visualizar las conexiones del grafo dirigido.
        '''
        for nodo in self.nodos:
            print(f"{nodo} -> {', '.join(map(str, self.nodos[nodo]))}")
