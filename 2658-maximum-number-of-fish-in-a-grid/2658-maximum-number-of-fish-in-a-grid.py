class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(row,col):
            
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == 0:
                return 0
            
            ans = grid[row][col]
            grid[row][col] = 0
            for x,y in directions:
                ans += dfs(row+x,col+y)
            
            return ans
        
        max_fish = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                max_fish = max(max_fish,dfs(row,col))
        return max_fish
            
        