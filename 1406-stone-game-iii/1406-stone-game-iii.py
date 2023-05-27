class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # stoneValue.so
        
        @lru_cache(None)
        def dp(index):
            
            if index >= len(stoneValue):
                return 0
            max_ = -math.inf
            for i in range(index, min((index+3),len(stoneValue))):
                max_ = max(max_,sum(stoneValue[index:i+1])-dp(i+1))
            
            return max_
        max_ = dp(0)  
        if max_ > 0:
            
            return "Alice"
        
        elif max_ < 0:
            return 'Bob'
        
        else:
            return "Tie"