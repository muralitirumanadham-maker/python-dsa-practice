from collections import deque
def updatematrix(mat):
    n=len(mat)
    m=len(mat[0])
    vis=[[False]*m for _ in range(n)]
    dis=[[0]*m for _ in range(n)]
    q=deque()
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                q.append(((i,j),0))
                vis[i][j]=True
    while q:
        (i,j),d=q.popleft()
        dis[i][j]=d
        if i-1>=0 and not vis[i-1][j]:
            q.append(((i-1,j),d+1))
            vis[i-1][j]=True
        if i+1<n and not vis[i+1][j]:
            q.append(((i+1,j),d+1))
            vis[i+1][j]=True
        if j-1>=0 and not vis[i][j-1]:
            q.append(((i,j-1),d+1))
            vis[i][j-1]=True
        if j+1<m and not vis[i][j+1]:
            q.append(((i,j+1),d+1))
            vis[i][j+1]=True
    return dis
# ---------- INPUT ----------
mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

# ---------- OUTPUT ----------
print("Distance Matrix:")
for row in updatematrix(mat):
    print(row)
