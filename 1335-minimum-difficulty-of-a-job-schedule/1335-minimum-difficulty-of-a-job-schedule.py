class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @cache
        def dp(index,d):
            
            if d < 0:
                return math.inf
            
            if index == len(jobDifficulty):
                
                return 0 if d == 0 else math.inf
            ans = math.inf
            maxx = 0
            for i in range(index,len(jobDifficulty)):
                maxx = max(maxx,jobDifficulty[i])
                ans = min(ans,maxx + dp(i+1,d-1))
            
            return ans
        
        return dp(0,d) if dp(0,d) != math.inf else -1
        
                