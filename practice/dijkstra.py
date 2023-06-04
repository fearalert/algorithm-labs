import heapq
from collections import defaultdict

def dijkstra(graph, start):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    visited = set()
    min_heap = [(0, start)]
    
    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)
        if curr_dist > distances[curr_node]:
            continue
        
        visited.add(curr_node)
        
        for neighbor, edge_weight in graph[curr_node]:
            new_dist = distances[curr_node] + edge_weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))
    
    return distances


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

start_node = 'A'
distances = dijkstra(graph, start_node)

# Print the shortest distances from the start node to all other nodes
for node, dist in distances.items():
    print(f"Shortest distance from {start_node} to {node}: {dist}")
