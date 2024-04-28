class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        @cache 
        def dp(row,col):
            
            if row == len(grid):
                return 0
            
            ans = math.inf
            
            for nex_col in range(len(grid[0])):
                
                if nex_col == col:
                    continue
                ans = min( ans, grid[row][nex_col] + dp(row+1,nex_col))
            
            return ans
        
        
        return dp(0,-1)