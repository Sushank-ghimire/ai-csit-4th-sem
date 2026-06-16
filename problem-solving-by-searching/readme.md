# Problem Solving by Searching

A small collection of search algorithms used in AI problem solving.

## Table of Contents

### Uninformed Search

1. [Depth First Search (DFS)](#depth-first-search-dfs)
2. [Breadth First Search (BFS)](#breadth-first-search-bfs)
3. [Uniform Cost Search](#uniform-cost-search)

### Heuristic Search (Informed Search)

1. [Greedy Best First Search](#greedy-best-first-search)
2. [A\* Search](#a-star-search)

---

## Overview

Searching is a basic AI technique used to find a path, solution, or goal state.

Common uses:

- path finding
- puzzle solving
- decision making
- state-space exploration

---

## Depth First Search (DFS)

DFS explores as deep as possible along one branch before backtracking.

### Key idea

- Start from a node
- Visit one neighbor deeply
- Backtrack when no unvisited node remains
- Stop when the goal is found

The DFS flow is shown in:

![DFS Architecture](arch/dfs.svg)

This diagram shows:

- the graph structure
- the search direction
- the backtracking process
- the final path found by DFS

### Advantages

- Uses less memory than BFS
- Simple to implement
- Good for deep search spaces

### Disadvantages

- May go down a wrong path for a long time
- Does not guarantee the shortest path
- Can get stuck in deep or infinite branches without proper handling

---

## Breadth First Search (BFS)

BFS explores all neighbors at the current depth before moving to nodes at the next depth level.

### Key idea

- Start from a node
- Visit all direct neighbors first
- Then visit their neighbors (level by level)
- Stop when the goal is found

The BFS flow is shown in:

![BFS Architecture](arch/bfs.svg)

This diagram shows:

- the grid structure with obstacles
- the breadth-first exploration pattern
- the level-by-level expansion
- the shortest path found by BFS

### Advantages

- Guarantees the shortest path in unweighted graphs
- Explores systematically level by level
- Good for finding nearest solutions
- Works well with large state spaces

### Disadvantages

- Uses more memory than DFS (stores all nodes at current level)
- Slower than DFS for deep search spaces
- Not suitable for infinite or very deep graphs without proper pruning

## Uniform Cost Search

Uniform Cost Search (UCS) expands the node with the lowest path cost first.

### Key idea

- Start from the initial node
- Use a priority queue ordered by path cost
- Expand the cheapest path available
- Stop when the goal node is removed from the queue

The UCS flow is shown in:

![Uniform Cost Search Architecture](arch/uniform-cost.svg)

This diagram shows:

- the weighted graph
- path costs between nodes
- the lowest-cost route selection
- the final least-cost path found by UCS

### Advantages

- Finds the least-cost path
- Works well for weighted graphs
- Guaranteed to be optimal if all edge costs are non-negative

### Disadvantages

- Slower than BFS in many cases
- Uses more memory than DFS
- Can explore many nodes when costs are similar

---

## Greedy Best First Search

Greedy Best First Search expands the node that appears closest to the goal according to a heuristic value.

### Key idea

- Start from the initial node
- Use a priority queue ordered by heuristic value
- Expand the most promising node first
- Stop when the goal node is found

The Greedy Best First Search flow is shown in:

![Greedy Best First Search Architecture](arch/greedy_bfs.svg)

This diagram shows:

- the graph structure
- heuristic-based node selection
- the search path chosen by the algorithm
- the final goal-reaching route

### Advantages

- Usually faster than uninformed search
- Useful when a good heuristic is available
- Often explores fewer nodes than BFS or DFS

### Disadvantages

- Does not guarantee the shortest path
- Can make poor choices if the heuristic is misleading
- May get stuck exploring suboptimal routes

---

<a id="a-star-search"></a>

## A\* Search

A\* Search combines actual path cost and heuristic estimate to find the optimal path efficiently.

### Key idea

- Start from the initial node
- Use a priority queue ordered by `f(n) = g(n) + h(n)`
- `g(n)` = cost from start to current node
- `h(n)` = estimated cost from current node to goal
- Expand the node with the smallest `f(n)` first
- Stop when the goal node is selected for expansion

The A\* Search flow is shown in:

![A* Search Architecture](arch/astar.svg)

This diagram shows:

- the weighted graph structure
- path cost accumulation (`g(n)`)
- heuristic guidance (`h(n)`)
- final least-cost path found by A\*

### Advantages

- Finds the optimal path when the heuristic is admissible
- Usually explores fewer nodes than UCS
- Works well for weighted pathfinding problems

### Disadvantages

- Performance depends on heuristic quality
- Uses more memory due to priority queue and bookkeeping
- Can behave like UCS if heuristic gives little guidance

---
