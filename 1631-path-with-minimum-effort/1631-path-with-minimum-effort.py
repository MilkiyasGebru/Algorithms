class Solution:
    def isValid(self,row,col,visited,heights):
        
        return 0 <= row < len(heights) and 0 <= col < len(heights[0]) and (row,col) not in visited
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        visited = set()
        heap =[(0,0,0)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while heap:
            
            cost,row,col = heappop(heap)
            if (row,col) in visited:
                continue
            if (row,col) == (len(heights)-1,len(heights[0])-1):
                return cost
            visited.add((row,col))
            for dx,dy in directions:
                if self.isValid(row+dx,col+dy,visited,heights):
                    heappush(heap,(max(cost , abs(heights[row][col]-heights[row+dx][col+dy])),row+dx,col+dy))
        
            
            