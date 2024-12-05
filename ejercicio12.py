import heapq

class Room:
    def __init__(self, id, value, cost):
        self.id = id
        self.value = value
        self.cost = cost
        self.neighbors = []

    def add_neighbor(self, neighbor, path_cost):
        self.neighbors.append((neighbor, path_cost))

def dijkstra(start_room, end_room, max_life):
    pq = [(0, 0, start_room, [])]  # (total_cost, total_value, current_room, path)
    visited = set()

    while pq:
        total_cost, total_value, current_room, path = heapq.heappop(pq)

        if current_room.id in visited:
            continue

        visited.add(current_room.id)
        path = path + [current_room.id]

        if current_room.id == end_room.id:
            return path, total_value

        for neighbor, path_cost in current_room.neighbors:
            if total_cost + neighbor.cost + path_cost <= max_life:
                heapq.heappush(pq, (total_cost + neighbor.cost + path_cost, total_value + neighbor.value, neighbor, path))

    return None, 0

def backtracking(current_room, end_room, max_life, current_life, current_value, path, best_path, best_value):
    if current_life <= 0:
        return best_path, best_value

    path = path + [current_room.id]

    if current_room.id == end_room.id:
        if current_value > best_value:
            return path, current_value
        return best_path, best_value

    for neighbor, path_cost in current_room.neighbors:
        if current_life - neighbor.cost - path_cost > 0:
            best_path, best_value = backtracking(neighbor, end_room, max_life, current_life - neighbor.cost - path_cost, current_value + neighbor.value, path, best_path, best_value)

    return best_path, best_value

# Define rooms
rooms = {
    1: Room(1, 0, 0),
    2: Room(2, 500, 10),
    3: Room(3, 300, 5),
    4: Room(4, 1000, 50),
    5: Room(5, 200, 15),
    6: Room(6, 400, 20)
}

# Define connections (room1, room2, path_cost)
connections = [
    (1, 2, 5),
    (1, 3, 10),
    (2, 4, 20),
    (2, 5, 25),
    (3, 6, 15),
    (5, 4, 10),
    (6, 4, 5)
]

# Add neighbors
for room1, room2, path_cost in connections:
    rooms[room1].add_neighbor(rooms[room2], path_cost)
    rooms[room2].add_neighbor(rooms[room1], path_cost)  # Assuming bidirectional paths

# Dijkstra's algorithm
start_room = rooms[1]
end_room = rooms[4]
max_life = 100

path, value = dijkstra(start_room, end_room, max_life)
print(f"Dijkstra's algorithm: Path: {path}, Value: {value}")

# Backtracking algorithm
best_path, best_value = backtracking(start_room, end_room, max_life, max_life, 0, [], [], 0)
print(f"Backtracking algorithm: Path: {best_path}, Value: {best_value}")