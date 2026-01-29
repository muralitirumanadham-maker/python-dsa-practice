class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        answer=[-1]*n
        stack=[]
        for i in range(2*n):
            index=i%n
            while stack and nums[index]>nums[stack[-1]]:
                prev_index=stack.pop()
                answer[prev_index]=nums[index]
            if i<n:
                stack.append(index)
        return answer
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))

    solution = Solution()
    result = solution.nextGreaterElements(nums)

    print("Next Greater Elements:", result)
