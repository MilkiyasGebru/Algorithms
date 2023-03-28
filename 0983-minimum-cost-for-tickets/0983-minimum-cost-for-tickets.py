class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        days_covered = [1,7,30]
        @lru_cache(None)
        def dp(index,prev):
            
            if index == len(days):
                return 0
            
            if days[index] < prev:
                return dp(index+1,prev)
            
            min_cost = math.inf
            
            for i in range(3):
                min_cost = min(min_cost,costs[i] + dp(index+1,days[index]+days_covered[i]))
                
            return min_cost
        
        return dp(0,0)
            
            
                