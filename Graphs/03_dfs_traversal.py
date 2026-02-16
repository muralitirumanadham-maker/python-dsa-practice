def dfs(graph,start,visited):
    visited[start]=True
    print(start,end=" ")
    for neighbors in graph[start]:
        if not visited[neighbors]:
            dfs(graph,neighbors,visited)

graph={
    0:[1,2],
    1:[3],
    2:[],
    3:[]
}
n=len(graph)
visited=[False]*n
dfs(graph,0,visited)
