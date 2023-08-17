class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        
        
        for i in range(1,len(nums)):
            
            if nums[i]  + nums[i-1] >= m:
                return True
        
        return len(nums) < 3 or False