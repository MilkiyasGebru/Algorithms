class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n <= 2:
                return n
            Max = n
            for i in range(1,n):
                Max = max(dp(n-i)*dp(i),Max)
            return Max
        
        answer = 1
        for i in range(1,n):
            answer = max(answer,(n-i)*(i))
            answer = max(dp(n-i)*dp(i),answer)
        return answer