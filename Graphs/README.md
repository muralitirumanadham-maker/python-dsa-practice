# Graphs

This folder contains Python implementations of **Graph Data Structures and Algorithms**
commonly asked in technical interviews.

The focus is on:
- Understanding graph representation
- Applying BFS and DFS traversal techniques
- Solving common graph interview problems step by step

---

## Concepts Covered

### Graph Basics
- Graph representation using **Adjacency List**
- Undirected graphs
- Vertex and edge operations

---

## Implementations

### 1. Graph Representation (Adjacency List)
- Undirected graph implementation
- Add vertex
- Add edge
- Remove edge
- Remove vertex
- Print graph structure

This implementation forms the foundation for
all graph traversal algorithms.

---

### 2. Breadth First Search (BFS)
- BFS traversal using a queue (`deque`)
- Uses `visited` set to avoid revisiting nodes
- Traverses graph level by level
- Time Complexity: **O(V + E)**

---

### 3. Depth First Search (DFS)
- Recursive DFS traversal
- Uses `visited` list to track visited nodes
- Explores one branch fully before backtracking
- Time Complexity: **O(V + E)**

---

## Graph-Based Interview Problems

### Flood Fill (DFS on Grid)
- DFS traversal on a 2D grid
- Each cell treated as a graph node
- 4-directional adjacency (up, down, left, right)
- Prevents infinite recursion using base conditions

---

### Detect Cycle in Undirected Graph (BFS)
- Uses Breadth First Search (BFS)
- Maintains parent information for each node
- A cycle is detected if a visited neighbor is not the parent
- Works for disconnected graphs

---

## Interview Problems (Implemented)

- Graph Representation using Adjacency List
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Flood Fill (DFS on Grid)
- Detect Cycle in Undirected Graph (BFS)

---

## Language Used

- Python

---

## Status

🚀 **In Progress**

Graph algorithms are being added incrementally with clean,
readable, and interview-focused implementations.
