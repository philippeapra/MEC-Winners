import uuid
from collections import defaultdict, deque
import json
import random
import string
import os

def do_maze(filename_raw):
    tiles = []

    filename = os.path.join(os.path.dirname(__file__), "./in/", filename_raw)

    json_file = open(filename, "r")
    json_file = json.load(json_file)

    letter = "a"

    for tile in json_file.get("tiles"):
        if tile[1].get("type") == "TileType.START":
            id = "start"
        elif tile[1].get("type") == "TileType.END":
            id = "end"
        elif tile[1].get("type") == "TileType.WALL":
            continue
        else:

            # id = uuid.uuid4().__str__()
            # id = id.replace("-", "")[0:10]
            # id = "o"
            # random 10 char string
            id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        tiles.append({
            "id": id,
            "a": tile[0].get("a"),
            "c": tile[0].get("c"),
            "r": tile[0].get("r")
        });

    links = []

    for tile in tiles:
        for neighbor in tiles:
            if tile.get("id") != neighbor.get("id"):
                if tile.get("a") == neighbor.get("a") and tile.get("c") == neighbor.get("c"):
                    if tile.get("r") == neighbor.get("r") - 1 or tile.get("r") == neighbor.get("r") + 1:
                        links.append((tile.get("id"), neighbor.get("id")))
                if tile.get("r") == neighbor.get("r") and tile.get("c") == neighbor.get("c"):
                    if tile.get("a") == neighbor.get("a") - 1 or tile.get("a") == neighbor.get("a") + 1:
                        links.append((tile.get("id"), neighbor.get("id")))
                if tile.get("r") == neighbor.get("r") and tile.get("a") == neighbor.get("a"):
                    if tile.get("c") == neighbor.get("c") - 1 or tile.get("c") == neighbor.get("c") + 1:
                        links.append((tile.get("id"), neighbor.get("id")))

                print(tile.get("id"), neighbor.get("id"))

    print(json.dumps(links, indent=4))

    def find_shortest_path(links, start_node, end_node):
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        for link in links:
            node_a, node_b = link
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)  # Assuming the graph is undirected

        # Initialize the BFS queue with the start node and a visited set
        queue = deque([(start_node, [start_node])])
        visited = set()

        while queue:
            current_node, path = queue.popleft()

            if current_node == end_node:
                return path  # Found the shortest path

            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

        return None  # No path from start_node to end_node

    start_node = "start"
    end_node = "end"
    shortest_path = find_shortest_path(links, start_node, end_node)

    shortest_path_nodes = []

    for node in shortest_path:
        for tile in tiles:
            if node == tile.get("id"):
                shortest_path_nodes.append((tile.get("a"), tile.get("r"), tile.get("c")))

    if shortest_path:
        print("Shortest path:", shortest_path_nodes)
    else:
        print("No path found from {} to {}".format(start_node, end_node))


    # make sure the out directory exists, and file too
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "./out")):
        os.makedirs(os.path.join(os.path.dirname(__file__), "./out"))
    # create file and then add
    with open(os.path.join(os.path.dirname(__file__), "./out/"+filename_raw.replace('.json', '.txt')), "w") as f:
        # put each tile on a new line
        for tile in shortest_path_nodes:
            f.write(json.dumps(tile) + "\n")




