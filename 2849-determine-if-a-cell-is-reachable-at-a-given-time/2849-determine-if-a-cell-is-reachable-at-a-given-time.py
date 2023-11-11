class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        
        shortest_time = max(abs(sx-fx),abs(sy-fy))
        if (sx == fx  ) and (sy == fy):
            return t != 1
        return shortest_time <= t  
        
        
        