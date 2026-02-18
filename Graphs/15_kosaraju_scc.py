from collections import defaultdict

def kosaraju_algo(V, edges):
    # Step 1: Build graph
    graph=defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
    visited=[False]*V
    stack=[]
    # Step 2: First DFS (ordering)
    def dfs1(node):
        visited[node]=True
        for nei in graph[node]:
            if not visited[nei]:
                dfs1(nei) 
        stack.append(node) # finish time

    for i in range(V):
        if not visited[i]:
           dfs1(i)

    # Step 3: Build transpose graph
    transpose=defaultdict(list)
    for u,v in edges:
        transpose[v].append(u)
    visited=[False]*V
    scc=[]

    # Step 4: Second DFS on transpose
    def dfs2(node, component):
        visited[node]=True
        component.append(node)
        for nei in transpose[node]:
            if not visited[nei]:
                dfs2(nei,component)


    # Step 5: Process nodes in reverse finish order
    while stack:
        node=stack.pop()
        if not visited[node]:
            component=[]
            dfs2(node,component)
            scc.append(component)
    return scc

# -------- INPUT --------
V = 5
edges = [
    (1, 0),
    (0, 2),
    (2, 1),
    (0, 3),
    (3, 4)
]

# -------- OUTPUT --------
print(kosaraju_algo(V, edges))
