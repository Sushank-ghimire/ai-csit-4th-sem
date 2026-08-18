import numpy as np

POP_SIZE = int(input("Enter population size: "))
GENERATIONS = int(input("Enter number of generations: "))
CROSSOVER_PROB = float(input("Enter crossover probability (0-1): "))
MUTATION_PROB = float(input("Enter mutation probability (0-1): "))
X_MIN, X_MAX = -1.0, 2.0
MUTATION_STD = 0.1

def fitness_function(x):
  return x * np.sin(10 * np.pi * x) + 1

np.random.seed(42)
population = np.random.uniform(X_MIN, X_MAX, POP_SIZE)

def tournament_selection(pop, fitness, k=3):
  selected = []
  for _ in range(len(pop)):
    idx = np.random.choice(len(pop), k, replace=False)
    selected.append(pop[idx[np.argmax(fitness[idx])]])
  return np.array(selected)

def arithmetic_crossover(p1, p2):
  alpha = np.random.rand()
  return alpha * p1 + (1 - alpha) * p2, alpha * p2 + (1 - alpha) * p1

def mutate(x):
  if np.random.rand() < MUTATION_PROB:
    x += np.random.normal(0, MUTATION_STD)
  return np.clip(x, X_MIN, X_MAX)

best_history = []
mean_history = []

print("\nGenetic Algorithm")

for generation in range(GENERATIONS):
  fitness = fitness_function(population)

  best_index = np.argmax(fitness)
  best_x = population[best_index]
  best_fitness = fitness[best_index]
  average_fitness = np.mean(fitness)

  if generation % 10 == 0 or generation == GENERATIONS - 1:
    print(
      f"Generation {generation + 1:3d} | "
      f"Best x: {best_x:8.5f} | "
      f"Best Fitness: {best_fitness:8.5f} | "
      f"Average Fitness: {average_fitness:8.5f}"
    )

  parents = tournament_selection(population, fitness)

  offspring = []
  np.random.shuffle(parents)

  for i in range(0, POP_SIZE, 2):
    if np.random.rand() < CROSSOVER_PROB:
      c1, c2 = arithmetic_crossover(
        parents[i],
        parents[i + 1]
      )
    else:
      c1, c2 = parents[i], parents[i + 1]

    offspring.extend([
      mutate(c1),
      mutate(c2)
    ])

  population = np.array(offspring)


# Final result
fitness = fitness_function(population)
best_index = np.argmax(fitness)

print("\nFinal Result")
print(f"Best Solution (x) : {population[best_index]:.6f}")
print(f"Best Fitness       : {fitness[best_index]:.6f}")
