from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            neighbors = graph[node]
            queue.extend(neighbors)


def dfs(graph, start_node):
    visited = set()

    def dfs_helper(node):
        visited.add(node)
        print(node)
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start_node)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS:")
bfs(graph, 'A')

print("DFS:")
dfs(graph, 'A')
