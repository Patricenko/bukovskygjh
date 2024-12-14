def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    previous = [-1] * n
    used_graph = [[0] * n for _ in range(n)]

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
                    previous[neighbor] = current

    for i in range(n):
        if previous[i] != -1:
            used_graph[i][previous[i]] = graph[i][previous[i]]
            used_graph[previous[i]][i] = graph[previous[i]][i]

    return used_graph, distances

graph = [
    [0, 5, 2, 0, 0],
    [5, 0, 1, 1, 0],
    [2, 1, 0, 2, 7],
    [0, 1, 2, 0, 4],
    [0, 0, 7, 4, 0]
]

start_node = 0
dijkstra = dijkstra(graph, start_node)
print("Updated graph with used paths only:")
for row in dijkstra[0]:
    print(row)
print(f"Paths: {dijkstra[1]}")
