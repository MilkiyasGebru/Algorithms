class Solution:
    
    def traverse(self,matrix,row,col,dr,dc,visited):
        if not (0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == 0):
            return 
        visited.add((row,col))
        self.traverse(matrix,row+dr,col+dc,dr,dc,visited)
        
    
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for row,col in walls:
            matrix[row][col] = -1
        for row, col in guards:
            matrix[row][col] = 1
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        for row,col in guards:
            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc
                self.traverse(matrix, new_row, new_col,dr,dc,visited)
        
        return m*n - len(walls) - len(guards) - len(visited)
        