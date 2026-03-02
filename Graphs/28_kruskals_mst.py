def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    rootx=find(parent,x)
    rooty=find(parent,y)
    if rootx!=rooty:
        parent[rooty]=rootx

def kruskals(n,edges):
    edges.sort(key=lambda x:x[2])
    parent=[i for i in range(n)]
    mst=[]
    total_cost=0
    for u,v,w in edges:
        if find(parent,u)!=find(parent,v):
            union(parent,u,v)
            mst.append((u,v,w))
            total_cost+=w
    return mst,total_cost

n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, cost = kruskals(n, edges)

print("MST:", mst)
print("Total Cost:", cost)
