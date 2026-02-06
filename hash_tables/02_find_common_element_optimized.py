#O(nsquare)
def item_finder(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return [i,j]
    return False

list1=[2,3,5]
list2=[1,6,5]
print(item_finder(list1,list2))

#O(n)
def itemfinder(l1,l2):
    my_dict={}
    for i in l1:
        my_dict[i]=True
    while l2:
        for j in l2:
            if j in my_dict:
                print(j)
        return True
            
    return False
l1=[1,2,3,4,5]
l2=[1,2,3,7,8]
print(itemfinder(l1,l2))


