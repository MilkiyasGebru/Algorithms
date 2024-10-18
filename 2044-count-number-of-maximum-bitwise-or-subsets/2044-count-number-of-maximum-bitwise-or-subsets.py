class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        total_score = 0
        for num in nums:
            total_score |= num
        @cache
        def dp(i,score):
            if i == len(nums):
                return score == total_score
            
            return dp(i+1,score) + dp(i+1,score | nums[i])
        
        return dp(0,0)