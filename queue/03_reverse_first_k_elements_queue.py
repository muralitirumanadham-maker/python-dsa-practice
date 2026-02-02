from collections import deque
def reverse(q,k):
    if k<=0 or k>len(q):
        return q
    stack=[]
    for _ in range(k):
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    size=len(q)
    for _ in range(size-k):
        q.append(q.popleft())
    return q

q = deque([1, 2, 3, 4, 5])
k = 3

result = reverse(q, k)
print("Queue after reversing first", k, "elements:", list(result))
    
