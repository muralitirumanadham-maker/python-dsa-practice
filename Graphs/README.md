# Graphs

This folder contains Python implementations of **Graph Data Structures and Algorithms**
commonly asked in technical interviews.

The implementations focus on strong fundamentals,
clean traversal patterns, and commonly asked interview problems.

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
- Uses visited set
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
- Grid treated as an implicit graph
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

### DFS-based Topological Sort
- Post-order DFS
- Works on Directed Acyclic Graphs (DAGs)

### BFS-based Topological Sort (Kahn’s Algorithm)
- Uses indegree array
- Detects cycles in directed graphs

---

## Graph Coloring

### Bipartite Graph Check
- BFS-based two-coloring
- Works for disconnected graphs
- Detects odd-length cycles

---

## Minimum Spanning Tree

### Prim’s Algorithm
- Weighted undirected graphs
- Greedy approach using min-heap
- Time Complexity: **O(E log V)**

---

## Shortest Path Algorithms

### Bellman–Ford Algorithm
- Supports negative edge weights
- Detects negative cycles
- Time Complexity: **O(V × E)**

### Floyd–Warshall Algorithm
- All-pairs shortest path
- Dynamic programming approach
- Time Complexity: **O(V³)**

---

## Reachability

### Warshall’s Algorithm (Transitive Closure)
- Determines reachability for all vertex pairs
- Uses adjacency matrix
- Time Complexity: **O(V³)**

---

## Strong Connectivity

### Kosaraju’s Algorithm
- Strongly Connected Components (SCC)
- Two DFS passes
- Works on directed graphs
- Time
