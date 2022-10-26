class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(index,status,action):
            
            if index >= len(prices) or action == 0:
                return 0
            
            return max(prices[index]*status + dp(index+1,status*-1,action-1), dp(index+1,status,action))
        
        return dp(0,-1,4)