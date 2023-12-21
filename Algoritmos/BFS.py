from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")

            # Añade todos los vecinos no visitados a la cola
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'
print("BFS desde el nodo", start_node)
bfs(graph, start_node)
