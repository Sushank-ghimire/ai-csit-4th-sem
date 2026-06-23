from collections import deque


def expand_frontier(graph, queue, visited, back_visited):
    current = queue.popleft()
    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            visited[neighbor] = current
            queue.append(neighbor)

            if neighbor in back_visited:
                return neighbor
    return None


def construct_path(meeting, forward_visit, backward_visit):
    # start -> meeting
    path1 = []
    node = meeting
    while node is not None:
        path1.append(node)
        node = forward_visit[node]
    path1.reverse()

    # meeting -> goal
    path2 = []
    node = backward_visit[meeting]
    while node is not None:
        path2.append(node)
        node = backward_visit[node]
    return path1 + path2


def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]
    forward_queue = deque([start])
    backward_queue = deque([goal])

    forward_visit = {start: None}
    backward_visit = {goal: None}

    while forward_queue and backward_queue:
        # Forward
        meeting = expand_frontier(graph, forward_queue, forward_visit, backward_visit)
        if meeting:
            return construct_path(meeting, forward_visit, backward_visit)
        # Backward
        meeting = expand_frontier(graph, backward_queue, backward_visit, forward_visit)
        if meeting:
            return construct_path(meeting, forward_visit, backward_visit)
    return None


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "H"],
    "F": ["C", "G"],
    "G": ["F", "H"],
    "H": ["E", "G"],
}

for key in graph.keys():
    print(f"{key}: {graph[key]}")

start = str(input("Enter start node: ")).upper()
goal = str(input("Enter goal node: ")).upper()

if start not in graph or goal not in graph:
    print("Invalid node")
    exit()

result = bidirectional_search(graph, start, goal)

if result:
    print(f"Path found: {' -> '.join(result)}")
else:
    print("No solution found")
