class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def isValid(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]==0 and (row,col) not in visited
        visited = set()
        
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        heap =[]
        if grid[0][0] !=0:
            return -1
        heapq.heappush(heap,(1,[0,0]))
        
        while(heap):
            
        
            dis,arr =heapq.heappop(heap)
            if arr[0] == len(grid)-1 and arr[1]==len(grid[0])-1 :
                return dis
            
            for a,b in directions:
                new_row = arr[0] + a
                new_col = arr[1] + b
                
                if isValid(new_row,new_col):
                    visited.add((new_row,new_col))
                    heapq.heappush(heap,(dis+1,(new_row,new_col)))
        return -1          