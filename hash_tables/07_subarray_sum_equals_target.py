def subarray_sum(nums,target):
    prefix_sum={}
    current_sum=0
    for i in range(len(nums)):
        current_sum+=nums[i]
        if current_sum==target:
            return [0,i]
        if (current_sum-target) in prefix_sum:
            return [prefix_sum[current_sum-target]+1,i]
        prefix_sum[current_sum]=i
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



