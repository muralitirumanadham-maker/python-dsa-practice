def topo_sort(graph):
    n=len(graph)
    visited=[False]*n
    stack=[]
    def dfs(curr):
        visited[curr]=True
        for u in graph[curr]:
            if not visited[u]:
                dfs(u)
        stack.append(curr)
    for i in range(n):
        if not visited[i]:
            dfs(i)
    return stack[::-1]

graph = [
    [1, 2],   # 0 → 1, 2
    [3],      # 1 → 3
    [3],      # 2 → 3
    []        # 3
]

print(topo_sort(graph))
