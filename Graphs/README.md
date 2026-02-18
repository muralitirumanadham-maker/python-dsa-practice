# Graphs

This folder contains Python implementations of **Graph Data Structures and Algorithms**
commonly asked in technical interviews.

The implementations focus on strong fundamentals,
clean traversal patterns, and frequently asked interview problems.

---

## Concepts Covered

### Graph Basics
- Graph representation using **Adjacency List**
- Graph representation using **Adjacency Matrix**
- Directed and Undirected graphs
- Weighted and Unweighted graphs

---

## Core Traversals

### Breadth First Search (BFS)
- Queue-based traversal
- Uses visited tracking
- Time Complexity: **O(V + E)**

### Depth First Search (DFS)
- Recursive traversal
- Uses visited list / set
- Time Complexity: **O(V + E)**

---

## Grid-Based Graph Problems

### Flood Fill
- DFS traversal on a 2D grid
- 4-directional adjacency
- Grid treated as a graph

### Number of Islands
- DFS-based connected component counting
- Each island is a connected group of land cells
- Time Complexity: **O(R × C)**

### Rotting Oranges
- Multi-source BFS on grid
- All rotten oranges processed simultaneously
- Computes minimum time to rot all oranges
- Time Complexity: **O(R × C)**

---

## Cycle Detection

### Undirected Graph
- BFS-based cycle detection (parent tracking)
- DFS-based cycle detection

### Directed Graph
- DFS-based cycle detection (recursion stack)
- BFS-based cycle detection (Kahn’s Algorithm)

---

## Topological Sorting
