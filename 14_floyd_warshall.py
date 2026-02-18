def floyd_warshall(graph):
    v=len(graph)
    dist=[row[:] for row in graph]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    return dist

INF = float('inf')

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)

for row in result:
    print(row)
        
