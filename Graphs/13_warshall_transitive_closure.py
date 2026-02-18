def warshall(graph):
    v=len(graph)
    reach=[row[:] for row in graph]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if reach[i][k] and reach[k][j]:#(i=0,k=1,j=3)->reach[0][1] == 1 and reach[1][3] == 1 both are true path exists
                    reach[i][j]=1#change the values to 1
    return reach

graph = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]


result = warshall(graph)


print("Transitive Closure Matrix:")
for row in result:
    print(row)
