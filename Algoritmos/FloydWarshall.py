def floyd_warshall(graph):
    # Número de vértices en el grafo
    V = len(graph)

    # Inicializar la matriz de distancias
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Aplicar Floyd-Warshall
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

# Grafo de ejemplo como matriz de adyacencia
graph = [[0, 5, float('inf'), 10],
         [float('inf'), 0, 3, float('inf')],
         [float('inf'), float('inf'), 0, 1],
         [float('inf'), float('inf'), float('inf'), 0]]

# Llamada al algoritmo
distances = floyd_warshall(graph)

print("Matriz de distancias más cortas:")
for row in distances:
    print(row)
