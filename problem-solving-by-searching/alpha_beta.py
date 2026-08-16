import math

def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        best = float("-inf")

        for i in range(2):
            value = alpha_beta(
                depth + 1, node_index * 2 + i, False, values, alpha, beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float("inf")

        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


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

if player == "MAX" or player == "MIN":
  result = alpha_beta(
    depth=max_depth,
    node_index=0,
    maximizing_player=player == "MAX",
    values=values,
    alpha=float("-inf"),
    beta=float("inf")
  )
else:
  print("Invalid player! Enter MAX or MIN.")
  exit()

print("\nLeaf Nodes:", values)
print("Optimal value:", result)
