from .depth_limited import depth_limited_search, graph


def iterative_deepening_search(graph, start, goal, max_depth=50):

    for depth in range(max_depth + 1):
        print(f"Searching with depth limit = {depth}")

        result = depth_limited_search(graph, start, goal, depth)

        if result:
            return result

    return None


for key in graph.keys():
    print(f"{key}: {graph[key]}")

start = str(input("Enter start node: ")).upper()
goal = str(input("Enter goal node: ")).upper()

if start not in graph or goal not in graph:
    print("Invalid node")
    exit()
path = iterative_deepening_search(graph, start, goal)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("Goal not found")
