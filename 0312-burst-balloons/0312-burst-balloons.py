class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache
        def dp(left,right):
            
            if left == right:
                return 0
            
            l = nums[left] if left >= 0 else 1
            r = nums[right] if right < len(nums) else 1
            max_value = 0
            for i in range(left+1,right):
                
                val = nums[i]*r*l + dp(left,i) + dp(i,right)
                max_value = max(val,max_value)
            
            return max_value
        
        return dp(-1,len(nums))
                