class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @cache
        def dp(n):
            
            if n == 0:
                return False
            
            if floor(n**0.5)**2 == n:
                return True
            
            maxNum = floor(n**0.5)
            best_answer = False
            
            for i in range(maxNum,0,-1):
                best_answer = best_answer or (not dp(n-i**2))
            
            return best_answer
        
        return dp(n)
            
            