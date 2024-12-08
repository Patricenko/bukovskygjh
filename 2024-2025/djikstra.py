def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n

    for _ in range(n):
        min_distance = float('inf')
        current = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                current = i
        
        if current == -1:
            break
        
        visited[current] = True
        
        for neighbor in range(n):
            if graph[current][neighbor] > 0 and not visited[neighbor]:
                new_distance = distances[current] + graph[current][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 6],
    [4, 2, 0, 3],
    [0, 6, 3, 0]
]

start_node = 0
result = dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}: {result}")