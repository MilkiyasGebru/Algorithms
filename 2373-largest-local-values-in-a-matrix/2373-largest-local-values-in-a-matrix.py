class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        
        new_matrix = []
        
        for row in range(1,len(grid)-1):
            arr = []
            for col in range(1,len(grid[0])-1):
                
                max_value = -math.inf
                for dr,dc in directions:
                    max_value = max(max_value,grid[row+dr][col+dc])
                arr.append(max_value)
            new_matrix.append(arr)
        return new_matrix
                