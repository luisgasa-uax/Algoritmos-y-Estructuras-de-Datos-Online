from typing import Any, Tuple, List, Set, Deque, Dict, Callable
from collections import deque
import heapq

class GrafoDirigidoPonderadoOnline: 
    def __init__(self) -> None:
        self.grafo = {}  # diccionario para almacenar el grafo


    def add_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []


    def add_arista(self, origen, destino, peso):
        if origen not in self.grafo:
            self.add_nodo(origen)
        if destino not in self.grafo:
            self.add_nodo(destino)
        
        self.grafo[origen].append((destino, peso))
        
        # si no es dirigido, debemos añadir la relación a ambos nodos
        # self.grafo[destino].append((origen, peso))
    
    def display_grafo(self):
        for nodo in self.grafo:
            for arista in self.grafo[nodo]:   # self.grafo[nodo]
                print(f"{nodo} -> {arista[0]} [peso: {arista[1]}]")
    
    
    def get_neighbors(self, nodo):   # vecinos o nodos adyacentes
        return self.grafo.get(nodo, [])
    
    def delete_nodo (self, nodo: Any):
        if nodo not in self.grafo:
            raise ValueError("El nodo no existe en el grafo.")

        #dirigido
        for origen in self.grafo: 
            self.grafo[origen] = [arista for arista in self.grafo[origen] if arista[0] != nodo ]

        '''
        # si no fuera dirigido
        for vecino in self.grafo[nodo][0]:
            for retorno in self.grafo[vecino]:
                if retorno[0] == nodo:
                    self.grafo[vecino].remove(retorno)
        '''

        del self.grafo[nodo]

    def exists(self, nodo): 
        return nodo in self.grafo
    
    def exists_arista(self, origen, destino):
        return any(arista[0] == destino for arista in self.grafo.get(origen, []))
        '''
        if destino in self.grafo[origen][0]:
            return True
        else:
            return False
        '''
    
    def grado_nodo(self, nodo ): 
        return self.grado_entrada_nodo(nodo) + self.grado_salida_nodo(nodo)

    def grado_salida_nodo(self, nodo ): 
        grado_salida = len(self.grafo[nodo])

        return grado_salida
    
    def grado_entrada_nodo(self, nodo):
        grado_entrada = sum( nodo in  [destino for destino, _ in self.grafo[origen]] for origen in self.grafo)
        return grado_entrada
    




    def dfs(self, nodo_inicial):
        # Recorre en profundidad
        visitados = set()   # Conjunto de datos no repetidos
        recorrido = []      # Lista almacenar el orden de los nodos visitados

        def dfs_recursivo(nodo):
            if nodo not in visitados:
                visitados.add(nodo)
                recorrido.append(nodo)
                for vecino, _ in self.grafo.get(nodo, []):
                    dfs_recursivo(vecino)
        
        dfs_recursivo(nodo_inicial)
        return recorrido

    def bfs(self, nodo_inicial):
        # recorre en amplitud
        visitados = set()
        cola: Deque[Any] = deque()      # almacena los nodos a vistar
        recorrido = []
        
        cola.append(nodo_inicial)
        visitados.add(nodo_inicial)

        while cola: 
            nodo_actual = cola.popleft()
            recorrido.append(nodo_actual)

            for vecino, _ in self.grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
        return recorrido

    def camino_mas_corto_dijkstra(self, origen, destino):
        """Devuelve la distancia mas corta entre dos nodos"""
        distancias: Dict[Any, float] = {nodo: float('inf') for nodo in self.grafo}
        distancias[origen] = 0
        previos : Dict[Any, float] = {nodo: None for nodo in self.grafo}
        cola = [(0, origen)]

        while cola: 
            distancia_actual, nodo_actual = heapq.heappop(cola)
            if nodo_actual == destino:
                camino = []
                while nodo_actual is not None:
                    camino.insert(0, nodo_actual)
                    nodo_actual = previos[nodo_actual]
                return camino, distancia_actual

            if distancia_actual > distancias[nodo_actual]:
                continue

            for vecino, peso in self.grafo.get(nodo_actual, []):
                distancia = distancia_actual + peso
                if distancia < distancia_actual:
                    distancias[vecino] = distancia
                    previos[vecino] = nodo_actual
                    heapq.heappush(cola, (distancia, vecino))
            return camino
        return [], float('inf') # No hay camino

    def are_connected( self, origen, destino ):
        """Comprueba que exista, al menos un camino entre dos nodos """
        visitados = set()

        def dfs( nodo_actual ):
            if nodo_actual == destino: 
                return True
            visitados.add(nodo_actual)
            for vecino in self.grafo.get(nodo_actual, []):
                if vecino not in visitados and dfs(vecino):
                    return True
            return False
        
        return dfs(origen) if origen in self.grafo else False
    
    def a_star(self, origen, destino, heuristica: Callable[[Any, Any], float]): 
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (0, origen))
        costos = {origen: 0}
        predecesores = {origen:None}

        while cola_prioridad:
            costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == destino:
                camino = []
                while nodo_actual: 
                    camino.insert(0, nodo_actual)
                    nodo_actual = predecesores[nodo_actual]
                return camino, costo_actual
            
            for vecino, peso in self.grafo.get(nodo_actual, []):
                nuevo_costo = costos[nodo_actual] + peso
                if vecino not in costos or nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(vecino, destino)
                    heapq.heappush(cola_prioridad, (prioridad, vecino))
                    predecesores[vecino] = nodo_actual
        
        return [], float('inf') # No hay camino
    


# Ejemplo de uso
grafo = GrafoDirigidoPonderadoOnline()
grafo.add_arista('A', 'B', 5)
grafo.add_arista('A', 'C', 3)
grafo.add_arista('B', 'C', 4)
grafo.add_arista('C', 'B', 2)

grafo.display_grafo()

'''
print("A" + str(grafo.get_neighbors('A')))
print("B" + str(grafo.get_neighbors('B')))
print("C" + str(grafo.get_neighbors('C')))


print("Borramos B")
#grafo.delete_nodo('B')

grafo.display_grafo()

print("A" + str(grafo.get_neighbors('A')))
print("C" + str(grafo.get_neighbors('C')))

print(grafo.exists('X'))

print("         Existe arista")
print(grafo.exists_arista('A', 'C'))
print(grafo.exists_arista('A', 'A'))
print(grafo.exists_arista('C', 'A'))
print(" Grado Nodo")
print( grafo.grado_nodo('B'))
print( grafo.grado_entrada_nodo('B'))
print( grafo.grado_salida_nodo('B'))
'''

print('DFS: ' +  str(grafo.dfs('B')))
print('BFS: ' +  str(grafo.bfs('B')))

print(grafo.camino_mas_corto_dijkstra('A','C'))