#O(n square)
def find_pairs(arr1,arr2,target):
    ans=[]
    for i in arr1:
        for j in arr2:
            if i+j==target:
                ans.append((i,j))
    return ans

#(O(1))

def find_pairs2(arr1,arr2,target):
    ans=[]
    s=set(arr2)
    for x in arr1:
        needed=target-x
        if needed in s:
            ans.append((x,needed))
    return ans    




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)
pairs1 = find_pairs2(arr1, arr2, target)
print (pairs1)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
