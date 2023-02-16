class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        answer = -inf
        for i in range(len(nums)):
            
            
            prev = max(nums[i],nums[i] + prev)
            answer = max(answer,prev)
            
        return answer