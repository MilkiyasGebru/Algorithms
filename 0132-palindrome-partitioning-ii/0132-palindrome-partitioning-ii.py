class Solution:
    def minCut(self, s: str) -> int:
        
        def check(s):
        
            return s == s[::-1]
        
        @lru_cache(None)
        def partition( s: str) -> int:
        
            answer = len(s)



            for i in range(len(s)):

                if check(s[:i+1]):

                    answer = min(1 + partition(s[i+1:]),answer)

            return answer
        
        
        
        return partition(s) - 1