class Solution:
    
    def condition(self,nums,size) -> bool:
        
        total = new_k = 0
        for num in nums:
            
            if total + num > size:
                new_k += 1
                total = 0
            
            total += num
        
        return new_k if total == 0 else new_k + 1
                
        
        
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left,right = max(nums),sum(nums)
        
        while left < right:
            
            mid = (left + right)//2
            
            if self.condition(nums,mid) <= k:
                
                right = mid 
            
            else:
                
                left = mid + 1
            
        
        return left 
            
        
        