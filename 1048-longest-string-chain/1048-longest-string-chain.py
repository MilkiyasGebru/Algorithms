class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key= lambda word : len(word))
        def check(word1,word2):
            if len(word2) - len(word1) != 1 :
                return False
            
            diff = 0
            i,j = 0,0
            while( i < len(word1) and j < len(word2)):
               
                if word1[i] != word2[j]:
                    diff += 1
                    i -= 1
                i += 1
                j += 1
            return diff < 2
        dp = [1 for _ in range(len(words))]
        
        for i in range(len(words)):
            for j in range(i):
                if check(words[j],words[i]):
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
                    
                
                
            