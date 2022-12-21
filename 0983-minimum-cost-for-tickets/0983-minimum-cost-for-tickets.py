class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durations = [1,7,30]
        
        @lru_cache(None)
        
        def topdown(index,final):
            
            if index == len(days):
                return 0
            
            if final > days[index]:
                return topdown(index+1,final)
            
            Min = math.inf
            
            for cost,duration in zip(costs,durations):

                Min = min( Min , topdown( index, days[index] + duration ) + cost )
                
            return Min
        return topdown(0,0)