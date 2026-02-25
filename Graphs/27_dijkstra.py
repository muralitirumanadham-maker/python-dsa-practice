import heapq
def dijkstra(src,graph,V):
    dist=[float("inf")]*V
    dist[src]=0
    pq=[]
    heapq.heappush(pq,(0,src))
    while pq:
        curr_dist,u=heapq.heappop(pq)
        for v,wt in graph[u]:
            if dist[v]>dist[u]+wt:
                dist[v]=dist[u]+wt
                heapq.heappush(pq,(dist[v],v))
    print("shortest distance from source:",src)
    for i in range(V):
        print(f"Node {i} -> {dist[i]}")

V = 5

# Graph (Adjacency List)
# graph[u] = [(v, weight)]
graph = {
    0: [(1, 2), (2, 4)],
    1: [(2, 1), (3, 7)],
    2: [(4, 3)],
    3: [(4, 1)],
    4: []
}

# Source node
src = 0

# Call Dijkstra
dijkstra(src, graph, V)
