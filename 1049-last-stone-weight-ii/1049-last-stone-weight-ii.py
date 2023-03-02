class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        @lru_cache(None)
        def rec(index,weight):
            if index == len(stones):
                return abs(weight)
            
            return min(rec(index+1,weight + stones[index]),rec(index + 1, weight - stones[index]))
        
        return rec(0,0)