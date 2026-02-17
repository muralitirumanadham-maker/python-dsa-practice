def bellman_ford(src,graph,v):
    dist=[float('inf')]*v
    dist[src]=0
    for _ in range(v-1):
        for u in range(v):
            for neigh,wt in graph[u]:
                if dist[u]!=float('inf') and dist[neigh]>dist[u]+wt:
                    dist[neigh]=dist[u]+wt
    for u in range(v):
        for neigh,wt in graph[u]:
            if dist[u]!=float('inf') and dist[neigh]>dist[u]+wt:
                print("Negative weighted cycle detected")
                return
    for i in range(v):
        print(dist[i],end=" ")
    print()

v = 5   # number of vertices

graph = [
    [(1, 6), (3, 7)],          # 0
    [(2, 5), (3, 8), (4, -4)], # 1
    [(1, -2)],                 # 2
    [(2, -3), (4, 9)],         # 3
    [(0, 2), (2, 7)]           # 4
]

src = 0 
bellman_ford(src, graph, v)
        
