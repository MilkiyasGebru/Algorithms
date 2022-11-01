class Solution:
    def check(self,row,col,n,m):
        
        return 0 <= row < n and 0 <= col < m
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        falls_array = [col for col in range(len(grid[0]))]
        
        for row in range(len(grid)):

            for col in range(len(grid[0])):
                
                if falls_array[col] == -1:
                    continue
                    
                c = falls_array[col]
                
                if self.check(row,c+ grid[row][c],len(grid),len(grid[0])) and grid[row][c] == grid[row][c + grid[row][c]]:
                    falls_array[col] = c+grid[row][c]
                    
                else:
                    
                    falls_array[col]=-1
                
        return falls_array
                    
                