class Solution:
    def countVowels(self, word: str) -> int:
        

        
        vowels = {"a","e","i","o","u"}
        ans = 0
        for i in range(len(word)):
            
            ans += ((i+1)*(len(word)-1-i) + (i+1))*(word[i] in vowels)
        
        return ans