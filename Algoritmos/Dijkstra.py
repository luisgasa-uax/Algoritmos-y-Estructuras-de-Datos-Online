import heapq

def dijkstra(graph, start):
    # Inicializa distancias con infinito
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Cola de prioridad
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Verificar si encontramos una ruta más corta
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Actualizar la distancia si se encuentra una más corta
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Grafo de ejemplo
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Los caminos más cortos desde {start_node}: {shortest_paths}")
