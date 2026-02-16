# Graphs

This folder contains Python implementations of **Graph Data Structures and Algorithms**
commonly asked in technical interviews.

The focus is on:
- Understanding graph representation
- Applying BFS and DFS traversal techniques
- Solving graph-based interview problems step by step

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

## Grid-Based Graph Problems

### Flood Fill (DFS)
- Depth First Search (DFS) on a 2D grid
- Each cell treated as a graph node
- 4-directional adjacency (up, down, left, right)
- Handles edge cases to prevent infinite recursion

---

## Interview Problems (Implemented)

- Graph Representation using Adjacency List
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Flood Fill (DFS on Grid)

---

## Language Used

- Python

---

## Status

🚀 **In Progress**

Graph algorithms are being added incrementally with clean,
readable, and interview-focused implementations.
