class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        
        max_ = summ = 0
        
        for i in range(len(nums)):
            
            summ += nums[i]
            max_ = max(max_,ceil(summ/(i+1) ))
        
        return max_
            
            
        
        