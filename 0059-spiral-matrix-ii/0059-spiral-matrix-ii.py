class Solution:
    
    def isValid(self, row, col, matrix):
        
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col]==0
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        direction = { 0 :(0,1), 1 : (1,0), 2: (0,-1), 3 : (-1,0) }
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        return self.rec(0, 0, matrix, 1, 0, direction)
    
    def rec(self, row, col, matrix, val, arrow, direction):
        
        matrix[row][col]=val
        
        if val == len(matrix)*len(matrix[0]):
            
            return matrix
        
        if self.isValid(row + direction[arrow][0], col + direction[arrow][1], matrix):
            
            return self.rec(row + direction[arrow][0], col + direction[arrow][1], matrix, val+1, arrow, direction)
        
        new_arrow = (arrow + 1)%4
        
        return self.rec(row + direction[new_arrow][0], col + direction[new_arrow][1], matrix, val+1, new_arrow, direction)
        