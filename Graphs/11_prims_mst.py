import heapq
def prims_mst(adj):
    v=len(adj)
    inmst=[False]*v
    pq=[]
    min_cost=0
    heapq.heappush(pq,(0,0))
    while pq:
        wt,u=heapq.heappop(pq)
        if inmst[u]:
            continue
        inmst[u]=True
        min_cost+=wt
        for v,w in adj[u]:
            if not inmst[v]:
                heapq.heappush(pq,(w,v))
    return min_cost

graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8)],
    [(1, 5), (2, 7)]
]

print(prims_mst(graph))
