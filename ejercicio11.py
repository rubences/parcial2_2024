class Room:
    def __init__(self, id, value, cost):
        self.id = id
        self.value = value
        self.cost = cost
        self.connections = []

    def add_connection(self, room):
        self.connections.append(room)

def find_best_path(current_room, life_points, current_value, visited, path, best_path, best_value):
    if life_points <= 0:
        return best_path, best_value

    if current_room.id == 4:  # Room with the lightsaber
        if current_value > best_value:
            best_value = current_value
            best_path = path[:]
        return best_path, best_value

    for next_room in current_room.connections:
        if next_room.id not in visited:
            visited.add(next_room.id)
            path.append(next_room.id)
            best_path, best_value = find_best_path(next_room, life_points - next_room.cost, current_value + next_room.value, visited, path, best_path, best_value)
            path.pop()
            visited.remove(next_room.id)

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

# Define connections
rooms[1].add_connection(rooms[2])
rooms[1].add_connection(rooms[3])
rooms[2].add_connection(rooms[4])
rooms[2].add_connection(rooms[5])
rooms[3].add_connection(rooms[5])
rooms[5].add_connection(rooms[6])
rooms[6].add_connection(rooms[4])

# Initialize variables
initial_life_points = 100
initial_value = 0
initial_room = rooms[1]
visited = set([initial_room.id])
path = [initial_room.id]
best_path, best_value = find_best_path(initial_room, initial_life_points, initial_value, visited, path, [], 0)

print(f"Best path: {best_path}")
print(f"Best value: {best_value}")