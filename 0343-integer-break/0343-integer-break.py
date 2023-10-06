class Solution:
    def integerBreak(self, n: int) -> int:
        
        
        @cache
        def dp(x):
            
            if x == 1:
                return 1
            
            max_val = x if x != n else -math.inf
            
            for i in range(1,x):
                
                max_val = max(max_val,dp(i)*dp(x-i))
            
            return max_val
        
        return dp(n)