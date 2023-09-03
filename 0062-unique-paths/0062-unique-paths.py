class Solution:
    def isValid(self,row,col,m,n):
        return 0 <= row < m and 0 <= col < n
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m) ]
        directions = [(-1,0),(0,-1)]
        grid[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                
                for dx,dy in directions:
                    
                    if self.isValid(row+dx,col+dy,m,n):
                        grid[row][col] += grid[row+dx][col+dy]
        
        return grid[-1][-1]
        
        