class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        count = 0
        vowels = {'a','e','i','o','u'}
        for i in range(len(s)):
            
            if s[i].lower() in vowels:
                
                count += 1 if i < len(s)//2 else -1
        
        return count == 0