from collections import deque

grid = [
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
]

print("Grid (0 = Free, 1 = Obstacle)")
for row in grid:
    print(*row)

start = tuple(map(int, input("Enter start (row col): ").split()))
goal = tuple(map(int, input("Enter goal (row col): ").split()))

queue = deque([(start, [start])])
visited = {start}
traversal = []

while queue:
    current, path = queue.popleft()
    traversal.append(current)

    if current == goal:
        print("Traversal Order:", traversal)
        print("Path Found:", path)
        break

    row, col = current

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc

        if (
            0 <= nr < len(grid)
            and 0 <= nc < len(grid[0])
            and grid[nr][nc] == 0
            and (nr, nc) not in visited
        ):
            visited.add((nr, nc))
            queue.append(((nr, nc), path + [(nr, nc)]))

else:
    print("No Path Found")
