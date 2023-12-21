class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    mst = []
    edges = sorted(graph['edges'], key=lambda edge: edge[2])
    ds = DisjointSet(graph['vertices'])

    for edge in edges:
        vertex1, vertex2, weight = edge
        if ds.find(vertex1) != ds.find(vertex2):
            ds.union(vertex1, vertex2)
            mst.append(edge)

    return mst

# Ejemplo de uso
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        ('A', 'B', 1), ('A', 'C', 3), ('B', 'C', 3),
        ('B', 'D', 6), ('B', 'E', 4), ('C', 'E', 2),
        ('D', 'E', 5), ('E', 'F', 7)
    ]
}

mst = kruskal(graph)
print("Árbol de Cobertura Mínima:", mst)
