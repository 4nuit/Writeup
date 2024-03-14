import requests
import json
import heapq

# Définition des coûts entre les terrains
terrain_costs = {
    ('P', 'P'): 1,
    ('C', 'G'): 1,
    ('G', 'C'): 1,
    ('M', 'P'): 5,
    ('P', 'M'): 2,
    ('P', 'S'): 2,
    ('S', 'P'): 5,
    ('M', 'S'): 7,
    ('S', 'M'): 5,
    ('M', 'R'): 10,
    ('R', 'M'): 8
}

def read_map(json_data):
    graph = {}
    player_position = tuple(json_data["player"]["position"])
    tiles = json_data["tiles"]
    width = json_data["width"]
    height = json_data["height"]

    # Parcourir chaque case de la carte
    for x in range(width):
        for y in range(height):
            pos = (x, y)
            terrain = tiles[str(pos)]["terrain"]
            neighbors = []

            # Vérifier les cases adjacentes
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # Calculer la position de la case adjacente
                new_x, new_y = x + dx, y + dy
                new_pos = (new_x, new_y)
                # Vérifier si la case adjacente est valide
                if 0 <= new_x < width and 0 <= new_y < height:
                    neighbor_terrain = tiles[str(new_pos)]["terrain"]
                    if neighbor_terrain != "E" and terrain != "E":
                        neighbors.append(new_pos)

            # Ajouter les voisins uniquement si la case n'est pas vide
            if terrain != "E":
                graph[pos] = neighbors

    return graph, player_position

# Fonction pour calculer le coût entre deux terrains
def calculate_cost(terrain1, terrain2):
    terrain_pair = (terrain1, terrain2)
    if terrain_pair in terrain_costs:
        return terrain_costs[terrain_pair]
    else:
        return float('inf')

# Fonction pour trouver le chemin optimal
def find_optimal_path(graph, start, goal):
    queue = [(0, start)]
    came_from = {}
    costs = {node: float("inf") for node in graph}

    costs[start] = 0

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_node == goal:
            break

        for next_node in graph[current_node]:
            new_cost = costs[current_node] + calculate_cost(graph[current_node], graph[next_node])
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
                came_from[next_node] = current_node

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Demander la carte au serveur
r = requests.post("http://83.136.249.159:50236/map")
json_data = json.loads(r.text)

# Lire la carte
graph, player_position = read_map(json_data)

# Trouver le chemin optimal vers chaque arme
for weapon_pos in [(3, 7), (6, 0)]:
    path = find_optimal_path(graph, player_position, weapon_pos)
    print("Chemin optimal vers l'arme à la position", weapon_pos, ":", path)
