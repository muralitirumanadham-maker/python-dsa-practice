def longest_consecutive_sequence(nums):
    num_set=set(nums)
    longest=0
    for num in nums:
        if num-1 not in num_set:
            current=num
            length=1
        while current+1 in num_set:
            current+=1
            length+=1
        longest=max(longest,length)
    return longest

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )
