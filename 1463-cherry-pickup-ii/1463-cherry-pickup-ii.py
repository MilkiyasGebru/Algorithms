class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        directions = [0,-1,1]
        @cache
        def dp(row,col1,col2):
            
            if row == len(grid):
                return 0
            
            if col1 < 0 or col2 < 0 or col1 >= len(grid[0]) or col2 >= len(grid[0]):
                return -math.inf
            
            val = grid[row][col1] + grid[row][col2] 
            val -= grid[row][col1] if col1 == col2 else 0
            maxx = 0
            for y in directions:
                for j in directions:
                    
                    maxx = max(dp(row+1,col1+y,col2+j),maxx)
            
            return maxx + val
        
        return dp(0,0,len(grid[0])-1)