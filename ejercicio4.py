import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

def shortest_path(graph, start, end):
    distances = dijkstra(graph, start)
    return distances[end]

graph = {
    'Rivendel': {'Gondor': 7},
    'Gondor': {'Rohan': 5, 'Mordor': 2},
    'Rohan': {'Mordor': 10},
    'Mordor': {'Rivendel': 15}
}

start = 'Rivendel'
end = 'Rivendel'
shortest_distance = shortest_path(graph, start, end)
print(f"El camino más corto de {start} a {end} es de {shortest_distance} días.")