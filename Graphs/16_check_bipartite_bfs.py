from collections import deque
def is_bipartate(graph):
    n=len(graph)
    color=[-1]*n
    for start in range(n):
        if color[start]==-1:
            queue=deque([start])
            color[start]=0
            while queue:
                node=queue.popleft()
                for neigh in graph[node]:
                    if color[neigh]==-1:
                        color[neigh]=1-color[node]
                        queue.append(neigh)
                    elif color[neigh]==color[node]:
                        return False
    return True

graph = [
    [1, 2, 3],  # 0
    [0, 2],     # 1
    [0, 1],     # 2
    [0, 4],     # 3
    [3]         # 4
]

print(is_bipartate(graph))

graph2 = [
    [1, 3],   # 0
    [0, 2],   # 1
    [1, 3],   # 2
    [0, 2]    # 3
]
print(is_bipartate(graph2))
