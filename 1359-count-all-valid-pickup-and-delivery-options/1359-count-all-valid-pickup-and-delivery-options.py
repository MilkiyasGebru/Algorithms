class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        def rec(n):
            
            if n == 1:
                return 1
            
            return ((2*n-1)*n * rec(n-1))%mod
        
        return rec(n)
            