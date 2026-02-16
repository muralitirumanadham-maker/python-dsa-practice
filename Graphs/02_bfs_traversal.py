from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque()
    visited.add(start)
    queue.append(start)
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbors in graph[node]:
            if neighbors not in visited:
                visited.add(neighbors)
                queue.append(neighbors)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Run BFS
bfs(graph, 'A')
