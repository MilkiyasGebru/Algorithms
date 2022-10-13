class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        q = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def isValid(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def dfs(row,col):
            q.append((row,col))
            grid[row][col]="#"
            
            for i,j in directions:
                
                if isValid(row+i,col+j) and grid[row+i][col+j]==1:
                    
                    dfs(row+i,col+j)
        b= False
        for row in range(len(grid)):
            if b:break
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    dfs(row,col)
                    b=True
                    break
        path = 0
        while(q):
            x = len(q)
            for _ in range(x):
                row,col = q.popleft()
                if grid[row][col]==".":
                    continue
                if grid[row][col]==1:
                    return path-1
                grid[row][col]="."
                for i,j in directions:
                    if isValid(row+i,col+j) and (grid[row+i][col+j]==0 or grid[row+i][col+j]==1):
                        q.append((row+i,col+j))
            path+=1
        
                
            
            
            