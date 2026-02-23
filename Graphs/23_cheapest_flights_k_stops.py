def findCheapestPrice(n, flights, src, dst, k):
    cost=[float("inf")]*n
    cost[src]=0
    for step in range(k+1):
        temp=cost[:]
        for u,v,price in flights:
            if cost[u]+price<temp[v]:
                temp[v]=cost[u]+price
        cost=temp
    if cost[dst]==float("inf"):
        return -1
    return cost[dst]

n = 4

flights = [
    [0,1,100],
    [1,2,100],
    [2,3,100],
    [0,2,500]
]

src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))
