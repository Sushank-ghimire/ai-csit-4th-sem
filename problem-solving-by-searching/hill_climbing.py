import numpy as np


def objective(x):
    return -(x[0] ** 2) + 3


def generate_neighbors(x, step_size=0.1):
    return [np.array([x[0] + step_size]), np.array([x[0] - step_size])]


def hill_climbing(objective, initial, iter=100, step_size=0.10):
    curr = np.array([initial])
    curr_eval = objective(curr)

    for i in range(iter):
        neighbors = generate_neighbors(curr, step_size)
        neighbor_evals = [objective(n) for n in neighbors]

        best_idx = np.argmax(neighbor_evals)
        if neighbor_evals[best_idx] > curr_eval:
            curr = neighbors[best_idx]
            curr_eval = neighbor_evals[best_idx]
            print(f"Step {i + 1}: x = {curr[0]:.4f}, f(x) = {curr_eval:.4f}")
        else:
            print("No better neighbors found. Algorithm converged.")
            break
    return curr, curr_eval


initial_guess = float(input("Enter your initial guess: "))
iterations = int(input("Enter maximum iterations: "))
step_size = float(input("Enter step size: "))

solution, value = hill_climbing(objective, initial_guess, iterations, step_size)
print(f"\nBest solution x = {solution[0]:.4f}, f(x) = {value:.4f}")

"""
Program without using the numpy
def objective(x):
    return -(x ** 2) + 3


def generate_neighbors(x, step_size=0.1):
    return [x + step_size, x - step_size]


def hill_climbing(objective, initial, iterations=100, step_size=0.1):
    current = initial

    for _ in range(iterations):
        neighbors = generate_neighbors(current, step_size)

        best_neighbor = max(neighbors, key=objective)

        if objective(best_neighbor) <= objective(current):
            break

        current = best_neighbor

    return current, objective(current)


best_x, best_value = hill_climbing(objective, initial=2.0)

print("Best x:", best_x)
print("Best value:", best_value)
"""
