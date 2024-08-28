class Solution:
    
    def isValid(self,grid,row,col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1
    
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def rec(row,col):
            answer = grid1[row][col] == grid2[row][col]
            grid2[row][col] = 0
            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if self.isValid(grid2,new_row,new_col):
                    answer =  rec(new_row,new_col) and answer
            return answer
        total = 0

        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                
                if grid2[row][col]:
                    total += rec(row,col)
        return total