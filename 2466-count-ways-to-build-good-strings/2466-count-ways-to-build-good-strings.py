class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        mod = 10**9 + 7
        
        @lru_cache(None)
        def dp(length):
            
            if length > high:
                return 0
            
            
            return 1*(length >= low) + dp(length + zero)%mod + dp(length+one)%mod
        
        return dp(0)%mod
            