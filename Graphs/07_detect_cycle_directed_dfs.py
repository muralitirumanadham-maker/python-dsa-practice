def has_cycle(graph):
    visited=[False]*len(graph)
    recstack=[False]*len(graph)
    def dfs(node):
        visited[node]=True
        recstack[node]=True
        for neigh in graph[node]:
            if not visited[neigh]:
                if dfs(neigh):
                    return True
            elif recstack[neigh]:
                return True
        recstack[node]=False
        return False
    for i in range(len(graph)):
        if not visited[i]:
            if dfs(i):
                return True
    return False

graph = [
    [1],    # 0 → 1
    [2],    # 1 → 2
    [0],    # 2 → 0 (cycle)
    [4],    # 3 → 4
    []      # 4
]
print(has_cycle(graph))
