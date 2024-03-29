class Solution:
    
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def dp(i,n,min_profit):
            
            if n < 0:
                return 0
            
            if i == len(group) or n == 0:
                return 1 if min_profit == minProfit else 0
            
            return (dp(i+1,n-group[i],min(minProfit,min_profit+profit[i])))%mod + (dp(i+1,n,min_profit))%mod
        
        return dp(0,n,0)%mod