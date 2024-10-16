class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        answer = 0
        for i in range(len(nums)):
            if stack and stack[-1][0] < nums[i]:
                continue
            stack.append((nums[i],i))
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1][0] <= nums[i]:
                answer = max(answer,i - stack[-1][-1] )
                stack.pop()
        return answer
                
        