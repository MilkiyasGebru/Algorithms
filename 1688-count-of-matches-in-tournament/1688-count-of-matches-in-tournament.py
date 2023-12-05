class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        def rec(n):
            
            if n == 1:
                return 0
            
            return (n//2) + rec((n//2) + n%2) 
        
        return rec(n)