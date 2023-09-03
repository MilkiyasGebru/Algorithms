class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(index,a,b):
            if a > len(costs)//2 or b > len(costs)//2:
                return float("inf")
            if index == len(costs):
                return 0
            
            return min(costs[index][0] + dp(index+1,a+1,b), costs[index][1] + dp(index+1,a,b+1))
        
        return dp(0,0,0)
            
            