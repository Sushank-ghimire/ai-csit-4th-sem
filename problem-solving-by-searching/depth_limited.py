def depth_limited_search(graph, current, goal, limit, depth=0, path=None):
    if path is None:
        path = []

    path.append(current)
    if current == goal:
        return path
    if depth == limit:
        path.pop()
        return None
    for neighbor in graph.get(current, []):
        if neighbor not in path:
            result = depth_limited_search(graph, neighbor, goal, limit, depth + 1, path)
            if result is not None:
                return result
    path.pop()
    return None


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": [],
}

for key in graph.keys():
    print(f"{key}: {graph[key]}")

start = str(input("Enter start node: ")).upper()
goal = str(input("Enter goal node: ")).upper()
limit = int(input("Enter depth limit: "))

if start not in graph or goal not in graph:
    print("Invalid node")
    exit()

result = depth_limited_search(graph, start, goal, limit)

if result:
    print(f"Path found: {' -> '.join(result)}")
else:
    print("No solution within depth limit")
