class Solution:
        
    def splitArray(self, nums: List[int], k: int) -> int:
        
        @lru_cache(None)
        
        def dp(i,length):
            
            if length == 1:
                return sum(nums[i:])
            
            ans  = math.inf
            
            for size in range(1,len(nums)-i + 1):
                
                
                max_split = max(sum(nums[i:i+size]),dp(i+size,length-1))
    
                if max_split > ans:
                    break
                
                ans = max_split
            
            return ans
        
        return dp(0,k)
            
        
        