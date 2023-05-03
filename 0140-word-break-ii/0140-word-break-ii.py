class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        self.answer = []
        
        min_length = math.inf
        max_length = -math.inf
        
        for word in wordDict:
            
            min_length = min(len(word),min_length)
            max_length = max(len(word),max_length)
        wordDict = set(wordDict)
        def backTrack(i,sentence):
            
            if i == len(s):
                if len(sentence) > 0:
                    self.answer.append(" ".join(sentence))
                return 
            
            for length in range(min_length,max_length+1):
                word = s[i:i+length]
                if word in wordDict:
                    backTrack(i+length,sentence+[word])
                if i + length >= len(s):
                    break
        
        backTrack(0,[])
        return self.answer