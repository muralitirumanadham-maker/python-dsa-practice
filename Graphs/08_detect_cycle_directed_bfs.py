from collections import deque
def has_cycle(graph):
    n=len(graph)
    indegree=[0]*n
    for u in range(n):
        for v in graph[u]:
            indegree[v]+=1
    queue=deque()
    for i in range(n):
        if indegree[i]==0:
            queue.append(i)
    proceed=0
    while queue:
        node=queue.popleft()
        proceed+=1
        for nei in graph[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                queue.append(nei)
    return proceed!=n

graph = [
    [1],    # 0 -> 1
    [2],    # 1 -> 2
    [0],    # 2 -> 0 (cycle)
    [4],    # 3 -> 4
    []      # 4
]

print(has_cycle(graph))  # True
