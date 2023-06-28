class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @cache
        def dp(index,fuel):
            
            
            if fuel < 0:
                return 0
            
            total = 0
            if index == finish:
                total += 1
            for i in range(len(locations)):
                if i != index:
                    
                    total += dp(i,fuel-abs(locations[i]-locations[index]))
                    total %= 10**9 + 7
            
            return total
        
        return dp(start,fuel)
                    