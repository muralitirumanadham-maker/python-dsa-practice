from collections import deque
def timeneeded(tickets,k):
    q=deque()
    for i in range(len(tickets)):
        q.append([i,tickets[i]])
    time=0
    while q:
        index,remaining=q.popleft()
        remaining-=1
        time+=1
        print(f"Second {time}: Person {index} buys a ticket, remaining = {remaining}")
        if index==k and remaining==0:
            print(f"👉 Person {k} finished buying tickets.")
            return True
        if remaining>0:
            q.append([index,remaining])

tickets = list(map(int, input("Enter tickets array: ").split()))
k = int(input("Enter k: "))


result = timeneeded(tickets,k)

print("Time required:", result)
