graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}

start = input("Enter start node: ").upper()
end = input("Enter end node: ").upper()

if start not in graph or end not in graph:
    print("Invalid node")
else:
    visited = set()
    traversal_order = []

    def dfs(node, path):
        visited.add(node)
        traversal_order.append(node)
        path.append(node)

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dfs(neighbor, path.copy())
                if result:
                    return result

        return None

    path = dfs(start, [])

    print("Traversal Order:", traversal_order)

    if path:
        print("Path Found:", " -> ".join(path))
    else:
        print(f"No path exists from {start} to {end}")
