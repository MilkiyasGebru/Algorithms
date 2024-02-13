class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        count = total = 0
        
        for i in range(len(s)):
            
            if s[i] == "(":
                count += 1
            else :
                count -= 1
            
            if count < 0:
                count = 0
                total += 1
        return total + count