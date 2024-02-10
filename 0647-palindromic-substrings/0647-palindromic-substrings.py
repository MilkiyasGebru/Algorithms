class Solution:
    def countSubstrings(self, s: str) -> int:
        
        palindroms = 0
        
        for i in range(len(s)):
            
            palindroms += 1
            j,k = i-1,i+1
            
            while j >= 0 and k < len(s) and s[j] == s[k]:
                
                palindroms += 1
                j -= 1
                k += 1
                
            j = i - 1
            k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                
                palindroms += 1
                j -= 1
                k += 1
        return palindroms