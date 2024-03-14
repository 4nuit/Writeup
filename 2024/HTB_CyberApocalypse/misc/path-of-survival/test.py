import heapq, json, requests

def create_graph(tiles, width, height):
    graph = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, bas, gauche, droite

    for (x, y), tile_info in tiles.items():
        neighbors = {}
        for dx, dy in directions:
            neighbor_pos = (x + dx, y + dy)
            if 0 <= neighbor_pos[0] < width and 0 <= neighbor_pos[1] < height and neighbor_pos in tiles:
                neighbors[neighbor_pos] = cost((dx, dy), tile_info, tiles[neighbor_pos])
        graph[(x, y)] = neighbors
    
    return graph

def cost(direction, source, destination):
    """
    Calcule le coût de déplacement d'une tuile source à une tuile destination en tenant compte de la direction.

    Args:
        direction (tuple): Le tuple de direction (dx, dy).
        source (dict): Informations sur la tuile source, y compris le terrain.
        destination (dict): Informations sur la tuile destination, y compris le terrain.

    Returns:
        int: Le coût de déplacement.
    """
    dx, dy = direction
    source_terrain = source['terrain']
    destination_terrain = destination['terrain']

    # Exemple simplifié de logique de coût. À ajuster selon vos règles spécifiques.
    base_cost = {"P": 1, "E": 2, "M": 3, "S": 5}  # Coût de base par terrain
    direction_modifier = 1.5 if dx != 0 and dy != 0 else 1  # Modifier si diagonale

    # Exemple de logique pour monter/descendre une colline
    if source_terrain == "M" and destination_terrain == "P":
        return base_cost["M"] * 2 * direction_modifier  # Plus coûteux de descendre
    elif source_terrain == "P" and destination_terrain == "M":
        return base_cost["M"] * direction_modifier  # Moins coûteux de monter

    # Coût par défaut
    return base_cost[destination_terrain] * direction_modifier

def dijkstra(graph, start, goal):
    queue = [(0, start)]
    distances = {start: 0}
    predecessors = {start: None}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_vertex == goal:
            break  # Chemin trouvé

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))
    
    # Reconstruire le chemin
    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    
    return path, distances[goal]

r = requests.post("http://94.237.58.224:49419/map")
data = json.loads(r.text)

tiles = {}
for pos, tile_info in data['tiles'].items():
    # Convertir la chaîne de position "(x, y)" en tuple (x, y)
    position = tuple(map(int, pos.strip("()").split(", ")))
    tiles[position] = tile_info

print(tiles)  # Affiche les données converties pour vérifier

# Utilisation des fonctions pour créer un graphe et trouver le chemin le plus court
graph = create_graph(tiles, data['width'], data['height'])
start = tuple(data['player']['position'])
# Définir la position de destination selon vos besoins
goal = (destination_x, destination_y)
path, cost = dijkstra(graph, start, goal)
print("Chemin:", path)
print("Coût:", cost)
