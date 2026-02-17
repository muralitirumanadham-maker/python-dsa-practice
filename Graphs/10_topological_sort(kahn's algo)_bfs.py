from collections import deque

def topo_sort_kahn(graph):
    V = len(graph)
    indegree = [0] * V

    for u in range(V):
        for i in graph[u]:
            indegree[i] += 1

    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    res = []

    while q:
        curr = q.popleft()
        res.append(curr)

        for nei in graph[curr]:  
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    if len(res) != V:   
        return []

    return res
graph = [
    [1, 2],
    [3],
    [3],
    []
]

print(topo_sort_kahn(graph))
