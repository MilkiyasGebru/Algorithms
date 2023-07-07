class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        total = sum(cost)
        @cache
        def dp(index,paid):
            
            
            
            if index == len(cost):
                return 0 if paid >= 0 else math.inf 
            
            return min(dp(index+1,paid-1),cost[index]+dp(index+1,min(len(time),time[index]+paid)))
        
        return dp(0,0)
            
            
                