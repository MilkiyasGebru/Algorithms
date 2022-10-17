class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        heap  = []
        heapq.heappush(heap,(0,0,0))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        
        def isValid(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        while(heap):
            
            cost,row,col = heapq.heappop(heap)
            
            if (row,col) in visited:
                continue
                
            visited.add((row,col))
            
            if (row,col)==(len(grid)-1,len(grid[0])-1):
                return cost
            
            for i in range(4):
                
                if isValid(row+directions[i][0],col+directions[i][1]):
                    heapq.heappush(heap,(cost + (((i+1)!=grid[row][col])==True),row+directions[i][0],col+directions[i][1]))
        
            