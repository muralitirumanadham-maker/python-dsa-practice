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

## Graph-Based Interview Problems

### Flood Fill (DFS on Grid)
- DFS traversal on 2D grid
- 4-directional adjacency
- Grid treated as a graph

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
- Works on DAGs

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
- Time Complexity: **O(V + E)**

---

## Interview Problems Implemented

- Graph Representation (Adjacency List)
- BFS Traversal
- DFS Traversal
- Flood Fill
- Cycle Detection (Undirected & Directed)
- Topological Sort (DFS & BFS)
- Bipartite Graph Check
- Minimum Spanning Tree (Prim’s)
- Shortest Path (Bellman–Ford)
- All-Pairs Shortest Path (Floyd–Warshall)
- Transitive Closure (Warshall)
- Strongly Connected Components (Kosaraju)

---

## Language Used
- Python

---

## Status

✅ **Graphs module completed with core and advanced algorithms**
