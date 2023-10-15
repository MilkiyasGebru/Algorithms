class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.mod = 10**9  + 7
        @cache
        def dp(steps,pos):
            if pos < 0 or pos >= arrLen or abs(pos - steps) > steps:
                return 0
            
            if steps == 0:
                return 1 
            
            return (dp(steps-1,pos) + dp(steps-1,pos+1) + dp(steps-1,pos-1))%self.mod
        
        return dp(steps,0)
            