class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        prefix = 0
        total = 0
        
        for i in range(len(nums)):
            
            prefix += nums[i]
            if prefix > 0:
                total += 1
        
        return total