class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        min_length = math.inf
        max_length = -math.inf
        for word in wordDict:
            min_length = min(len(word),min_length)
            max_length = max(len(word),max_length)
        
        wordDict = set(wordDict)
        @lru_cache(None)
        def dp(i):
            if i >= len(s):
                return True
            boolean = False
            for length in range(min_length,max_length+1):
                boolean = boolean or (s[i:i+length] in wordDict and dp(i+length))
            
            return boolean
        
        return dp(0)
        