# Graphs

This folder contains Python implementations of **Graph Data Structures and Algorithms**
commonly asked in technical interviews.

The implementations focus on strong fundamentals,
clean traversal patterns, and frequently asked interview problems.

---

## Concepts Covered

### Graph Basics
- Graph representation using Adjacency List
- Graph representation using Adjacency Matrix
- Directed and Undirected graphs
- Weighted and Unweighted graphs

---

## Core Traversals

### Breadth First Search (BFS)
- Queue-based traversal
- Time Complexity: O(V + E)

### Depth First Search (DFS)
- Recursive traversal
- Time Complexity: O(V + E)

---

## Graph Construction Problems

### Clone Graph (LeetCode 133)
- Deep copy of graph structure
- BFS traversal with hashmap mapping
- Preserves adjacency relationships
- Time Complexity: O(V + E)

---

## Grid-Based Graph Problems

### Flood Fill
- DFS on grid

### Number of Islands
- DFS connected components

### Rotting Oranges
- Multi-source BFS

### 01 Matrix
- Multi-source BFS shortest distance

---

## Cycle Detection

### Undirected Graph
- BFS parent tracking
- DFS parent tracking

### Directed Graph
- DFS recursion stack
- Kahn’s Algorithm (BFS)

---

## Topological Sorting

### DFS-based Topological Sort
- Postorder DFS

### BFS-based Topological Sort
- Kahn’s Algorithm

---

## Advanced Topological Problems

### Course Schedule I
- Detect cycle in directed graph

### Course Schedule II
- Return valid ordering

### Alien Dictionary
- Character ordering using topo sort

---

## Graph Coloring

### Bipartite Graph Check
- BFS two coloring

---

## Minimum Spanning Tree

### Prim’s Algorithm
- Greedy MST using min heap
- Time Complexity: O(E log V)

---

## Shortest Path Algorithms

### Bellman–Ford Algorithm
- Handles negative weights
- Detects negative cycles

### Cheapest Flights Within K Stops
- Bellman Ford variation

### Floyd–Warshall Algorithm
- All pairs shortest path

---

## Reachability

### Warshall’s Algorithm
- Transitive closure

---

## Strong Connectivity

### Kosaraju’s Algorithm
- Strongly Connected Components

---

## Interview Problems Implemented

- Graph Representation
- BFS Traversal
- DFS Traversal
- Clone Graph
- Flood Fill
- Number of Islands
- Rotting Oranges
- 01 Matrix
- Cycle Detection (Directed & Undirected)
- Topological Sort (DFS & BFS)
- Course Schedule I & II
- Alien Dictionary
- Bipartite Graph Check
- Prim’s MST
- Bellman Ford
- Cheapest Flights Within K Stops
- Floyd Warshall
- Warshall Transitive Closure
- Kosaraju SCC

---

## Language Used
Python

---

## Status

✅ Graphs module completed with advanced interview-level coverage.
