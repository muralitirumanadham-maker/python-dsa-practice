def removestones(stones):
    parent={}
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        rootx=find(x)
        rooty=find(y)
        if rootx!=rooty:
            parent[rootx]=rooty
    for r,c in stones:
        parent.setdefault(r,r)
        parent.setdefault(~c,~c)
        union(r,~c)
    roots=set()
    for x in parent:
        roots.add(find(x))
    return len(stones)-len(roots)
# -------- Input --------

stones=[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

print("Maximum stones removed:",removestones(stones))
