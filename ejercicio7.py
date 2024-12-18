import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

# Create the graph
graph = Graph()
for node in ["Gondor", "Rohan", "Isengard", "Rivendel", "Mirkwood"]:
    graph.add_node(node)

graph.add_edge("Gondor", "Rohan", 3)
graph.add_edge("Rohan", "Isengard", 2)
graph.add_edge("Isengard", "Rivendel", 5)
graph.add_edge("Rivendel", "Mirkwood", 4)

# Find the shortest path from Gondor to Mirkwood
distances, paths = dijkstra(graph, "Gondor")
print("Shortest path from Gondor to Mirkwood:", distances["Mirkwood"])