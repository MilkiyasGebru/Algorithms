class Solution:
    
    def isValid(self,row,col,grid,visited):
        
        return 0 <= row < len(grid) and 0 <= col < len(grid) and grid[row][col] == 0 and (row,col) not in visited
    
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        n = len(grid)
        q= deque()
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    q.append((row,col))
        
        visited = set()
        path = 0
        max_distance = 0
        
        while(q):
            
            size = len(q)
            
            for _ in range(size):
                
                row,col = q.popleft()
                
                if (row,col) in visited:
                    continue
                    
                visited.add((row,col))
                max_distance = max(max_distance,path)
                
                for dx,dy in directions:
                    
                    new_row, new_col = row + dx, col + dy
                    
                    if self.isValid(new_row,new_col,grid,visited):
                        q.append((new_row,new_col))
                        
            path += 1
        
        return max_distance if max_distance != 0 else -1
        