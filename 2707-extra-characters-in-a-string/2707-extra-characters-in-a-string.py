class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        
        @cache
        def dp(index):
            
            if index == len(s):
                return 0
            
            min_characters = 1 + dp(index+1)
            for i in range(index+1,len(s)+1):
                
                if s[index:i] in words:
                    min_characters = min(min_characters,dp(i))
            
            return min_characters
        
        return dp(0)