import heapq

def prim(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_heap = []
    min_spanning_tree = []

    # Start with the first vertex
    start_vertex = 0
    visited[start_vertex] = True

    # Add edges from the starting vertex to the heap
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(min_heap, (weight, start_vertex, neighbor))

    # Continue adding edges until all vertices are visited
    while len(min_heap) > 0:
        weight, src, dest = heapq.heappop(min_heap)

        # Check if adding the edge creates a cycle
        if not visited[dest]:
            visited[dest] = True
            min_spanning_tree.append((src, dest, weight))

            # Add edges from the newly visited vertex to the heap
            for neighbor, weight in graph[dest]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (weight, dest, neighbor))

    return min_spanning_tree

graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)]
]

mst = prim(graph)

# Print the minimum spanning tree
for edge in mst:
    src, dest, weight = edge
    print(f"({src} - {dest}): {weight}")
