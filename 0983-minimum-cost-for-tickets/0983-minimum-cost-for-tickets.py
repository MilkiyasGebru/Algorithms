class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def topdown(index,final):
            
            if index == len(days):
                return 0
            if final > days[index]:
                return topdown(index+1,final)
            
            Min = math.inf
            for i in range(3):
                c = 1
                if i == 1:
                    c = 7
                elif i == 2:
                    c = 30
                    
                Min = min(Min,topdown(index,days[index] + c)+costs[i])
            return Min
        return topdown(0,0)