class Solution:
    
     
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        total,left,mod,right = 0,0,10**9+7,len(nums)-1
        
        
        while left <= right:
            
            if nums[right] + nums[left] > target:
                
                right -= 1
            else:
                
                gap = right - left
                total += pow(2,gap,mod)
                total %= mod
                left += 1
                
        return total
        
         
            
            
            
            