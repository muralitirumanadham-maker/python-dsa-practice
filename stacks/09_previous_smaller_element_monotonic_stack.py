def prev_smaller(arr):
    stack=[]
    result=[]
    for x in arr:
        while stack and stack[-1]>=x:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
           result.append(stack[-1])
            
        stack.append(x)
    return result

arr=list(map(int, input("Enter numbers separated by space: ").split()))
answer=prev_smaller(arr)
print("the previous elements are:",answer)
