from collections import deque
def has_cycle(graph):
    visited=set()
    parent={}
    for start in graph:
        if start not in visited:
            queue=deque()
            queue.append(start)
            visited.add(start)
            parent[start]=-1
            while queue:
                current=queue.popleft()
                for neigh in graph[current]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
                        parent[neigh]=current
                    elif parent[current]!=neigh:
                        return True
    return False

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [2, 0],
    4: []         
}

# -------- OUTPUT --------
if has_cycle(graph):
    print("Cycle exists")
else:
    print("No cycle")
            
