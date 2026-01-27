class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        answer=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_day=stack.pop()
                answer[prev_day]=i-prev_day
            stack.append(i)
        return answer
    
if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    obj = Solution()
    result = obj.dailyTemperatures(temperatures)

    print("Temperatures:", temperatures)
    print("Days to wait :", result)
