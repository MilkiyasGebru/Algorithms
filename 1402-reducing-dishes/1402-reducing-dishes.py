class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @lru_cache(None)
        def dp(i,time):
            
            if i == len(satisfaction):
                return 0
            
            return max(time*satisfaction[i] + dp(i+1,time+1),dp(i+1,time))
        
        return dp(0,1)