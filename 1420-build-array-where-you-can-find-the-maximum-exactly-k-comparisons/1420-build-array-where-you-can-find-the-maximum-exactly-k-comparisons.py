class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        @cache
        def dp(i,prev,count):
            
            if i == n:
                return 1 if count == 0 else 0
            
            if count < 0:
                return 0
            
            total_ways = 0
            for num in range(1,m+1):
                if num  > prev:
                    total_ways += dp(i+1,num,count - 1)%(mod)
                else:
                    total_ways += dp(i+1,prev,count)%(mod)
            
            return total_ways%mod
        
        return dp(0,0,k)
            
            
        
        