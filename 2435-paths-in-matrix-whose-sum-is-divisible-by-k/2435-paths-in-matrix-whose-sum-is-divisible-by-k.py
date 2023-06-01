class Solution:
    def isValid(self,row,col,prev_row,prev_col,grid,memo):
        mod = 10**9 + 7
        if 0 <= prev_row and 0 <= prev_col:
            for i in range(len(memo[(prev_row,prev_col)])):
                if memo[(prev_row,prev_col)][i] != 0: 
                    x = (i +grid[row][col] )%(len(memo[(prev_row,prev_col)]))
                    memo[(row,col)][x] += memo[(prev_row,prev_col)][i]
                    memo[(row,col)][x] %= mod
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
        memo = defaultdict(lambda: [0 for _ in range(k)])
        grid[0][0] %= k
        memo[(0,0)][grid[0][0]] = 1
        directions =[(-1,0),(0,-1)]
        n,m = len(grid),len(grid[0])
        
        for row in range(n):
            for col in range(m):
                
                for dx,dy in directions:
                    self.isValid(row,col,row+dx,col+dy,grid,memo)
        
        return memo[(n-1,m-1)][0]
        