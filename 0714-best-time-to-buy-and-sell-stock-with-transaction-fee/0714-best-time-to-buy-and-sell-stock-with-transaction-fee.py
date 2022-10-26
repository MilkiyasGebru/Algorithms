class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @lru_cache(None)
        
        def dp(index,status):
            
            if index >= len(prices):
                return 0
            
            b = 1 if status==1 else 0
            
            return max(prices[index]*status - fee*(b) + dp(index+1,status*-1), dp(index+1,status))
        
        return dp(0,-1)