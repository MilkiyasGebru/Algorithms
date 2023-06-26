class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @cache
        def dp(index,sum1):
            
            
            
            if index == len(rods):
                return 0 if sum1 == 0 else -math.inf
            
            
            return max( rods[index] + dp(index+1,sum1+rods[index]),
                      dp(index+1,sum1-rods[index]),
                      dp(index+1,sum1))
        
        return dp(0,0) if dp(0,0) != -math.inf else 0
        
        