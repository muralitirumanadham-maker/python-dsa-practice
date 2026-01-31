def largest_rectangle_area(heights):
    stack=[]
    max_area=0
    n=len(heights)
    for i in range(n+1):
        curr_height=0 if i==n else heights[i]
        while stack and curr_height<heights[stack[-1]]:
            h=heights[stack.pop()]
            if not stack:
                width=i
            else:
                width=i-stack[-1]-1
            area=h*width
            max_area=max(max_area,area)
        stack.append(i)
    return max_area

arr = list(map(int, input("Enter heights: ").split()))
print("Largest rectangle area:", largest_rectangle_area(arr)) 
