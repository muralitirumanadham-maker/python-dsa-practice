def canFinish(numCourses, prerequisites):
    graph=[[] for _ in range(numCourses)]
    for a,b in prerequisites:
        graph[b].append(a)
    visited=[False]*numCourses
    recstack=[False]*numCourses
    def dfs(node):
        visited[node]=True
        recstack[node]=True
        for neigh in graph[node]:
            if not visited[neigh]:
                if dfs(neigh):
                    return True
            elif recstack[neigh]:
                return True
        recstack[node]=False
        return False
    for i in range(numCourses):
        if not visited[i]:
            if dfs(i):
                return False
    return True

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    
    print("Can finish:", canFinish(numCourses, prerequisites))
