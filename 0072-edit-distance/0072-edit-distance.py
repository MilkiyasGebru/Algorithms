class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def dp(i,j):
            
            if i == len(word1) or j == len(word2):
                return max(len(word1)-i, len(word2)-j)
            
            if word1[i] == word2[j]:
                return dp(i+1,j+1)
            
            return min(1 + dp(i,j+1), 1 + dp(i+1,j+1), 1+ dp(i+1,j))
        
        return dp(0,0)