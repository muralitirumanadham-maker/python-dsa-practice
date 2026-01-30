def stockspan(prices):
    stack=[]
    span=[0]*len(prices)
    for i in range(len(prices)):
        while stack and prices[stack[-1]]<=prices[i]:
            stack.pop()
        if not stack:
            span[i]=i+1
        else:
            span[i]=i-stack[-1]
        stack.append(i)
    return span


arr = list(map(int, input("Enter prices: ").split()))
print(stockspan(arr))
