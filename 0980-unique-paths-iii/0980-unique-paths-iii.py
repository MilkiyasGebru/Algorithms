class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        def isValid(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row,col) not in visited and grid[row][col] != -1
        #count 
        negative,start,end =0,[0,0],[0,0]
       
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                if grid[i][j] ==-1:
                    negative +=1
                elif grid[i][j]==1:
                    start=[i,j]
                elif grid[i][j]==2:
                    end=[i,j]
        visited.add((start[0],start[1]))            
        def dfs(row,col):
            if (end[0],end[1]) in visited:
                return 1 if len(visited)==len(grid)*len(grid[0])-negative else 0
            x=0
            for i, j in directions:
                nr=row+i
                nc = col + j
                if isValid(nr,nc):
                    visited.add((nr,nc))
                    x+=dfs(nr,nc)
                    visited.remove((nr,nc))
            return x 
        return dfs(start[0],start[1])
                    
        