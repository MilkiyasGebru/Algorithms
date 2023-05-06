class Solution:
    
    @lru_cache(None)
    def possible(self,num):
        if num == 0:
            return 0
        return 1 + 2*possible(num-1)
    
    def binary_search(binary_search,nums,val,right):
        
        left = 0
        # right = len(nums)
        
        while left <= right:
            
            mid = (left + right)//2
            if nums[mid] <= val:
                left = mid + 1
            else:
                right = mid
        
        return left 
    
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
        
         
            
            
            
            