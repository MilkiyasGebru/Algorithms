class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for i in range(len(piles)):
            for j in range(1,len(piles[i])):
                piles[i][j] += piles[i][j-1]
        
        @lru_cache(None)
        def dp(index,k):
            
            if index == len(piles) or k == 0:
                return 0
            
            ans = dp(index+1,k)
            
            for i in range(min(k,len(piles[index]))):
                
                ans = max( ans, piles[index][i] + dp(index+1,k-(i+1))  )
            
            return ans
        
        return dp(0,k)