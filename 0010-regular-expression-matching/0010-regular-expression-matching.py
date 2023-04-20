class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        @lru_cache(None)
        def dp(i,j):
            
            if j == len(p):
                return i == len(s)
            
            first = i < len(s) and p[j] in {s[i],"."}
            second = j + 1 < len(p) and p[j+1] == "*"
            
            return (first and dp(i+1,j+1)) or (first and second and (dp(i+1,j) or dp(i+1,j+2) or dp(i,j+2))) or (second and dp(i,j+2))
        
        return dp(0,0)