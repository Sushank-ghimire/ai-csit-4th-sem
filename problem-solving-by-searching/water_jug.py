from collections import deque

def water_jug(a, b, target):
  q = deque([((0, 0), [])])
  visited = set()

  while q:
    (x, y), path = q.popleft()
    if (x, y) in visited:
      continue
    visited.add((x, y))
    path = path + [(x, y)]
    if x == target or y == target:
      return path

    states = [
      (a, y), (x, b), #Fill jugs
      (0, y), (x, 0), #Empty jugs
      (x - min(x, b-y), y + min(x, b-y)), # A -> B
      (x + min(y, a-x), y - min(y, a-x)), # A -> B
    ]

    for s in states:
      if s not in visited:
        q.append((s, path))
  return None

a = int(input("Enter capcacity of jug 1: "))
b = int(input("Enter capcacity of jug 2: "))

target = int(input("Enter target amount: "))
result = water_jug(a, b, target)

if result:
  print("\nSolution: ")
  for state in result:
    print(state)
else:
  print("No solution exists.")
