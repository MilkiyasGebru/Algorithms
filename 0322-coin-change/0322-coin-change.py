class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(amount):
            
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            answer = math.inf
            for coin in coins:
                answer = min(1+dp(amount-coin),answer)
            
            return answer
        
        return dp(amount) if dp(amount) != math.inf else -1