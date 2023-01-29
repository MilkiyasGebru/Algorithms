class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        total = total // 2
        
        @lru_cache(None)
        def dp(index,s):
            
            if s == total:
                return True
            elif index == len(nums) or s > total:
                return False
            return dp(index+1,s+nums[index]) or dp(index + 1, s)
        
        return dp(0,0)