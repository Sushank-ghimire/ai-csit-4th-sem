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


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alpha_beta(
    depth=0,
    node_index=0,
    maximizing_player=True,
    values=values,
    alpha=float("-inf"),
    beta=float("inf"),
)

print("Optimal value:", result)
