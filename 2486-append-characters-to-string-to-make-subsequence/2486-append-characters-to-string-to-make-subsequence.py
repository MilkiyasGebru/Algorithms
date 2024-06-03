class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left1 = 0
        left2 = 0
        
        while left1 < len(s) and left2 < len(t):
            
            if s[left1] == t[left2]:
                left2 += 1
            left1 +=1 
        
        return len(t) - left2

            