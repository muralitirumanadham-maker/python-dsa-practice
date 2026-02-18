# Graphs

This folder contains Python implementations of **Graph Data Structures and Algorithms**
commonly asked in technical interviews.

The focus is on:
- Understanding graph representation
- Applying BFS and DFS traversal techniques
- Solving common graph interview problems step by step
- Learning weighted graph algorithms and all-pairs reachability

---

## Concepts Covered

### Graph Basics
- Graph representation using **Adjacency List**
- Graph representation using **Adjacency Matrix**
- Directed and Undirected graphs
- Weighted and Unweighted graphs
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
- Uses `visited` list / set to track visited nodes
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
- Maintains parent information
- Detects cycles in disconnected graphs

---

### Detect Cycle in Undirected Graph (DFS)
- Uses Depth First Search (DFS)
- Tracks parent node during recursion
- A cycle exists if a visited neighbor is not the parent
- Works for disconnected graphs

---

### Detect Cycle in Directed Graph (DFS)
- Uses Depth First Search (DFS)
- Maintains a recursion stack
- A cycle exists if a node is revisited in the current DFS path
- Works for disconnected directed graphs

---

### Detect Cycle in Directed Graph (BFS / Kahn’s Algorithm)
- Uses indegree array and BFS
- Based on topological sorting
- If all nodes are not processed, a cycle exists

---

### Topological Sort (DFS)
- Works on **Directed Acyclic Graphs (DAGs)**
- Uses DFS and post-order traversal
- Nodes are added after all dependencies are processed
- Final order obtained by reversing the stack

---

### Topological Sort (BFS / Kahn’s Algorithm)
- Uses BFS with indegree array
- Repeatedly processes nodes with indegree zero
- Detects cycles in directed graphs
- Commonly used in scheduling problems

---

### Minimum Spanning Tree – Prim’s Algorithm
- Works on **weighted undirected graphs**
- Uses a min-heap (priority queue)
- Greedily selects minimum weight edges
- Time Complexity: **O(E log V)**

---

### Shortest Path – Bellman Ford Algorithm
- Works on **weighted directed graphs**
- Supports **negative edge weights**
- Detects **negative weight cycles**
- Relaxes all edges **V−1 times**
- Time Complexity: **O(V × E)**

---

### Transitive Closure – Warshall’s Algorithm
- Works on **directed graphs**
- Uses **adjacency matrix**
- Finds reachability between **all pairs of vertices**
- Time Complexity: **O(V³)**
- Used to answer path-existence queries

---

## Interview Problems (Implemented)

- Graph Representation using Adjacency List
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Flood Fill (DFS on Grid)
- Detect Cycle in Undirected Graph (BFS)
- Detect Cycle in Undirected Graph (DFS)
- Detect Cycle in Directed Graph (DFS)
- Detect Cycle in Directed Graph (BFS / Kahn’s Algorithm)
- Topological Sort (DFS)
- Topological Sort (BFS / Kahn’s Algorithm)
- Minimum Spanning Tree – Prim’s Algorithm
- Shortest Path – Bellman Ford Algorithm
- Transitive Closure – Warshall’s Algorithm

---

## Language Used

- Python

---

## Status

🚀 **In Progress**

Graph algorithms are being added incrementally with clean,
readable, and interview-focused implementations.
