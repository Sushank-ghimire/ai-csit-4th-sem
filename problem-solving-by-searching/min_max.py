import math

def minimax(depth, node_idx, is_max, values, max_depth):
  # Base case: If leaf node is reached
  if depth == max_depth:
    return values[node_idx]
  if is_max:
    left = minimax(depth+1, node_idx * 2, False, values, max_depth)
    right = minimax(depth+1, node_idx * 2 + 1, False, values, max_depth)
    return max(left, right)
  else:
    left = minimax(depth+1, node_idx * 2, True, values, max_depth)
    right = minimax(depth+1, node_idx * 2 + 1, True, values, max_depth)
    return max(left, right)

# Check if n is power of 2
n = int(input("Enter number of leaf nodes (power of 2): "))

if n<= 0 or (n & (n-1)) != 0:
  print("Error: number of leaf nodes must be a power of 2")
  exit()

print(f"Enter {n} leaf node values: ")
values = []

for i in range(n):
  value = int(input(f"Leaf Node {i+1}: "))
  values.append(value)

player = input("Enter starting player (MAX/MIN): ").strip().upper()

max_depth = int(math.log2(n))

if player == "MAX":
  result = minimax(0, 0, True, values, max_depth)
elif player == "MIN":
  result = minimax(0, 0, False, values, max_depth)
else:
  print("Invalid player! Please enter MAX or MIN.")
  exit()

print("\nLeaf Nodes: ", values)
print("Optimal Value: ", result)
