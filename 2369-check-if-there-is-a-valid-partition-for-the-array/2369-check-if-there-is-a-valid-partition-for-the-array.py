class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        @cache
        def dp(i):
            if i == len(nums):
                return True
            
            oneGreat = i + 1 < len(nums) and (nums[i] == nums[i+1])
            twoGreat = i + 2 < len(nums) and ((oneGreat and nums[i] == nums[i+2]) or ((nums[i+1] == 1 + nums[i]) and (nums[i+2] == 1 + nums[i+1])))
            
            return (oneGreat and dp(i+2) ) or (twoGreat and dp(i+3))
        
        return dp(0)
            
            