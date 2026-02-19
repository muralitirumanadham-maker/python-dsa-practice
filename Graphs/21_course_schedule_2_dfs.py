def findOrder(numCourses, prerequisites):
    n=numCourses
    p=prerequisites
    graph=[[] for _ in range(n)]
    for a,b in p:
        graph[b].append(a)
    visited=[False]*n
    recstack=[False]*n
    stack=[]
    def dfs(node):
        visited[node]=True
        recstack[node]=True
        for neigh in graph[node]:
            if not visited[neigh]:
                if not dfs(neigh):
                    return False
            elif recstack[neigh]:
                return False
        recstack[node]=False
        stack.append(node)
        return True
    for i in range(n):
        if not visited[i]:
            if not dfs(i):
                return []
    return stack[::-1]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses,prerequisites))
                       
