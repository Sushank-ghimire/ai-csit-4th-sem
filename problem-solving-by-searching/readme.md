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
