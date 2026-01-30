def nextGreaterElement(nums1, nums2):
    stack=[]
    nge_map={}
    for num in nums2:
        while stack and num>stack[-1]:
            smaller=stack.pop()
            nge_map[smaller]=num
        stack.append(num)
    while stack:
        nge_map[stack.pop()]=-1
    result=[]
    for num in nums1:
        result.append(nge_map[num])
    return result

nums1 = list(map(int, input("Enter nums1: ").split()))
nums2 = list(map(int, input("Enter nums2: ").split()))

print("Output:", nextGreaterElement(nums1, nums2))
