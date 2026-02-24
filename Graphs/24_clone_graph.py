from collections import deque

class Node:
    def __init__(self,val):
        self.val=val
        self.neighbors=[]

class Solution:
    def cloneGraph(self,node):
        if not node:
            return None
        visited={}
        q=deque([node])
        visited[node]=Node(node.val)
        while q:
            curr=q.popleft()
            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei]=Node(nei.val)
                    q.append(nei)
                visited[curr].neighbors.append(visited[nei])
        return visited[node]

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)

node1.neighbors=[node2,node4]
node2.neighbors=[node1,node3]
node3.neighbors=[node2,node4]
node4.neighbors=[node1,node3]

sol=Solution()
clone=sol.cloneGraph(node1)

visited=set()
q=deque([clone])

while q:
    curr=q.popleft()
    if curr in visited:
        continue
    visited.add(curr)
    print("Node:",curr.val,"Neighbors:",[n.val for n in curr.neighbors])
    for nei in curr.neighbors:
        q.append(nei)
