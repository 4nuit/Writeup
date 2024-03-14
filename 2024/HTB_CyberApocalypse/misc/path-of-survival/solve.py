import requests
import json
from queue import PriorityQueue

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

class Node:
    def __init__(self, x, y, terrain):
        self.x = x
        self.y = y
        self.terrain = terrain

    def __eq__(self, other):
        return isinstance(other, Node) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        # Comparaison basée sur les coûts des nœuds
        return self.cost < other.cost


def read_map(json_data):
    graph = {}
    player_position = tuple(json_data["player"]["position"])
    tiles = json_data["tiles"]
    width = json_data["width"]
    height = json_data["height"]

    for x in range(width):
        for y in range(height):
            pos = (x, y)
            terrain = tiles[str(pos)]["terrain"]
            if terrain != "E":
                node = Node(x, y, terrain)
                neighbors = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = x + dx, y + dy
                    new_pos = (new_x, new_y)
                    if 0 <= new_x < width and 0 <= new_y < height:
                        neighbor_terrain = tiles[str(new_pos)]["terrain"]
                        if neighbor_terrain != "E":
                            neighbors.append(Node(new_x, new_y, neighbor_terrain))
                graph[node] = neighbors

    return graph, player_position

def calculate_cost(node1, node2):
    terrain_pair = (node1.terrain, node2.terrain)
    if terrain_pair in terrain_costs:
        return terrain_costs[terrain_pair]
    else:
        return float('inf')

def find_optimal_path(graph, start, goal):
    queue = PriorityQueue()
    start.cost = 0  # Mettre le coût du nœud de départ à 0
    queue.put(start)
    came_from = {}
    costs = {node: float("inf") for node in graph}

    costs[start] = 0

    while not queue.empty():
        current = queue.get()

        if current == goal:
            break

        for next_node_key in graph[current]:
            next_node = next_node_key  # Récupérer le nœud associé à la clé
            new_cost = costs[current] + calculate_cost(current, next_node)
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                next_node.cost = new_cost  # Mettre à jour le coût du nœud
                queue.put(next_node)
                came_from[next_node] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path



r = requests.post("http://94.237.58.224:49419/map")
json_data = json.loads(r.text)

graph, player_position = read_map(json_data)

weapon_positions = []
for pos, tile_info in json_data["tiles"].items():
    if tile_info["has_weapon"]:
        x, y = eval(pos)
        terrain = tile_info["terrain"]
        weapon_positions.append((x, y, terrain))

print("Positions des armes :")
for pos in weapon_positions:
    print(pos)

for weapon_pos in weapon_positions:
    graph, player_position = read_map(json_data)
    weapon_node = Node(*weapon_pos)
    print("Position du joueur:", player_position)
    print("Position de l'arme:", weapon_pos)
    print("Graphe:")
    for node, neighbors in graph.items():
        neighbor_positions = [(neighbor.x, neighbor.y) for neighbor in neighbors]
        print(f"Node: {node.x}, {node.y}, Terrain: {node.terrain}, Neighbors: {neighbor_positions}")

    print(type(graph),weapon_node)
    path = find_optimal_path(graph, Node(*player_position, json_data["tiles"][str(player_position)]["terrain"]), weapon_node)
    print("Chemin optimal vers l'arme à la position", weapon_pos, ":", path)
