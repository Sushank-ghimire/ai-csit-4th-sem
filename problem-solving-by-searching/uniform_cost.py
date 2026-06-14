import heapq


def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]
    # Dictionary to store the cost of the shortest path to each node
    visited = {start: (0, None)}

    while priority_queue:
        # Pop the node with the lowest cost from the priority queue
        curr_cost, curr_node = heapq.heappop(priority_queue)

        if curr_node == goal:
            return curr_cost, reconstruct_path(visited, goal)
        # Exploring the neighbours
        for neighbor, cost in graph[curr_node]:
            total_cost = curr_cost + cost
            if neighbor not in visited or total_cost < visited[neighbor][0]:
                visited[neighbor] = (total_cost, curr_node)
                heapq.heappush(priority_queue, (total_cost, neighbor))

    return None


def reconstruct_path(visited, goal):
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = visited[curr][1]  # Get the parent node
    path.reverse()
    return path


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 1), ("E", 3)],
    "C": [("F", 5)],
    "D": [("G", 2)],
    "E": [("G", 1)],
    "F": [("G", 2)],
    "G": [],
}


print("Graph & Costs")
for key in graph.keys():
    print(f"{key}: {graph[key]}")

start_node = str(input("Enter start node: ")).upper()
goal_node = str(input("Enter goal node: ")).upper()

if start_node not in graph.keys() or goal_node not in graph.keys():
    print("Invalid node")
else:
    result = uniform_cost_search(graph, start_node, goal_node)
    if result:
        total_cost, path = result
        print(f"The cost of the path is {total_cost}")
        print(f"The path with least cost is \n {' -> '.join(path)}")
