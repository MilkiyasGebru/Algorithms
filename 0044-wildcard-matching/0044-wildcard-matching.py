class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def dp(i,j):
            
            if j == len(p):
                return i == len(s)
            
            if i > len(s):
                return False
            
            first = i < len(s) and p[j] in ("?",s[i])
            second =  p[j] in ("*")
            
            return (first and dp(i+1,j+1)) or (second and (dp(i+1,j+1) or dp(i+1,j) or dp(i,j+1)))
        
        return dp(0,0)