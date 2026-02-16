def has_cycle(graph):
    visited=set()
    def dfs(node,parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor,node):
                    return True
            elif neighbor!=parent:
                return True
        return False
    for node in graph:
        if node not in visited:
            if dfs(node,-1):
                return True
    return False

graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}

print(has_cycle(graph))
