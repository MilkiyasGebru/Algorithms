class Solution:
    
    def isValid(self,row,col,grid,bitmask,positions):
        
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0 and ((bitmask & (1 << positions[(row,col)])) == 0)
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        positions = {}
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] != 0:
                    positions[(row,col)] = count
                    count += 1
                    
        @cache
        def dp(row,col,bitmask):
            
            bitmask ^= (1 << positions[(row,col)])
            max_gold = 0
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc 
                
            
                if self.isValid(new_row,new_col,grid,bitmask,positions):

                    max_gold = max(max_gold, dp(new_row,new_col,bitmask))
            
            bitmask ^= (1 << positions[(row,col)])
            
            return max_gold + grid[row][col]
        
        max_gold = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] != 0:
                    max_gold = max(max_gold,dp(row,col,0))
        
        return max_gold
                    
            