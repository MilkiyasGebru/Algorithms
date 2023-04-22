class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def dp(left,right):
            
            if left >= right:
                return 0
            
            if s[left] == s[right]:
                return dp(left+1,right-1)
            
            return 1 + min( dp(left,right-1), dp(left + 1,right))
        
        return dp(0,len(s)-1)