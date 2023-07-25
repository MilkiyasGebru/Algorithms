class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        
        def checkPalindrom(i1,i2):
            
            count = 0
            while i1 < i2:
                
                if s[i1] != s[i2]:
                    count += 1
                i1+=1
                i2 -= 1
            return count
        @cache
        def dp(i,part):
            
            if part > k:
                return float("inf")
            
            if i == len(s):
                return float("inf") if part != k else 0
            answer = float("inf")
            for j in range(i,len(s)):
                
                answer = min(checkPalindrom(i,j) + dp(j+1,part+1), answer)
            
            return answer
        
        return dp(0,0)