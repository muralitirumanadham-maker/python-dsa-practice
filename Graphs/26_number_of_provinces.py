def findcirclenum(isconnected):
    n=len(isconnected)
    visited=set()
    def dfs(city):
        for nei in range(n):
            if isconnected[city][nei]==1 and nei not in visited:
                visited.add(nei)
                dfs(nei)
    provinces=0
    for city in range(n):
        if city not in visited:
            visited.add(city)
            dfs(city)
            provinces+=1
    return provinces


isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

print(findcirclenum(isConnected))
