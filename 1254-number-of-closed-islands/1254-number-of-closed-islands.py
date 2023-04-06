class Solution:
    
    def isValid(self,row,col,grid):
        
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0 
    
    def dfs(self,row,col,grid):
        
        grid[row][col] = 1
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        for dx,dy in directions:
            new_row = dx + row
            new_col = dy + col
            
            if self.isValid(new_row,new_col,grid):
                self.dfs(new_row,new_col,grid)
         
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        answer = 0
        
        for row in range(len(grid)):
            for col in range(0,len(grid[0]),max(1,len(grid[0])-1)):
                
                if grid[row][col] == 0:
                    self.dfs(row,col,grid)
        
        for col in range(len(grid[0])):
            for row in range(0,len(grid),max(len(grid)-1,1)):
                
                if grid[row][col] == 0:
                    self.dfs(row,col,grid)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 0 :
                    
                    answer += 1
                    self.dfs(row,col,grid)
        
        return answer 
                    