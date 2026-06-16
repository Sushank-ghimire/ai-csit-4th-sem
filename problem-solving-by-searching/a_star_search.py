import heapq


def print_graph(graph):
    print("Graph Representation: ")
    for node in graph:
        print(f"{node} -> {graph[node]}")


def reconstruct_path(parent, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]


def astar(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start))

    g_cost = {node: float("inf") for node in graph}
    g_cost[start] = 0

    parent = {node: None for node in graph}
    closed_set = set()

    print("\n A* Search ")
    while open_list:
        f, curr_g, curr = heapq.heappop(open_list)
        print(f"Expanding Node: {curr}")
        print(f"f(n)={curr_g}, h(n)={heuristic[curr]}, f(n)={f}")

        if curr == goal:
            path = reconstruct_path(parent, goal)
            return path, g_cost[goal]

        closed_set.add(curr)
        for neighbor, cost in graph[curr]:
            if neighbor in closed_set:
                continue
            tentative_g = g_cost[curr] + cost
            if tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                parent[neighbor] = curr
                heapq.heappush(open_list, (f_cost, tentative_g, neighbor))
                print(
                    f"Updated {neighbor}"
                    f"g={tentative_g}, "
                    f"h={heuristic[neighbor]}, "
                    f"h={f_cost}, "
                )
    return None, None


graph = {
    "A": [("B", 4), ("C", 3)],
    "B": [("D", 5), ("E", 2)],
    "C": [("E", 4), ("F", 6)],
    "D": [("G", 7)],
    "E": [("G", 3)],
    "F": [("G", 2)],
    "G": [],
}

heuristic = {"A": 10, "B": 7, "C": 6, "D": 6, "E": 2, "F": 1, "G": 0}

print_graph(graph)

start = str(input("Enter start node: ")).upper()
goal = str(input("Enter goal node: ")).upper()

if start not in graph or goal not in graph:
    print("Invalid node")
else:
    path, cost = astar(graph, heuristic, start, goal)
    if path:
        print("\nShortest Path: ")
        print(" -> ".join(path))
        print("Total Cost = ", cost)
    else:
        print("No path found")
