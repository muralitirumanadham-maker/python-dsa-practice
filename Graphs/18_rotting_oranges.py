from collections import deque
def rotten_oranges(grid):
    n=len(grid)
    m=len(grid[0])
    vis=[[False]*m for _ in range(n)]
    q=deque()
    ans=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                q.append(((i,j),0))
                vis[i][j]=True
    while q:
        (i,j),time=q.popleft()
        ans=max(ans,time)
        if i-1>=0 and not vis[i-1][j] and grid[i-1][j]==1:
            q.append(((i-1,j),time+1))
            vis[i-1][j]=True

        if i+1<n and not vis[i+1][j] and grid[i+1][j]==1:
            q.append(((i+1,j),time+1))
            vis[i+1][j]=True
        if j-1>=0 and not vis[i][j-1] and grid[i][j-1]==1:
            q.append(((i,j-1),time+1))
            vis[i][j-1]=True
        if j+1<m and not vis[i][j+1] and grid[i][j+1]==1:
            q.append(((i,j+1),time+1))
            vis[i][j+1]=True

    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not vis[i][j]:
                return -1
    return ans



# ---------- INPUT ----------
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

# ---------- OUTPUT ----------
print("Minutes to rot all oranges:", rotten_oranges(grid))
