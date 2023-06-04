class UnionFind:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


def kruskal(graph):
    num_vertices = len(graph)
    edges = []

    # Collect all edges from the graph
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] != 0:
                edges.append(Edge(i, j, graph[i][j]))

    # Sort edges in ascending order based on weight
    edges.sort(key=lambda x: x.weight)

    # Initialize an empty MST
    mst = []

    # Create a Union-Find data structure
    uf = UnionFind(num_vertices)

    # Process each edge in the sorted order
    for edge in edges:
        src = edge.src
        dest = edge.dest

        # Check if adding the edge creates a cycle
        if uf.find(src) != uf.find(dest):
            uf.union(src, dest)
            mst.append(edge)

    return mst


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst = kruskal(graph)

# Print the minimum spanning tree
for edge in mst:
    print(f"({edge.src} - {edge.dest}): {edge.weight}")
