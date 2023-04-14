class Solution:
    def maxProduct(self, s: str) -> int:
        def isPalindrom(s):
            
            if s != "" and s == s[::-1]:
                return len(s)
            return 0
        
        @lru_cache(None)
        def dp(index,s1,s2):
            
            if index == len(s):
                
                return isPalindrom(s1)*isPalindrom(s2)
            
            return max(
                dp(index+1,s1+s[index],s2),
                dp(index+1,s1,s2+s[index]),
                dp(index+1,s1,s2)
            )
        
        return dp(0,"","")
            
        
        