class Solution:
    
    
        
    def checkPartitioning(self, s: str) -> bool:
        
        @cache
        def checkPalindrom(i1,i2):
            if i1 >= i2:
                return True
            if s[i1] != s[i2]:
                return False
            return checkPalindrom(i1+1,i2-1)
            
        
        @cache
        def dp(i,part):
            if part > 3:
                return False
            if i == len(s):
                return part == 3
            answer = False
            for j in range(i,len(s)):
                if checkPalindrom(i,j) :
                    answer = answer or dp(j+1,part+1)
            
            return answer
        return dp(0,0)
            
        