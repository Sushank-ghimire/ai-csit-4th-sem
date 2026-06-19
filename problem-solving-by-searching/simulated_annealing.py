import math
import random


def objective_function(x):
    return 10 * len(x) + sum([(xi**2 - 10 * math.cos(2 * math.pi * xi)) for xi in x])


def get_neighbor(x, step_size=0.1):
    neighbor = x[:]
    index = random.randint(0, len(x) - 1)
    neighbor[index] += random.uniform(-step_size, step_size)
    return neighbor


def simulated_annealing(objective, bounds, iter=5000, step_size=0.5, temp=100):
    best = [random.uniform(bound[0], bound[1]) for bound in bounds]
    best_eval = objective(best)
    curr, curr_eval = best, best_eval
    scores = [best_eval]

    for i in range(iter):
        t = temp / float(i + 1)
        candidate = get_neighbor(curr, step_size)
        candidate_eval = objective(candidate)

        if candidate_eval < best_eval or random.random() < math.exp(
            (curr_eval - candidate_eval) / t
        ):
            curr, curr_eval = candidate, candidate_eval
            if candidate_eval < best_eval:
                best, best_eval = candidate, candidate_eval
                scores.append(best_eval)
        if i % 100 == 0:
            print(
                f"Iteration {i}, Temperature {t:.3f}, Best Evaluation {best_eval:.3f}"
            )
    return best, best_eval, scores


bounds = [(-10, 10) for _ in range(2)]


temp = int(input("Enter initial temperature: "))
iterations = int(input("Enter maximum iterations: "))
step_size = float(input("Enter step size: "))

best, score, scores = simulated_annealing(
    objective_function, bounds, iterations, step_size, temp
)

print(f"Best Solution: {[round(x, 3) for x in best]}")
print(f"Best Score: {score:.3f}")
