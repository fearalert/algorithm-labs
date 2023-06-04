from collections import defaultdict

def ford_fulkerson(graph, source, sink):
    def dfs(node, min_capacity):
        visited.add(node)

        if node == sink:
            return min_capacity

        for next_node, capacity in graph[node]:
            residual_capacity = capacity - flow[node, next_node]

            if residual_capacity > 0 and next_node not in visited:
                min_capacity = min(min_capacity, residual_capacity)
                result = dfs(next_node, min_capacity)

                if result > 0:
                    flow[node, next_node] += result
                    flow[next_node, node] -= result
                    return result

        return 0

    flow = defaultdict(int)
    max_flow = 0

    while True:
        visited = set()
        augmenting_path = dfs(source, float('inf'))

        if augmenting_path == 0:
            break

        max_flow += augmenting_path

    return max_flow

graph = {
    's': [('v1', 10), ('v2', 5)],
    'v1': [('v2', 6), ('v3', 3)],
    'v2': [('v1', 4), ('v4', 2)],
    'v3': [('v4', 6)],
    'v4': [('sink', 8)],
    'sink': []
}

source = 's'
sink = 'sink'

max_flow = ford_fulkerson(graph, source, sink)
print("Max Flow:", max_flow)
