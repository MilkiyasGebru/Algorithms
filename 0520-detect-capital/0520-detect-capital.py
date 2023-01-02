class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower = True
        upper = True
        
        for i in range(1,len(word)):
            
            lower = lower and word[i].islower()
            upper = upper and word[i].isupper()
            
        return lower or (upper and word[0].isupper())