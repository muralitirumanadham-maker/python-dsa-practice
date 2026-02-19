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

### Number of Islands
- DFS-based connected component counting
- Time Complexity: **O(R × C)**

### Rotting Oranges
- Multi-source BFS
- Time Complexity: **O(R × C)**

### 01 Matrix
- Multi-source BFS
- Computes distance to nearest zero
- Time Complexity: **O(R × C)**

---

## Cycle Detection

### Undirected Graph
- BFS-based cycle detection
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
- Detects cycles

---

## Advanced Topological Problems

### Course Schedule (LeetCode 207)
- Detect cycle in directed graph

### Course Schedule II (LeetCode 210)
- Return valid topological ordering

### Alien Dictionary (LeetCode 269)
- Derives character ordering from sorted words
- Builds graph from word comparisons
- Uses BFS-based topological sorting
- Detects invalid prefix and cycles

---

## Graph Coloring

### Bipartite Graph Check
- BFS-based two-coloring
- Detects odd-length cycles

---

## Minimum Spanning Tree

### Prim’s Algorithm
- Weighted undirected graphs
- Min-heap based greedy approach
- Time Complexity: **O(E log V)**

---

## Shortest Path Algorithms

### Bellman–Ford Algorithm
- Handles negative edge weights
- Detects negative cycles
- Time Complexity: **O(V × E)**

### Floyd–Warshall Algorithm
- All-pairs shortest path
- Dynamic programming
- Time Complexity: **O(V³)**

---

## Reachability

### Warshall’s Algorithm
- Transitive closure
- Determines reachability between all pairs
- Time Complexity: **O(V³)**

---

## Strong Connectivity

### Kosaraju’s Algorithm
- Strongly Connected Components (SCC)
- Two DFS passes
- Time Complexity: **O(V + E)**

---

## Interview Problems Implemented

- Graph Representation
- BFS Traversal
- DFS Traversal
- Flood Fill
- Number of Islands
- Rotting Oranges
- 01 Matrix
- Cycle Detection (Directed & Undirected)
- Topological Sort (DFS & BFS)
- Course Schedule I & II
- Alien Dictionary
- Bipartite Graph Check
- Minimum Spanning Tree (Prim’s)
- Bellman–Ford
- Floyd–Warshall
- Warshall (Transitive Closure)
- Kosaraju (SCC)

---

## Language Used
- Python

---

## Status

✅ Graphs module completed with advanced interview-level coverage
