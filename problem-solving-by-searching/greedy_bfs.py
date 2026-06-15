import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic


def reconstruct_path(path, goal):
    curr = goal
    result_path = []
    while curr is not None:
        result_path.append(curr)
        curr = path[curr]
    result_path.reverse()
    return result_path


def greedy_bfs(graph, start, goal, heuristic, region_map):
    priority_queue = []
    heapq.heappush(priority_queue, Node(start, heuristic[start]))

    visited = set()
    path = {start: None}

    while priority_queue:
        curr_node = heapq.heappop(priority_queue).name
        if curr_node == goal:
            return reconstruct_path(path, goal)
        visited.add(curr_node)

        curr_region = region_map[curr_node]
        for neighbor in graph[curr_node]:
            if neighbor not in visited and region_map[neighbor] == curr_region:
                heapq.heappush(priority_queue, Node(neighbor, heuristic[neighbor]))
                if neighbor not in path:
                    path[neighbor] = curr_node
        for neighbor in graph[curr_node]:
            if neighbor not in visited and region_map[neighbor] != curr_region:
                heapq.heappush(priority_queue, Node(neighbor, heuristic[neighbor]))
                if neighbor not in path:
                    path[neighbor] = curr_node
    return None


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I", "J"],
    "F": ["K", "M", "E"],
    "G": ["L", "M"],
    "H": [],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
    "M": [],
}

heuristic = {
    "A": 8,
    "B": 6,
    "C": 7,
    "D": 5,
    "E": 4,
    "F": 5,
    "G": 4,
    "H": 3,
    "I": 2,
    "J": 1,
    "K": 3,
    "L": 2,
    "M": 1,
}

region_map = {
    "A": 1,
    "B": 1,
    "C": 1,
    "D": 2,
    "E": 2,
    "F": 3,
    "G": 3,
    "H": 2,
    "I": 2,
    "J": 2,
    "K": 3,
    "L": 3,
    "M": 3,
}

for key in graph.keys():
    print(f"{key}: {graph[key]}")


start_node = str(input("Enter start node: ")).upper()
goal_node = str(input("Enter goal node: ")).upper()

if start_node not in graph.keys() or goal_node not in graph.keys():
    print("Invalid node")
else:
    result_path = greedy_bfs(graph, start_node, goal_node, heuristic, region_map)
    if result_path:
        print(f"Path from {start_node} to {goal_node}: {' -> '.join(result_path)}")
